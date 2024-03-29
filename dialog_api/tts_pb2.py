# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tts.proto
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
from . import media_and_files_pb2 as media__and__files__pb2
from . import users_pb2 as users__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tts.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ttts.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x15media_and_files.proto\x1a\x0busers.proto\x1a\x15scalapb/scalapb.proto\"\x9f\x01\n\tVoiceInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12%\n\x06sample\x18\x03 \x01(\x0b\x32\x15.dialog.AudioLocation\x12)\n\x06gender\x18\x04 \x01(\x0e\x32\x19.dialog.VoiceInfo.Genders\"\x1f\n\x07Genders\x12\x08\n\x04MALE\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\"\xe7\x01\n\x16RequestGetMessageVoice\x12\x1e\n\x03mid\x18\x01 \x01(\x0b\x32\x11.dialog.UUIDValue\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.dialog.RequestGetMessageVoice.VoiceParams\x1aq\n\x0bVoiceParams\x12\x17\n\x0f\x66\x65male_voice_id\x18\x01 \x01(\t\x12\x15\n\rmale_voice_id\x18\x02 \x01(\t\x12\x18\n\x10\x64\x65\x66\x61ult_voice_id\x18\x03 \x01(\t\x12\x18\n\x10low_quality_mode\x18\x04 \x01(\x08\"\xc7\x02\n\x17ResponseGetMessageVoice\x12\x1e\n\x03mid\x18\x01 \x01(\x0b\x32\x11.dialog.UUIDValue\x12:\n\x07success\x18\x02 \x01(\x0b\x32\'.dialog.ResponseGetMessageVoice.SuccessH\x00\x12:\n\x07skipped\x18\x03 \x01(\x0b\x32\'.dialog.ResponseGetMessageVoice.SkippedH\x00\x12\x36\n\x05\x65rror\x18\x04 \x01(\x0b\x32%.dialog.ResponseGetMessageVoice.ErrorH\x00\x1a/\n\x07Success\x12$\n\x05\x61udio\x18\x01 \x01(\x0b\x32\x15.dialog.AudioLocation\x1a\t\n\x07Skipped\x1a\x16\n\x05\x45rror\x12\r\n\x05\x65rror\x18\x01 \x01(\tB\x08\n\x06result\"\x16\n\x14RequestGetVoicesInfo\";\n\x15ResponseGetVoicesInfo\x12\"\n\x07results\x18\x01 \x03(\x0b\x32\x11.dialog.VoiceInfo2\xb8\x01\n\x0cTextToSpeech\x12X\n\x0fGetMessageVoice\x12\x1e.dialog.RequestGetMessageVoice\x1a\x1f.dialog.ResponseGetMessageVoice\"\x00(\x01\x30\x01\x12N\n\rGetVoicesInfo\x12\x1c.dialog.RequestGetVoicesInfo\x1a\x1d.dialog.ResponseGetVoicesInfo\"\x00\x42\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,media__and__files__pb2.DESCRIPTOR,users__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])



_VOICEINFO_GENDERS = _descriptor.EnumDescriptor(
  name='Genders',
  full_name='dialog.VoiceInfo.Genders',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MALE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=311,
  serialized_end=342,
)
_sym_db.RegisterEnumDescriptor(_VOICEINFO_GENDERS)


_VOICEINFO = _descriptor.Descriptor(
  name='VoiceInfo',
  full_name='dialog.VoiceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='dialog.VoiceInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='dialog.VoiceInfo.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample', full_name='dialog.VoiceInfo.sample', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gender', full_name='dialog.VoiceInfo.gender', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VOICEINFO_GENDERS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=183,
  serialized_end=342,
)


_REQUESTGETMESSAGEVOICE_VOICEPARAMS = _descriptor.Descriptor(
  name='VoiceParams',
  full_name='dialog.RequestGetMessageVoice.VoiceParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='female_voice_id', full_name='dialog.RequestGetMessageVoice.VoiceParams.female_voice_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='male_voice_id', full_name='dialog.RequestGetMessageVoice.VoiceParams.male_voice_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_voice_id', full_name='dialog.RequestGetMessageVoice.VoiceParams.default_voice_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low_quality_mode', full_name='dialog.RequestGetMessageVoice.VoiceParams.low_quality_mode', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=463,
  serialized_end=576,
)

_REQUESTGETMESSAGEVOICE = _descriptor.Descriptor(
  name='RequestGetMessageVoice',
  full_name='dialog.RequestGetMessageVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mid', full_name='dialog.RequestGetMessageVoice.mid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='dialog.RequestGetMessageVoice.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTGETMESSAGEVOICE_VOICEPARAMS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=345,
  serialized_end=576,
)


