# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from google.protobuf import field_mask_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.talent_v4beta1.types import application as gct_application
from google.cloud.talent_v4beta1.types import common

__protobuf__ = proto.module(
    package="google.cloud.talent.v4beta1",
    manifest={
        "CreateApplicationRequest",
        "GetApplicationRequest",
        "UpdateApplicationRequest",
        "DeleteApplicationRequest",
        "ListApplicationsRequest",
        "ListApplicationsResponse",
    },
)


class CreateApplicationRequest(proto.Message):
    r"""The Request of the CreateApplication method.

    Attributes:
        parent (str):
            Required. Resource name of the profile under which the
            application is created.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/profiles/{profile_id}".
            For example, "projects/foo/tenants/bar/profiles/baz".
        application (google.cloud.talent_v4beta1.types.Application):
            Required. The application to be created.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    application = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gct_application.Application,
    )


class GetApplicationRequest(proto.Message):
    r"""Request for getting a application by name.

    Attributes:
        name (str):
            Required. The resource name of the application to be
            retrieved.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/profiles/{profile_id}/applications/{application_id}".
            For example,
            "projects/foo/tenants/bar/profiles/baz/applications/qux".
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateApplicationRequest(proto.Message):
    r"""Request for updating a specified application.

    Attributes:
        application (google.cloud.talent_v4beta1.types.Application):
            Required. The application resource to replace
            the current resource in the system.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Strongly recommended for the best service experience.

            If
            [update_mask][google.cloud.talent.v4beta1.UpdateApplicationRequest.update_mask]
            is provided, only the specified fields in
            [application][google.cloud.talent.v4beta1.UpdateApplicationRequest.application]
            are updated. Otherwise all the fields are updated.

            A field mask to specify the application fields to be
            updated. Only top level fields of
            [Application][google.cloud.talent.v4beta1.Application] are
            supported.
    """

    application = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gct_application.Application,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteApplicationRequest(proto.Message):
    r"""Request to delete a application.

    Attributes:
        name (str):
            Required. The resource name of the application to be
            deleted.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/profiles/{profile_id}/applications/{application_id}".
            For example,
            "projects/foo/tenants/bar/profiles/baz/applications/qux".
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListApplicationsRequest(proto.Message):
    r"""List applications for which the client has ACL visibility.

    Attributes:
        parent (str):
            Required. Resource name of the profile under which the
            application is created.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/profiles/{profile_id}",
            for example, "projects/foo/tenants/bar/profiles/baz".
        page_token (str):
            The starting indicator from which to return
            results.
        page_size (int):
            The maximum number of applications to be
            returned, at most 100. Default is 100 if a
            non-positive number is provided.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size = proto.Field(
        proto.INT32,
        number=3,
    )


class ListApplicationsResponse(proto.Message):
    r"""The List applications response object.

    Attributes:
        applications (Sequence[google.cloud.talent_v4beta1.types.Application]):
            Applications for the current client.
        next_page_token (str):
            A token to retrieve the next page of results.
        metadata (google.cloud.talent_v4beta1.types.ResponseMetadata):
            Additional information for the API
            invocation, such as the request tracking id.
    """

    @property
    def raw_page(self):
        return self

    applications = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gct_application.Application,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    metadata = proto.Field(
        proto.MESSAGE,
        number=3,
        message=common.ResponseMetadata,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
