# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/company_service.proto

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
    common_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2,
)
from google.cloud.talent_v4beta1.proto import (
    company_pb2 as google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/company_service.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.talent.v4beta1B\023CompanyServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n7google/cloud/talent_v4beta1/proto/company_service.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/talent_v4beta1/proto/common.proto\x1a/google/cloud/talent_v4beta1/proto/company.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x87\x01\n\x14\x43reateCompanyRequest\x12\x33\n\x06parent\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\x12\x1bjobs.googleapis.com/Company\x12:\n\x07\x63ompany\x18\x02 \x01(\x0b\x32$.google.cloud.talent.v4beta1.CompanyB\x03\xe0\x41\x02"F\n\x11GetCompanyRequest\x12\x31\n\x04name\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1bjobs.googleapis.com/Company"\x83\x01\n\x14UpdateCompanyRequest\x12:\n\x07\x63ompany\x18\x01 \x01(\x0b\x32$.google.cloud.talent.v4beta1.CompanyB\x03\xe0\x41\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask"I\n\x14\x44\x65leteCompanyRequest\x12\x31\n\x04name\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\n\x1bjobs.googleapis.com/Company"\x8d\x01\n\x14ListCompaniesRequest\x12\x33\n\x06parent\x18\x01 \x01(\tB#\xe0\x41\x02\xfa\x41\x1d\x12\x1bjobs.googleapis.com/Company\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x19\n\x11require_open_jobs\x18\x04 \x01(\x08"\xaa\x01\n\x15ListCompaniesResponse\x12\x37\n\tcompanies\x18\x01 \x03(\x0b\x32$.google.cloud.talent.v4beta1.Company\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12?\n\x08metadata\x18\x03 \x01(\x0b\x32-.google.cloud.talent.v4beta1.ResponseMetadata2\xd2\t\n\x0e\x43ompanyService\x12\xe3\x01\n\rCreateCompany\x12\x31.google.cloud.talent.v4beta1.CreateCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company"y\x82\xd3\xe4\x93\x02\x62"0/v4beta1/{parent=projects/*/tenants/*}/companies:\x01*Z+"&/v4beta1/{parent=projects/*}/companies:\x01*\xda\x41\x0eparent,company\x12\xcd\x01\n\nGetCompany\x12..google.cloud.talent.v4beta1.GetCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company"i\x82\xd3\xe4\x93\x02\\\x12\x30/v4beta1/{name=projects/*/tenants/*/companies/*}Z(\x12&/v4beta1/{name=projects/*/companies/*}\xda\x41\x04name\x12\xed\x01\n\rUpdateCompany\x12\x31.google.cloud.talent.v4beta1.UpdateCompanyRequest\x1a$.google.cloud.talent.v4beta1.Company"\x82\x01\x82\xd3\xe4\x93\x02r28/v4beta1/{company.name=projects/*/tenants/*/companies/*}:\x01*Z32./v4beta1/{company.name=projects/*/companies/*}:\x01*\xda\x41\x07\x63ompany\x12\xc5\x01\n\rDeleteCompany\x12\x31.google.cloud.talent.v4beta1.DeleteCompanyRequest\x1a\x16.google.protobuf.Empty"i\x82\xd3\xe4\x93\x02\\*0/v4beta1/{name=projects/*/tenants/*/companies/*}Z(*&/v4beta1/{name=projects/*/companies/*}\xda\x41\x04name\x12\xe3\x01\n\rListCompanies\x12\x31.google.cloud.talent.v4beta1.ListCompaniesRequest\x1a\x32.google.cloud.talent.v4beta1.ListCompaniesResponse"k\x82\xd3\xe4\x93\x02\\\x12\x30/v4beta1/{parent=projects/*/tenants/*}/companiesZ(\x12&/v4beta1/{parent=projects/*}/companies\xda\x41\x06parent\x1al\xca\x41\x13jobs.googleapis.com\xd2\x41Shttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobsB\x81\x01\n\x1f\x63om.google.cloud.talent.v4beta1B\x13\x43ompanyServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3',
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,
    ],
)


_CREATECOMPANYREQUEST = _descriptor.Descriptor(
    name="CreateCompanyRequest",
    full_name="google.cloud.talent.v4beta1.CreateCompanyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.CreateCompanyRequest.parent",
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
            name="company",
            full_name="google.cloud.talent.v4beta1.CreateCompanyRequest.company",
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
    serialized_start=364,
    serialized_end=499,
)


_GETCOMPANYREQUEST = _descriptor.Descriptor(
    name="GetCompanyRequest",
    full_name="google.cloud.talent.v4beta1.GetCompanyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.GetCompanyRequest.name",
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
            serialized_options=b"\340A\002\372A\035\n\033jobs.googleapis.com/Company",
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
    serialized_start=501,
    serialized_end=571,
)


_UPDATECOMPANYREQUEST = _descriptor.Descriptor(
    name="UpdateCompanyRequest",
    full_name="google.cloud.talent.v4beta1.UpdateCompanyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="company",
            full_name="google.cloud.talent.v4beta1.UpdateCompanyRequest.company",
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
            full_name="google.cloud.talent.v4beta1.UpdateCompanyRequest.update_mask",
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
    serialized_start=574,
    serialized_end=705,
)


_DELETECOMPANYREQUEST = _descriptor.Descriptor(
    name="DeleteCompanyRequest",
    full_name="google.cloud.talent.v4beta1.DeleteCompanyRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="name",
            full_name="google.cloud.talent.v4beta1.DeleteCompanyRequest.name",
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
            serialized_options=b"\340A\002\372A\035\n\033jobs.googleapis.com/Company",
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
    serialized_start=707,
    serialized_end=780,
)


_LISTCOMPANIESREQUEST = _descriptor.Descriptor(
    name="ListCompaniesRequest",
    full_name="google.cloud.talent.v4beta1.ListCompaniesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.talent.v4beta1.ListCompaniesRequest.parent",
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
            name="page_token",
            full_name="google.cloud.talent.v4beta1.ListCompaniesRequest.page_token",
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
            full_name="google.cloud.talent.v4beta1.ListCompaniesRequest.page_size",
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
        _descriptor.FieldDescriptor(
            name="require_open_jobs",
            full_name="google.cloud.talent.v4beta1.ListCompaniesRequest.require_open_jobs",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=783,
    serialized_end=924,
)


_LISTCOMPANIESRESPONSE = _descriptor.Descriptor(
    name="ListCompaniesResponse",
    full_name="google.cloud.talent.v4beta1.ListCompaniesResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="companies",
            full_name="google.cloud.talent.v4beta1.ListCompaniesResponse.companies",
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
            full_name="google.cloud.talent.v4beta1.ListCompaniesResponse.next_page_token",
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
            full_name="google.cloud.talent.v4beta1.ListCompaniesResponse.metadata",
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
    serialized_start=927,
    serialized_end=1097,
)

_CREATECOMPANYREQUEST.fields_by_name[
    "company"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2._COMPANY
)
_UPDATECOMPANYREQUEST.fields_by_name[
    "company"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2._COMPANY
)
_UPDATECOMPANYREQUEST.fields_by_name[
    "update_mask"
].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_LISTCOMPANIESRESPONSE.fields_by_name[
    "companies"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2._COMPANY
)
_LISTCOMPANIESRESPONSE.fields_by_name[
    "metadata"
].message_type = (
    google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_common__pb2._RESPONSEMETADATA
)
DESCRIPTOR.message_types_by_name["CreateCompanyRequest"] = _CREATECOMPANYREQUEST
DESCRIPTOR.message_types_by_name["GetCompanyRequest"] = _GETCOMPANYREQUEST
DESCRIPTOR.message_types_by_name["UpdateCompanyRequest"] = _UPDATECOMPANYREQUEST
DESCRIPTOR.message_types_by_name["DeleteCompanyRequest"] = _DELETECOMPANYREQUEST
DESCRIPTOR.message_types_by_name["ListCompaniesRequest"] = _LISTCOMPANIESREQUEST
DESCRIPTOR.message_types_by_name["ListCompaniesResponse"] = _LISTCOMPANIESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateCompanyRequest = _reflection.GeneratedProtocolMessageType(
    "CreateCompanyRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATECOMPANYREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.company_service_pb2",
        "__doc__": """The Request of the CreateCompany method.
  
  Attributes:
      parent:
          Required. Resource name of the tenant under which the company
          is created.  The format is
          “projects/{project_id}/tenants/{tenant_id}”, for example,
          “projects/foo/tenant/bar”. If tenant id is unspecified, a
          default tenant is created, for example, “projects/foo”.
      company:
          Required. The company to be created.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.CreateCompanyRequest)
    },
)
_sym_db.RegisterMessage(CreateCompanyRequest)

GetCompanyRequest = _reflection.GeneratedProtocolMessageType(
    "GetCompanyRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETCOMPANYREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.company_service_pb2",
        "__doc__": """Request for getting a company by name.
  
  Attributes:
      name:
          Required. The resource name of the company to be retrieved.
          The format is “projects/{project_id}/tenants/{tenant_id}/compa
          nies/{company_id}”, for example, “projects/api-test-
          project/tenants/foo/companies/bar”.  If tenant id is
          unspecified, the default tenant is used, for example,
          “projects/api-test-project/companies/bar”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.GetCompanyRequest)
    },
)
_sym_db.RegisterMessage(GetCompanyRequest)

UpdateCompanyRequest = _reflection.GeneratedProtocolMessageType(
    "UpdateCompanyRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATECOMPANYREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.company_service_pb2",
        "__doc__": """Request for updating a specified company.
  
  Attributes:
      company:
          Required. The company resource to replace the current resource
          in the system.
      update_mask:
          Strongly recommended for the best service experience.  If [upd
          ate_mask][google.cloud.talent.v4beta1.UpdateCompanyRequest.upd
          ate_mask] is provided, only the specified fields in [company][
          google.cloud.talent.v4beta1.UpdateCompanyRequest.company] are
          updated. Otherwise all the fields are updated.  A field mask
          to specify the company fields to be updated. Only top level
          fields of [Company][google.cloud.talent.v4beta1.Company] are
          supported.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.UpdateCompanyRequest)
    },
)
_sym_db.RegisterMessage(UpdateCompanyRequest)

DeleteCompanyRequest = _reflection.GeneratedProtocolMessageType(
    "DeleteCompanyRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DELETECOMPANYREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.company_service_pb2",
        "__doc__": """Request to delete a company.
  
  Attributes:
      name:
          Required. The resource name of the company to be deleted.  The
          format is “projects/{project_id}/tenants/{tenant_id}/companies
          /{company_id}”, for example,
          “projects/foo/tenants/bar/companies/baz”.  If tenant id is
          unspecified, the default tenant is used, for example,
          “projects/foo/companies/bar”.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.DeleteCompanyRequest)
    },
)
_sym_db.RegisterMessage(DeleteCompanyRequest)

