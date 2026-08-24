import keyword
import logging
import re
import subprocess
from functools import cached_property
from pathlib import Path
from typing import Annotated, Self

import httpx2
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    HttpUrl,
    model_validator,
)

SPEC_URL = "https://raw.githubusercontent.com/PaulSonOfLars/telegram-bot-api-spec/main/api.min.json"

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "generated"

SPEC_FILE = BASE_DIR / "api.min.json"


TYPES = {"Boolean": "bool", "Integer": "int", "Float": "float", "String": "str"}

logger = logging.getLogger(__name__)


def escape_keyword(string: str) -> str:
    return string + "_" if keyword.iskeyword(string) else string


def parse_type(type_: str) -> str:
    arr_depth = type_.count("Array of ")
    type_ = type_.removeprefix("Array of " * arr_depth)
    type_ = TYPES.get(type_, type_)

    return "list[" * arr_depth + type_ + "]" * arr_depth


def convert_types(types: list[str]) -> list[str]:
    return [parse_type(type_) for type_ in types]


class BaseInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    href: HttpUrl
    description: Annotated[str, BeforeValidator(lambda x: " ".join(x))]
    fields: list[FieldInfo] = []


class FieldInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    required: bool
    description: Annotated[str, BeforeValidator(lambda x: x.removeprefix("Optional. "))]
    types: Annotated[list[str], BeforeValidator(convert_types)]

    @cached_property
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
    def alias(self) -> str:
        return escape_keyword(self.name)

    @property
    def type_annotation(self) -> str:
        if self.literal:
            assert len(self.types) == 1
            assert self.types[0] in {"str", "int"}

            return f"Literal[{self.literal}]"

        types = self.types
        if not self.required:
            types = [*types, "None"]

        return " | ".join(types)


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


class MethodInfo(BaseInfo):
    returns: list[str]


def flatten_dict[T](value: dict[str, T]) -> list[T]:
    # api.min.json maps objects by name: {"name": Info}
    # Since Info already stores name, flatten to a list
    return list(value.values())


class APISpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    types: Annotated[list[TypeInfo], BeforeValidator(flatten_dict)]
    methods: Annotated[list[MethodInfo], BeforeValidator(flatten_dict)]

    version: str
    release_date: str
    changelog: HttpUrl

    @cached_property
    def types_map(self) -> dict[str, TypeInfo]:
        return {type_.name: type_ for type_ in self.types}

    @cached_property
    def methods_map(self) -> dict[str, MethodInfo]:
        return {method.name: method for method in self.methods}

    def find_union_discriminator(self, subtypes: list[str]) -> str | None:
        for discriminator in ("type", "source", "status"):
            for type_info in (self.types_map.get(i) for i in subtypes):
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

                # We use escape_keyword because of this ^
                return escape_keyword(discriminator)


def get_spec() -> str:
    if SPEC_FILE.exists():
        return SPEC_FILE.read_text()

    resp = httpx2.get(SPEC_URL)
    resp.raise_for_status()

    spec = resp.content.decode("utf-8")
    SPEC_FILE.write_text(spec)

    return spec


def to_snake_case(string: str) -> str:
    # NOTE: This is ~30% faster
    # PATTERN = re.compile(r"(?<!^)(?=[A-Z])")
    # PATTERN.sub("_", string).lower()

    return "".join("_" + c.lower() if c.isupper() else c for c in string)


def main() -> None:
    spec = APISpec.model_validate_json(get_spec())

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    env.filters["to_snake_case"] = to_snake_case

    OUTPUT_DIR.mkdir(exist_ok=True)

    for name in ("types.py.jinja", "methods.py.jinja"):
        template = env.get_template(name)
        code = template.render(spec=spec)
        (OUTPUT_DIR / Path(name).stem).write_text(code)

    subprocess.run(["ruff", "format", OUTPUT_DIR], check=True)


if __name__ == "__main__":
    main()
