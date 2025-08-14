# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import TypeAlias, TypedDict

__all__ = ["StreamOptionsParam"]


class StreamOptionsParamTyped(TypedDict, total=False):
    include_usage: Optional[bool]


StreamOptionsParam: TypeAlias = Union[StreamOptionsParamTyped, Dict[str, object]]