ListCompaniesRequest = _reflection.GeneratedProtocolMessageType(
    "ListCompaniesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTCOMPANIESREQUEST,
        "__module__": "google.cloud.talent_v4beta1.proto.company_service_pb2",
        "__doc__": """List companies for which the client has ACL visibility.
  
  Attributes:
      parent:
          Required. Resource name of the tenant under which the company
          is created.  The format is
          “projects/{project_id}/tenants/{tenant_id}”, for example,
          “projects/foo/tenant/bar”.  If tenant id is unspecified, the
          default tenant will be used, for example, “projects/foo”.
      page_token:
          The starting indicator from which to return results.
      page_size:
          The maximum number of companies to be returned, at most 100.
          Default is 100 if a non-positive number is provided.
      require_open_jobs:
          Set to true if the companies requested must have open jobs.
          Defaults to false.  If true, at most [page_size][google.cloud.
          talent.v4beta1.ListCompaniesRequest.page_size] of companies
          are fetched, among which only those with open jobs are
          returned.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListCompaniesRequest)
    },
)
_sym_db.RegisterMessage(ListCompaniesRequest)

ListCompaniesResponse = _reflection.GeneratedProtocolMessageType(
    "ListCompaniesResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _LISTCOMPANIESRESPONSE,
        "__module__": "google.cloud.talent_v4beta1.proto.company_service_pb2",
        "__doc__": """The List companies response object.
  
  Attributes:
      companies:
          Companies for the current client.
      next_page_token:
          A token to retrieve the next page of results.
      metadata:
          Additional information for the API invocation, such as the
          request tracking id.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.ListCompaniesResponse)
    },
)
_sym_db.RegisterMessage(ListCompaniesResponse)


