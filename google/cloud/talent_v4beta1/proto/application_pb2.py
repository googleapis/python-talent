# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/application.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.talent_v4beta1.proto import (
    common_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/application.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.talent.v4beta1B\030ApplicationResourceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n3google/cloud/talent_v4beta1/proto/application.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/talent_v4beta1/proto/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16google/type/date.proto"\x9c\t\n\x0b\x41pplication\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0b\x65xternal_id\x18\x1f \x01(\tB\x03\xe0\x41\x02\x12\x14\n\x07profile\x18\x02 \x01(\tB\x03\xe0\x41\x03\x12,\n\x03job\x18\x04 \x01(\tB\x1f\xfa\x41\x19\n\x17jobs.googleapis.com/Job\xe0\x41\x02\x12\x31\n\x07\x63ompany\x18\x05 \x01(\tB \xfa\x41\x1d\n\x1bjobs.googleapis.com/Company\x12+\n\x10\x61pplication_date\x18\x07 \x01(\x0b\x32\x11.google.type.Date\x12M\n\x05stage\x18\x0b \x01(\x0e\x32\x39.google.cloud.talent.v4beta1.Application.ApplicationStageB\x03\xe0\x41\x02\x12H\n\x05state\x18\r \x01(\x0e\x32\x39.google.cloud.talent.v4beta1.Application.ApplicationState\x12:\n\ninterviews\x18\x10 \x03(\x0b\x32&.google.cloud.talent.v4beta1.Interview\x12,\n\x08referral\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x0b\x63reate_time\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x03\xe0\x41\x02\x12/\n\x0bupdate_time\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\routcome_notes\x18\x15 \x01(\t\x12\x35\n\x07outcome\x18\x16 \x01(\x0e\x32$.google.cloud.talent.v4beta1.Outcome\x12\x31\n\x08is_match\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.BoolValueB\x03\xe0\x41\x03\x12\x1e\n\x11job_title_snippet\x18\x1d \x01(\tB\x03\xe0\x41\x03"\x90\x01\n\x10\x41pplicationState\x12!\n\x1d\x41PPLICATION_STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\x16\n\x12\x43\x41NDIDATE_WITHDREW\x10\x02\x12\x15\n\x11\x45MPLOYER_WITHDREW\x10\x03\x12\r\n\tCOMPLETED\x10\x04\x12\n\n\x06\x43LOSED\x10\x05"\xa9\x01\n\x10\x41pplicationStage\x12!\n\x1d\x41PPLICATION_STAGE_UNSPECIFIED\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\n\n\x06SCREEN\x10\x02\x12\x19\n\x15HIRING_MANAGER_REVIEW\x10\x03\x12\r\n\tINTERVIEW\x10\x04\x12\x12\n\x0eOFFER_EXTENDED\x10\x05\x12\x12\n\x0eOFFER_ACCEPTED\x10\x06\x12\x0b\n\x07STARTED\x10\x07:w\xea\x41t\n\x1fjobs.googleapis.com/Application\x12Qprojects/{project}/tenants/{tenant}/profiles/{profile}/applications/{application}B\x86\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x18\x41pplicationResourceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,
        google_dot_type_dot_date__pb2.DESCRIPTOR,
    ],
)


_APPLICATION_APPLICATIONSTATE = _descriptor.EnumDescriptor(
    name="ApplicationState",
    full_name="google.cloud.talent.v4beta1.Application.ApplicationState",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_STATE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="IN_PROGRESS",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CANDIDATE_WITHDREW",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="EMPLOYER_WITHDREW",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="COMPLETED",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CLOSED",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1055,
    serialized_end=1199,
)
_sym_db.RegisterEnumDescriptor(_APPLICATION_APPLICATIONSTATE)

_APPLICATION_APPLICATIONSTAGE = _descriptor.EnumDescriptor(
    name="ApplicationStage",
    full_name="google.cloud.talent.v4beta1.Application.ApplicationStage",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="APPLICATION_STAGE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="NEW",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="SCREEN",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="HIRING_MANAGER_REVIEW",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="INTERVIEW",
            index=4,
            number=4,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OFFER_EXTENDED",
            index=5,
            number=5,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="OFFER_ACCEPTED",
            index=6,
            number=6,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="STARTED",
            index=7,
            number=7,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1202,
    serialized_end=1371,
)
_sym_db.RegisterEnumDescriptor(_APPLICATION_APPLICATIONSTAGE)


