# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .chat_completion_log_probs import ChatCompletionLogProbs
from .assistant_tool_call_function import AssistantToolCallFunction

__all__ = ["ChatChunkChoice", "Delta", "DeltaToolCall"]


class DeltaToolCall(BaseModel):
    id: str

    function: AssistantToolCallFunction
    """A function call for an assistant tool."""

    type: Literal["function"]

    index: Optional[int] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class Delta(BaseModel):
    content: Optional[str] = None

    role: Optional[Literal["assistant", "user", "system", "tool"]] = None

    tokens: Optional[List[int]] = None

    tool_calls: Optional[List[DeltaToolCall]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class ChatChunkChoice(BaseModel):
    index: int

    delta: Optional[Delta] = None

    finish_reason: Optional[Literal["stop", "length", "content_filter", "tool_calls"]] = None

    logprobs: Optional[ChatCompletionLogProbs] = None

    text: Optional[str] = None

    tokens: Optional[List[int]] = None

    __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
