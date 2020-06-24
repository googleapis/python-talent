# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/event_service.proto

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
    event_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_event__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/event_service.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.talent.v4beta1B\021EventServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n5google/cloud/talent_v4beta1/proto/event_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/talent_v4beta1/proto/event.proto"\x94\x01\n\x18\x43reateClientEventRequest\x12\x33\n\x06parent\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\x12\x1bjobs.googleapis.com/Company\x12\x43\n\x0c\x63lient_event\x18\x02 \x01(\x0b\x32(.google.cloud.talent.v4beta1.ClientEventB\x03\xe0\x41\x02\x32\xfa\x02\n\x0c\x45ventService\x12\xfb\x01\n\x11\x43reateClientEvent\x12\x35.google.cloud.talent.v4beta1.CreateClientEventRequest\x1a(.google.cloud.talent.v4beta1.ClientEvent"\x84\x01\x82\xd3\xe4\x93\x02h"3/v4beta1/{parent=projects/*/tenants/*}/clientEvents:\x01*Z.")/v4beta1/{parent=projects/*}/clientEvents:\x01*\xda\x41\x13parent,client_event\x1al\xca\x41\x13jobs.googleapis.com\xd2\x41Shttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsB\x7f\n\x1f\x63om.google.cloud.talent.v4beta1B\x11\x45ventServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_event__pb2.DESCRIPTOR,
    ],
)


_CREATECLIENTEVENTREQUEST = _descriptor.Descriptor(
    name="CreateClientEventRequest",
    full_name="google.cloud.talent.v4beta1.CreateClientEventRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.CreateClientEventRequest.parent",
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
            serialized_options=b"\340A\002\372A\035\022\033jobs.googleapis.com/Company",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="client_event",
            full_name="google.cloud.talent.v4beta1.CreateClientEventRequest.client_event",
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
    serialized_start=249,
    serialized_end=397,
)

_CREATECLIENTEVENTREQUEST.fields_by_name[
    "client_event"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_event__pb2._CLIENTEVENT
)
DESCRIPTOR.message_types_by_name["CreateClientEventRequest"] = _CREATECLIENTEVENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateClientEventRequest = _reflection.GeneratedProtocolMessageType(
    "CreateClientEventRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATECLIENTEVENTREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.event_service_pb2",
        "__doc__": """The report event request.
  
  Attributes:
      parent:
          Required. Resource name of the tenant under which the event is
          created.  The format is
          “projects/{project_id}/tenants/{tenant_id}”, for example,
          “projects/foo/tenant/bar”. If tenant id is unspecified, a
          default tenant is created, for example, “projects/foo”.
      client_event:
          Required. Events issued when end user interacts with
          customer’s application that uses Cloud Talent Solution.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.CreateClientEventRequest)
    },
)
_sym_db.RegisterMessage(CreateClientEventRequest)


DESCRIPTOR._options = None
_CREATECLIENTEVENTREQUEST.fields_by_name["parent"]._options = None
_CREATECLIENTEVENTREQUEST.fields_by_name["client_event"]._options = None

_EVENTSERVICE = _descriptor.ServiceDescriptor(
    name="EventService",
    full_name="google.cloud.talent.v4beta1.EventService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\023jobs.googleapis.com\322AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs",
    create_key=_descriptor._internal_create_key,
    serialized_start=400,
    serialized_end=778,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateClientEvent",
            full_name="google.cloud.talent.v4beta1.EventService.CreateClientEvent",
            index=0,
            containing_service=None,
            input_type=_CREATECLIENTEVENTREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_event__pb2._CLIENTEVENT,
            serialized_options=b'\202\323\344\223\002h"3/v4beta1/{parent=projects/*/tenants/*}/clientEvents:\001*Z.")/v4beta1/{parent=projects/*}/clientEvents:\001*\332A\023parent,client_event',
            create_key=_descriptor._internal_create_key,
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_EVENTSERVICE)

DESCRIPTOR.services_by_name["EventService"] = _EVENTSERVICE

# @@protoc_insertion_point(module_scope)
