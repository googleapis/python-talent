# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import (
    Any,
    AsyncIterator,
    Awaitable,
    Callable,
    Sequence,
    Tuple,
    Optional,
    Iterator,
)

from google.cloud.talent_v4beta1.types import job
from google.cloud.talent_v4beta1.types import job_service


class ListJobsPager:
    """A pager for iterating through ``list_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.talent_v4beta1.types.ListJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListJobs`` requests and continue to iterate
    through the ``jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.talent_v4beta1.types.ListJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., job_service.ListJobsResponse],
        request: job_service.ListJobsRequest,
        response: job_service.ListJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.talent_v4beta1.types.ListJobsRequest):
                The initial request object.
            response (google.cloud.talent_v4beta1.types.ListJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = job_service.ListJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[job_service.ListJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[job.Job]:
        for page in self.pages:
            yield from page.jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListJobsAsyncPager:
    """A pager for iterating through ``list_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.talent_v4beta1.types.ListJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListJobs`` requests and continue to iterate
    through the ``jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.talent_v4beta1.types.ListJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[job_service.ListJobsResponse]],
        request: job_service.ListJobsRequest,
        response: job_service.ListJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.talent_v4beta1.types.ListJobsRequest):
                The initial request object.
            response (google.cloud.talent_v4beta1.types.ListJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = job_service.ListJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[job_service.ListJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[job.Job]:
        async def async_generator():
            async for page in self.pages:
                for response in page.jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchJobsPager:
    """A pager for iterating through ``search_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``matching_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchJobs`` requests and continue to iterate
    through the ``matching_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., job_service.SearchJobsResponse],
        request: job_service.SearchJobsRequest,
        response: job_service.SearchJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.talent_v4beta1.types.SearchJobsRequest):
                The initial request object.
            response (google.cloud.talent_v4beta1.types.SearchJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = job_service.SearchJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[job_service.SearchJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[job_service.SearchJobsResponse.MatchingJob]:
        for page in self.pages:
            yield from page.matching_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchJobsAsyncPager:
    """A pager for iterating through ``search_jobs`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``matching_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchJobs`` requests and continue to iterate
    through the ``matching_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[job_service.SearchJobsResponse]],
        request: job_service.SearchJobsRequest,
        response: job_service.SearchJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.talent_v4beta1.types.SearchJobsRequest):
                The initial request object.
            response (google.cloud.talent_v4beta1.types.SearchJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = job_service.SearchJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[job_service.SearchJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[job_service.SearchJobsResponse.MatchingJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.matching_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchJobsForAlertPager:
    """A pager for iterating through ``search_jobs_for_alert`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``matching_jobs`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchJobsForAlert`` requests and continue to iterate
    through the ``matching_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., job_service.SearchJobsResponse],
        request: job_service.SearchJobsRequest,
        response: job_service.SearchJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.talent_v4beta1.types.SearchJobsRequest):
                The initial request object.
            response (google.cloud.talent_v4beta1.types.SearchJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = job_service.SearchJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[job_service.SearchJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[job_service.SearchJobsResponse.MatchingJob]:
        for page in self.pages:
            yield from page.matching_jobs

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchJobsForAlertAsyncPager:
    """A pager for iterating through ``search_jobs_for_alert`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``matching_jobs`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchJobsForAlert`` requests and continue to iterate
    through the ``matching_jobs`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.talent_v4beta1.types.SearchJobsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[job_service.SearchJobsResponse]],
        request: job_service.SearchJobsRequest,
        response: job_service.SearchJobsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.talent_v4beta1.types.SearchJobsRequest):
                The initial request object.
            response (google.cloud.talent_v4beta1.types.SearchJobsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = job_service.SearchJobsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[job_service.SearchJobsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterator[job_service.SearchJobsResponse.MatchingJob]:
        async def async_generator():
            async for page in self.pages:
                for response in page.matching_jobs:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
