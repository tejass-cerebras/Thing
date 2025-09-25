# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .usage import Usage
from .._models import BaseModel
from .time_info import TimeInfo
from .chat_chunk_choice import ChatChunkChoice
from .assistant_tool_call import AssistantToolCall
from .error_chunk_response import ErrorChunkResponse
from .chat_completion_log_probs import ChatCompletionLogProbs

__all__ = [
    "ChatCreateCompletionResponse",
    "ChatCompletionResponse",
    "ChatCompletionResponseChoice",
    "ChatCompletionResponseChoiceMessage",
    "ChatChunkResponse",
]


class ChatCompletionResponseChoiceMessage(BaseModel):
    role: Literal["assistant", "user", "system", "tool"]

    content: Optional[str] = None

    tool_calls: Optional[List[AssistantToolCall]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ChatCompletionResponseChoice(BaseModel):
    finish_reason: Literal["stop", "length", "content_filter", "tool_calls"]

    index: int

    message: ChatCompletionResponseChoiceMessage

    logprobs: Optional[ChatCompletionLogProbs] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ChatCompletionResponse(BaseModel):
    id: str

    choices: List[ChatCompletionResponseChoice]

    created: int

    model: str

    object: Literal["chat.completion"]

    system_fingerprint: str

    time_info: TimeInfo

    usage: Usage

    extra_body: Optional[builtins.object] = None
    """
    Extra body response parameters for /v1/chat/completions endpoint. This class is
    used to define additional fields that can be included in the response body that
    are not currently supported by the OpenAI API.
    """

    internal_fields: Optional[builtins.object] = None
    """Internal response fields for /v1/chat/completions endpoint."""

    service_tier: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]


class ChatChunkResponse(BaseModel):
    id: str

    created: int

    model: str

    object: Literal["chat.completion.chunk", "text_completion"]

    system_fingerprint: str

    choices: Optional[List[ChatChunkChoice]] = None

    service_tier: Optional[str] = None

    time_info: Optional[TimeInfo] = None

    usage: Optional[Usage] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]


ChatCreateCompletionResponse: TypeAlias = Union[ChatCompletionResponse, ChatChunkResponse, ErrorChunkResponse]
