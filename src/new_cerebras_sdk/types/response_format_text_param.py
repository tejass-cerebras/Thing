# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ResponseFormatTextParam"]


class ResponseFormatTextParamTyped(TypedDict, total=False):
    type: Required[Literal["text"]]


ResponseFormatTextParam: TypeAlias = Union[ResponseFormatTextParamTyped, Dict[str, object]]
