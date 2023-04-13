# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config_sync.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import definitions_pb2 as definitions__pb2
from . import miscellaneous_pb2 as miscellaneous__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config_sync.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x63onfig_sync.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x15scalapb/scalapb.proto\"b\n\tParameter\x12\x1a\n\x03key\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x1b\n\x05value\x18\x02 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden\x12\x1c\n\x05\x63lock\x18\x03 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible\"H\n\x14RequestGetParameters\x12\x12\n\nfrom_clock\x18\x01 \x01(\x03:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"]\n\x15ResponseGetParameters\x12%\n\nparameters\x18\x01 \x03(\x0b\x32\x11.dialog.Parameter:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"\xa9\x01\n\x14RequestEditParameter\x12\x1a\n\x03key\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x0c\x8a\xea\x30\x08\n\x06hidden\x12\x1c\n\x05\x63lock\x18\x03 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"e\n\x0b\x46\x65\x61tureFlag\x12\x1a\n\x03key\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x1c\n\x05value\x18\x02 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x1c\n\x05\x63lock\x18\x03 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible\"G\n\x13RequestFeatureFlags\x12\x12\n\nfrom_clock\x18\x01 \x01(\x03:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"b\n\x14ResponseFeatureFlags\x12+\n\x0e\x66\x65\x61ture_config\x18\x01 \x03(\x0b\x32\x13.dialog.FeatureFlag:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"O\n\x18UpdateFeatureFlagChanged\x12\x33\n\x07\x66\x65\x61ture\x18\x01 \x01(\x0b\x32\x13.dialog.FeatureFlagB\r\x8a\xea\x30\t\n\x07visible\"\x95\x01\n\x16UpdateParameterChanged\x12\x1a\n\x03key\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x0c\x8a\xea\x30\x08\n\x06hidden\x12$\n\tparameter\x18\x03 \x01(\x0b\x32\x11.dialog.Parameter2\xf2\x02\n\nConfigSync\x12z\n\rGetParameters\x12\x1c.dialog.RequestGetParameters\x1a\x1d.dialog.ResponseGetParameters\",\x82\xd3\xe4\x93\x02&\"!/v1/grpc/ConfigSync/GetParameters:\x01*\x12p\n\rEditParameter\x12\x1c.dialog.RequestEditParameter\x1a\x13.dialog.ResponseSeq\",\x82\xd3\xe4\x93\x02&\"!/v1/grpc/ConfigSync/EditParameter:\x01*\x12v\n\x0c\x46\x65\x61tureFlags\x12\x1b.dialog.RequestFeatureFlags\x1a\x1c.dialog.ResponseFeatureFlags\"+\x82\xd3\xe4\x93\x02%\" /v1/grpc/ConfigSync/FeatureFlags:\x01*B\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_PARAMETER = _descriptor.Descriptor(
  name='Parameter',
  full_name='dialog.Parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dialog.Parameter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dialog.Parameter.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clock', full_name='dialog.Parameter.clock', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=252,
)


_REQUESTGETPARAMETERS = _descriptor.Descriptor(
  name='RequestGetParameters',
  full_name='dialog.RequestGetParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_clock', full_name='dialog.RequestGetParameters.from_clock', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=326,
)


_RESPONSEGETPARAMETERS = _descriptor.Descriptor(
  name='ResponseGetParameters',
  full_name='dialog.ResponseGetParameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='dialog.ResponseGetParameters.parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=421,
)


_REQUESTEDITPARAMETER = _descriptor.Descriptor(
  name='RequestEditParameter',
  full_name='dialog.RequestEditParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dialog.RequestEditParameter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dialog.RequestEditParameter.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clock', full_name='dialog.RequestEditParameter.clock', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=424,
  serialized_end=593,
)


_FEATUREFLAG = _descriptor.Descriptor(
  name='FeatureFlag',
  full_name='dialog.FeatureFlag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dialog.FeatureFlag.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dialog.FeatureFlag.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clock', full_name='dialog.FeatureFlag.clock', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=696,
)


_REQUESTFEATUREFLAGS = _descriptor.Descriptor(
  name='RequestFeatureFlags',
  full_name='dialog.RequestFeatureFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_clock', full_name='dialog.RequestFeatureFlags.from_clock', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=698,
  serialized_end=769,
)


_RESPONSEFEATUREFLAGS = _descriptor.Descriptor(
  name='ResponseFeatureFlags',
  full_name='dialog.ResponseFeatureFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_config', full_name='dialog.ResponseFeatureFlags.feature_config', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=869,
)


_UPDATEFEATUREFLAGCHANGED = _descriptor.Descriptor(
  name='UpdateFeatureFlagChanged',
  full_name='dialog.UpdateFeatureFlagChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature', full_name='dialog.UpdateFeatureFlagChanged.feature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=871,
  serialized_end=950,
)


_UPDATEPARAMETERCHANGED = _descriptor.Descriptor(
  name='UpdateParameterChanged',
  full_name='dialog.UpdateParameterChanged',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dialog.UpdateParameterChanged.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dialog.UpdateParameterChanged.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter', full_name='dialog.UpdateParameterChanged.parameter', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=1102,
)

_RESPONSEGETPARAMETERS.fields_by_name['parameters'].message_type = _PARAMETER
_REQUESTEDITPARAMETER.fields_by_name['value'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_RESPONSEFEATUREFLAGS.fields_by_name['feature_config'].message_type = _FEATUREFLAG
_UPDATEFEATUREFLAGCHANGED.fields_by_name['feature'].message_type = _FEATUREFLAG
_UPDATEPARAMETERCHANGED.fields_by_name['value'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPARAMETERCHANGED.fields_by_name['parameter'].message_type = _PARAMETER
DESCRIPTOR.message_types_by_name['Parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['RequestGetParameters'] = _REQUESTGETPARAMETERS
DESCRIPTOR.message_types_by_name['ResponseGetParameters'] = _RESPONSEGETPARAMETERS
DESCRIPTOR.message_types_by_name['RequestEditParameter'] = _REQUESTEDITPARAMETER
DESCRIPTOR.message_types_by_name['FeatureFlag'] = _FEATUREFLAG
DESCRIPTOR.message_types_by_name['RequestFeatureFlags'] = _REQUESTFEATUREFLAGS
DESCRIPTOR.message_types_by_name['ResponseFeatureFlags'] = _RESPONSEFEATUREFLAGS
DESCRIPTOR.message_types_by_name['UpdateFeatureFlagChanged'] = _UPDATEFEATUREFLAGCHANGED
DESCRIPTOR.message_types_by_name['UpdateParameterChanged'] = _UPDATEPARAMETERCHANGED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Parameter = _reflection.GeneratedProtocolMessageType('Parameter', (_message.Message,), {
  'DESCRIPTOR' : _PARAMETER,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.Parameter)
  })
_sym_db.RegisterMessage(Parameter)

RequestGetParameters = _reflection.GeneratedProtocolMessageType('RequestGetParameters', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTGETPARAMETERS,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestGetParameters)
  })
_sym_db.RegisterMessage(RequestGetParameters)

ResponseGetParameters = _reflection.GeneratedProtocolMessageType('ResponseGetParameters', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEGETPARAMETERS,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseGetParameters)
  })
