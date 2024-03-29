# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: push_content.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import definitions_pb2 as definitions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='push_content.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12push_content.proto\x12\x06\x64ialog\x1a\x11\x64\x65\x66initions.proto\"6\n\x11LocalizableString\x12\x0f\n\x07loc_key\x18\x01 \x01(\t\x12\x10\n\x08loc_args\x18\x02 \x03(\t\"J\n\x08PushPeer\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.dialog.PushPeerType\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0e\n\x06str_id\x18\x03 \x01(\t\"\xd2\x03\n\x14\x45ncryptedPushContent\x12\x33\n\x0eloc_alert_body\x18\x01 \x01(\x0b\x32\x19.dialog.LocalizableStringH\x00\x12\x1b\n\x11simple_alert_body\x18\x02 \x01(\tH\x00\x12\x34\n\x0floc_alert_title\x18\x03 \x01(\x0b\x32\x19.dialog.LocalizableStringH\x01\x12\x1c\n\x12simple_alert_title\x18\x04 \x01(\tH\x01\x12\r\n\x05sound\x18\x05 \x01(\t\x12\x1e\n\x16unread_message_counter\x18\x06 \x01(\x05\x12\x1e\n\x04peer\x18\x07 \x01(\x0b\x32\x10.dialog.PushPeer\x12\x34\n\nmessage_id\x18\n \x01(\x0b\x32\x11.dialog.UUIDValueB\r\x8a\xea\x30\t\n\x07visible\x12\x15\n\risRespondable\x18\x0b \x01(\x08\x12\x16\n\x0esender_user_id\x18\x0c \x01(\x05\x12\x0c\n\x04\x64\x61te\x18\r \x01(\x03\x12)\n\nevent_type\x18\x0e \x01(\x0e\x32\x15.dialog.PushEventTypeB\x0c\n\nalert_bodyB\r\n\x0b\x61lert_titleJ\x04\x08\x08\x10\tJ\x04\x08\t\x10\n\"U\n\x18\x45ncryptedJazzPushContent\x12\x11\n\troom_link\x18\x01 \x01(\t\x12\x0f\n\x07room_id\x18\x02 \x01(\t\x12\x15\n\rroom_password\x18\x03 \x01(\t*w\n\x0cPushPeerType\x12\x1a\n\x16PUSH_PEER_TYPE_PRIVATE\x10\x00\x12\x18\n\x14PUSH_PEER_TYPE_GROUP\x10\x01\x12\x16\n\x12PUSH_PEER_TYPE_SIP\x10\x02\x12\x19\n\x15PUSH_PEER_TYPE_THREAD\x10\x03*3\n\rPushEventType\x12\n\n\x06\x43REATE\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\n\n\x06\x44\x45LETE\x10\x02\x42\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[definitions__pb2.DESCRIPTOR,])

_PUSHPEERTYPE = _descriptor.EnumDescriptor(
  name='PushPeerType',
  full_name='dialog.PushPeerType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PUSH_PEER_TYPE_PRIVATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUSH_PEER_TYPE_GROUP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUSH_PEER_TYPE_SIP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUSH_PEER_TYPE_THREAD', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=737,
  serialized_end=856,
)
_sym_db.RegisterEnumDescriptor(_PUSHPEERTYPE)

PushPeerType = enum_type_wrapper.EnumTypeWrapper(_PUSHPEERTYPE)
_PUSHEVENTTYPE = _descriptor.EnumDescriptor(
  name='PushEventType',
  full_name='dialog.PushEventType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=858,
  serialized_end=909,
)
_sym_db.RegisterEnumDescriptor(_PUSHEVENTTYPE)

PushEventType = enum_type_wrapper.EnumTypeWrapper(_PUSHEVENTTYPE)
PUSH_PEER_TYPE_PRIVATE = 0
PUSH_PEER_TYPE_GROUP = 1
PUSH_PEER_TYPE_SIP = 2
PUSH_PEER_TYPE_THREAD = 3
CREATE = 0
UPDATE = 1
DELETE = 2



_LOCALIZABLESTRING = _descriptor.Descriptor(
  name='LocalizableString',
  full_name='dialog.LocalizableString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='loc_key', full_name='dialog.LocalizableString.loc_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loc_args', full_name='dialog.LocalizableString.loc_args', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=49,
  serialized_end=103,
)


_PUSHPEER = _descriptor.Descriptor(
  name='PushPeer',
  full_name='dialog.PushPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='dialog.PushPeer.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='dialog.PushPeer.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='str_id', full_name='dialog.PushPeer.str_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=105,
  serialized_end=179,
)


