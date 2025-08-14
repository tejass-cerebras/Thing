# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .text_content_param import TextContentParam

__all__ = ["UserMessageRequestParam"]


class UserMessageRequestParamTyped(TypedDict, total=False):
    content: Required[Union[str, Iterable[TextContentParam]]]

    name: Optional[str]

    role: Literal["user"]


UserMessageRequestParam: TypeAlias = Union[UserMessageRequestParamTyped, Dict[str, object]]
