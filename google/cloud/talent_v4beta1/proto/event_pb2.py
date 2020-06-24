# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/event.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/event.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.talent.v4beta1B\nEventProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n-google/cloud/talent_v4beta1/proto/event.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\x8c\x02\n\x0b\x43lientEvent\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x15\n\x08\x65vent_id\x18\x02 \x01(\tB\x03\xe0\x41\x02\x12\x34\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x02\x12:\n\tjob_event\x18\x05 \x01(\x0b\x32%.google.cloud.talent.v4beta1.JobEventH\x00\x12\x42\n\rprofile_event\x18\x06 \x01(\x0b\x32).google.cloud.talent.v4beta1.ProfileEventH\x00\x12\x13\n\x0b\x65vent_notes\x18\t \x01(\tB\x07\n\x05\x65vent"\xf6\x03\n\x08JobEvent\x12\x45\n\x04type\x18\x01 \x01(\x0e\x32\x32.google.cloud.talent.v4beta1.JobEvent.JobEventTypeB\x03\xe0\x41\x02\x12\x11\n\x04jobs\x18\x02 \x03(\tB\x03\xe0\x41\x02\x12\x0f\n\x07profile\x18\x03 \x01(\t"\xfe\x02\n\x0cJobEventType\x12\x1e\n\x1aJOB_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nIMPRESSION\x10\x01\x12\x08\n\x04VIEW\x10\x02\x12\x11\n\rVIEW_REDIRECT\x10\x03\x12\x15\n\x11\x41PPLICATION_START\x10\x04\x12\x16\n\x12\x41PPLICATION_FINISH\x10\x05\x12 \n\x1c\x41PPLICATION_QUICK_SUBMISSION\x10\x06\x12\x18\n\x14\x41PPLICATION_REDIRECT\x10\x07\x12!\n\x1d\x41PPLICATION_START_FROM_SEARCH\x10\x08\x12$\n APPLICATION_REDIRECT_FROM_SEARCH\x10\t\x12\x1e\n\x1a\x41PPLICATION_COMPANY_SUBMIT\x10\n\x12\x0c\n\x08\x42OOKMARK\x10\x0b\x12\x10\n\x0cNOTIFICATION\x10\x0c\x12\t\n\x05HIRED\x10\r\x12\x0b\n\x07SENT_CV\x10\x0e\x12\x15\n\x11INTERVIEW_GRANTED\x10\x0f"\xe2\x01\n\x0cProfileEvent\x12M\n\x04type\x18\x01 \x01(\x0e\x32:.google.cloud.talent.v4beta1.ProfileEvent.ProfileEventTypeB\x03\xe0\x41\x02\x12\x15\n\x08profiles\x18\x02 \x03(\tB\x03\xe0\x41\x02\x12\x0c\n\x04jobs\x18\x06 \x03(\t"^\n\x10ProfileEventType\x12"\n\x1ePROFILE_EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nIMPRESSION\x10\x01\x12\x08\n\x04VIEW\x10\x02\x12\x0c\n\x08\x42OOKMARK\x10\x03\x42x\n\x1f\x63om.google.cloud.talent.v4beta1B\nEventProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_JOBEVENT_JOBEVENTTYPE = _descriptor.EnumDescriptor(
    name="JobEventType",
    full_name="google.cloud.talent.v4beta1.JobEvent.JobEventType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="JOB_EVENT_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMPRESSION",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="VIEW",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="VIEW_REDIRECT",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_START",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_FINISH",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_QUICK_SUBMISSION",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_REDIRECT",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_START_FROM_SEARCH",
            index=8,
            number=8,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_REDIRECT_FROM_SEARCH",
            index=9,
            number=9,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_COMPANY_SUBMIT",
            index=10,
            number=10,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BOOKMARK",
            index=11,
            number=11,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NOTIFICATION",
            index=12,
            number=12,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HIRED",
            index=13,
            number=13,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SENT_CV",
            index=14,
            number=14,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INTERVIEW_GRANTED",
            index=15,
            number=15,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=566,
    serialized_end=948,
)
_sym_db.RegisterEnumDescriptor(_JOBEVENT_JOBEVENTTYPE)

