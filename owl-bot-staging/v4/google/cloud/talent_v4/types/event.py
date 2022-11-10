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
from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.talent.v4',
    manifest={
        'ClientEvent',
        'JobEvent',
    },
)


class ClientEvent(proto.Message):
    r"""An event issued when an end user interacts with the
    application that implements Cloud Talent Solution. Providing
    this information improves the quality of results for the API
    clients, enabling the service to perform optimally. The number
    of events sent must be consistent with other calls, such as job
    searches, issued to the service by the client.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        request_id (str):
            Strongly recommended for the best service experience.

            A unique ID generated in the API responses. It can be found
            in
            [ResponseMetadata.request_id][google.cloud.talent.v4.ResponseMetadata.request_id].
        event_id (str):
            Required. A unique identifier, generated by
            the client application.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Required. The timestamp of the event.
        job_event (google.cloud.talent_v4.types.JobEvent):
            An event issued when a job seeker interacts
            with the application that implements Cloud
            Talent Solution.

            This field is a member of `oneof`_ ``event``.
        event_notes (str):
            Notes about the event provided by recruiters
            or other users, for example, feedback on why a
            job was bookmarked.
    """

    request_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    event_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    job_event: 'JobEvent' = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof='event',
        message='JobEvent',
    )
    event_notes: str = proto.Field(
        proto.STRING,
        number=9,
    )


class JobEvent(proto.Message):
    r"""An event issued when a job seeker interacts with the
    application that implements Cloud Talent Solution.

    Attributes:
        type_ (google.cloud.talent_v4.types.JobEvent.JobEventType):
            Required. The type of the event (see
            [JobEventType][google.cloud.talent.v4.JobEvent.JobEventType]).
        jobs (MutableSequence[str]):
            Required. The [job name(s)][google.cloud.talent.v4.Job.name]
            associated with this event. For example, if this is an
            [impression][google.cloud.talent.v4.JobEvent.JobEventType.IMPRESSION]
            event, this field contains the identifiers of all jobs shown
            to the job seeker. If this was a
            [view][google.cloud.talent.v4.JobEvent.JobEventType.VIEW]
            event, this field contains the identifier of the viewed job.

            The format is
            "projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}",
            for example, "projects/foo/tenants/bar/jobs/baz".
    """
    class JobEventType(proto.Enum):
        r"""An enumeration of an event attributed to the behavior of the
        end user, such as a job seeker.
        """
        JOB_EVENT_TYPE_UNSPECIFIED = 0
        IMPRESSION = 1
        VIEW = 2
        VIEW_REDIRECT = 3
        APPLICATION_START = 4
        APPLICATION_FINISH = 5
        APPLICATION_QUICK_SUBMISSION = 6
        APPLICATION_REDIRECT = 7
        APPLICATION_START_FROM_SEARCH = 8
        APPLICATION_REDIRECT_FROM_SEARCH = 9
        APPLICATION_COMPANY_SUBMIT = 10
        BOOKMARK = 11
        NOTIFICATION = 12
        HIRED = 13
        SENT_CV = 14
        INTERVIEW_GRANTED = 15

    type_: JobEventType = proto.Field(
        proto.ENUM,
        number=1,
        enum=JobEventType,
    )
    jobs: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
