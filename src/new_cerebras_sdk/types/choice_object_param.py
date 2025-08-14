# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ChoiceObjectParam", "Function"]


class FunctionTyped(TypedDict, total=False):
    name: Required[str]


Function: TypeAlias = Union[FunctionTyped, Dict[str, object]]


class ChoiceObjectParamTyped(TypedDict, total=False):
    function: Required[Function]
    """A function for a choice object."""

    type: Required[str]


ChoiceObjectParam: TypeAlias = Union[ChoiceObjectParamTyped, Dict[str, object]]
