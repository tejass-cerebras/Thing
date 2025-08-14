# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from new_cerebras_sdk import NewCerebrasSDK, AsyncNewCerebrasSDK
from new_cerebras_sdk.types import ModelMetadata, ModelListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: NewCerebrasSDK) -> None:
        model = client.models.retrieve(
            model_id="model_id",
        )
        assert_matches_type(ModelMetadata, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: NewCerebrasSDK) -> None:
        model = client.models.retrieve(
            model_id="model_id",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
        )
        assert_matches_type(ModelMetadata, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: NewCerebrasSDK) -> None:
        response = client.models.with_raw_response.retrieve(
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelMetadata, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: NewCerebrasSDK) -> None:
        with client.models.with_streaming_response.retrieve(
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelMetadata, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: NewCerebrasSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            client.models.with_raw_response.retrieve(
                model_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: NewCerebrasSDK) -> None:
        model = client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: NewCerebrasSDK) -> None:
        model = client.models.list(
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
        )
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: NewCerebrasSDK) -> None:
        response = client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: NewCerebrasSDK) -> None:
        with client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        model = await async_client.models.retrieve(
            model_id="model_id",
        )
        assert_matches_type(ModelMetadata, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncNewCerebrasSDK) -> None:
        model = await async_client.models.retrieve(
            model_id="model_id",
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
        )
        assert_matches_type(ModelMetadata, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.models.with_raw_response.retrieve(
            model_id="model_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelMetadata, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.models.with_streaming_response.retrieve(
            model_id="model_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelMetadata, model, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncNewCerebrasSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `model_id` but received ''"):
            await async_client.models.with_raw_response.retrieve(
                model_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncNewCerebrasSDK) -> None:
        model = await async_client.models.list()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncNewCerebrasSDK) -> None:
        model = await async_client.models.list(
            cf_ray="CF-RAY",
            x_amz_cf_id="X-Amz-Cf-Id",
        )
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncNewCerebrasSDK) -> None:
        response = await async_client.models.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelListResponse, model, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncNewCerebrasSDK) -> None:
        async with async_client.models.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelListResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
