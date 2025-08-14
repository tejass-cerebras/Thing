# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from new_cerebras_sdk import NewCerebrasSDK, AsyncNewCerebrasSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTcpWarming:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NewCerebrasSDK) -> None:
        tcp_warming = client.tcp_warming.retrieve()
        assert_matches_type(object, tcp_warming, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NewCerebrasSDK) -> None:
        response = client.tcp_warming.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tcp_warming = response.parse()
        assert_matches_type(object, tcp_warming, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NewCerebrasSDK) -> None:
        with client.tcp_warming.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tcp_warming = response.parse()
            assert_matches_type(object, tcp_warming, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTcpWarming:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        tcp_warming = await async_client.tcp_warming.retrieve()
        assert_matches_type(object, tcp_warming, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.tcp_warming.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tcp_warming = await response.parse()
        assert_matches_type(object, tcp_warming, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.tcp_warming.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tcp_warming = await response.parse()
            assert_matches_type(object, tcp_warming, path=["response"])

        assert cast(Any, response.is_closed) is True