_APPLICATION = _descriptor.Descriptor(
    name="Application",
    full_name="google.cloud.talent.v4beta1.Application",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.Application.name",
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
            name="external_id",
            full_name="google.cloud.talent.v4beta1.Application.external_id",
            index=1,
            number=31,
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
            name="profile",
            full_name="google.cloud.talent.v4beta1.Application.profile",
            index=2,
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
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="job",
            full_name="google.cloud.talent.v4beta1.Application.job",
            index=3,
            number=4,
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
            serialized_options=b"\372A\031\n\027jobs.googleapis.com/Job\340A\002",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="company",
            full_name="google.cloud.talent.v4beta1.Application.company",
            index=4,
            number=5,
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
            serialized_options=b"\372A\035\n\033jobs.googleapis.com/Company",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="application_date",
            full_name="google.cloud.talent.v4beta1.Application.application_date",
            index=5,
            number=7,
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
            name="stage",
            full_name="google.cloud.talent.v4beta1.Application.stage",
            index=6,
            number=11,
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
            name="state",
            full_name="google.cloud.talent.v4beta1.Application.state",
            index=7,
            number=13,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="interviews",
            full_name="google.cloud.talent.v4beta1.Application.interviews",
            index=8,
            number=16,
            type=11,
            cpp_type=10,
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
        _descriptor.FieldDescriptor(
            name="referral",
            full_name="google.cloud.talent.v4beta1.Application.referral",
            index=9,
            number=18,
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
            name="create_time",
            full_name="google.cloud.talent.v4beta1.Application.create_time",
            index=10,
            number=19,
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
            name="update_time",
            full_name="google.cloud.talent.v4beta1.Application.update_time",
            index=11,
            number=20,
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
            name="outcome_notes",
            full_name="google.cloud.talent.v4beta1.Application.outcome_notes",
            index=12,
            number=21,
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
            name="outcome",
            full_name="google.cloud.talent.v4beta1.Application.outcome",
            index=13,
            number=22,
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="is_match",
            full_name="google.cloud.talent.v4beta1.Application.is_match",
            index=14,
            number=28,
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
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="job_title_snippet",
            full_name="google.cloud.talent.v4beta1.Application.job_title_snippet",
            index=15,
            number=29,
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
            serialized_options=b"\340A\003",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[_APPLICATION_APPLICATIONSTATE, _APPLICATION_APPLICATIONSTAGE,],
    serialized_options=b"\352At\n\037jobs.googleapis.com/Application\022Qprojects/{project}/tenants/{tenant}/profiles/{profile}/applications/{application}",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=312,
    serialized_end=1492,
)

_APPLICATION.fields_by_name[
    "application_date"
].message_type = google_dot_type_dot_date__pb2._DATE
_APPLICATION.fields_by_name["stage"].enum_type = _APPLICATION_APPLICATIONSTAGE
_APPLICATION.fields_by_name["state"].enum_type = _APPLICATION_APPLICATIONSTATE
_APPLICATION.fields_by_name[
    "interviews"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2._INTERVIEW
)
_APPLICATION.fields_by_name[
    "referral"
].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_APPLICATION.fields_by_name[
    "create_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_APPLICATION.fields_by_name[
    "update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_APPLICATION.fields_by_name[
    "outcome"
].enum_type = google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2._OUTCOME
_APPLICATION.fields_by_name[
    "is_match"
].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_APPLICATION_APPLICATIONSTATE.containing_type = _APPLICATION
_APPLICATION_APPLICATIONSTAGE.containing_type = _APPLICATION
DESCRIPTOR.message_types_by_name["Application"] = _APPLICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Application = _reflection.GeneratedProtocolMessageType(
    "Application",
    (_message.Message,),
    {
        "DESCRIPTOR": _APPLICATION,
        "__module__": "google.cloud.talent_v4beta1.proto.application_pb2",
        "__doc__": """Resource that represents a job application record of a candidate.
  
  Attributes:
      name:
          Required during application update.  Resource name assigned to
          an application by the API.  The format is “projects/{project_i
          d}/tenants/{tenant_id}/profiles/{profile_id}/applications/{app
          lication_id}”. For example,
          “projects/foo/tenants/bar/profiles/baz/applications/qux”.
      external_id:
          Required. Client side application identifier, used to uniquely
          identify the application.  The maximum number of allowed
          characters is 255.
      profile:
          Output only. Resource name of the candidate of this
          application.  The format is “projects/{project_id}/tenants/{te
          nant_id}/profiles/{profile_id}”. For example,
          “projects/foo/tenants/bar/profiles/baz”.
      job:
          Required. Resource name of the job which the candidate applied
          for.  The format is
          “projects/{project_id}/tenants/{tenant_id}/jobs/{job_id}”. For
          example, “projects/foo/tenants/bar/jobs/baz”.
      company:
          Resource name of the company which the candidate applied for.
          The format is “projects/{project_id}/tenants/{tenant_id}/compa
          nies/{company_id}”. For example,
          “projects/foo/tenants/bar/companies/baz”.
      application_date:
          The application date.
      stage:
          Required. What is the most recent stage of the application
          (that is, new, screen, send cv, hired, finished work)? This
          field is intentionally not comprehensive of every possible
          status, but instead, represents statuses that would be used to
          indicate to the ML models good / bad matches.
      state:
          The application state.
      interviews:
          All interviews (screen, onsite, and so on) conducted as part
          of this application (includes details such as user conducting
          the interview, timestamp, feedback, and so on).
      referral:
          If the candidate is referred by a employee.
      create_time:
          Required. Reflects the time that the application was created.
      update_time:
          The last update timestamp.
      outcome_notes:
          Free text reason behind the recruitement outcome (for example,
          reason for withdraw / reject, reason for an unsuccessful
          finish, and so on).  Number of characters allowed is 100.
      outcome:
          Outcome positiveness shows how positive the outcome is.
      is_match:
          Output only. Indicates whether this job application is a match
          to application related filters. This value is only applicable
          in profile search response.
      job_title_snippet:
          Output only. Job title snippet shows how the job title is
          related to a search query. It’s empty if the job title isn’t
          related to the search query.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.Application)
    },
)
_sym_db.RegisterMessage(Application)


DESCRIPTOR._options = None
_APPLICATION.fields_by_name["external_id"]._options = None
_APPLICATION.fields_by_name["profile"]._options = None
_APPLICATION.fields_by_name["job"]._options = None
_APPLICATION.fields_by_name["company"]._options = None
_APPLICATION.fields_by_name["stage"]._options = None
_APPLICATION.fields_by_name["create_time"]._options = None
_APPLICATION.fields_by_name["is_match"]._options = None
_APPLICATION.fields_by_name["job_title_snippet"]._options = None
_APPLICATION._options = None
# @@protoc_insertion_point(module_scope)
