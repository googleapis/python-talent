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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.talent.v4',
    manifest={
        'Tenant',
    },
)


class Tenant(proto.Message):
    r"""A Tenant resource represents a tenant in the service. A
    tenant is a group or entity that shares common access with
    specific privileges for resources like jobs. Customer may create
    multiple tenants to provide data isolation for different groups.

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
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    external_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
