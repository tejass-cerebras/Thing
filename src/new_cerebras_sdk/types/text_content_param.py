# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["TextContentParam"]


class TextContentParamTyped(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


TextContentParam: TypeAlias = Union[TextContentParamTyped, Dict[str, object]]