_sym_db.RegisterMessage(ResponseGetParameters)

RequestEditParameter = _reflection.GeneratedProtocolMessageType('RequestEditParameter', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITPARAMETER,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditParameter)
  })
_sym_db.RegisterMessage(RequestEditParameter)

FeatureFlag = _reflection.GeneratedProtocolMessageType('FeatureFlag', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREFLAG,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.FeatureFlag)
  })
_sym_db.RegisterMessage(FeatureFlag)

RequestFeatureFlags = _reflection.GeneratedProtocolMessageType('RequestFeatureFlags', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTFEATUREFLAGS,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestFeatureFlags)
  })
_sym_db.RegisterMessage(RequestFeatureFlags)

ResponseFeatureFlags = _reflection.GeneratedProtocolMessageType('ResponseFeatureFlags', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEFEATUREFLAGS,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseFeatureFlags)
  })
_sym_db.RegisterMessage(ResponseFeatureFlags)

UpdateFeatureFlagChanged = _reflection.GeneratedProtocolMessageType('UpdateFeatureFlagChanged', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEFEATUREFLAGCHANGED,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateFeatureFlagChanged)
  })
_sym_db.RegisterMessage(UpdateFeatureFlagChanged)

UpdateParameterChanged = _reflection.GeneratedProtocolMessageType('UpdateParameterChanged', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPARAMETERCHANGED,
  '__module__' : 'config_sync_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateParameterChanged)
  })
_sym_db.RegisterMessage(UpdateParameterChanged)


DESCRIPTOR._options = None
_PARAMETER.fields_by_name['key']._options = None
_PARAMETER.fields_by_name['value']._options = None
_PARAMETER.fields_by_name['clock']._options = None
_REQUESTGETPARAMETERS._options = None
_RESPONSEGETPARAMETERS._options = None
_REQUESTEDITPARAMETER.fields_by_name['key']._options = None
_REQUESTEDITPARAMETER.fields_by_name['value']._options = None
_REQUESTEDITPARAMETER.fields_by_name['clock']._options = None
_REQUESTEDITPARAMETER._options = None
_FEATUREFLAG.fields_by_name['key']._options = None
_FEATUREFLAG.fields_by_name['value']._options = None
_FEATUREFLAG.fields_by_name['clock']._options = None
_REQUESTFEATUREFLAGS._options = None
_RESPONSEFEATUREFLAGS._options = None
_UPDATEFEATUREFLAGCHANGED.fields_by_name['feature']._options = None
_UPDATEPARAMETERCHANGED.fields_by_name['key']._options = None
_UPDATEPARAMETERCHANGED.fields_by_name['value']._options = None

_CONFIGSYNC = _descriptor.ServiceDescriptor(
  name='ConfigSync',
  full_name='dialog.ConfigSync',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1105,
  serialized_end=1475,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetParameters',
    full_name='dialog.ConfigSync.GetParameters',
    index=0,
    containing_service=None,
    input_type=_REQUESTGETPARAMETERS,
    output_type=_RESPONSEGETPARAMETERS,
    serialized_options=b'\202\323\344\223\002&\"!/v1/grpc/ConfigSync/GetParameters:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditParameter',
    full_name='dialog.ConfigSync.EditParameter',
    index=1,
    containing_service=None,
    input_type=_REQUESTEDITPARAMETER,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002&\"!/v1/grpc/ConfigSync/EditParameter:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FeatureFlags',
    full_name='dialog.ConfigSync.FeatureFlags',
    index=2,
    containing_service=None,
    input_type=_REQUESTFEATUREFLAGS,
    output_type=_RESPONSEFEATUREFLAGS,
    serialized_options=b'\202\323\344\223\002%\" /v1/grpc/ConfigSync/FeatureFlags:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONFIGSYNC)

DESCRIPTOR.services_by_name['ConfigSync'] = _CONFIGSYNC

# @@protoc_insertion_point(module_scope)
