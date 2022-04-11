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
import proto  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.talent.v4beta1',
    manifest={
        'Tenant',
    },
)


class Tenant(proto.Message):
    r"""A Tenant resource represents a tenant in the service. A
    tenant is a group or entity that shares common access with
    specific privileges for resources like profiles. Customer may
    create multiple tenants to provide data isolation for different
    groups.

    Attributes:
        name (str):
            Required during tenant update.

            The resource name for a tenant. This is generated by the
            service when a tenant is created.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenants/bar".
        external_id (str):
            Required. Client side tenant identifier, used
            to uniquely identify the tenant.
            The maximum number of allowed characters is 255.
        usage_type (google.cloud.talent_v4beta1.types.Tenant.DataUsageType):
            Indicates whether data owned by this tenant may be used to
            provide product improvements across other tenants.

            Defaults behavior is
            [DataUsageType.ISOLATED][google.cloud.talent.v4beta1.Tenant.DataUsageType.ISOLATED]
            if it's unset.
        keyword_searchable_profile_custom_attributes (Sequence[str]):
            A list of keys of filterable
            [Profile.custom_attributes][google.cloud.talent.v4beta1.Profile.custom_attributes],
            whose corresponding ``string_values`` are used in keyword
            searches. Profiles with ``string_values`` under these
            specified field keys are returned if any of the values match
            the search keyword. Custom field values with parenthesis,
            brackets and special symbols are not searchable as-is, and
            must be surrounded by quotes.
    """
    class DataUsageType(proto.Enum):
        r"""Enum that represents how user data owned by the tenant is
        used.
        """
        DATA_USAGE_TYPE_UNSPECIFIED = 0
        AGGREGATED = 1
        ISOLATED = 2

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    external_id = proto.Field(
        proto.STRING,
        number=2,
    )
    usage_type = proto.Field(
        proto.ENUM,
        number=3,
        enum=DataUsageType,
    )
    keyword_searchable_profile_custom_attributes = proto.RepeatedField(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
