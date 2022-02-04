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
# Snippet for BatchUpdateJobs
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-talent


# [START jobs_generated_talent_v4beta1_JobService_BatchUpdateJobs_sync]
from google.cloud import talent_v4beta1


def sample_batch_update_jobs():
    # Create a client
    client = talent_v4beta1.JobServiceClient()

    # Initialize request argument(s)
    jobs = talent_v4beta1.Job()
    jobs.company = "company_value"
    jobs.requisition_id = "requisition_id_value"
    jobs.title = "title_value"
    jobs.description = "description_value"

    request = talent_v4beta1.BatchUpdateJobsRequest(
        parent="parent_value",
        jobs=jobs,
    )

    # Make the request
    operation = client.batch_update_jobs(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END jobs_generated_talent_v4beta1_JobService_BatchUpdateJobs_sync]
