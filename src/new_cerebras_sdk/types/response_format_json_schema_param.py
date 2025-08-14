# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ResponseFormatJsonSchemaParam", "JsonSchema"]


class JsonSchemaTyped(TypedDict, total=False):
    name: Required[str]

    description: Optional[str]

    schema: Optional[object]

    strict: Optional[bool]


JsonSchema: TypeAlias = Union[JsonSchemaTyped, Dict[str, object]]


class ResponseFormatJsonSchemaParamTyped(TypedDict, total=False):
    json_schema: Required[JsonSchema]
    """A JSON Schema object."""

    type: Required[Literal["json_schema"]]


ResponseFormatJsonSchemaParam: TypeAlias = Union[ResponseFormatJsonSchemaParamTyped, Dict[str, object]]
