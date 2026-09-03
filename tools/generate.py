import keyword
import logging
import re
import subprocess
import textwrap
from collections.abc import Generator
from pathlib import Path
from typing import Annotated, Final, Self

import httpx2
from mako.lookup import TemplateLookup
from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    HttpUrl,
    model_validator,
)

SPEC_URL: Final = "https://raw.githubusercontent.com/PaulSonOfLars/telegram-bot-api-spec/main/api.min.json"

BASE_DIR: Final = Path(__file__).parent
TEMPLATES_DIR: Final = BASE_DIR / "templates"
OUTPUT_DIR: Final = BASE_DIR.parent / "src/aogami"

SPEC_FILE: Final = BASE_DIR / "api.min.json"

TELEGRAM_SCALAR_TYPES: Final = {
    "Boolean": "bool",
    "Float": "float",
    "Integer": "int",
    "String": "str",
}
DOCSTRING_WIDTH: Final = 88

logger = logging.getLogger(__name__)


def wrap_paragraphs(
    paragraphs: list[str],
    initial_indent: str = "",
    subsequent_indent: str = "",
    width: int = DOCSTRING_WIDTH,
) -> Generator[str]:

    for p in paragraphs:
        yield textwrap.fill(
            p,
            width,
            initial_indent=initial_indent,
            subsequent_indent=subsequent_indent,
        )


def to_snake_case(string: str) -> str:
    # NOTE: This is ~30% faster
    # PATTERN = re.compile(r"(?<!^)(?=[A-Z])")
    # PATTERN.sub("_", string).lower()

    return "".join("_" + c.lower() if c.isupper() else c for c in string)


def escape_keyword(string: str) -> str:
    # TODO: maybe add hardcoded overrides like: "from" -> "from_user"
    return string + "_" if keyword.iskeyword(string) else string


def parse_type(type_: str) -> str:
    arr_depth = type_.count("Array of ")
    type_ = type_.removeprefix("Array of " * arr_depth)
    type_ = TELEGRAM_SCALAR_TYPES.get(type_, type_)

    return "list[" * arr_depth + type_ + "]" * arr_depth


def convert_types(types: list[str]) -> list[str]:
    return [parse_type(type_) for type_ in types]


class BaseInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    href: HttpUrl
    description: list[str] = []
    fields: list[FieldInfo] = []


class TypeInfo(BaseInfo):
    subtypes: Annotated[list[str], BeforeValidator(convert_types)] = []
    subtype_of: list[str] = []

    @property
    def is_union(self) -> bool:
        return bool(self.subtypes)

    @model_validator(mode="after")
    def check_union_type_has_no_fields(self) -> Self:
        if self.subtypes and self.fields:
            raise ValueError("Unions should not have fields")
        return self

    @property
    def type_hint(self) -> str:
        return " | ".join(self.subtypes)

    def get_docstring(self) -> str:
        if not self.description:
            return "No description"
        return "\n".join(wrap_paragraphs(self.description, " " * 4, " " * 4))


class MethodInfo(BaseInfo):
    returns: Annotated[list[str], BeforeValidator(convert_types)]

    @property
    def python_name(self) -> str:
        return to_snake_case(self.name)

    @property
    def type_hint(self) -> str:
        return " | ".join(self.returns)

    @property
    def sorted_fields(self) -> list[FieldInfo]:
        return sorted(self.fields, key=lambda f: not f.required)

    def get_docstring(self) -> str:
        if not self.fields:
            return "\n".join(wrap_paragraphs(self.description, " " * 8, " " * 8))

        paragraphs = self.description + ["\n", "Args:"]
        docstring = list(wrap_paragraphs(paragraphs, " " * 8, " " * 8))

        args = [f"{f.name} ({f.type_hint}): {f.description}" for f in self.fields]
        docstring += wrap_paragraphs(args, " " * 12, " " * 16)
        return "\n".join(docstring)


class FieldInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    required: bool
    description: Annotated[str, BeforeValidator(lambda s: s.removeprefix("Optional. "))]
    types: Annotated[list[str], BeforeValidator(convert_types)] = []

    @property
    def python_name(self) -> str:
        return escape_keyword(self.name)

    @property
    def literal(self) -> str | None:
        if self.description.startswith("Always 0."):
            return "0"

        patterns = [
            r".*always \"([\w_]+)\"$",
            r".*must be ([\w_]+)$",
        ]
        for pattern in patterns:
            if match := re.search(pattern, self.description):
                subgroup = match.group(1)
                assert isinstance(subgroup, str)
                return f'"{subgroup}"'

    @property
    def type_hint(self) -> str:
        if self.literal:
            assert len(self.types) == 1
            assert self.types[0] in {"str", "int"}

            return f"Literal[{self.literal}]"

        types = self.types

        if not self.required:
            types = [*types, "None"]

        if "InputFile" not in types and "attach://" in self.description:
            # InputFile is first to remain consistent with docs: "InputFile or String"
            types = ["InputFile", *types]

        return " | ".join(types)

    def get_docstring(self) -> str:
        return "\n".join(wrap_paragraphs([self.description], " " * 4, " " * 4))


class APISpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    types: dict[str, TypeInfo]
    methods: dict[str, MethodInfo]

    version: str
    release_date: str
    changelog: HttpUrl

    def find_union_discriminator(self, subtypes: list[str]) -> str | None:
        for discriminator in ("source", "status", "type"):
            for type_info in (self.types.get(i) for i in subtypes):
                if not type_info:
                    break
                if discriminator not in {field.name for field in type_info.fields}:
                    break
            else:
                """
                class Foo(BaseModel):
                    from_: Literal["foo"] = Field(alias="from")

                class Bar(BaseModel):
                    from_: Literal["bar"] = Field(alias="from")

                type FooBar = Annotated[Foo | Bar, Field(discriminator="from_")]

                TypeAdapter(FooBar).validate_json('{"from": "foo"}')
                TypeAdapter(FooBar).validate_json('{"from": "bar"}')
                """

                # Field discriminator needs to be the python attribute name ^
                return escape_keyword(discriminator)


def get_spec() -> str:
    if SPEC_FILE.exists():
        return SPEC_FILE.read_text()

    resp = httpx2.get(SPEC_URL)
    resp.raise_for_status()

    spec = resp.content.decode("utf-8")
    SPEC_FILE.write_text(spec)

    return spec


def main() -> None:
    spec = APISpec.model_validate_json(get_spec())
    # We use a manually defined InputFile type
    spec.types.pop("InputFile", None)

    OUTPUT_DIR.mkdir(exist_ok=True)

    lookup = TemplateLookup(directories=[TEMPLATES_DIR])

    for filename in (
        "methods.py.mako",
        "types.py.mako",
    ):
        template = lookup.get_template(filename)
        code = template.render(spec=spec)

        path = OUTPUT_DIR / Path(filename).stem
        path.write_text(code)

        subprocess.run(["ruff", "check", "--fix", path], check=True)
        subprocess.run(["ruff", "format", path], check=True)


if __name__ == "__main__":
    main()
