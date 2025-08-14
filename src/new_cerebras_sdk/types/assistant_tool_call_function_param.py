# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AssistantToolCallFunctionParam"]


class AssistantToolCallFunctionParamTyped(TypedDict, total=False):
    arguments: Required[str]

    name: Required[str]


AssistantToolCallFunctionParam: TypeAlias = Union[AssistantToolCallFunctionParamTyped, Dict[str, object]]