DESCRIPTOR._options = None
_CREATECOMPANYREQUEST.fields_by_name["parent"]._options = None
_CREATECOMPANYREQUEST.fields_by_name["company"]._options = None
_GETCOMPANYREQUEST.fields_by_name["name"]._options = None
_UPDATECOMPANYREQUEST.fields_by_name["company"]._options = None
_DELETECOMPANYREQUEST.fields_by_name["name"]._options = None
_LISTCOMPANIESREQUEST.fields_by_name["parent"]._options = None

_COMPANYSERVICE = _descriptor.ServiceDescriptor(
    name="CompanyService",
    full_name="google.cloud.talent.v4beta1.CompanyService",
    file=DESCRIPTOR,
    index=0,
    serialized_options=b"\312A\023jobs.googleapis.com\322AShttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/jobs",
    create_key=_descriptor._internal_create_key,
    serialized_start=1100,
    serialized_end=2334,
    methods=[
        _descriptor.MethodDescriptor(
            name="CreateCompany",
            full_name="google.cloud.talent.v4beta1.CompanyService.CreateCompany",
            index=0,
            containing_service=None,
            input_type=_CREATECOMPANYREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2._COMPANY,
            serialized_options=b'\202\323\344\223\002b"0/v4beta1/{parent=projects/*/tenants/*}/companies:\001*Z+"&/v4beta1/{parent=projects/*}/companies:\001*\332A\016parent,company',
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="GetCompany",
            full_name="google.cloud.talent.v4beta1.CompanyService.GetCompany",
            index=1,
            containing_service=None,
            input_type=_GETCOMPANYREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2._COMPANY,
            serialized_options=b"\202\323\344\223\002\\\0220/v4beta1/{name=projects/*/tenants/*/companies/*}Z(\022&/v4beta1/{name=projects/*/companies/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="UpdateCompany",
            full_name="google.cloud.talent.v4beta1.CompanyService.UpdateCompany",
            index=2,
            containing_service=None,
            input_type=_UPDATECOMPANYREQUEST,
            output_type=google_dot_cloud_dot_talent__v4beta1_dot_proto_dot_company__pb2._COMPANY,
            serialized_options=b"\202\323\344\223\002r28/v4beta1/{company.name=projects/*/tenants/*/companies/*}:\001*Z32./v4beta1/{company.name=projects/*/companies/*}:\001*\332A\007company",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="DeleteCompany",
            full_name="google.cloud.talent.v4beta1.CompanyService.DeleteCompany",
            index=3,
            containing_service=None,
            input_type=_DELETECOMPANYREQUEST,
            output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
            serialized_options=b"\202\323\344\223\002\\*0/v4beta1/{name=projects/*/tenants/*/companies/*}Z(*&/v4beta1/{name=projects/*/companies/*}\332A\004name",
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.MethodDescriptor(
            name="ListCompanies",
            full_name="google.cloud.talent.v4beta1.CompanyService.ListCompanies",
            index=4,
            containing_service=None,
            input_type=_LISTCOMPANIESREQUEST,
            output_type=_LISTCOMPANIESRESPONSE,
            serialized_options=b"\202\323\344\223\002\\\0220/v4beta1/{parent=projects/*/tenants/*}/companiesZ(\022&/v4beta1/{parent=projects/*}/companies\332A\006parent",
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_COMPANYSERVICE)

DESCRIPTOR.services_by_name["CompanyService"] = _COMPANYSERVICE

# @@protoc_insertion_point(module_scope)
