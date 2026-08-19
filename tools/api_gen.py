import json
import logging
from functools import cached_property
from http import HTTPStatus
from pathlib import Path
from typing import Annotated, Any, Self

import httpx2
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from pydantic import (
    BaseModel,
    BeforeValidator,
    ConfigDict,
    HttpUrl,
    ValidationError,
    model_validator,
)

SPEC_URL = "https://raw.githubusercontent.com/PaulSonOfLars/telegram-bot-api-spec/main/api.min.json"

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
OUTPUT_DIR = BASE_DIR / "generated"

SPEC_FILE = BASE_DIR / "api.min.json"


TYPES = {"Boolean": "bool", "Integer": "int", "Float": "float", "String": "str"}

logger = logging.getLogger(__name__)


def parse_type(type_: str) -> str:
    arr_depth = type_.count("Array of ")
    type_ = type_.removeprefix("Array of " * arr_depth)
    type_ = TYPES.get(type_, type_)

    return "list[" * arr_depth + type_ + "]" * arr_depth


def convert_types(types: list[str]) -> list[str]:
    return [parse_type(type_) for type_ in types]


class FieldInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    required: bool
    description: str
    types: Annotated[list[str], BeforeValidator(convert_types)]


def join_description(desc: list[str]) -> str:
    return "\n".join(desc)


class BaseInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    href: HttpUrl
    description: Annotated[str, BeforeValidator(join_description)]
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
            raise ValueError("Union types should not have fields")
        return self


class MethodInfo(BaseInfo):
    returns: list[str]

    @property
    def snake_case_name(self) -> str:
        # NOTE: This is ~30% faster
        # SNAKE_CASE_PATTERN = re.compile(r"(?<!^)(?=[A-Z])")
        # SNAKE_CASE_PATTERN.sub("_", name).lower()

        return "".join("_" + c.lower() if c.isupper() else c for c in self.name)


def flatten_dict(value: Any) -> Any:
    # api.min.json maps objects by name: {"name": Info}
    # Since Info already stores name, flatten to a list
    if isinstance(value, dict):
        return list(value.values())
    return value


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
        # Special case
        if "InaccessibleMessage" in subtypes:
            return "date"

        possible_discriminators = ["type", "source", "status"]
        for disc in possible_discriminators:
            disc_all = True
            for type_info in (self.types_map.get(subtype) for subtype in subtypes):
                if not type_info:
                    continue

                field_names = {field.name for field in type_info.fields}
                if disc not in field_names:
                    disc_all = False
                    break

            if disc_all:
                return disc


def get_spec() -> str:
    if SPEC_FILE.exists():
        return SPEC_FILE.read_text()

    resp = httpx2.get(SPEC_URL)
    assert resp.status_code == HTTPStatus.OK

    spec = resp.content.decode("utf-8")
    SPEC_FILE.write_text(spec)

    return spec


def main() -> None:
    try:
        spec = APISpec.model_validate_json(get_spec())
    except ValidationError as validation_error:
        print(validation_error.errors(include_input=False))
        raise

    for type in spec.types:
        if type.is_union:
            disc = spec.find_union_discriminator(type.subtypes)
            # print(type.name, disc)

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        undefined=StrictUndefined,
        # trim_blocks=True,
        # lstrip_blocks=True,
    )

    template = env.get_template("types.py.jinja")
    code = template.render(spec=spec)

    print(code)


if __name__ == "__main__":
    main()
