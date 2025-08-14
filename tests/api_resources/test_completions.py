# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from new_cerebras_sdk import NewCerebrasSDK, AsyncNewCerebrasSDK
from new_cerebras_sdk.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: NewCerebrasSDK) -> None:
        completion = client.completions.create(
            model="model",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: NewCerebrasSDK) -> None:
        completion = client.completions.create(
            model="model",
            best_of=0,
            echo=True,
            api_extra_body={},
            frequency_penalty=-2,
            grammar_root="grammar_root",
            logit_bias={},
            logprobs=True,
            max_tokens=0,
            min_tokens=0,
            n=0,
            presence_penalty=-2,
            prompt="string",
            return_raw_tokens=True,
            seed=0,
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: NewCerebrasSDK) -> None:
        response = client.completions.with_raw_response.create(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: NewCerebrasSDK) -> None:
        with client.completions.with_streaming_response.create(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: NewCerebrasSDK) -> None:
        completion = client.completions.create(
            model="model",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: NewCerebrasSDK) -> None:
        completion = client.completions.create(
            model="model",
            best_of=0,
            echo=True,
            api_extra_body={"repetition_penalty": 0},
            frequency_penalty=-2,
            grammar_root="grammar_root",
            logit_bias={},
            logprobs=True,
            max_tokens=0,
            min_tokens=0,
            n=0,
            presence_penalty=-2,
            prompt="string",
            return_raw_tokens=True,
            seed=0,
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: NewCerebrasSDK) -> None:
        response = client.completions.with_raw_response.create(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: NewCerebrasSDK) -> None:
        with client.completions.with_streaming_response.create(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        completion = await async_client.completions.create(
            model="model",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        completion = await async_client.completions.create(
            model="model",
            best_of=0,
            echo=True,
            api_extra_body={},
            frequency_penalty=-2,
            grammar_root="grammar_root",
            logit_bias={},
            logprobs=True,
            max_tokens=0,
            min_tokens=0,
            n=0,
            presence_penalty=-2,
            prompt="string",
            return_raw_tokens=True,
            seed=0,
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        completion = await async_client.completions.create(
            model="model",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        completion = await async_client.completions.create(
            model="model",
            best_of=0,
            echo=True,
            api_extra_body={"repetition_penalty": 0},
            frequency_penalty=-2,
            grammar_root="grammar_root",
            logit_bias={},
            logprobs=True,
            max_tokens=0,
            min_tokens=0,
            n=0,
            presence_penalty=-2,
            prompt="string",
            return_raw_tokens=True,
            seed=0,
            stop="string",
            stream=True,
            stream_options={"include_usage": True},
            suffix="suffix",
            temperature=0,
            top_p=0,
            user="user",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
            x_delay_time=0,
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.completions.with_raw_response.create(
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.completions.with_streaming_response.create(
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True
