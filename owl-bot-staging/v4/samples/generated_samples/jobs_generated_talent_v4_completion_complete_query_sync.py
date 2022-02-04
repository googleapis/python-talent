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
# Snippet for CompleteQuery
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-talent


# [START jobs_generated_talent_v4_Completion_CompleteQuery_sync]
from google.cloud import talent_v4


def sample_complete_query():
    # Create a client
    client = talent_v4.CompletionClient()

    # Initialize request argument(s)
    request = talent_v4.CompleteQueryRequest(
        tenant="tenant_value",
        query="query_value",
        page_size=951,
    )

    # Make the request
    response = client.complete_query(request=request)

    # Handle response
    print(response)

# [END jobs_generated_talent_v4_Completion_CompleteQuery_sync]