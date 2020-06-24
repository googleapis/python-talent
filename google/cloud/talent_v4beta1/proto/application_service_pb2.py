# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/application_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.talent_v4beta1.proto import (
    application_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2,
)
from google.cloud.talent_v4beta1.proto import (
    common_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/application_service.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.talent.v4beta1B\027ApplicationServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n;google/cloud/talent_v4beta1/proto/application_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x33google/cloud/talent_v4beta1/proto/application.proto\x1a.google/cloud/talent_v4beta1/proto/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x93\x01\n\x18\x43reateApplicationRequest\x12\x33\n\x06parent\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1bjobs.googleapis.com/Profile\x12\x42\n\x0b\x61pplication\x18\x02 \x01(\x0b\x32(.google.cloud.talent.v4beta1.ApplicationB\x03\xe0\x41\x02"N\n\x15GetApplicationRequest\x12\x35\n\x04name\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fjobs.googleapis.com/Application"\x8f\x01\n\x18UpdateApplicationRequest\x12\x42\n\x0b\x61pplication\x18\x01 \x01(\x0b\x32(.google.cloud.talent.v4beta1.ApplicationB\x03\xe0\x41\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask"Q\n\x18\x44\x65leteApplicationRequest\x12\x35\n\x04name\x18\x01 \x01(\tB\'\xe0\x41\x02\xfa\x41!\n\x1fjobs.googleapis.com/Application"u\n\x17ListApplicationsRequest\x12\x33\n\x06parent\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1bjobs.googleapis.com/Profile\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"\xb4\x01\n\x18ListApplicationsResponse\x12>\n\x0c\x61pplications\x18\x01 \x03(\x0b\x32(.google.cloud.talent.v4beta1.Application\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12?\n\x08metadata\x18\x03 \x01(\x0b\x32-.google.cloud.talent.v4beta1.ResponseMetadata2\xfc\x08\n\x12\x41pplicationService\x12\xd4\x01\n\x11\x43reateApplication\x12\x35.google.cloud.talent.v4beta1.CreateApplicationRequest\x1a(.google.cloud.talent.v4beta1.Application"^\x82\xd3\xe4\x93\x02\x43">/v4beta1/{parent=projects/*/tenants/*/profiles/*}/applications:\x01*\xda\x41\x12parent,application\x12\xbd\x01\n\x0eGetApplication\x12\x32.google.cloud.talent.v4beta1.GetApplicationRequest\x1a(.google.cloud.talent.v4beta1.Application"M\x82\xd3\xe4\x93\x02@\x12>/v4beta1/{name=projects/*/tenants/*/profiles/*/applications/*}\xda\x41\x04name\x12\xd9\x01\n\x11UpdateApplication\x12\x35.google.cloud.talent.v4beta1.UpdateApplicationRequest\x1a(.google.cloud.talent.v4beta1.Application"c\x82\xd3\xe4\x93\x02O2J/v4beta1/{application.name=projects/*/tenants/*/profiles/*/applications/*}:\x01*\xda\x41\x0b\x61pplication\x12\xb1\x01\n\x11\x44\x65leteApplication\x12\x35.google.cloud.talent.v4beta1.DeleteApplicationRequest\x1a\x16.google.protobuf.Empty"M\x82\xd3\xe4\x93\x02@*>/v4beta1/{name=projects/*/tenants/*/profiles/*/applications/*}\xda\x41\x04name\x12\xd0\x01\n\x10ListApplications\x12\x34.google.cloud.talent.v4beta1.ListApplicationsRequest\x1a\x35.google.cloud.talent.v4beta1.ListApplicationsResponse"O\x82\xd3\xe4\x93\x02@\x12>/v4beta1/{parent=projects/*/tenants/*/profiles/*}/applications\xda\x41\x06parent\x1al\xca\x41\x13jobs.googleapis.com\xd2\x41Shttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsB\x85\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x17\x41pplicationServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_CREATEAPPLICATIONREQUEST = _descriptor.Descriptor(
    name="CreateApplicationRequest",
    full_name="google.cloud.talent.v4beta1.CreateApplicationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.CreateApplicationRequest.parent",
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
            serialized_options=b"\340A\002\372A\035\n\033jobs.googleapis.com/Profile",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="application",
            full_name="google.cloud.talent.v4beta1.CreateApplicationRequest.application",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=372,
    serialized_end=519,
)


_GETAPPLICATIONREQUEST = _descriptor.Descriptor(
    name="GetApplicationRequest",
    full_name="google.cloud.talent.v4beta1.GetApplicationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.GetApplicationRequest.name",
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
            serialized_options=b"\340A\002\372A!\n\037jobs.googleapis.com/Application",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=521,
    serialized_end=599,
)


_UPDATEAPPLICATIONREQUEST = _descriptor.Descriptor(
    name="UpdateApplicationRequest",
    full_name="google.cloud.talent.v4beta1.UpdateApplicationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="application",
            full_name="google.cloud.talent.v4beta1.UpdateApplicationRequest.application",
            index=0,
            number=1,
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
            name="update_mask",
            full_name="google.cloud.talent.v4beta1.UpdateApplicationRequest.update_mask",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=602,
    serialized_end=745,
)


_DELETEAPPLICATIONREQUEST = _descriptor.Descriptor(
    name="DeleteApplicationRequest",
    full_name="google.cloud.talent.v4beta1.DeleteApplicationRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.DeleteApplicationRequest.name",
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
            serialized_options=b"\340A\002\372A!\n\037jobs.googleapis.com/Application",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=747,
    serialized_end=828,
)


_LISTAPPLICATIONSREQUEST = _descriptor.Descriptor(
    name="ListApplicationsRequest",
    full_name="google.cloud.talent.v4beta1.ListApplicationsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.ListApplicationsRequest.parent",
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
            serialized_options=b"\340A\002\372A\035\n\033jobs.googleapis.com/Profile",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_token",
            full_name="google.cloud.talent.v4beta1.ListApplicationsRequest.page_token",
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="page_size",
            full_name="google.cloud.talent.v4beta1.ListApplicationsRequest.page_size",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=830,
    serialized_end=947,
)


_LISTAPPLICATIONSRESPONSE = _descriptor.Descriptor(
    name="ListApplicationsResponse",
    full_name="google.cloud.talent.v4beta1.ListApplicationsResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="applications",
            full_name="google.cloud.talent.v4beta1.ListApplicationsResponse.applications",
            index=0,
            number=1,
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
            name="next_page_token",
            full_name="google.cloud.talent.v4beta1.ListApplicationsResponse.next_page_token",
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
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="metadata",
            full_name="google.cloud.talent.v4beta1.ListApplicationsResponse.metadata",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=950,
    serialized_end=1130,
)

_CREATEAPPLICATIONREQUEST.fields_by_name[
    "application"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2._APPLICATION
)
_UPDATEAPPLICATIONREQUEST.fields_by_name[
    "application"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2._APPLICATION
)
_UPDATEAPPLICATIONREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTAPPLICATIONSRESPONSE.fields_by_name[
    "applications"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2._APPLICATION
)
_LISTAPPLICATIONSRESPONSE.fields_by_name[
    "metadata"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2._RESPONSEMETADATA
)
DESCRIPTOR.message_types_by_name["CreateApplicationRequest"] = _CREATEAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name["GetApplicationRequest"] = _GETAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name["UpdateApplicationRequest"] = _UPDATEAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name["DeleteApplicationRequest"] = _DELETEAPPLICATIONREQUEST
DESCRIPTOR.message_types_by_name["ListApplicationsRequest"] = _LISTAPPLICATIONSREQUEST
DESCRIPTOR.message_types_by_name["ListApplicationsResponse"] = _LISTAPPLICATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateApplicationRequest = _reflection.GeneratedProtocolMessageType(
    "CreateApplicationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEAPPLICATIONREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.application_service_pb2",
        "__doc__": """The Request of the CreateApplication method.
  Attributes:
      parent:
          Required. Resource name of the profile under which the
          application is created.  The format is “projects/{project_id}/
          tenants/{tenant_id}/profiles/{profile_id}”. For example,
          “projects/foo/tenants/bar/profiles/baz”.
      application:
          Required. The application to be created.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.CreateApplicationRequest)
    },
)
_sym_db.RegisterMessage(CreateApplicationRequest)

GetApplicationRequest = _reflection.GeneratedProtocolMessageType(
    "GetApplicationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETAPPLICATIONREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.application_service_pb2",
        "__doc__": """Request for getting a application by name.
  Attributes:
      name:
          Required. The resource name of the application to be
          retrieved.  The format is “projects/{project_id}/tenants/{tena
          nt_id}/profiles/{profile_id}/applications/{application_id}”.
          For example,
          “projects/foo/tenants/bar/profiles/baz/applications/qux”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.GetApplicationRequest)
    },
)
_sym_db.RegisterMessage(GetApplicationRequest)

UpdateApplicationRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateApplicationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEAPPLICATIONREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.application_service_pb2",
        "__doc__": """Request for updating a specified application.
  Attributes:
      application:
          Required. The application resource to replace the current
          resource in the system.
      update_mask:
          Strongly recommended for the best service experience.  If [upd
          ate_mask][google.cloud.talent.v4beta1.UpdateApplicationRequest
          .update_mask] is provided, only the specified fields in [appli
          cation][google.cloud.talent.v4beta1.UpdateApplicationRequest.a
          pplication] are updated. Otherwise all the fields are updated.
          A field mask to specify the application fields to be updated.
          Only top level fields of
          [Application][google.cloud.talent.v4beta1.Application] are
          supported.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.UpdateApplicationRequest)
    },
)
_sym_db.RegisterMessage(UpdateApplicationRequest)

DeleteApplicationRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteApplicationRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETEAPPLICATIONREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.application_service_pb2",
        "__doc__": """Request to delete a application.
  Attributes:
      name:
          Required. The resource name of the application to be deleted.
          The format is “projects/{project_id}/tenants/{tenant_id}/profi
          les/{profile_id}/applications/{application_id}”. For example,
          “projects/foo/tenants/bar/profiles/baz/applications/qux”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.DeleteApplicationRequest)
    },
)
_sym_db.RegisterMessage(DeleteApplicationRequest)

ListApplicationsRequest = _reflection.GeneratedProtocolMessageType(
    "ListApplicationsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTAPPLICATIONSREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.application_service_pb2",
        "__doc__": """List applications for which the client has ACL visibility.
  Attributes:
      parent:
          Required. Resource name of the profile under which the
          application is created.  The format is “projects/{project_id}/
          tenants/{tenant_id}/profiles/{profile_id}”, for example,
          “projects/foo/tenants/bar/profiles/baz”.
      page_token:
          The starting indicator from which to return results.
      page_size:
          The maximum number of applications to be returned, at most
          100. Default is 100 if a non-positive number is provided.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListApplicationsRequest)
    },
)
_sym_db.RegisterMessage(ListApplicationsRequest)

ListApplicationsResponse = _reflection.GeneratedProtocolMessageType(
    "ListApplicationsResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTAPPLICATIONSRESPONSE,
        "__module__": "google.cloud.talent_v4beta1.proto.application_service_pb2",
        "__doc__": """The List applications response object.
  Attributes:
      applications:
          Applications for the current client.
      next_page_token:
          A token to retrieve the next page of results.
      metadata:
          Additional information for the API invocation, such as the
          request tracking id.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListApplicationsResponse)
    },
)
_sym_db.RegisterMessage(ListApplicationsResponse)


DESCRIPTOR._options = None
_CREATEAPPLICATIONREQUEST.fields_by_name["parent"]._options = None
_CREATEAPPLICATIONREQUEST.fields_by_name["application"]._options = None
_GETAPPLICATIONREQUEST.fields_by_name["name"]._options = None
_UPDATEAPPLICATIONREQUEST.fields_by_name["application"]._options = None
_DELETEAPPLICATIONREQUEST.fields_by_name["name"]._options = None
_LISTAPPLICATIONSREQUEST.fields_by_name["parent"]._options = None

_APPLICATIONSERVICE = _descriptor.ServiceDescriptor(
    name="ApplicationService",
    full_name="google.cloud.talent.v4beta1.ApplicationService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\023jobs.googleapis.com\322AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs",
    create_key=_descriptor._internal_create_key,
    serialized_start=1133,
    serialized_end=2281,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateApplication",
            full_name="google.cloud.talent.v4beta1.ApplicationService.CreateApplication",
            index=0,
            containing_service=None,
            input_type=_CREATEAPPLICATIONREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2._APPLICATION,
            serialized_options=b'\202\323\344\223\002C">/v4beta1/{parent=projects/*/tenants/*/profiles/*}/applications:\001*\332A\022parent,application',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetApplication",
            full_name="google.cloud.talent.v4beta1.ApplicationService.GetApplication",
            index=1,
            containing_service=None,
            input_type=_GETAPPLICATIONREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2._APPLICATION,
            serialized_options=b"\202\323\344\223\002@\022>/v4beta1/{name=projects/*/tenants/*/profiles/*/applications/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateApplication",
            full_name="google.cloud.talent.v4beta1.ApplicationService.UpdateApplication",
            index=2,
            containing_service=None,
            input_type=_UPDATEAPPLICATIONREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_application__pb2._APPLICATION,
            serialized_options=b"\202\323\344\223\002O2J/v4beta1/{application.name=projects/*/tenants/*/profiles/*/applications/*}:\001*\332A\013application",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteApplication",
            full_name="google.cloud.talent.v4beta1.ApplicationService.DeleteApplication",
            index=3,
            containing_service=None,
            input_type=_DELETEAPPLICATIONREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002@*>/v4beta1/{name=projects/*/tenants/*/profiles/*/applications/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListApplications",
            full_name="google.cloud.talent.v4beta1.ApplicationService.ListApplications",
            index=4,
            containing_service=None,
            input_type=_LISTAPPLICATIONSREQUEST,
            output_type=_LISTAPPLICATIONSRESPONSE,
            serialized_options=b"\202\323\344\223\002@\022>/v4beta1/{parent=projects/*/tenants/*/profiles/*}/applications\332A\006parent",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_APPLICATIONSERVICE)

DESCRIPTOR.services_by_name["ApplicationService"] = _APPLICATIONSERVICE

# @@protoc_insertion_point(module_scope)
