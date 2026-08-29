<%!
    import textwrap

    def field_assignment(type_info, field):
        value = None

        if literal := field.literal:
            value = literal
        elif not field.required:
            value = "None"

        args = []

        # Message.date is a special case
        if type_info.name == "Message" and field.name == "date":
            args.append("gt=0")

        if field.name != field.python_name:
            args.append(f'alias="{field.name}"')

        if args:
            args = [value, *args] if value is not None else args
            return f"Field({", ".join(args)})"

        return value or ""
%>
<%include file="header.py.mako"/>
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, ReprArgs


class TelegramObject(BaseModel):
    model_config = ConfigDict(frozen=True)


class Response[T](TelegramObject):
    ok: bool
    result: T | None = None
    error_code: int | None = None
    description: str | None = None
    parameters: ResponseParameters | None = None
% for t in spec.types.values():


% if t.is_union:
% if discriminator := spec.find_union_discriminator(t.subtypes):
type ${t.name} = Annotated[${t.type_hint}, Field(discriminator="${discriminator}")]
% else:
type ${t.name} = ${t.type_hint}
% endif
% else:
class ${t.name}(TelegramObject):
    """
${t.get_docstring()}
    """
    % for f in t.fields:

    % if assignment := field_assignment(t, f):
    ${f.python_name}: ${f.type_hint} = ${assignment}
    % else:
    ${f.python_name}: ${f.type_hint}
    % endif
    """
${f.get_docstring()}
    """
    % endfor
% endif
% endfor