_PROFILEEVENT_PROFILEEVENTTYPE = _descriptor.EnumDescriptor(
    name="ProfileEventType",
    full_name="google.cloud.talent.v4beta1.ProfileEvent.ProfileEventType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="PROFILE_EVENT_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IMPRESSION",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="VIEW",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="BOOKMARK",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1083,
    serialized_end=1177,
)
_sym_db.RegisterEnumDescriptor(_PROFILEEVENT_PROFILEEVENTTYPE)


_CLIENTEVENT = _descriptor.Descriptor(
    name="ClientEvent",
    full_name="google.cloud.talent.v4beta1.ClientEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="request_id",
            full_name="google.cloud.talent.v4beta1.ClientEvent.request_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="event_id",
            full_name="google.cloud.talent.v4beta1.ClientEvent.event_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="create_time",
            full_name="google.cloud.talent.v4beta1.ClientEvent.create_time",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="job_event",
            full_name="google.cloud.talent.v4beta1.ClientEvent.job_event",
            index=3,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="profile_event",
            full_name="google.cloud.talent.v4beta1.ClientEvent.profile_event",
            index=4,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="event_notes",
            full_name="google.cloud.talent.v4beta1.ClientEvent.event_notes",
            index=5,
            number=9,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="event",
            full_name="google.cloud.talent.v4beta1.ClientEvent.event",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=175,
    serialized_end=443,
)


_JOBEVENT = _descriptor.Descriptor(
    name="JobEvent",
    full_name="google.cloud.talent.v4beta1.JobEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.cloud.talent.v4beta1.JobEvent.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="jobs",
            full_name="google.cloud.talent.v4beta1.JobEvent.jobs",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="profile",
            full_name="google.cloud.talent.v4beta1.JobEvent.profile",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_JOBEVENT_JOBEVENTTYPE,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=446,
    serialized_end=948,
)


_PROFILEEVENT = _descriptor.Descriptor(
    name="ProfileEvent",
    full_name="google.cloud.talent.v4beta1.ProfileEvent",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="type",
            full_name="google.cloud.talent.v4beta1.ProfileEvent.type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="profiles",
            full_name="google.cloud.talent.v4beta1.ProfileEvent.profiles",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="jobs",
            full_name="google.cloud.talent.v4beta1.ProfileEvent.jobs",
            index=2,
            number=6,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_PROFILEEVENT_PROFILEEVENTTYPE,],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=951,
    serialized_end=1177,
)

