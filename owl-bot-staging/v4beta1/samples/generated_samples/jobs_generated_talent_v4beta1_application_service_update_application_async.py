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
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateApplication
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-talent


# [START jobs_generated_talent_v4beta1_ApplicationService_UpdateApplication_async]
from google.cloud import talent_v4beta1


async def sample_update_application():
    # Create a client
    client = talent_v4beta1.ApplicationServiceAsyncClient()

    # Initialize request argument(s)
    application = talent_v4beta1.Application()
    application.external_id = "external_id_value"
    application.job = "job_value"
    application.stage = "STARTED"

    request = talent_v4beta1.UpdateApplicationRequest(
        application=application,
    )

    # Make the request
    response = await client.update_application(request=request)

    # Handle response
    print(response)

# [END jobs_generated_talent_v4beta1_ApplicationService_UpdateApplication_async]
