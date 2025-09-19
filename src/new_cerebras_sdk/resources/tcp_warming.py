# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["TcpWarmingResource", "AsyncTcpWarmingResource"]


class TcpWarmingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TcpWarmingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tejass-cerebras/Thing#accessing-raw-response-data-eg-headers
        """
        return TcpWarmingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TcpWarmingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tejass-cerebras/Thing#with_streaming_response
        """
        return TcpWarmingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Tcp Warming"""
        return self._get(
            "/v1/tcp_warming",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTcpWarmingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTcpWarmingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/tejass-cerebras/Thing#accessing-raw-response-data-eg-headers
        """
        return AsyncTcpWarmingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTcpWarmingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/tejass-cerebras/Thing#with_streaming_response
        """
        return AsyncTcpWarmingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Tcp Warming"""
        return await self._get(
            "/v1/tcp_warming",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TcpWarmingResourceWithRawResponse:
    def __init__(self, tcp_warming: TcpWarmingResource) -> None:
        self._tcp_warming = tcp_warming

        self.retrieve = to_raw_response_wrapper(
            tcp_warming.retrieve,
        )


class AsyncTcpWarmingResourceWithRawResponse:
    def __init__(self, tcp_warming: AsyncTcpWarmingResource) -> None:
        self._tcp_warming = tcp_warming

        self.retrieve = async_to_raw_response_wrapper(
            tcp_warming.retrieve,
        )


class TcpWarmingResourceWithStreamingResponse:
    def __init__(self, tcp_warming: TcpWarmingResource) -> None:
        self._tcp_warming = tcp_warming

        self.retrieve = to_streamed_response_wrapper(
            tcp_warming.retrieve,
        )


class AsyncTcpWarmingResourceWithStreamingResponse:
    def __init__(self, tcp_warming: AsyncTcpWarmingResource) -> None:
        self._tcp_warming = tcp_warming

        self.retrieve = async_to_streamed_response_wrapper(
            tcp_warming.retrieve,
        )
