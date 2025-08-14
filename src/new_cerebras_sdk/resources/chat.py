# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Union, Iterable, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..types import chat_create_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import is_given, required_args, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.tool_param import ToolParam
from ..types.stream_options_param import StreamOptionsParam
from ..types.chat_create_completion_response import ChatCreateCompletionResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tejass-cerebras/Thing#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tejass-cerebras/Thing#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    @overload
    def create_completion(
        self,
        *,
        model: str,
        api_extra_body: Optional[object] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        messages: Optional[
            Iterable[chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestMessage]
        ]
        | NotGiven = NOT_GIVEN,
        min_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestResponseFormat
        ]
        | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[StreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestToolChoice
        ]
        | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[ToolParam]] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateCompletionResponse:
        """
        Chat

        Args:
          api_extra_body: Extra body parameters for /v1/chat/completions endpoint. This class is used to
              define additional fields that can be included in the request body that are not
              currently supported by the OpenAI API.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the content of
              message.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and reasoning tokens.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length. This value is now deprecated in favor of max_completion_tokens.

          min_completion_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          min_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep n as 1 to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: A response format for text.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming.

          temperature: What sampling temperature to use, between 0 and 1.5. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: A choice object.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability. logprobs
              must be set to true if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help Cerebras to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create_completion(
        self,
        *,
        model: str,
        api_extra_body: Optional[
            chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestExtraBody
        ]
        | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        messages: Optional[
            Iterable[chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestMessage]
        ]
        | NotGiven = NOT_GIVEN,
        min_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[
            chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestResponseFormat
        ]
        | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[StreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[
            chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestToolChoice
        ]
        | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[ToolParam]] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateCompletionResponse:
        """
        Chat

        Args:
          api_extra_body: Extra body parameters for Llama for /v1/chat/completions.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the content of
              message.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and reasoning tokens.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length. This value is now deprecated in favor of max_completion_tokens.

          min_completion_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          min_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep n as 1 to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: A response format for text.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming.

          temperature: What sampling temperature to use, between 0 and 1.5. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: A choice object.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability. logprobs
              must be set to true if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help Cerebras to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model"])
    def create_completion(
        self,
        *,
        model: str,
        api_extra_body: Optional[object]
        | Optional[chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestExtraBody]
        | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        messages: Optional[
            Iterable[chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestMessage]
        ]
        | NotGiven = NOT_GIVEN,
        min_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestResponseFormat
        ]
        | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[StreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestToolChoice
        ]
        | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[ToolParam]] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateCompletionResponse:
        extra_headers = {
            **strip_not_given(
                {
                    "CF-RAY": cf_ray,
                    "X-Amz-Cf-Id": x_amz_cf_id,
                    "X-delay-time": str(x_delay_time) if is_given(x_delay_time) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ChatCreateCompletionResponse,
            self._post(
                "/v1/chat/completions",
                body=maybe_transform(
                    {
                        "model": model,
                        "api_extra_body": api_extra_body,
                        "frequency_penalty": frequency_penalty,
                        "logit_bias": logit_bias,
                        "logprobs": logprobs,
                        "max_completion_tokens": max_completion_tokens,
                        "max_tokens": max_tokens,
                        "messages": messages,
                        "min_completion_tokens": min_completion_tokens,
                        "min_tokens": min_tokens,
                        "n": n,
                        "parallel_tool_calls": parallel_tool_calls,
                        "presence_penalty": presence_penalty,
                        "response_format": response_format,
                        "seed": seed,
                        "service_tier": service_tier,
                        "stop": stop,
                        "stream": stream,
                        "stream_options": stream_options,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_logprobs": top_logprobs,
                        "top_p": top_p,
                        "user": user,
                    },
                    chat_create_completion_params.ChatCreateCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCreateCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tejass-cerebras/Thing#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tejass-cerebras/Thing#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    @overload
    async def create_completion(
        self,
        *,
        model: str,
        api_extra_body: Optional[object] | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        messages: Optional[
            Iterable[chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestMessage]
        ]
        | NotGiven = NOT_GIVEN,
        min_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestResponseFormat
        ]
        | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[StreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestToolChoice
        ]
        | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[ToolParam]] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateCompletionResponse:
        """
        Chat

        Args:
          api_extra_body: Extra body parameters for /v1/chat/completions endpoint. This class is used to
              define additional fields that can be included in the request body that are not
              currently supported by the OpenAI API.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the content of
              message.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and reasoning tokens.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length. This value is now deprecated in favor of max_completion_tokens.

          min_completion_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          min_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep n as 1 to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: A response format for text.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming.

          temperature: What sampling temperature to use, between 0 and 1.5. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: A choice object.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability. logprobs
              must be set to true if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help Cerebras to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create_completion(
        self,
        *,
        model: str,
        api_extra_body: Optional[
            chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestExtraBody
        ]
        | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        messages: Optional[
            Iterable[chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestMessage]
        ]
        | NotGiven = NOT_GIVEN,
        min_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[
            chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestResponseFormat
        ]
        | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[StreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[
            chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestToolChoice
        ]
        | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[ToolParam]] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateCompletionResponse:
        """
        Chat

        Args:
          api_extra_body: Extra body parameters for Llama for /v1/chat/completions.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the content of
              message.

          max_completion_tokens: An upper bound for the number of tokens that can be generated for a completion,
              including visible output tokens and reasoning tokens.

          max_tokens: The maximum number of tokens that can be generated in the chat completion. The
              total length of input tokens and generated tokens is limited by the model's
              context length. This value is now deprecated in favor of max_completion_tokens.

          min_completion_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          min_tokens: The minimum number of tokens to generate for a completion. If not specified or
              set to 0, the model will generate as many tokens as it deems necessary. Setting
              to -1 sets to max sequence length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep n as 1 to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: A response format for text.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result. Determinism is not guaranteed.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream_options: Options for streaming.

          temperature: What sampling temperature to use, between 0 and 1.5. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic. We generally recommend altering this or `top_p` but
              not both.

          tool_choice: A choice object.

          top_logprobs: An integer between 0 and 20 specifying the number of most likely tokens to
              return at each token position, each with an associated log probability. logprobs
              must be set to true if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered. We
              generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help Cerebras to
              monitor and detect abuse.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["model"])
    async def create_completion(
        self,
        *,
        model: str,
        api_extra_body: Optional[object]
        | Optional[chat_create_completion_params.LlamaChatCompletionsExtraBodyCerebrasChatCompletionRequestExtraBody]
        | NotGiven = NOT_GIVEN,
        frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        logit_bias: Optional[object] | NotGiven = NOT_GIVEN,
        logprobs: Optional[bool] | NotGiven = NOT_GIVEN,
        max_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        messages: Optional[
            Iterable[chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestMessage]
        ]
        | NotGiven = NOT_GIVEN,
        min_completion_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        min_tokens: Optional[int] | NotGiven = NOT_GIVEN,
        n: Optional[int] | NotGiven = NOT_GIVEN,
        parallel_tool_calls: Optional[bool] | NotGiven = NOT_GIVEN,
        presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
        response_format: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestResponseFormat
        ]
        | NotGiven = NOT_GIVEN,
        seed: Optional[int] | NotGiven = NOT_GIVEN,
        service_tier: Optional[Literal["auto", "default"]] | NotGiven = NOT_GIVEN,
        stop: Union[str, List[str], None] | NotGiven = NOT_GIVEN,
        stream: Optional[bool] | NotGiven = NOT_GIVEN,
        stream_options: Optional[StreamOptionsParam] | NotGiven = NOT_GIVEN,
        temperature: Optional[float] | NotGiven = NOT_GIVEN,
        tool_choice: Optional[
            chat_create_completion_params.CerebrasChatCompletionsExtraBodyCerebrasChatCompletionRequestToolChoice
        ]
        | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[ToolParam]] | NotGiven = NOT_GIVEN,
        top_logprobs: Optional[int] | NotGiven = NOT_GIVEN,
        top_p: Optional[float] | NotGiven = NOT_GIVEN,
        user: Optional[str] | NotGiven = NOT_GIVEN,
        cf_ray: str | NotGiven = NOT_GIVEN,
        x_amz_cf_id: str | NotGiven = NOT_GIVEN,
        x_delay_time: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateCompletionResponse:
        extra_headers = {
            **strip_not_given(
                {
                    "CF-RAY": cf_ray,
                    "X-Amz-Cf-Id": x_amz_cf_id,
                    "X-delay-time": str(x_delay_time) if is_given(x_delay_time) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ChatCreateCompletionResponse,
            await self._post(
                "/v1/chat/completions",
                body=await async_maybe_transform(
                    {
                        "model": model,
                        "api_extra_body": api_extra_body,
                        "frequency_penalty": frequency_penalty,
                        "logit_bias": logit_bias,
                        "logprobs": logprobs,
                        "max_completion_tokens": max_completion_tokens,
                        "max_tokens": max_tokens,
                        "messages": messages,
                        "min_completion_tokens": min_completion_tokens,
                        "min_tokens": min_tokens,
                        "n": n,
                        "parallel_tool_calls": parallel_tool_calls,
                        "presence_penalty": presence_penalty,
                        "response_format": response_format,
                        "seed": seed,
                        "service_tier": service_tier,
                        "stop": stop,
                        "stream": stream,
                        "stream_options": stream_options,
                        "temperature": temperature,
                        "tool_choice": tool_choice,
                        "tools": tools,
                        "top_logprobs": top_logprobs,
                        "top_p": top_p,
                        "user": user,
                    },
                    chat_create_completion_params.ChatCreateCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ChatCreateCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_raw_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_raw_response_wrapper(
            chat.create_completion,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create_completion = to_streamed_response_wrapper(
            chat.create_completion,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create_completion = async_to_streamed_response_wrapper(
            chat.create_completion,
        )
