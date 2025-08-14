# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .usage import Usage
from .._models import BaseModel
from .time_info import TimeInfo
from .chat_chunk_choice import ChatChunkChoice
from .error_chunk_response import ErrorChunkResponse

__all__ = [
    "CompletionCreateResponse",
    "CompletionResponse",
    "CompletionResponseChoice",
    "CompletionResponseChoiceLogprobs",
    "CompletionChunkResponse",
]


class CompletionResponseChoiceLogprobs(BaseModel):
    text_offset: Optional[List[int]] = None

    token_logprobs: Optional[List[float]] = None

    tokens: Optional[List[str]] = None

    top_logprobs: Optional[List[Dict[str, float]]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CompletionResponseChoice(BaseModel):
    index: int

    finish_reason: Optional[Literal["stop", "length", "content_filter"]] = None

    logprobs: Optional[CompletionResponseChoiceLogprobs] = None

    text: Optional[str] = None

    tokens: Optional[List[int]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CompletionResponse(BaseModel):
    id: str

    choices: List[CompletionResponseChoice]

    created: int

    model: str

    object: Literal["text_completion"]

    system_fingerprint: str

    extra_body: Optional[builtins.object] = None
    """
    Extra body response parameters for /v1/completions endpoint. This class is used
    to define additional fields that can be included in the response body that are
    not currently supported by the OpenAI API.
    """

    internal_fields: Optional[builtins.object] = None
    """Internal response fields for /v1/completions endpoint."""

    time_info: Optional[TimeInfo] = None

    usage: Optional[Usage] = None

    __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...


class CompletionChunkResponse(BaseModel):
    id: str

    created: int

    model: str

    object: Literal["chat.completion.chunk", "text_completion"]

    system_fingerprint: str

    choices: Optional[List[ChatChunkChoice]] = None

    service_tier: Optional[str] = None

    time_info: Optional[TimeInfo] = None

    usage: Optional[Usage] = None

    __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...


CompletionCreateResponse: TypeAlias = Union[CompletionResponse, CompletionChunkResponse, ErrorChunkResponse]
