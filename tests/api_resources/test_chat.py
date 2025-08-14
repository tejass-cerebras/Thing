# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from new_cerebras_sdk import NewCerebrasSDK, AsyncNewCerebrasSDK
from new_cerebras_sdk.types import ChatCreateCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_overload_1(self, client: NewCerebrasSDK) -> None:
        chat = client.chat.create_completion(
            model="model",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params_overload_1(self, client: NewCerebrasSDK) -> None:
        chat = client.chat.create_completion(
            model="model",
            api_extra_body={},
            frequency_penalty=-2,
            logit_bias={},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            messages=[
                {
                    "content": "string",
                    "name": "name",
                    "role": "system",
                }
            ],
            min_completion_tokens=0,
            min_tokens=0,
            n=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "text"},
            seed=0,
            service_tier="auto",
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {},
                        "strict": True,
                    },
                    "type": "type",
                }
            ],
            top_logprobs=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion_overload_1(self, client: NewCerebrasSDK) -> None:
        response = client.chat.with_raw_response.create_completion(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion_overload_1(self, client: NewCerebrasSDK) -> None:
        with client.chat.with_streaming_response.create_completion(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_overload_2(self, client: NewCerebrasSDK) -> None:
        chat = client.chat.create_completion(
            model="model",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_completion_with_all_params_overload_2(self, client: NewCerebrasSDK) -> None:
        chat = client.chat.create_completion(
            model="model",
            api_extra_body={"repetition_penalty": 0},
            frequency_penalty=-2,
            logit_bias={},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            messages=[
                {
                    "content": "string",
                    "name": "name",
                    "role": "system",
                }
            ],
            min_completion_tokens=0,
            min_tokens=0,
            n=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "text"},
            seed=0,
            service_tier="auto",
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {},
                        "strict": True,
                    },
                    "type": "type",
                }
            ],
            top_logprobs=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_completion_overload_2(self, client: NewCerebrasSDK) -> None:
        response = client.chat.with_raw_response.create_completion(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_completion_overload_2(self, client: NewCerebrasSDK) -> None:
        with client.chat.with_streaming_response.create_completion(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        chat = await async_client.chat.create_completion(
            model="model",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        chat = await async_client.chat.create_completion(
            model="model",
            api_extra_body={},
            frequency_penalty=-2,
            logit_bias={},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            messages=[
                {
                    "content": "string",
                    "name": "name",
                    "role": "system",
                }
            ],
            min_completion_tokens=0,
            min_tokens=0,
            n=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "text"},
            seed=0,
            service_tier="auto",
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {},
                        "strict": True,
                    },
                    "type": "type",
                }
            ],
            top_logprobs=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        chat = await async_client.chat.create_completion(
            model="model",
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_completion_with_all_params_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        chat = await async_client.chat.create_completion(
            model="model",
            api_extra_body={"repetition_penalty": 0},
            frequency_penalty=-2,
            logit_bias={},
            logprobs=True,
            max_completion_tokens=0,
            max_tokens=0,
            messages=[
                {
                    "content": "string",
                    "name": "name",
                    "role": "system",
                }
            ],
            min_completion_tokens=0,
            min_tokens=0,
            n=0,
            parallel_tool_calls=True,
            presence_penalty=-2,
            response_format={"type": "text"},
            seed=0,
            service_tier="auto",
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            temperature=0,
            tool_choice="none",
            tools=[
                {
                    "function": {
                        "name": "name",
                        "description": "description",
                        "parameters": {},
                        "strict": True,
                    },
                    "type": "type",
                }
            ],
            top_logprobs=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_completion_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.chat.with_raw_response.create_completion(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_completion_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.chat.with_streaming_response.create_completion(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True