_ENCRYPTEDPUSHCONTENT = _descriptor.Descriptor(
  name='EncryptedPushContent',
  full_name='dialog.EncryptedPushContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='loc_alert_body', full_name='dialog.EncryptedPushContent.loc_alert_body', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simple_alert_body', full_name='dialog.EncryptedPushContent.simple_alert_body', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loc_alert_title', full_name='dialog.EncryptedPushContent.loc_alert_title', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='simple_alert_title', full_name='dialog.EncryptedPushContent.simple_alert_title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sound', full_name='dialog.EncryptedPushContent.sound', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unread_message_counter', full_name='dialog.EncryptedPushContent.unread_message_counter', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.EncryptedPushContent.peer', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='dialog.EncryptedPushContent.message_id', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007visible', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isRespondable', full_name='dialog.EncryptedPushContent.isRespondable', index=8,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender_user_id', full_name='dialog.EncryptedPushContent.sender_user_id', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='dialog.EncryptedPushContent.date', index=10,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event_type', full_name='dialog.EncryptedPushContent.event_type', index=11,
      number=14, type=14, cpp_type=8, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='alert_body', full_name='dialog.EncryptedPushContent.alert_body',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='alert_title', full_name='dialog.EncryptedPushContent.alert_title',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=182,
  serialized_end=648,
)


_ENCRYPTEDJAZZPUSHCONTENT = _descriptor.Descriptor(
  name='EncryptedJazzPushContent',
  full_name='dialog.EncryptedJazzPushContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='room_link', full_name='dialog.EncryptedJazzPushContent.room_link', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_id', full_name='dialog.EncryptedJazzPushContent.room_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='room_password', full_name='dialog.EncryptedJazzPushContent.room_password', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=650,
  serialized_end=735,
)

_PUSHPEER.fields_by_name['type'].enum_type = _PUSHPEERTYPE
_ENCRYPTEDPUSHCONTENT.fields_by_name['loc_alert_body'].message_type = _LOCALIZABLESTRING
_ENCRYPTEDPUSHCONTENT.fields_by_name['loc_alert_title'].message_type = _LOCALIZABLESTRING
_ENCRYPTEDPUSHCONTENT.fields_by_name['peer'].message_type = _PUSHPEER
_ENCRYPTEDPUSHCONTENT.fields_by_name['message_id'].message_type = definitions__pb2._UUIDVALUE
_ENCRYPTEDPUSHCONTENT.fields_by_name['event_type'].enum_type = _PUSHEVENTTYPE
_ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_body'].fields.append(
  _ENCRYPTEDPUSHCONTENT.fields_by_name['loc_alert_body'])
_ENCRYPTEDPUSHCONTENT.fields_by_name['loc_alert_body'].containing_oneof = _ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_body']
_ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_body'].fields.append(
  _ENCRYPTEDPUSHCONTENT.fields_by_name['simple_alert_body'])
_ENCRYPTEDPUSHCONTENT.fields_by_name['simple_alert_body'].containing_oneof = _ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_body']
_ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_title'].fields.append(
  _ENCRYPTEDPUSHCONTENT.fields_by_name['loc_alert_title'])
_ENCRYPTEDPUSHCONTENT.fields_by_name['loc_alert_title'].containing_oneof = _ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_title']
_ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_title'].fields.append(
  _ENCRYPTEDPUSHCONTENT.fields_by_name['simple_alert_title'])
_ENCRYPTEDPUSHCONTENT.fields_by_name['simple_alert_title'].containing_oneof = _ENCRYPTEDPUSHCONTENT.oneofs_by_name['alert_title']
DESCRIPTOR.message_types_by_name['LocalizableString'] = _LOCALIZABLESTRING
DESCRIPTOR.message_types_by_name['PushPeer'] = _PUSHPEER
DESCRIPTOR.message_types_by_name['EncryptedPushContent'] = _ENCRYPTEDPUSHCONTENT
DESCRIPTOR.message_types_by_name['EncryptedJazzPushContent'] = _ENCRYPTEDJAZZPUSHCONTENT
DESCRIPTOR.enum_types_by_name['PushPeerType'] = _PUSHPEERTYPE
DESCRIPTOR.enum_types_by_name['PushEventType'] = _PUSHEVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocalizableString = _reflection.GeneratedProtocolMessageType('LocalizableString', (_message.Message,), {
  'DESCRIPTOR' : _LOCALIZABLESTRING,
  '__module__' : 'push_content_pb2'
  # @@protoc_insertion_point(class_scope:dialog.LocalizableString)
  })
_sym_db.RegisterMessage(LocalizableString)

PushPeer = _reflection.GeneratedProtocolMessageType('PushPeer', (_message.Message,), {
  'DESCRIPTOR' : _PUSHPEER,
  '__module__' : 'push_content_pb2'
  # @@protoc_insertion_point(class_scope:dialog.PushPeer)
  })
_sym_db.RegisterMessage(PushPeer)

EncryptedPushContent = _reflection.GeneratedProtocolMessageType('EncryptedPushContent', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTEDPUSHCONTENT,
  '__module__' : 'push_content_pb2'
  # @@protoc_insertion_point(class_scope:dialog.EncryptedPushContent)
  })
_sym_db.RegisterMessage(EncryptedPushContent)

EncryptedJazzPushContent = _reflection.GeneratedProtocolMessageType('EncryptedJazzPushContent', (_message.Message,), {
  'DESCRIPTOR' : _ENCRYPTEDJAZZPUSHCONTENT,
  '__module__' : 'push_content_pb2'
  # @@protoc_insertion_point(class_scope:dialog.EncryptedJazzPushContent)
  })
_sym_db.RegisterMessage(EncryptedJazzPushContent)


DESCRIPTOR._options = None
_ENCRYPTEDPUSHCONTENT.fields_by_name['message_id']._options = None
# @@protoc_insertion_point(module_scope)
