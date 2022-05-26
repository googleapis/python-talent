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

from google.cloud.talent_v4.types import common
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.talent.v4',
    manifest={
        'Job',
    },
)


class Job(proto.Message):
    r"""A Job resource represents a job posting (also referred to as a "job
    listing" or "job requisition"). A job belongs to a
    [Company][google.cloud.talent.v4.Company], which is the hiring
    entity responsible for the job.

    Attributes:
        name (str):
            Required during job update.

            The resource name for the job. This is generated by the
            service when a job is created.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}".
            For example, "projects/foo/tenants/bar/jobs/baz".

            Use of this field in job queries and API calls is preferred
            over the use of
            [requisition_id][google.cloud.talent.v4.Job.requisition_id]
            since this value is unique.
        company (str):
            Required. The resource name of the company listing the job.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}".
            For example, "projects/foo/tenants/bar/companies/baz".
        requisition_id (str):
            Required. The requisition ID, also referred to as the
            posting ID, is assigned by the client to identify a job.
            This field is intended to be used by clients for client
            identification and tracking of postings. A job isn't allowed
            to be created if there is another job with the same
            [company][google.cloud.talent.v4.Job.name],
            [language_code][google.cloud.talent.v4.Job.language_code]
            and
            [requisition_id][google.cloud.talent.v4.Job.requisition_id].

            The maximum number of allowed characters is 255.
        title (str):
            Required. The title of the job, such as
            "Software Engineer"
            The maximum number of allowed characters is 500.
        description (str):
            Required. The description of the job, which typically
            includes a multi-paragraph description of the company and
            related information. Separate fields are provided on the job
            object for
            [responsibilities][google.cloud.talent.v4.Job.responsibilities],
            [qualifications][google.cloud.talent.v4.Job.qualifications],
            and other job characteristics. Use of these separate job
            fields is recommended.

            This field accepts and sanitizes HTML input, and also
            accepts bold, italic, ordered list, and unordered list
            markup tags.

            The maximum number of allowed characters is 100,000.
        addresses (Sequence[str]):
            Strongly recommended for the best service experience.

            Location(s) where the employer is looking to hire for this
            job posting.

            Specifying the full street address(es) of the hiring
            location enables better API results, especially job searches
            by commute time.

            At most 50 locations are allowed for best search
            performance. If a job has more locations, it is suggested to
            split it into multiple jobs with unique
            [requisition_id][google.cloud.talent.v4.Job.requisition_id]s
            (e.g. 'ReqA' becomes 'ReqA-1', 'ReqA-2', and so on.) as
            multiple jobs with the same
            [company][google.cloud.talent.v4.Job.company],
            [language_code][google.cloud.talent.v4.Job.language_code]
            and
            [requisition_id][google.cloud.talent.v4.Job.requisition_id]
            are not allowed. If the original
            [requisition_id][google.cloud.talent.v4.Job.requisition_id]
            must be preserved, a custom field should be used for
            storage. It is also suggested to group the locations that
            close to each other in the same job for better search
            experience.

            Jobs with multiple addresses must have their addresses with
            the same [LocationType][] to allow location filtering to
            work properly. (For example, a Job with addresses "1600
            Amphitheatre Parkway, Mountain View, CA, USA" and "London,
            UK" may not have location filters applied correctly at
            search time since the first is a
            [LocationType.STREET_ADDRESS][] and the second is a
            [LocationType.LOCALITY][].) If a job needs to have multiple
            addresses, it is suggested to split it into multiple jobs
            with same LocationTypes.

            The maximum number of allowed characters is 500.
        application_info (google.cloud.talent_v4.types.Job.ApplicationInfo):
            Job application information.
        job_benefits (Sequence[google.cloud.talent_v4.types.JobBenefit]):
            The benefits included with the job.
        compensation_info (google.cloud.talent_v4.types.CompensationInfo):
            Job compensation information (a.k.a. "pay
            rate") i.e., the compensation that will paid to
            the employee.
        custom_attributes (Mapping[str, google.cloud.talent_v4.types.CustomAttribute]):
            A map of fields to hold both filterable and non-filterable
            custom job attributes that are not covered by the provided
            structured fields.

            The keys of the map are strings up to 64 bytes and must
            match the pattern: ``[a-zA-Z][a-zA-Z0-9_]*``. For example,
            key0LikeThis or KEY_1_LIKE_THIS.

            At most 100 filterable and at most 100 unfilterable keys are
            supported. For filterable ``string_values``, across all keys
            at most 200 values are allowed, with each string no more
            than 255 characters. For unfilterable ``string_values``, the
            maximum total size of ``string_values`` across all keys is
            50KB.
        degree_types (Sequence[google.cloud.talent_v4.types.DegreeType]):
            The desired education degrees for the job,
            such as Bachelors, Masters.
        department (str):
            The department or functional area within the
            company with the open position.

            The maximum number of allowed characters is 255.
        employment_types (Sequence[google.cloud.talent_v4.types.EmploymentType]):
            The employment type(s) of a job, for example, [full
            time][google.cloud.talent.v4.EmploymentType.FULL_TIME] or
            [part
            time][google.cloud.talent.v4.EmploymentType.PART_TIME].
        incentives (str):
            A description of bonus, commission, and other
            compensation incentives associated with the job
            not including salary or pay.
            The maximum number of allowed characters is
            10,000.
        language_code (str):
            The language of the posting. This field is distinct from any
            requirements for fluency that are associated with the job.

            Language codes must be in BCP-47 format, such as "en-US" or
            "sr-Latn". For more information, see `Tags for Identifying
            Languages <https://tools.ietf.org/html/bcp47>`__\ {:
            class="external" target="_blank" }.

            If this field is unspecified and
            [Job.description][google.cloud.talent.v4.Job.description] is
            present, detected language code based on
            [Job.description][google.cloud.talent.v4.Job.description] is
            assigned, otherwise defaults to 'en_US'.
        job_level (google.cloud.talent_v4.types.JobLevel):
            The experience level associated with the job,
            such as "Entry Level".
        promotion_value (int):
            A promotion value of the job, as determined by the client.
            The value determines the sort order of the jobs returned
            when searching for jobs using the featured jobs search call,
            with higher promotional values being returned first and ties
            being resolved by relevance sort. Only the jobs with a
            promotionValue >0 are returned in a FEATURED_JOB_SEARCH.

            Default value is 0, and negative values are treated as 0.
        qualifications (str):
            A description of the qualifications required to perform the
            job. The use of this field is recommended as an alternative
            to using the more general
            [description][google.cloud.talent.v4.Job.description] field.

            This field accepts and sanitizes HTML input, and also
            accepts bold, italic, ordered list, and unordered list
            markup tags.

            The maximum number of allowed characters is 10,000.
        responsibilities (str):
            A description of job responsibilities. The use of this field
            is recommended as an alternative to using the more general
            [description][google.cloud.talent.v4.Job.description] field.

            This field accepts and sanitizes HTML input, and also
            accepts bold, italic, ordered list, and unordered list
            markup tags.

            The maximum number of allowed characters is 10,000.
        posting_region (google.cloud.talent_v4.types.PostingRegion):
            The job
            [PostingRegion][google.cloud.talent.v4.PostingRegion] (for
            example, state, country) throughout which the job is
            available. If this field is set, a
            [LocationFilter][google.cloud.talent.v4.LocationFilter] in a
            search query within the job region finds this job posting if
            an exact location match isn't specified. If this field is
            set to
            [PostingRegion.NATION][google.cloud.talent.v4.PostingRegion.NATION]
            or
            [PostingRegion.ADMINISTRATIVE_AREA][google.cloud.talent.v4.PostingRegion.ADMINISTRATIVE_AREA],
            setting job
            [Job.addresses][google.cloud.talent.v4.Job.addresses] to the
            same location level as this field is strongly recommended.
        visibility (google.cloud.talent_v4.types.Visibility):
            Deprecated. The job is only visible to the owner.

            The visibility of the job.

            Defaults to
            [Visibility.ACCOUNT_ONLY][google.cloud.talent.v4.Visibility.ACCOUNT_ONLY]
            if not specified.
        job_start_time (google.protobuf.timestamp_pb2.Timestamp):
            The start timestamp of the job in UTC time
            zone. Typically this field is used for
            contracting engagements. Invalid timestamps are
            ignored.
        job_end_time (google.protobuf.timestamp_pb2.Timestamp):
            The end timestamp of the job. Typically this
            field is used for contracting engagements.
            Invalid timestamps are ignored.
        posting_publish_time (google.protobuf.timestamp_pb2.Timestamp):
            The timestamp this job posting was most
            recently published. The default value is the
            time the request arrives at the server. Invalid
            timestamps are ignored.
        posting_expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Strongly recommended for the best service experience.

            The expiration timestamp of the job. After this timestamp,
            the job is marked as expired, and it no longer appears in
            search results. The expired job can't be listed by the
            [ListJobs][google.cloud.talent.v4.JobService.ListJobs] API,
            but it can be retrieved with the
            [GetJob][google.cloud.talent.v4.JobService.GetJob] API or
            updated with the
            [UpdateJob][google.cloud.talent.v4.JobService.UpdateJob] API
            or deleted with the
            [DeleteJob][google.cloud.talent.v4.JobService.DeleteJob]
            API. An expired job can be updated and opened again by using
            a future expiration timestamp. Updating an expired job fails
            if there is another existing open job with same
            [company][google.cloud.talent.v4.Job.company],
            [language_code][google.cloud.talent.v4.Job.language_code]
            and
            [requisition_id][google.cloud.talent.v4.Job.requisition_id].

            The expired jobs are retained in our system for 90 days.
            However, the overall expired job count cannot exceed 3 times
            the maximum number of open jobs over previous 7 days. If
            this threshold is exceeded, expired jobs are cleaned out in
            order of earliest expire time. Expired jobs are no longer
            accessible after they are cleaned out.

            Invalid timestamps are ignored, and treated as expire time
            not provided.

            If the timestamp is before the instant request is made, the
            job is treated as expired immediately on creation. This kind
            of job can not be updated. And when creating a job with past
            timestamp, the
            [posting_publish_time][google.cloud.talent.v4.Job.posting_publish_time]
            must be set before
            [posting_expire_time][google.cloud.talent.v4.Job.posting_expire_time].
            The purpose of this feature is to allow other objects, such
            as [Application][], to refer a job that didn't exist in the
            system prior to becoming expired. If you want to modify a
            job that was expired on creation, delete it and create a new
            one.

            If this value isn't provided at the time of job creation or
            is invalid, the job posting expires after 30 days from the
            job's creation time. For example, if the job was created on
            2017/01/01 13:00AM UTC with an unspecified expiration date,
            the job expires after 2017/01/31 13:00AM UTC.

            If this value isn't provided on job update, it depends on
            the field masks set by
            [UpdateJobRequest.update_mask][google.cloud.talent.v4.UpdateJobRequest.update_mask].
            If the field masks include
            [job_end_time][google.cloud.talent.v4.Job.job_end_time], or
            the masks are empty meaning that every field is updated, the
            job posting expires after 30 days from the job's last update
            time. Otherwise the expiration date isn't updated.
        posting_create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this job
            posting was created.
        posting_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when this job
            posting was last updated.
        company_display_name (str):
            Output only. Display name of the company
            listing the job.
        derived_info (google.cloud.talent_v4.types.Job.DerivedInfo):
            Output only. Derived details about the job
            posting.
        processing_options (google.cloud.talent_v4.types.Job.ProcessingOptions):
            Options for job processing.
    """

    class ApplicationInfo(proto.Message):
        r"""Application related details of a job posting.

        Attributes:
            emails (Sequence[str]):
                Use this field to specify email address(es)
                to which resumes or applications can be sent.
                The maximum number of allowed characters for
                each entry is 255.
            instruction (str):
                Use this field to provide instructions, such
                as "Mail your application to ...", that a
                candidate can follow to apply for the job.
                This field accepts and sanitizes HTML input, and
                also accepts bold, italic, ordered list, and
                unordered list markup tags.
                The maximum number of allowed characters is
                3,000.
            uris (Sequence[str]):
                Use this URI field to direct an applicant to
                a website, for example to link to an online
                application form.
                The maximum number of allowed characters for
                each entry is 2,000.
        """

        emails = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        instruction = proto.Field(
            proto.STRING,
            number=2,
        )
        uris = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class DerivedInfo(proto.Message):
        r"""Derived details about the job posting.

        Attributes:
            locations (Sequence[google.cloud.talent_v4.types.Location]):
                Structured locations of the job, resolved from
                [Job.addresses][google.cloud.talent.v4.Job.addresses].

                [locations][google.cloud.talent.v4.Job.DerivedInfo.locations]
                are exactly matched to
                [Job.addresses][google.cloud.talent.v4.Job.addresses] in the
                same order.
            job_categories (Sequence[google.cloud.talent_v4.types.JobCategory]):
                Job categories derived from
                [Job.title][google.cloud.talent.v4.Job.title] and
                [Job.description][google.cloud.talent.v4.Job.description].
        """

        locations = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=common.Location,
        )
        job_categories = proto.RepeatedField(
            proto.ENUM,
            number=3,
            enum=common.JobCategory,
        )

    class ProcessingOptions(proto.Message):
        r"""Options for job processing.

        Attributes:
            disable_street_address_resolution (bool):
                If set to ``true``, the service does not attempt to resolve
                a more precise address for the job.
            html_sanitization (google.cloud.talent_v4.types.HtmlSanitization):
                Option for job HTML content sanitization. Applied fields
                are:

                -  description
                -  applicationInfo.instruction
                -  incentives
                -  qualifications
                -  responsibilities

                HTML tags in these fields may be stripped if sanitiazation
                isn't disabled.

                Defaults to
                [HtmlSanitization.SIMPLE_FORMATTING_ONLY][google.cloud.talent.v4.HtmlSanitization.SIMPLE_FORMATTING_ONLY].
        """

        disable_street_address_resolution = proto.Field(
            proto.BOOL,
            number=1,
        )
        html_sanitization = proto.Field(
            proto.ENUM,
            number=2,
            enum=common.HtmlSanitization,
        )

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    company = proto.Field(
        proto.STRING,
        number=2,
    )
    requisition_id = proto.Field(
        proto.STRING,
        number=3,
    )
    title = proto.Field(
        proto.STRING,
        number=4,
    )
    description = proto.Field(
        proto.STRING,
        number=5,
    )
    addresses = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    application_info = proto.Field(
        proto.MESSAGE,
        number=7,
        message=ApplicationInfo,
    )
    job_benefits = proto.RepeatedField(
        proto.ENUM,
        number=8,
        enum=common.JobBenefit,
    )
    compensation_info = proto.Field(
        proto.MESSAGE,
        number=9,
        message=common.CompensationInfo,
    )
    custom_attributes = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=10,
        message=common.CustomAttribute,
    )
    degree_types = proto.RepeatedField(
        proto.ENUM,
        number=11,
        enum=common.DegreeType,
    )
    department = proto.Field(
        proto.STRING,
        number=12,
    )
    employment_types = proto.RepeatedField(
        proto.ENUM,
        number=13,
        enum=common.EmploymentType,
    )
    incentives = proto.Field(
        proto.STRING,
        number=14,
    )
    language_code = proto.Field(
        proto.STRING,
        number=15,
    )
    job_level = proto.Field(
        proto.ENUM,
        number=16,
        enum=common.JobLevel,
    )
    promotion_value = proto.Field(
        proto.INT32,
        number=17,
    )
    qualifications = proto.Field(
        proto.STRING,
        number=18,
    )
    responsibilities = proto.Field(
        proto.STRING,
        number=19,
    )
    posting_region = proto.Field(
        proto.ENUM,
        number=20,
        enum=common.PostingRegion,
    )
    visibility = proto.Field(
        proto.ENUM,
        number=21,
        enum=common.Visibility,
    )
    job_start_time = proto.Field(
        proto.MESSAGE,
        number=22,
        message=timestamp_pb2.Timestamp,
    )
    job_end_time = proto.Field(
        proto.MESSAGE,
        number=23,
        message=timestamp_pb2.Timestamp,
    )
    posting_publish_time = proto.Field(
        proto.MESSAGE,
        number=24,
        message=timestamp_pb2.Timestamp,
    )
    posting_expire_time = proto.Field(
        proto.MESSAGE,
        number=25,
        message=timestamp_pb2.Timestamp,
    )
    posting_create_time = proto.Field(
        proto.MESSAGE,
        number=26,
        message=timestamp_pb2.Timestamp,
    )
    posting_update_time = proto.Field(
        proto.MESSAGE,
        number=27,
        message=timestamp_pb2.Timestamp,
    )
    company_display_name = proto.Field(
        proto.STRING,
        number=28,
    )
    derived_info = proto.Field(
        proto.MESSAGE,
        number=29,
        message=DerivedInfo,
    )
    processing_options = proto.Field(
        proto.MESSAGE,
        number=30,
        message=ProcessingOptions,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
