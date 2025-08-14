# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ToolParam", "Function"]


class FunctionTyped(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    parameters: Optional[object]
    """
    Represents the parameters a function accepts. This model is designed to be
    flexible to accommodate any JSON Schema. The key-value pairs you provide will
    define the parameters.
    """

    strict: bool


Function: TypeAlias = Union[FunctionTyped, Dict[str, object]]


class ToolParamTyped(TypedDict, total=False):
    function: Required[Function]
    """A function object."""

    type: Required[str]


ToolParam: TypeAlias = Union[ToolParamTyped, Dict[str, object]]