_RESPONSEGETMESSAGEVOICE_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='dialog.ResponseGetMessageVoice.Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio', full_name='dialog.ResponseGetMessageVoice.Success.audio', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=814,
  serialized_end=861,
)

_RESPONSEGETMESSAGEVOICE_SKIPPED = _descriptor.Descriptor(
  name='Skipped',
  full_name='dialog.ResponseGetMessageVoice.Skipped',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=863,
  serialized_end=872,
)

_RESPONSEGETMESSAGEVOICE_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='dialog.ResponseGetMessageVoice.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='dialog.ResponseGetMessageVoice.Error.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=874,
  serialized_end=896,
)

_RESPONSEGETMESSAGEVOICE = _descriptor.Descriptor(
  name='ResponseGetMessageVoice',
  full_name='dialog.ResponseGetMessageVoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mid', full_name='dialog.ResponseGetMessageVoice.mid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success', full_name='dialog.ResponseGetMessageVoice.success', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skipped', full_name='dialog.ResponseGetMessageVoice.skipped', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='dialog.ResponseGetMessageVoice.error', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEGETMESSAGEVOICE_SUCCESS, _RESPONSEGETMESSAGEVOICE_SKIPPED, _RESPONSEGETMESSAGEVOICE_ERROR, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='result', full_name='dialog.ResponseGetMessageVoice.result',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=579,
  serialized_end=906,
)


_REQUESTGETVOICESINFO = _descriptor.Descriptor(
  name='RequestGetVoicesInfo',
  full_name='dialog.RequestGetVoicesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=908,
  serialized_end=930,
)


_RESPONSEGETVOICESINFO = _descriptor.Descriptor(
  name='ResponseGetVoicesInfo',
  full_name='dialog.ResponseGetVoicesInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='dialog.ResponseGetVoicesInfo.results', index=0,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=932,
  serialized_end=991,
)

_VOICEINFO.fields_by_name['sample'].message_type = media__and__files__pb2._AUDIOLOCATION
_VOICEINFO.fields_by_name['gender'].enum_type = _VOICEINFO_GENDERS
_VOICEINFO_GENDERS.containing_type = _VOICEINFO
_REQUESTGETMESSAGEVOICE_VOICEPARAMS.containing_type = _REQUESTGETMESSAGEVOICE
_REQUESTGETMESSAGEVOICE.fields_by_name['mid'].message_type = definitions__pb2._UUIDVALUE
_REQUESTGETMESSAGEVOICE.fields_by_name['params'].message_type = _REQUESTGETMESSAGEVOICE_VOICEPARAMS
_RESPONSEGETMESSAGEVOICE_SUCCESS.fields_by_name['audio'].message_type = media__and__files__pb2._AUDIOLOCATION
_RESPONSEGETMESSAGEVOICE_SUCCESS.containing_type = _RESPONSEGETMESSAGEVOICE
_RESPONSEGETMESSAGEVOICE_SKIPPED.containing_type = _RESPONSEGETMESSAGEVOICE
_RESPONSEGETMESSAGEVOICE_ERROR.containing_type = _RESPONSEGETMESSAGEVOICE
_RESPONSEGETMESSAGEVOICE.fields_by_name['mid'].message_type = definitions__pb2._UUIDVALUE
_RESPONSEGETMESSAGEVOICE.fields_by_name['success'].message_type = _RESPONSEGETMESSAGEVOICE_SUCCESS
_RESPONSEGETMESSAGEVOICE.fields_by_name['skipped'].message_type = _RESPONSEGETMESSAGEVOICE_SKIPPED
_RESPONSEGETMESSAGEVOICE.fields_by_name['error'].message_type = _RESPONSEGETMESSAGEVOICE_ERROR
_RESPONSEGETMESSAGEVOICE.oneofs_by_name['result'].fields.append(
  _RESPONSEGETMESSAGEVOICE.fields_by_name['success'])
_RESPONSEGETMESSAGEVOICE.fields_by_name['success'].containing_oneof = _RESPONSEGETMESSAGEVOICE.oneofs_by_name['result']
_RESPONSEGETMESSAGEVOICE.oneofs_by_name['result'].fields.append(
  _RESPONSEGETMESSAGEVOICE.fields_by_name['skipped'])
_RESPONSEGETMESSAGEVOICE.fields_by_name['skipped'].containing_oneof = _RESPONSEGETMESSAGEVOICE.oneofs_by_name['result']
_RESPONSEGETMESSAGEVOICE.oneofs_by_name['result'].fields.append(
  _RESPONSEGETMESSAGEVOICE.fields_by_name['error'])
