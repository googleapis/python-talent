# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.cloud.talent.v4beta1 ApplicationService API."""

import functools
import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.talent_v4beta1.gapic import application_service_client_config
from google.cloud.talent_v4beta1.gapic import enums
from google.cloud.talent_v4beta1.gapic.transports import (
    application_service_grpc_transport,
)
from google.cloud.talent_v4beta1.proto import application_pb2
from google.cloud.talent_v4beta1.proto import application_service_pb2
from google.cloud.talent_v4beta1.proto import application_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import common_pb2
from google.cloud.talent_v4beta1.proto import company_pb2
from google.cloud.talent_v4beta1.proto import company_service_pb2
from google.cloud.talent_v4beta1.proto import company_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import completion_service_pb2
from google.cloud.talent_v4beta1.proto import completion_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import filters_pb2
from google.cloud.talent_v4beta1.proto import histogram_pb2
from google.cloud.talent_v4beta1.proto import job_pb2
from google.cloud.talent_v4beta1.proto import job_service_pb2
from google.cloud.talent_v4beta1.proto import job_service_pb2_grpc
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-talent").version


class ApplicationServiceClient(object):
    """
    A service that handles application management, including CRUD and
    enumeration.
    """

    SERVICE_ADDRESS = "jobs.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.talent.v4beta1.ApplicationService"

    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ApplicationServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def application_path(cls, project, tenant, profile, application):
        """Return a fully-qualified application string."""
        return google.api_core.path_template.expand(
            "projects/{project}/tenants/{tenant}/profiles/{profile}/applications/{application}",
            project=project,
            tenant=tenant,
            profile=profile,
            application=application,
        )

    @classmethod
    def company_path(cls, project, tenant, company):
        """Return a fully-qualified company string."""
        return google.api_core.path_template.expand(
            "projects/{project}/tenants/{tenant}/companies/{company}",
            project=project,
            tenant=tenant,
            company=company,
        )

    @classmethod
    def company_without_tenant_path(cls, project, company):
        """Return a fully-qualified company_without_tenant string."""
        return google.api_core.path_template.expand(
            "projects/{project}/companies/{company}", project=project, company=company
        )

    @classmethod
    def job_path(cls, project, tenant, job):
        """Return a fully-qualified job string."""
        return google.api_core.path_template.expand(
            "projects/{project}/tenants/{tenant}/jobs/{job}",
            project=project,
            tenant=tenant,
            job=job,
        )

    @classmethod
    def job_without_tenant_path(cls, project, job):
        """Return a fully-qualified job_without_tenant string."""
        return google.api_core.path_template.expand(
            "projects/{project}/jobs/{job}", project=project, job=job
        )

    @classmethod
    def profile_path(cls, project, tenant, profile):
        """Return a fully-qualified profile string."""
        return google.api_core.path_template.expand(
            "projects/{project}/tenants/{tenant}/profiles/{profile}",
            project=project,
            tenant=tenant,
            profile=profile,
        )

    def __init__(
        self,
        transport=None,
        channel=None,
        credentials=None,
        client_config=None,
        client_info=None,
        client_options=None,
    ):
        """Constructor.

        Args:
            transport (Union[~.ApplicationServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.ApplicationServiceGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn(
                "The `client_config` argument is deprecated.",
                PendingDeprecationWarning,
                stacklevel=2,
            )
        else:
            client_config = application_service_client_config.config

        if channel:
            warnings.warn(
                "The `channel` argument is deprecated; use " "`transport` instead.",
                PendingDeprecationWarning,
                stacklevel=2,
            )

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(
                    client_options
                )
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=application_service_grpc_transport.ApplicationServiceGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        "Received both a transport instance and "
                        "credentials; these are mutually exclusive."
                    )
                self.transport = transport
        else:
            self.transport = application_service_grpc_transport.ApplicationServiceGrpcTransport(
                address=api_endpoint, channel=channel, credentials=credentials
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config["interfaces"][self._INTERFACE_NAME]
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def delete_application(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes specified application.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.ApplicationServiceClient()
            >>>
            >>> name = client.application_path('[PROJECT]', '[TENANT]', '[PROFILE]', '[APPLICATION]')
            >>>
            >>> client.delete_application(name)

        Args:
            name (str): Required. The resource name of the application to be deleted.

                The format is
                "projects/{project\_id}/tenants/{tenant\_id}/profiles/{profile\_id}/applications/{application\_id}".
                For example, "projects/foo/tenants/bar/profiles/baz/applications/qux".
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "delete_application" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_application"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_application,
                default_retry=self._method_configs["DeleteApplication"].retry,
                default_timeout=self._method_configs["DeleteApplication"].timeout,
                client_info=self._client_info,
            )

        request = application_service_pb2.DeleteApplicationRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        self._inner_api_calls["delete_application"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_application(
        self,
        parent,
        application,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new application entity.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.ApplicationServiceClient()
            >>>
            >>> parent = client.profile_path('[PROJECT]', '[TENANT]', '[PROFILE]')
            >>>
            >>> # TODO: Initialize `application`:
            >>> application = {}
            >>>
            >>> response = client.create_application(parent, application)

        Args:
            parent (str): Required. Resource name of the profile under which the application is
                created.

                The format is
                "projects/{project\_id}/tenants/{tenant\_id}/profiles/{profile\_id}".
                For example, "projects/foo/tenants/bar/profiles/baz".
            application (Union[dict, ~google.cloud.talent_v4beta1.types.Application]): Required. The application to be created.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.Application`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.talent_v4beta1.types.Application` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_application" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_application"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_application,
                default_retry=self._method_configs["CreateApplication"].retry,
                default_timeout=self._method_configs["CreateApplication"].timeout,
                client_info=self._client_info,
            )

        request = application_service_pb2.CreateApplicationRequest(
            parent=parent, application=application
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["create_application"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def get_application(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves specified application.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.ApplicationServiceClient()
            >>>
            >>> name = client.application_path('[PROJECT]', '[TENANT]', '[PROFILE]', '[APPLICATION]')
            >>>
            >>> response = client.get_application(name)

        Args:
            name (str): Required. The resource name of the application to be retrieved.

                The format is
                "projects/{project\_id}/tenants/{tenant\_id}/profiles/{profile\_id}/applications/{application\_id}".
                For example, "projects/foo/tenants/bar/profiles/baz/applications/qux".
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.talent_v4beta1.types.Application` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_application" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_application"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_application,
                default_retry=self._method_configs["GetApplication"].retry,
                default_timeout=self._method_configs["GetApplication"].timeout,
                client_info=self._client_info,
            )

        request = application_service_pb2.GetApplicationRequest(name=name)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("name", name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["get_application"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_application(
        self,
        application,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates specified application.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.ApplicationServiceClient()
            >>>
            >>> # TODO: Initialize `application`:
            >>> application = {}
            >>>
            >>> response = client.update_application(application)

        Args:
            application (Union[dict, ~google.cloud.talent_v4beta1.types.Application]): Required. The application resource to replace the current resource in the system.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.Application`
            update_mask (Union[dict, ~google.cloud.talent_v4beta1.types.FieldMask]): Strongly recommended for the best service experience.

                If ``update_mask`` is provided, only the specified fields in
                ``application`` are updated. Otherwise all the fields are updated.

                A field mask to specify the application fields to be updated. Only top
                level fields of ``Application`` are supported.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.FieldMask`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.talent_v4beta1.types.Application` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_application" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_application"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_application,
                default_retry=self._method_configs["UpdateApplication"].retry,
                default_timeout=self._method_configs["UpdateApplication"].timeout,
                client_info=self._client_info,
            )

        request = application_service_pb2.UpdateApplicationRequest(
            application=application, update_mask=update_mask
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("application.name", application.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_application"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_applications(
        self,
        parent,
        page_size=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists all applications associated with the profile.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.ApplicationServiceClient()
            >>>
            >>> parent = client.profile_path('[PROJECT]', '[TENANT]', '[PROFILE]')
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_applications(parent):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_applications(parent).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. Resource name of the profile under which the application is
                created.

                The format is
                "projects/{project\_id}/tenants/{tenant\_id}/profiles/{profile\_id}",
                for example, "projects/foo/tenants/bar/profiles/baz".
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.api_core.page_iterator.PageIterator` instance.
            An iterable of :class:`~google.cloud.talent_v4beta1.types.Application` instances.
            You can also iterate over the pages of the response
            using its `pages` property.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "list_applications" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_applications"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_applications,
                default_retry=self._method_configs["ListApplications"].retry,
                default_timeout=self._method_configs["ListApplications"].timeout,
                client_info=self._client_info,
            )

        request = application_service_pb2.ListApplicationsRequest(
            parent=parent, page_size=page_size
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("parent", parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        iterator = google.api_core.page_iterator.GRPCIterator(
            client=None,
            method=functools.partial(
                self._inner_api_calls["list_applications"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="applications",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator
