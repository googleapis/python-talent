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

"""Accesses the google.cloud.talent.v4beta1 JobService API."""

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
import google.api_core.operation
import google.api_core.operations_v1
import google.api_core.page_iterator
import google.api_core.path_template
import grpc

from google.cloud.talent_v4beta1.gapic import enums
from google.cloud.talent_v4beta1.gapic import job_service_client_config
from google.cloud.talent_v4beta1.gapic.transports import job_service_grpc_transport
from google.cloud.talent_v4beta1.proto import application_pb2
from google.cloud.talent_v4beta1.proto import application_service_pb2
from google.cloud.talent_v4beta1.proto import application_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import common_pb2
from google.cloud.talent_v4beta1.proto import company_pb2
from google.cloud.talent_v4beta1.proto import company_service_pb2
from google.cloud.talent_v4beta1.proto import company_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import completion_service_pb2
from google.cloud.talent_v4beta1.proto import completion_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import event_pb2
from google.cloud.talent_v4beta1.proto import event_service_pb2
from google.cloud.talent_v4beta1.proto import event_service_pb2_grpc
from google.cloud.talent_v4beta1.proto import filters_pb2
from google.cloud.talent_v4beta1.proto import histogram_pb2
from google.cloud.talent_v4beta1.proto import job_pb2
from google.cloud.talent_v4beta1.proto import job_service_pb2
from google.cloud.talent_v4beta1.proto import job_service_pb2_grpc
from google.longrunning import operations_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution("google-cloud-talent").version