_RESPONSEGETMESSAGEVOICE.fields_by_name['error'].containing_oneof = _RESPONSEGETMESSAGEVOICE.oneofs_by_name['result']
_RESPONSEGETVOICESINFO.fields_by_name['results'].message_type = _VOICEINFO
DESCRIPTOR.message_types_by_name['VoiceInfo'] = _VOICEINFO
DESCRIPTOR.message_types_by_name['RequestGetMessageVoice'] = _REQUESTGETMESSAGEVOICE
DESCRIPTOR.message_types_by_name['ResponseGetMessageVoice'] = _RESPONSEGETMESSAGEVOICE
DESCRIPTOR.message_types_by_name['RequestGetVoicesInfo'] = _REQUESTGETVOICESINFO
DESCRIPTOR.message_types_by_name['ResponseGetVoicesInfo'] = _RESPONSEGETVOICESINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VoiceInfo = _reflection.GeneratedProtocolMessageType('VoiceInfo', (_message.Message,), {
  'DESCRIPTOR' : _VOICEINFO,
  '__module__' : 'tts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.VoiceInfo)
  })
_sym_db.RegisterMessage(VoiceInfo)

RequestGetMessageVoice = _reflection.GeneratedProtocolMessageType('RequestGetMessageVoice', (_message.Message,), {

  'VoiceParams' : _reflection.GeneratedProtocolMessageType('VoiceParams', (_message.Message,), {
    'DESCRIPTOR' : _REQUESTGETMESSAGEVOICE_VOICEPARAMS,
    '__module__' : 'tts_pb2'
    # @@protoc_insertion_point(class_scope:dialog.RequestGetMessageVoice.VoiceParams)
    })
  ,
  'DESCRIPTOR' : _REQUESTGETMESSAGEVOICE,
  '__module__' : 'tts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestGetMessageVoice)
  })
_sym_db.RegisterMessage(RequestGetMessageVoice)
_sym_db.RegisterMessage(RequestGetMessageVoice.VoiceParams)

ResponseGetMessageVoice = _reflection.GeneratedProtocolMessageType('ResponseGetMessageVoice', (_message.Message,), {

  'Success' : _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSEGETMESSAGEVOICE_SUCCESS,
    '__module__' : 'tts_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ResponseGetMessageVoice.Success)
    })
  ,

  'Skipped' : _reflection.GeneratedProtocolMessageType('Skipped', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSEGETMESSAGEVOICE_SKIPPED,
    '__module__' : 'tts_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ResponseGetMessageVoice.Skipped)
    })
  ,

  'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSEGETMESSAGEVOICE_ERROR,
    '__module__' : 'tts_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ResponseGetMessageVoice.Error)
    })
  ,
  'DESCRIPTOR' : _RESPONSEGETMESSAGEVOICE,
  '__module__' : 'tts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseGetMessageVoice)
  })
_sym_db.RegisterMessage(ResponseGetMessageVoice)
_sym_db.RegisterMessage(ResponseGetMessageVoice.Success)
_sym_db.RegisterMessage(ResponseGetMessageVoice.Skipped)
_sym_db.RegisterMessage(ResponseGetMessageVoice.Error)

RequestGetVoicesInfo = _reflection.GeneratedProtocolMessageType('RequestGetVoicesInfo', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTGETVOICESINFO,
  '__module__' : 'tts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestGetVoicesInfo)
  })
_sym_db.RegisterMessage(RequestGetVoicesInfo)

ResponseGetVoicesInfo = _reflection.GeneratedProtocolMessageType('ResponseGetVoicesInfo', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEGETVOICESINFO,
  '__module__' : 'tts_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseGetVoicesInfo)
  })
_sym_db.RegisterMessage(ResponseGetVoicesInfo)


DESCRIPTOR._options = None

_TEXTTOSPEECH = _descriptor.ServiceDescriptor(
  name='TextToSpeech',
  full_name='dialog.TextToSpeech',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=994,
  serialized_end=1178,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMessageVoice',
    full_name='dialog.TextToSpeech.GetMessageVoice',
    index=0,
    containing_service=None,
    input_type=_REQUESTGETMESSAGEVOICE,
    output_type=_RESPONSEGETMESSAGEVOICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetVoicesInfo',
    full_name='dialog.TextToSpeech.GetVoicesInfo',
    index=1,
    containing_service=None,
    input_type=_REQUESTGETVOICESINFO,
    output_type=_RESPONSEGETVOICESINFO,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTTOSPEECH)

DESCRIPTOR.services_by_name['TextToSpeech'] = _TEXTTOSPEECH

# @@protoc_insertion_point(module_scope)
