# Chat

Types:

```python
from new_cerebras_sdk.types import (
    AssistantMessageRequest,
    AssistantToolCall,
    AssistantToolCallFunction,
    ChatChunkChoice,
    ChatCompletionLogProbs,
    ChoiceObject,
    ErrorChunkResponse,
    LogProbsContent,
    ResponseFormatJsonObject,
    ResponseFormatJsonSchema,
    ResponseFormatText,
    StreamOptions,
    SystemMessageRequest,
    TextContent,
    TimeInfo,
    Tool,
    ToolMessageRequest,
    Usage,
    UserMessageRequest,
    ChatCreateCompletionResponse,
)
```

Methods:

- <code title="post /v1/chat/completions">client.chat.<a href="./src/new_cerebras_sdk/resources/chat.py">create_completion</a>(\*\*<a href="src/new_cerebras_sdk/types/chat_create_completion_params.py">params</a>) -> <a href="./src/new_cerebras_sdk/types/chat_create_completion_response.py">ChatCreateCompletionResponse</a></code>

# Completions

Types:

```python
from new_cerebras_sdk.types import CompletionCreateResponse
```

Methods:

- <code title="post /v1/completions">client.completions.<a href="./src/new_cerebras_sdk/resources/completions.py">create</a>(\*\*<a href="src/new_cerebras_sdk/types/completion_create_params.py">params</a>) -> <a href="./src/new_cerebras_sdk/types/completion_create_response.py">CompletionCreateResponse</a></code>

# Models

Types:

```python
from new_cerebras_sdk.types import ModelMetadata, ModelListResponse
```

Methods:

- <code title="get /v1/models/{model_id}">client.models.<a href="./src/new_cerebras_sdk/resources/models.py">retrieve</a>(model_id) -> <a href="./src/new_cerebras_sdk/types/model_metadata.py">ModelMetadata</a></code>
- <code title="get /v1/models">client.models.<a href="./src/new_cerebras_sdk/resources/models.py">list</a>() -> <a href="./src/new_cerebras_sdk/types/model_list_response.py">ModelListResponse</a></code>

# TcpWarming

Methods:

- <code title="get /v1/tcp_warming">client.tcp_warming.<a href="./src/new_cerebras_sdk/resources/tcp_warming.py">retrieve</a>() -> object</code>
