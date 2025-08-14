# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .assistant_tool_call_function_param import AssistantToolCallFunctionParam

__all__ = ["AssistantToolCallParam"]


class AssistantToolCallParamTyped(TypedDict, total=False):
    id: Required[str]

    function: Required[AssistantToolCallFunctionParam]
    """A function call for an assistant tool."""

    type: Required[Literal["function"]]


AssistantToolCallParam: TypeAlias = Union[AssistantToolCallParamTyped, Dict[str, object]]
