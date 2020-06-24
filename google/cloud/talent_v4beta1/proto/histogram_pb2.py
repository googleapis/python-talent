# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/talent_v4beta1/proto/histogram.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/talent_v4beta1/proto/histogram.proto",
    package="google.cloud.talent.v4beta1",
    syntax="proto3",
    serialized_options=b"\n\037com.google.cloud.talent.v4beta1B\016HistogramProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\242\002\003CTS",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n1google/cloud/talent_v4beta1/proto/histogram.proto\x12\x1bgoogle.cloud.talent.v4beta1\x1a\x1cgoogle/api/annotations.proto")\n\x0eHistogramQuery\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t"\xb6\x01\n\x14HistogramQueryResult\x12\x17\n\x0fhistogram_query\x18\x01 \x01(\t\x12S\n\thistogram\x18\x02 \x03(\x0b\x32@.google.cloud.talent.v4beta1.HistogramQueryResult.HistogramEntry\x1a\x30\n\x0eHistogramEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x42|\n\x1f\x63om.google.cloud.talent.v4beta1B\x0eHistogramProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/talent/v4beta1;talent\xa2\x02\x03\x43TSb\x06proto3',
    dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR],
)


_HISTOGRAMQUERY = _descriptor.Descriptor(
    name="HistogramQuery",
    full_name="google.cloud.talent.v4beta1.HistogramQuery",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="histogram_query",
            full_name="google.cloud.talent.v4beta1.HistogramQuery.histogram_query",
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
    serialized_start=112,
    serialized_end=153,
)


_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY = _descriptor.Descriptor(
    name="HistogramEntry",
    full_name="google.cloud.talent.v4beta1.HistogramQueryResult.HistogramEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.talent.v4beta1.HistogramQueryResult.HistogramEntry.key",
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
            name="value",
            full_name="google.cloud.talent.v4beta1.HistogramQueryResult.HistogramEntry.value",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
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
    serialized_options=b"8\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=290,
    serialized_end=338,
)

_HISTOGRAMQUERYRESULT = _descriptor.Descriptor(
    name="HistogramQueryResult",
    full_name="google.cloud.talent.v4beta1.HistogramQueryResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="histogram_query",
            full_name="google.cloud.talent.v4beta1.HistogramQueryResult.histogram_query",
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
            name="histogram",
            full_name="google.cloud.talent.v4beta1.HistogramQueryResult.histogram",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=156,
    serialized_end=338,
)

_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY.containing_type = _HISTOGRAMQUERYRESULT
_HISTOGRAMQUERYRESULT.fields_by_name[
    "histogram"
].message_type = _HISTOGRAMQUERYRESULT_HISTOGRAMENTRY
DESCRIPTOR.message_types_by_name["HistogramQuery"] = _HISTOGRAMQUERY
DESCRIPTOR.message_types_by_name["HistogramQueryResult"] = _HISTOGRAMQUERYRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HistogramQuery = _reflection.GeneratedProtocolMessageType(
    "HistogramQuery",
    (_message.Message,),
    {
        "DESCRIPTOR": _HISTOGRAMQUERY,
        "__module__": "google.cloud.talent_v4beta1.proto.histogram_pb2",
        "__doc__": """The histogram request.
  
  Attributes:
      histogram_query:
          An expression specifies a histogram request against matching
          resources (for example, jobs, profiles) for searches.  See [Se
          archJobsRequest.histogram_queries][google.cloud.talent.v4beta1
          .SearchJobsRequest.histogram_queries] and [SearchProfilesReque
          st.histogram_queries][google.cloud.talent.v4beta1.SearchProfil
          esRequest.histogram_queries] for details about syntax.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.HistogramQuery)
    },
)
_sym_db.RegisterMessage(HistogramQuery)

HistogramQueryResult = _reflection.GeneratedProtocolMessageType(
    "HistogramQueryResult",
    (_message.Message,),
    {
        "HistogramEntry": _reflection.GeneratedProtocolMessageType(
            "HistogramEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _HISTOGRAMQUERYRESULT_HISTOGRAMENTRY,
                "__module__": "google.cloud.talent_v4beta1.proto.histogram_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.HistogramQueryResult.HistogramEntry)
            },
        ),
        "DESCRIPTOR": _HISTOGRAMQUERYRESULT,
        "__module__": "google.cloud.talent_v4beta1.proto.histogram_pb2",
        "__doc__": """Histogram result that matches
  [HistogramQuery][google.cloud.talent.v4beta1.HistogramQuery] specified
  in searches.
  
  Attributes:
      histogram_query:
          Requested histogram expression.
      histogram:
          A map from the values of the facet associated with distinct
          values to the number of matching entries with corresponding
          value.  The key format is:  -  (for string histogram) string
          values stored in the field. -  (for named numeric bucket) name
          specified in ``bucket()`` function,    like for ``bucket(0,
          MAX, "non-negative")``, the key will be    ``non-negative``. -
          (for anonymous numeric bucket) range formatted as
          ``<low>-<high>``,    for example, ``0-1000``, ``MIN-0``, and
          ``0-MAX``.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.talent.v4beta1.HistogramQueryResult)
    },
)
_sym_db.RegisterMessage(HistogramQueryResult)
_sym_db.RegisterMessage(HistogramQueryResult.HistogramEntry)


DESCRIPTOR._options = None
_HISTOGRAMQUERYRESULT_HISTOGRAMENTRY._options = None
# @@protoc_insertion_point(module_scope)