_CLIENTEVENT.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CLIENTEVENT.fields_by_name["job_event"].message_type = _JOBEVENT
_CLIENTEVENT.fields_by_name["profile_event"].message_type = _PROFILEEVENT
_CLIENTEVENT.oneofs_by_name["event"].fields.append(
    _CLIENTEVENT.fields_by_name["job_event"]
)
_CLIENTEVENT.fields_by_name["job_event"].containing_oneof = _CLIENTEVENT.oneofs_by_name[
    "event"
]
_CLIENTEVENT.oneofs_by_name["event"].fields.append(
    _CLIENTEVENT.fields_by_name["profile_event"]
)
_CLIENTEVENT.fields_by_name[
    "profile_event"
].containing_oneof = _CLIENTEVENT.oneofs_by_name["event"]
_JOBEVENT.fields_by_name["type"].enum_type = _JOBEVENT_JOBEVENTTYPE
_JOBEVENT_JOBEVENTTYPE.containing_type = _JOBEVENT
_PROFILEEVENT.fields_by_name["type"].enum_type = _PROFILEEVENT_PROFILEEVENTTYPE
_PROFILEEVENT_PROFILEEVENTTYPE.containing_type = _PROFILEEVENT
DESCRIPTOR.message_types_by_name["ClientEvent"] = _CLIENTEVENT
DESCRIPTOR.message_types_by_name["JobEvent"] = _JOBEVENT
DESCRIPTOR.message_types_by_name["ProfileEvent"] = _PROFILEEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientEvent = _reflection.GeneratedProtocolMessageType(
    "ClientEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTEVENT,
        "__module__": "google.cloud.talent_v4beta1.proto.event_pb2",
        "__doc__": """An event issued when an end user interacts with the application that
  implements Cloud Talent Solution. Providing this information improves
  the quality of results for the API clients, enabling the service to
  perform optimally. The number of events sent must be consistent with
  other calls, such as job searches, issued to the service by the
  client.
  
  Attributes:
      request_id:
          Strongly recommended for the best service experience.  A
          unique ID generated in the API responses. It can be found in [
          ResponseMetadata.request_id][google.cloud.talent.v4beta1.Respo
          nseMetadata.request_id].
      event_id:
          Required. A unique identifier, generated by the client
          application.
      create_time:
          Required. The timestamp of the event.
      event:
          Required.  The detail information of a specific event type.
      job_event:
          An event issued when a job seeker interacts with the
          application that implements Cloud Talent Solution.
      profile_event:
          An event issued when a profile searcher interacts with the
          application that implements Cloud Talent Solution.
      event_notes:
          Notes about the event provided by recruiters or other users,
          for example, feedback on why a profile was bookmarked.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ClientEvent)
    },
)
_sym_db.RegisterMessage(ClientEvent)

JobEvent = _reflection.GeneratedProtocolMessageType(
    "JobEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _JOBEVENT,
        "__module__": "google.cloud.talent_v4beta1.proto.event_pb2",
        "__doc__": """An event issued when a job seeker interacts with the application that
  implements Cloud Talent Solution.
  
  Attributes:
      type:
          Required. The type of the event (see [JobEventType][google.clo
          ud.talent.v4beta1.JobEvent.JobEventType]).
      jobs:
          Required. The [job
          name(s)][google.cloud.talent.v4beta1.Job.name] associated with
          this event. For example, if this is an [impression][google.clo
          ud.talent.v4beta1.JobEvent.JobEventType.IMPRESSION] event,
          this field contains the identifiers of all jobs shown to the
          job seeker. If this was a
          [view][google.cloud.talent.v4beta1.JobEvent.JobEventType.VIEW]
          event, this field contains the identifier of the viewed job.
          The format is
          “projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}”, for
          example, “projects/foo/tenants/bar/jobs/baz”.
      profile:
          The [profile name][google.cloud.talent.v4beta1.Profile.name]
          associated with this client event.  The format is “projects/{p
          roject_id}/tenants/{tenant_id}/profiles/{profile_id}”, for
          example, “projects/foo/tenants/bar/profiles/baz”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.JobEvent)
    },
)
_sym_db.RegisterMessage(JobEvent)

ProfileEvent = _reflection.GeneratedProtocolMessageType(
    "ProfileEvent",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROFILEEVENT,
        "__module__": "google.cloud.talent_v4beta1.proto.event_pb2",
        "__doc__": """An event issued when a profile searcher interacts with the application
  that implements Cloud Talent Solution.
  
  Attributes:
      type:
          Required. Type of event.
      profiles:
          Required. The [profile
          name(s)][google.cloud.talent.v4beta1.Profile.name] associated
          with this client event.  The format is “projects/{project_id}/
          tenants/{tenant_id}/profiles/{profile_id}”, for example,
          “projects/foo/tenants/bar/profiles/baz”.
      jobs:
          The [job name(s)][google.cloud.talent.v4beta1.Job.name]
          associated with this client event. Leave it empty if the event
          isn’t associated with a job.  The format is
          “projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}”, for
          example, “projects/foo/tenants/bar/jobs/baz”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ProfileEvent)
    },
)
_sym_db.RegisterMessage(ProfileEvent)


DESCRIPTOR._options = None
_CLIENTEVENT.fields_by_name["event_id"]._options = None
_CLIENTEVENT.fields_by_name["create_time"]._options = None
_JOBEVENT.fields_by_name["type"]._options = None
_JOBEVENT.fields_by_name["jobs"]._options = None
_PROFILEEVENT.fields_by_name["type"]._options = None
_PROFILEEVENT.fields_by_name["profiles"]._options = None
# @@protoc_insertion_point(module_scope)