class JobServiceClient(object):
    """A service handles job management, including job CRUD, enumeration and search."""

    SERVICE_ADDRESS = "jobs.googleapis.com:443"
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = "google.cloud.talent.v4beta1.JobService"

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
            JobServiceClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

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
    def project_path(cls, project):
        """Return a fully-qualified project string."""
        return google.api_core.path_template.expand(
            "projects/{project}", project=project
        )

    @classmethod
    def tenant_path(cls, project, tenant):
        """Return a fully-qualified tenant string."""
        return google.api_core.path_template.expand(
            "projects/{project}/tenants/{tenant}", project=project, tenant=tenant
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
            transport (Union[~.JobServiceGrpcTransport,
                    Callable[[~.Credentials, type], ~.JobServiceGrpcTransport]): A transport
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
            client_config = job_service_client_config.config

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
                    default_class=job_service_grpc_transport.JobServiceGrpcTransport,
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
            self.transport = job_service_grpc_transport.JobServiceGrpcTransport(
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
    def delete_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Deletes the specified job.

        Typically, the job becomes unsearchable within 10 seconds, but it may take
        up to 5 minutes.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[TENANT]', '[JOB]')
            >>>
            >>> client.delete_job(name)

        Args:
            name (str): Controls whether highly similar jobs are returned next to each other
                in the search results. Jobs are identified as highly similar based on
                their titles, job categories, and locations. Highly similar results are
                clustered so that only one representative job of the cluster is
                displayed to the job seeker higher up in the results, with the other
                jobs being displayed lower down in the results.

                Defaults to ``DiversificationLevel.SIMPLE`` if no value is specified.
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
        if "delete_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "delete_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_job,
                default_retry=self._method_configs["DeleteJob"].retry,
                default_timeout=self._method_configs["DeleteJob"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.DeleteJobRequest(name=name)
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

        self._inner_api_calls["delete_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def create_job(
        self,
        parent,
        job,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Creates a new job.

        Typically, the job becomes searchable within 10 seconds, but it may take
        up to 5 minutes.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `job`:
            >>> job = {}
            >>>
            >>> response = client.create_job(parent, job)

        Args:
            parent (str): Exactly one of ``string_values`` or ``long_values`` must be
                specified.

                This field is used to perform number range search. (``EQ``, ``GT``,
                ``GE``, ``LE``, ``LT``) over filterable ``long_value``.

                Currently at most 1 ``long_values`` is supported.
            job (Union[dict, ~google.cloud.talent_v4beta1.types.Job]): Required. The Job to be created.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.Job`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.talent_v4beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "create_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "create_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_job,
                default_retry=self._method_configs["CreateJob"].retry,
                default_timeout=self._method_configs["CreateJob"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.CreateJobRequest(parent=parent, job=job)
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

        return self._inner_api_calls["create_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_create_jobs(
        self,
        parent,
        jobs,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Begins executing a batch create jobs operation.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `jobs`:
            >>> jobs = []
            >>>
            >>> response = client.batch_create_jobs(parent, jobs)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): A Location identifies a piece of source code in a .proto file which
                corresponds to a particular definition. This information is intended to
                be useful to IDEs, code indexers, documentation generators, and similar
                tools.

                For example, say we have a file like: message Foo { optional string foo
                = 1; } Let's look at just the field definition: optional string foo = 1;
                ^ ^^ ^^ ^ ^^^ a bc de f ghi We have the following locations: span path
                represents [a,i) [ 4, 0, 2, 0 ] The whole field definition. [a,b) [ 4,
                0, 2, 0, 4 ] The label (optional). [c,d) [ 4, 0, 2, 0, 5 ] The type
                (string). [e,f) [ 4, 0, 2, 0, 1 ] The name (foo). [g,h) [ 4, 0, 2, 0, 3
                ] The number (1).

                Notes:

                -  A location may refer to a repeated field itself (i.e. not to any
                   particular index within it). This is used whenever a set of elements
                   are logically enclosed in a single code segment. For example, an
                   entire extend block (possibly containing multiple extension
                   definitions) will have an outer location whose path refers to the
                   "extensions" repeated field without an index.
                -  Multiple locations may have the same path. This happens when a single
                   logical declaration is spread out across multiple places. The most
                   obvious example is the "extend" block again -- there may be multiple
                   extend blocks in the same scope, each of which will have the same
                   path.
                -  A location's span is not always a subset of its parent's span. For
                   example, the "extendee" of an extension declaration appears at the
                   beginning of the "extend" block and is shared by all extensions
                   within the block.
                -  Just because a location's span is a subset of some other location's
                   span does not mean that it is a descendant. For example, a "group"
                   defines both a type and a field in a single declaration. Thus, the
                   locations corresponding to the type and field and their components
                   will overlap.
                -  Code which tries to interpret locations should probably be designed
                   to ignore those that it doesn't understand, as more types of
                   locations could be recorded in the future.
            jobs (list[Union[dict, ~google.cloud.talent_v4beta1.types.Job]]): Required. The jobs to be created.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.Job`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.talent_v4beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_create_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_create_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_create_jobs,
                default_retry=self._method_configs["BatchCreateJobs"].retry,
                default_timeout=self._method_configs["BatchCreateJobs"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.BatchCreateJobsRequest(parent=parent, jobs=jobs)
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

        operation = self._inner_api_calls["batch_create_jobs"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            job_service_pb2.JobOperationResult,
            metadata_type=common_pb2.BatchOperationMetadata,
        )

    def get_job(
        self,
        name,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Retrieves the specified job, whose status is OPEN or recently EXPIRED
        within the last 90 days.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> name = client.job_path('[PROJECT]', '[TENANT]', '[JOB]')
            >>>
            >>> response = client.get_job(name)

        Args:
            name (str): The criteria determining how search results are sorted. Default is
                ``"relevance desc"``.

                Supported options are:

                -  ``"relevance desc"``: By relevance descending, as determined by the
                   API algorithms. Relevance thresholding of query results is only
                   available with this ordering.
                -  ``"posting_publish_time desc"``: By ``Job.posting_publish_time``
                   descending.
                -  ``"posting_update_time desc"``: By ``Job.posting_update_time``
                   descending.
                -  ``"title"``: By ``Job.title`` ascending.
                -  ``"title desc"``: By ``Job.title`` descending.
                -  ``"annualized_base_compensation"``: By job's
                   ``CompensationInfo.annualized_base_compensation_range`` ascending.
                   Jobs whose annualized base compensation is unspecified are put at the
                   end of search results.
                -  ``"annualized_base_compensation desc"``: By job's
                   ``CompensationInfo.annualized_base_compensation_range`` descending.
                   Jobs whose annualized base compensation is unspecified are put at the
                   end of search results.
                -  ``"annualized_total_compensation"``: By job's
                   ``CompensationInfo.annualized_total_compensation_range`` ascending.
                   Jobs whose annualized base compensation is unspecified are put at the
                   end of search results.
                -  ``"annualized_total_compensation desc"``: By job's
                   ``CompensationInfo.annualized_total_compensation_range`` descending.
                   Jobs whose annualized base compensation is unspecified are put at the
                   end of search results.
                -  ``"custom_ranking desc"``: By the relevance score adjusted to the
                   ``SearchJobsRequest.CustomRankingInfo.ranking_expression`` with
                   weight factor assigned by
                   ``SearchJobsRequest.CustomRankingInfo.importance_level`` in
                   descending order.
                -  Location sorting: Use the special syntax to order jobs by distance:
                   ``"distance_from('Hawaii')"``: Order by distance from Hawaii.
                   ``"distance_from(19.89, 155.5)"``: Order by distance from a
                   coordinate.
                   ``"distance_from('Hawaii'), distance_from('Puerto Rico')"``: Order by
                   multiple locations. See details below.
                   ``"distance_from('Hawaii'), distance_from(19.89, 155.5)"``: Order by
                   multiple locations. See details below. The string can have a maximum
                   of 256 characters. When multiple distance centers are provided, a job
                   that is close to any of the distance centers would have a high rank.
                   When a job has multiple locations, the job location closest to one of
                   the distance centers will be used. Jobs that don't have locations
                   will be ranked at the bottom. Distance is calculated with a precision
                   of 11.3 meters (37.4 feet). Diversification strategy is still applied
                   unless explicitly disabled in ``diversification_level``.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.talent_v4beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "get_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "get_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_job,
                default_retry=self._method_configs["GetJob"].retry,
                default_timeout=self._method_configs["GetJob"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.GetJobRequest(name=name)
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

        return self._inner_api_calls["get_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def update_job(
        self,
        job,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Updates specified job.

        Typically, updated contents become visible in search results within 10
        seconds, but it may take up to 5 minutes.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> # TODO: Initialize `job`:
            >>> job = {}
            >>>
            >>> response = client.update_job(job)

        Args:
            job (Union[dict, ~google.cloud.talent_v4beta1.types.Job]): Required. The Job to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.Job`
            update_mask (Union[dict, ~google.cloud.talent_v4beta1.types.FieldMask]): If the ``filterable`` flag is true, custom field values are
                searchable. If false, values are not searchable.

                Default is false.

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
            A :class:`~google.cloud.talent_v4beta1.types.Job` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "update_job" not in self._inner_api_calls:
            self._inner_api_calls[
                "update_job"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_job,
                default_retry=self._method_configs["UpdateJob"].retry,
                default_timeout=self._method_configs["UpdateJob"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.UpdateJobRequest(job=job, update_mask=update_mask)
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [("job.name", job.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(
                routing_header
            )
            metadata.append(routing_metadata)

        return self._inner_api_calls["update_job"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def batch_update_jobs(
        self,
        parent,
        jobs,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Begins executing a batch update jobs operation.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `jobs`:
            >>> jobs = []
            >>>
            >>> response = client.batch_update_jobs(parent, jobs)
            >>>
            >>> def callback(operation_future):
            ...     # Handle result.
            ...     result = operation_future.result()
            >>>
            >>> response.add_done_callback(callback)
            >>>
            >>> # Handle metadata.
            >>> metadata = response.metadata()

        Args:
            parent (str): The type of compensation.

                For compensation amounts specified in non-monetary amounts, describe the
                compensation scheme in the ``CompensationEntry.description``.

                For example, tipping format is described in
                ``CompensationEntry.description`` (for example, "expect 15-20% tips
                based on customer bill.") and an estimate of the tips provided in
                ``CompensationEntry.amount`` or ``CompensationEntry.range`` ($10 per
                hour).

                For example, equity is described in ``CompensationEntry.description``
                (for example, "1% - 2% equity vesting over 4 years, 1 year cliff") and
                value estimated in ``CompensationEntry.amount`` or
                ``CompensationEntry.range``. If no value estimate is possible, units are
                ``CompensationUnit.COMPENSATION_UNIT_UNSPECIFIED`` and then further
                clarified in ``CompensationEntry.description`` field.
            jobs (list[Union[dict, ~google.cloud.talent_v4beta1.types.Job]]): Required. The jobs to be updated.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.Job`
            update_mask (Union[dict, ~google.cloud.talent_v4beta1.types.FieldMask]): Strongly recommended for the best service experience.

                A unique ID generated in the API responses. It can be found in
                ``ResponseMetadata.request_id``.

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
            A :class:`~google.cloud.talent_v4beta1.types._OperationFuture` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if "batch_update_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_update_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_update_jobs,
                default_retry=self._method_configs["BatchUpdateJobs"].retry,
                default_timeout=self._method_configs["BatchUpdateJobs"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.BatchUpdateJobsRequest(
            parent=parent, jobs=jobs, update_mask=update_mask
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

        operation = self._inner_api_calls["batch_update_jobs"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )
        return google.api_core.operation.from_gapic(
            operation,
            self.transport._operations_client,
            job_service_pb2.JobOperationResult,
            metadata_type=common_pb2.BatchOperationMetadata,
        )

    def batch_delete_jobs(
        self,
        parent,
        filter_,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The list of languages of the query. This is the BCP-47 language
        code, such as "en-US" or "sr-Latn". For more information, see `Tags for
        Identifying Languages <https://tools.ietf.org/html/bcp47>`__.

        The maximum number of allowed characters is 255.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `filter_`:
            >>> filter_ = ''
            >>>
            >>> client.batch_delete_jobs(parent, filter_)

        Args:
            parent (str): If provided, restricts completion to specified company.

                The format is
                "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for
                example, "projects/foo/tenants/bar/companies/baz".

                If tenant id is unspecified, the default tenant is used, for example,
                "projects/foo".
            filter_ (str): JSON name of this field. The value is set by protocol compiler. If
                the user has set a "json_name" option on this field, that option's value
                will be used. Otherwise, it's deduced from the field's name by
                converting it to camelCase.
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
        if "batch_delete_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "batch_delete_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.batch_delete_jobs,
                default_retry=self._method_configs["BatchDeleteJobs"].retry,
                default_timeout=self._method_configs["BatchDeleteJobs"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.BatchDeleteJobsRequest(parent=parent, filter=filter_)
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

        self._inner_api_calls["batch_delete_jobs"](
            request, retry=retry, timeout=timeout, metadata=metadata
        )

    def list_jobs(
        self,
        parent,
        filter_,
        page_size=None,
        job_view=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        Lists jobs by filter.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `filter_`:
            >>> filter_ = ''
            >>>
            >>> # Iterate over all results
            >>> for element in client.list_jobs(parent, filter_):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.list_jobs(parent, filter_).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): The name of the uninterpreted option. Each string represents a
                segment in a dot-separated name. is_extension is true iff a segment
                represents an extension (denoted with parentheses in options specs in
                .proto files). E.g.,{ ["foo", false], ["bar.baz", true], ["qux", false]
                } represents "foo.(bar.baz).qux".
            filter_ (str): The scope of the completion. The defaults is
                ``CompletionScope.PUBLIC``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            job_view (~google.cloud.talent_v4beta1.types.JobView): A generic empty message that you can re-use to avoid defining
                duplicated empty messages in your APIs. A typical example is to use it
                as the request or the response type of an API method. For instance:

                ::

                    service Foo {
                      rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);
                    }

                The JSON representation for ``Empty`` is empty JSON object ``{}``.
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
            An iterable of :class:`~google.cloud.talent_v4beta1.types.Job` instances.
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
        if "list_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "list_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_jobs,
                default_retry=self._method_configs["ListJobs"].retry,
                default_timeout=self._method_configs["ListJobs"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.ListJobsRequest(
            parent=parent, filter=filter_, page_size=page_size, job_view=job_view
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
                self._inner_api_calls["list_jobs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="jobs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def search_jobs(
        self,
        parent,
        request_metadata,
        search_mode=None,
        job_query=None,
        enable_broadening=None,
        require_precise_result_size=None,
        histogram_queries=None,
        job_view=None,
        offset=None,
        page_size=None,
        order_by=None,
        diversification_level=None,
        custom_ranking_info=None,
        disable_keyword_match=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        The token specifying the current offset within search results. See
        ``SearchJobsResponse.next_page_token`` for an explanation of how to
        obtain the next set of query results.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `request_metadata`:
            >>> request_metadata = {}
            >>>
            >>> # Iterate over all results
            >>> for element in client.search_jobs(parent, request_metadata):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.search_jobs(parent, request_metadata).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The maximum travel time in seconds. The maximum allowed
                value is ``3600s`` (one hour). Format is ``123s``.
            request_metadata (Union[dict, ~google.cloud.talent_v4beta1.types.RequestMetadata]): Contains snippets of text from the ``Job.description`` and similar
                fields that most closely match a search query's keywords, if available.
                All HTML tags in the original fields are stripped when returned in this
                field, and matching query keywords are enclosed in HTML bold tags.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.RequestMetadata`
            search_mode (~google.cloud.talent_v4beta1.types.SearchMode): Output only. The job title snippet shows how the ``job_title`` is
                related to a search query. It's empty if the ``job_title`` isn't related
                to the search query.
            job_query (Union[dict, ~google.cloud.talent_v4beta1.types.JobQuery]): Query used to search against jobs, such as keyword, location filters, etc.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.JobQuery`
            enable_broadening (bool): Controls whether to broaden the search when it produces sparse results.
                Broadened queries append results to the end of the matching results
                list.

                Defaults to false.
            require_precise_result_size (bool): Additional information regarding long-running operations. In
                particular, this specifies the types that are returned from long-running
                operations.

                Required for methods that return ``google.longrunning.Operation``;
                invalid otherwise.
            histogram_queries (list[Union[dict, ~google.cloud.talent_v4beta1.types.HistogramQuery]]): ``FieldMask`` represents a set of symbolic field paths, for example:

                ::

                    paths: "f.a"
                    paths: "f.b.d"

                Here ``f`` represents a field in some root message, ``a`` and ``b``
                fields in the message found in ``f``, and ``d`` a field found in the
                message in ``f.b``.

                Field masks are used to specify a subset of fields that should be
                returned by a get operation or modified by an update operation. Field
                masks also have a custom JSON encoding (see below).

                # Field Masks in Projections

                When used in the context of a projection, a response message or
                sub-message is filtered by the API to only contain those fields as
                specified in the mask. For example, if the mask in the previous example
                is applied to a response message as follows:

                ::

                    f {
                      a : 22
                      b {
                        d : 1
                        x : 2
                      }
                      y : 13
                    }
                    z: 8

                The result will not contain specific values for fields x,y and z (their
                value will be set to the default, and omitted in proto text output):

                ::

                    f {
                      a : 22
                      b {
                        d : 1
                      }
                    }

                A repeated field is not allowed except at the last position of a paths
                string.

                If a FieldMask object is not present in a get operation, the operation
                applies to all fields (as if a FieldMask of all fields had been
                specified).

                Note that a field mask does not necessarily apply to the top-level
                response message. In case of a REST get operation, the field mask
                applies directly to the response, but in case of a REST list operation,
                the mask instead applies to each individual message in the returned
                resource list. In case of a REST custom method, other definitions may be
                used. Where the mask applies will be clearly documented together with
                its declaration in the API. In any case, the effect on the returned
                resource/resources is required behavior for APIs.

                # Field Masks in Update Operations

                A field mask in update operations specifies which fields of the targeted
                resource are going to be updated. The API is required to only change the
                values of the fields as specified in the mask and leave the others
                untouched. If a resource is passed in to describe the updated values,
                the API ignores the values of all fields not covered by the mask.

                If a repeated field is specified for an update operation, new values
                will be appended to the existing repeated field in the target resource.
                Note that a repeated field is only allowed in the last position of a
                ``paths`` string.

                If a sub-message is specified in the last position of the field mask for
                an update operation, then new value will be merged into the existing
                sub-message in the target resource.

                For example, given the target message:

                ::

                    f {
                      b {
                        d: 1
                        x: 2
                      }
                      c: [1]
                    }

                And an update message:

                ::

                    f {
                      b {
                        d: 10
                      }
                      c: [2]
                    }

                then if the field mask is:

                paths: ["f.b", "f.c"]

                then the result will be:

                ::

                    f {
                      b {
                        d: 10
                        x: 2
                      }
                      c: [1, 2]
                    }

                An implementation may provide options to override this default behavior
                for repeated and message fields.

                In order to reset a field's value to the default, the field must be in
                the mask and set to the default value in the provided resource. Hence,
                in order to reset all fields of a resource, provide a default instance
                of the resource and set all fields in the mask, or do not provide a mask
                as described below.

                If a field mask is not present on update, the operation applies to all
                fields (as if a field mask of all fields has been specified). Note that
                in the presence of schema evolution, this may mean that fields the
                client does not know and has therefore not filled into the request will
                be reset to their default. If this is unwanted behavior, a specific
                service may require a client to always specify a field mask, producing
                an error if not.

                As with get operations, the location of the resource which describes the
                updated values in the request message depends on the operation kind. In
                any case, the effect of the field mask is required to be honored by the
                API.

                ## Considerations for HTTP REST

                The HTTP kind of an update operation which uses a field mask must be set
                to PATCH instead of PUT in order to satisfy HTTP semantics (PUT must
                only be used for full updates).

                # JSON Encoding of Field Masks

                In JSON, a field mask is encoded as a single string where paths are
                separated by a comma. Fields name in each path are converted to/from
                lower-camel naming conventions.

                As an example, consider the following message declarations:

                ::

                    message Profile {
                      User user = 1;
                      Photo photo = 2;
                    }
                    message User {
                      string display_name = 1;
                      string address = 2;
                    }

                In proto a field mask for ``Profile`` may look as such:

                ::

                    mask {
                      paths: "user.display_name"
                      paths: "photo"
                    }

                In JSON, the same mask is represented as below:

                ::

                    {
                      mask: "user.displayName,photo"
                    }

                # Field Masks and Oneof Fields

                Field masks treat fields in oneofs just as regular fields. Consider the
                following message:

                ::

                    message SampleMessage {
                      oneof test_oneof {
                        string name = 4;
                        SubMessage sub_message = 9;
                      }
                    }

                The field mask can be:

                ::

                    mask {
                      paths: "name"
                    }

                Or:

                ::

                    mask {
                      paths: "sub_message"
                    }

                Note that oneof type names ("test_oneof" in this case) cannot be used in
                paths.

                ## Field Mask Verification

                The implementation of any API method which has a FieldMask type field in
                the request should verify the included field paths, and return an
                ``INVALID_ARGUMENT`` error if any path is unmappable.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.HistogramQuery`
            job_view (~google.cloud.talent_v4beta1.types.JobView): The language of the posting. This field is distinct from any
                requirements for fluency that are associated with the job.

                Language codes must be in BCP-47 format, such as "en-US" or "sr-Latn".
                For more information, see `Tags for Identifying
                Languages <https://tools.ietf.org/html/bcp47>`__\ {: class="external"
                target="_blank" }.

                If this field is unspecified and ``Job.description`` is present,
                detected language code based on ``Job.description`` is assigned,
                otherwise defaults to 'en_US'.
            offset (int): Commute information which is generated based on specified
                ``CommuteFilter``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            order_by (str): Manages long-running operations with an API service.

                When an API method normally takes long time to complete, it can be
                designed to return ``Operation`` to the client, and the client can use
                this interface to receive the real response asynchronously by polling
                the operation resource, or pass the operation resource to another API
                (such as Google Cloud Pub/Sub API) to receive the response. Any API
                service that returns long-running operations should implement the
                ``Operations`` interface so developers can have a consistent client
                experience.
            diversification_level (~google.cloud.talent_v4beta1.types.DiversificationLevel): The candidate's postal addresses. It's highly recommended to input
                this information as accurately as possible to help improve search
                quality. Here are some recommendations:

                -  Provide ``Address.usage`` if possible, especially if the address is
                   PERSONAL. During a search only personal addresses are considered. If
                   there is no such address, all addresses with unspecified usage are
                   assumed to be personal.
                -  Provide ``Address.current`` for the current address if possible.
                   During a search, only current addresses are considered. If there is
                   no such address, all addresses are assumed to be current.

                When displaying a candidate's addresses, it is sometimes desirable to
                limit the number of addresses shown. In these cases we recommend that
                you display the addresses in the following order of priority:

                1. ``Address.usage`` is PERSONAL and ``Address.current`` is true.
                2. ``Address.usage`` is PERSONAL and ``Address.current`` is false or not
                   set.
                3. ``Address.usage`` is CONTACT_INFO_USAGE_UNSPECIFIED and
                   ``Address.current`` is true.
                4. ``Address.usage`` is CONTACT_INFO_USAGE_UNSPECIFIED and
                   ``Address.current`` is false or not set.
            custom_ranking_info (Union[dict, ~google.cloud.talent_v4beta1.types.CustomRankingInfo]): Controls over how job documents get ranked on top of existing relevance
                score (determined by API algorithm).

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.CustomRankingInfo`
            disable_keyword_match (bool): Lists operations that match the specified filter in the request. If
                the server doesn't support this method, it returns ``UNIMPLEMENTED``.

                NOTE: the ``name`` binding allows API services to override the binding
                to use different resource name schemes, such as ``users/*/operations``.
                To override the binding, API services can add a binding such as
                ``"/v1/{name=users/*}/operations"`` to their service configuration. For
                backwards compatibility, the default name includes the operations
                collection id, however overriding users must ensure the name binding is
                the parent resource, without the operations collection id.
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
            An iterable of :class:`~google.cloud.talent_v4beta1.types.MatchingJob` instances.
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
        if "search_jobs" not in self._inner_api_calls:
            self._inner_api_calls[
                "search_jobs"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.search_jobs,
                default_retry=self._method_configs["SearchJobs"].retry,
                default_timeout=self._method_configs["SearchJobs"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.SearchJobsRequest(
            parent=parent,
            request_metadata=request_metadata,
            search_mode=search_mode,
            job_query=job_query,
            enable_broadening=enable_broadening,
            require_precise_result_size=require_precise_result_size,
            histogram_queries=histogram_queries,
            job_view=job_view,
            offset=offset,
            page_size=page_size,
            order_by=order_by,
            diversification_level=diversification_level,
            custom_ranking_info=custom_ranking_info,
            disable_keyword_match=disable_keyword_match,
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
                self._inner_api_calls["search_jobs"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="matching_jobs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator

    def search_jobs_for_alert(
        self,
        parent,
        request_metadata,
        search_mode=None,
        job_query=None,
        enable_broadening=None,
        require_precise_result_size=None,
        histogram_queries=None,
        job_view=None,
        offset=None,
        page_size=None,
        order_by=None,
        diversification_level=None,
        custom_ranking_info=None,
        disable_keyword_match=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
        """
        A developer-facing error message, which should be in English. Any
        user-facing error message should be localized and sent in the
        ``google.rpc.Status.details`` field, or localized by the client.

        Example:
            >>> from google.cloud import talent_v4beta1
            >>>
            >>> client = talent_v4beta1.JobServiceClient()
            >>>
            >>> parent = client.tenant_path('[PROJECT]', '[TENANT]')
            >>>
            >>> # TODO: Initialize `request_metadata`:
            >>> request_metadata = {}
            >>>
            >>> # Iterate over all results
            >>> for element in client.search_jobs_for_alert(parent, request_metadata):
            ...     # process element
            ...     pass
            >>>
            >>>
            >>> # Alternatively:
            >>>
            >>> # Iterate over results one page at a time
            >>> for page in client.search_jobs_for_alert(parent, request_metadata).pages:
            ...     for element in page:
            ...         # process element
            ...         pass

        Args:
            parent (str): Required. The maximum travel time in seconds. The maximum allowed
                value is ``3600s`` (one hour). Format is ``123s``.
            request_metadata (Union[dict, ~google.cloud.talent_v4beta1.types.RequestMetadata]): Contains snippets of text from the ``Job.description`` and similar
                fields that most closely match a search query's keywords, if available.
                All HTML tags in the original fields are stripped when returned in this
                field, and matching query keywords are enclosed in HTML bold tags.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.RequestMetadata`
            search_mode (~google.cloud.talent_v4beta1.types.SearchMode): Output only. The job title snippet shows how the ``job_title`` is
                related to a search query. It's empty if the ``job_title`` isn't related
                to the search query.
            job_query (Union[dict, ~google.cloud.talent_v4beta1.types.JobQuery]): Query used to search against jobs, such as keyword, location filters, etc.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.JobQuery`
            enable_broadening (bool): Controls whether to broaden the search when it produces sparse results.
                Broadened queries append results to the end of the matching results
                list.

                Defaults to false.
            require_precise_result_size (bool): Additional information regarding long-running operations. In
                particular, this specifies the types that are returned from long-running
                operations.

                Required for methods that return ``google.longrunning.Operation``;
                invalid otherwise.
            histogram_queries (list[Union[dict, ~google.cloud.talent_v4beta1.types.HistogramQuery]]): ``FieldMask`` represents a set of symbolic field paths, for example:

                ::

                    paths: "f.a"
                    paths: "f.b.d"

                Here ``f`` represents a field in some root message, ``a`` and ``b``
                fields in the message found in ``f``, and ``d`` a field found in the
                message in ``f.b``.

                Field masks are used to specify a subset of fields that should be
                returned by a get operation or modified by an update operation. Field
                masks also have a custom JSON encoding (see below).

                # Field Masks in Projections

                When used in the context of a projection, a response message or
                sub-message is filtered by the API to only contain those fields as
                specified in the mask. For example, if the mask in the previous example
                is applied to a response message as follows:

                ::

                    f {
                      a : 22
                      b {
                        d : 1
                        x : 2
                      }
                      y : 13
                    }
                    z: 8

                The result will not contain specific values for fields x,y and z (their
                value will be set to the default, and omitted in proto text output):

                ::

                    f {
                      a : 22
                      b {
                        d : 1
                      }
                    }

                A repeated field is not allowed except at the last position of a paths
                string.

                If a FieldMask object is not present in a get operation, the operation
                applies to all fields (as if a FieldMask of all fields had been
                specified).

                Note that a field mask does not necessarily apply to the top-level
                response message. In case of a REST get operation, the field mask
                applies directly to the response, but in case of a REST list operation,
                the mask instead applies to each individual message in the returned
                resource list. In case of a REST custom method, other definitions may be
                used. Where the mask applies will be clearly documented together with
                its declaration in the API. In any case, the effect on the returned
                resource/resources is required behavior for APIs.

                # Field Masks in Update Operations

                A field mask in update operations specifies which fields of the targeted
                resource are going to be updated. The API is required to only change the
                values of the fields as specified in the mask and leave the others
                untouched. If a resource is passed in to describe the updated values,
                the API ignores the values of all fields not covered by the mask.

                If a repeated field is specified for an update operation, new values
                will be appended to the existing repeated field in the target resource.
                Note that a repeated field is only allowed in the last position of a
                ``paths`` string.

                If a sub-message is specified in the last position of the field mask for
                an update operation, then new value will be merged into the existing
                sub-message in the target resource.

                For example, given the target message:

                ::

                    f {
                      b {
                        d: 1
                        x: 2
                      }
                      c: [1]
                    }

                And an update message:

                ::

                    f {
                      b {
                        d: 10
                      }
                      c: [2]
                    }

                then if the field mask is:

                paths: ["f.b", "f.c"]

                then the result will be:

                ::

                    f {
                      b {
                        d: 10
                        x: 2
                      }
                      c: [1, 2]
                    }

                An implementation may provide options to override this default behavior
                for repeated and message fields.

                In order to reset a field's value to the default, the field must be in
                the mask and set to the default value in the provided resource. Hence,
                in order to reset all fields of a resource, provide a default instance
                of the resource and set all fields in the mask, or do not provide a mask
                as described below.

                If a field mask is not present on update, the operation applies to all
                fields (as if a field mask of all fields has been specified). Note that
                in the presence of schema evolution, this may mean that fields the
                client does not know and has therefore not filled into the request will
                be reset to their default. If this is unwanted behavior, a specific
                service may require a client to always specify a field mask, producing
                an error if not.

                As with get operations, the location of the resource which describes the
                updated values in the request message depends on the operation kind. In
                any case, the effect of the field mask is required to be honored by the
                API.

                ## Considerations for HTTP REST

                The HTTP kind of an update operation which uses a field mask must be set
                to PATCH instead of PUT in order to satisfy HTTP semantics (PUT must
                only be used for full updates).

                # JSON Encoding of Field Masks

                In JSON, a field mask is encoded as a single string where paths are
                separated by a comma. Fields name in each path are converted to/from
                lower-camel naming conventions.

                As an example, consider the following message declarations:

                ::

                    message Profile {
                      User user = 1;
                      Photo photo = 2;
                    }
                    message User {
                      string display_name = 1;
                      string address = 2;
                    }

                In proto a field mask for ``Profile`` may look as such:

                ::

                    mask {
                      paths: "user.display_name"
                      paths: "photo"
                    }

                In JSON, the same mask is represented as below:

                ::

                    {
                      mask: "user.displayName,photo"
                    }

                # Field Masks and Oneof Fields

                Field masks treat fields in oneofs just as regular fields. Consider the
                following message:

                ::

                    message SampleMessage {
                      oneof test_oneof {
                        string name = 4;
                        SubMessage sub_message = 9;
                      }
                    }

                The field mask can be:

                ::

                    mask {
                      paths: "name"
                    }

                Or:

                ::

                    mask {
                      paths: "sub_message"
                    }

                Note that oneof type names ("test_oneof" in this case) cannot be used in
                paths.

                ## Field Mask Verification

                The implementation of any API method which has a FieldMask type field in
                the request should verify the included field paths, and return an
                ``INVALID_ARGUMENT`` error if any path is unmappable.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.HistogramQuery`
            job_view (~google.cloud.talent_v4beta1.types.JobView): The language of the posting. This field is distinct from any
                requirements for fluency that are associated with the job.

                Language codes must be in BCP-47 format, such as "en-US" or "sr-Latn".
                For more information, see `Tags for Identifying
                Languages <https://tools.ietf.org/html/bcp47>`__\ {: class="external"
                target="_blank" }.

                If this field is unspecified and ``Job.description`` is present,
                detected language code based on ``Job.description`` is assigned,
                otherwise defaults to 'en_US'.
            offset (int): Commute information which is generated based on specified
                ``CommuteFilter``.
            page_size (int): The maximum number of resources contained in the
                underlying API response. If page streaming is performed per-
                resource, this parameter does not affect the return value. If page
                streaming is performed per-page, this determines the maximum number
                of resources in a page.
            order_by (str): Manages long-running operations with an API service.

                When an API method normally takes long time to complete, it can be
                designed to return ``Operation`` to the client, and the client can use
                this interface to receive the real response asynchronously by polling
                the operation resource, or pass the operation resource to another API
                (such as Google Cloud Pub/Sub API) to receive the response. Any API
                service that returns long-running operations should implement the
                ``Operations`` interface so developers can have a consistent client
                experience.
            diversification_level (~google.cloud.talent_v4beta1.types.DiversificationLevel): The candidate's postal addresses. It's highly recommended to input
                this information as accurately as possible to help improve search
                quality. Here are some recommendations:

                -  Provide ``Address.usage`` if possible, especially if the address is
                   PERSONAL. During a search only personal addresses are considered. If
                   there is no such address, all addresses with unspecified usage are
                   assumed to be personal.
                -  Provide ``Address.current`` for the current address if possible.
                   During a search, only current addresses are considered. If there is
                   no such address, all addresses are assumed to be current.

                When displaying a candidate's addresses, it is sometimes desirable to
                limit the number of addresses shown. In these cases we recommend that
                you display the addresses in the following order of priority:

                1. ``Address.usage`` is PERSONAL and ``Address.current`` is true.
                2. ``Address.usage`` is PERSONAL and ``Address.current`` is false or not
                   set.
                3. ``Address.usage`` is CONTACT_INFO_USAGE_UNSPECIFIED and
                   ``Address.current`` is true.
                4. ``Address.usage`` is CONTACT_INFO_USAGE_UNSPECIFIED and
                   ``Address.current`` is false or not set.
            custom_ranking_info (Union[dict, ~google.cloud.talent_v4beta1.types.CustomRankingInfo]): Controls over how job documents get ranked on top of existing relevance
                score (determined by API algorithm).

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.talent_v4beta1.types.CustomRankingInfo`
            disable_keyword_match (bool): Lists operations that match the specified filter in the request. If
                the server doesn't support this method, it returns ``UNIMPLEMENTED``.

                NOTE: the ``name`` binding allows API services to override the binding
                to use different resource name schemes, such as ``users/*/operations``.
                To override the binding, API services can add a binding such as
                ``"/v1/{name=users/*}/operations"`` to their service configuration. For
                backwards compatibility, the default name includes the operations
                collection id, however overriding users must ensure the name binding is
                the parent resource, without the operations collection id.
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
            An iterable of :class:`~google.cloud.talent_v4beta1.types.MatchingJob` instances.
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
        if "search_jobs_for_alert" not in self._inner_api_calls:
            self._inner_api_calls[
                "search_jobs_for_alert"
            ] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.search_jobs_for_alert,
                default_retry=self._method_configs["SearchJobsForAlert"].retry,
                default_timeout=self._method_configs["SearchJobsForAlert"].timeout,
                client_info=self._client_info,
            )

        request = job_service_pb2.SearchJobsRequest(
            parent=parent,
            request_metadata=request_metadata,
            search_mode=search_mode,
            job_query=job_query,
            enable_broadening=enable_broadening,
            require_precise_result_size=require_precise_result_size,
            histogram_queries=histogram_queries,
            job_view=job_view,
            offset=offset,
            page_size=page_size,
            order_by=order_by,
            diversification_level=diversification_level,
            custom_ranking_info=custom_ranking_info,
            disable_keyword_match=disable_keyword_match,
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
                self._inner_api_calls["search_jobs_for_alert"],
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            ),
            request=request,
            items_field="matching_jobs",
            request_token_field="page_token",
            response_token_field="next_page_token",
        )
        return iterator
