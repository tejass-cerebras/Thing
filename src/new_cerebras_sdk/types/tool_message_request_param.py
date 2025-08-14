# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ToolMessageRequestParam"]


class ToolMessageRequestParamTyped(TypedDict, total=False):
    content: Required[str]

    tool_call_id: Required[str]

    name: Optional[str]

    role: Literal["tool"]


ToolMessageRequestParam: TypeAlias = Union[ToolMessageRequestParamTyped, Dict[str, object]]
