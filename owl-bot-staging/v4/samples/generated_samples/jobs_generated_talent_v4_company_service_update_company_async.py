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
# Snippet for UpdateCompany
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-talent


# [START jobs_generated_talent_v4_CompanyService_UpdateCompany_async]
from google.cloud import talent_v4


async def sample_update_company():
    # Create a client
    client = talent_v4.CompanyServiceAsyncClient()

    # Initialize request argument(s)
    company = talent_v4.Company()
    company.display_name = "display_name_value"
    company.external_id = "external_id_value"

    request = talent_v4.UpdateCompanyRequest(
        company=company,
    )

    # Make the request
    response = await client.update_company(request=request)

    # Handle response
    print(response)

# [END jobs_generated_talent_v4_CompanyService_UpdateCompany_async]