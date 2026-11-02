<%include file="header.py.mako"/>

from dataclasses import dataclass
from typing import Literal

from pydantic import Field

from aogami.types import (
    InputFile,
    TelegramObject,
% for name in spec.types:
    ${name},
% endfor
)
from aogami.types_manual import WebhookResponse

% for m in spec.methods.values():


class ${m.webhook_name}(WebhookResponse):
    """
${m.get_docstring(1)}
    """
    % for f in m.sorted_fields:
    ${f.name}: ${f.type_hint}${" = None" if not f.required else ""}
    % endfor

    method_: Literal["${m.name}"] = Field("${m.name}", alias="method")
% endfor
