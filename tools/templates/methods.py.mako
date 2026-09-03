<%include file="header.py.mako"/>
from typing_extensions import TypeForm

from aogami.types import (
    InputFile,
% for name in spec.types:
    ${name},
% endfor
)


class TelegramMethods:

    async def method[T](
        self, name: str, returns: TypeForm[T], /, **params: object
    ) -> T:
        raise NotImplementedError
% for m in spec.methods.values():

    async def ${m.python_name}(
        self,
        % if m.fields:
        *,
        % for f in m.sorted_fields:
        ${f.python_name}: ${f.type_hint}${" = None" if not f.required else ""},
        % endfor
        % endif
    ) -> ${m.type_hint}:
        """
${m.get_docstring()}
        """
        params = {
            % for f in m.fields:
            "${f.name}": ${f.python_name},
            % endfor
        }
        return await self.method(
            "${m.name}",
            ${m.type_hint},
            **params
        )
% endfor
