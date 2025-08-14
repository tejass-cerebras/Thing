# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .assistant_tool_call_param import AssistantToolCallParam

__all__ = ["AssistantMessageRequestParam"]


class AssistantMessageRequestParamTyped(TypedDict, total=False):
    role: Required[Literal["assistant"]]

    content: Optional[str]

    name: Optional[str]

    tool_calls: Optional[Iterable[AssistantToolCallParam]]


AssistantMessageRequestParam: TypeAlias = Union[AssistantMessageRequestParamTyped, Dict[str, object]]
