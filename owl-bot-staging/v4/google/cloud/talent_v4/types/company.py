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
import proto  # type: ignore

from google.cloud.talent_v4.types import common


__protobuf__ = proto.module(
    package='google.cloud.talent.v4',
    manifest={
        'Company',
    },
)


class Company(proto.Message):
    r"""A Company resource represents a company in the service. A
    company is the entity that owns job postings, that is, the
    hiring entity responsible for employing applicants for the job
    position.

    Attributes:
        name (str):
            Required during company update.

            The resource name for a company. This is generated by the
            service when a company is created.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}",
            for example, "projects/foo/tenants/bar/companies/baz".
        display_name (str):
            Required. The display name of the company,
            for example, "Google LLC".
        external_id (str):
            Required. Client side company identifier,
            used to uniquely identify the company.

            The maximum number of allowed characters is 255.
        size (google.cloud.talent_v4.types.CompanySize):
            The employer's company size.
        headquarters_address (str):
            The street address of the company's main headquarters, which
            may be different from the job location. The service attempts
            to geolocate the provided address, and populates a more
            specific location wherever possible in
            [DerivedInfo.headquarters_location][google.cloud.talent.v4.Company.DerivedInfo.headquarters_location].
        hiring_agency (bool):
            Set to true if it is the hiring agency that
            post jobs for other employers.

            Defaults to false if not provided.
        eeo_text (str):
            Equal Employment Opportunity legal disclaimer
            text to be associated with all jobs, and
            typically to be displayed in all roles.

            The maximum number of allowed characters is 500.
        website_uri (str):
            The URI representing the company's primary
            web site or home page, for example,
            "https://www.google.com".
            The maximum number of allowed characters is 255.
        career_site_uri (str):
            The URI to employer's career site or careers
            page on the employer's web site, for example,
            "https://careers.google.com".
        image_uri (str):
            A URI that hosts the employer's company logo.
        keyword_searchable_job_custom_attributes (Sequence[str]):
            A list of keys of filterable
            [Job.custom_attributes][google.cloud.talent.v4.Job.custom_attributes],
            whose corresponding ``string_values`` are used in keyword
            searches. Jobs with ``string_values`` under these specified
            field keys are returned if any of the values match the
            search keyword. Custom field values with parenthesis,
            brackets and special symbols are not searchable as-is, and
            those keyword queries must be surrounded by quotes.
        derived_info (google.cloud.talent_v4.types.Company.DerivedInfo):
            Output only. Derived details about the
            company.
        suspended (bool):
            Output only. Indicates whether a company is
            flagged to be suspended from public availability
            by the service when job content appears
            suspicious, abusive, or spammy.
    """

    class DerivedInfo(proto.Message):
        r"""Derived details about the company.

        Attributes:
            headquarters_location (google.cloud.talent_v4.types.Location):
                A structured headquarters location of the company, resolved
                from
                [Company.headquarters_address][google.cloud.talent.v4.Company.headquarters_address]
                if provided.
        """

        headquarters_location = proto.Field(
            proto.MESSAGE,
            number=1,
            message=common.Location,
        )

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name = proto.Field(
        proto.STRING,
        number=2,
    )
    external_id = proto.Field(
        proto.STRING,
        number=3,
    )
    size = proto.Field(
        proto.ENUM,
        number=4,
        enum=common.CompanySize,
    )
    headquarters_address = proto.Field(
        proto.STRING,
        number=5,
    )
    hiring_agency = proto.Field(
        proto.BOOL,
        number=6,
    )
    eeo_text = proto.Field(
        proto.STRING,
        number=7,
    )
    website_uri = proto.Field(
        proto.STRING,
        number=8,
    )
    career_site_uri = proto.Field(
        proto.STRING,
        number=9,
    )
    image_uri = proto.Field(
        proto.STRING,
        number=10,
    )
    keyword_searchable_job_custom_attributes = proto.RepeatedField(
        proto.STRING,
        number=11,
    )
    derived_info = proto.Field(
        proto.MESSAGE,
        number=12,
        message=DerivedInfo,
    )
    suspended = proto.Field(
        proto.BOOL,
        number=13,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
