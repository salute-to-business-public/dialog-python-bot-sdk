# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from . import peers_pb2 as peers__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='notification.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12notification.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0bpeers.proto\x1a\x15scalapb/scalapb.proto\"?\n\x11SendByUserOutPeer\x12*\n\ruser_out_peer\x18\x01 \x01(\x0b\x32\x13.dialog.UserOutPeer\"\xcc\x03\n\x10SendMailResponse\x12;\n\x07success\x18\x01 \x01(\x0b\x32(.dialog.SendMailResponse.SendMailSuccessH\x00\x12\x39\n\x06reject\x18\x02 \x01(\x0b\x32\'.dialog.SendMailResponse.SendMailRejectH\x00\x1a\x11\n\x0fSendMailSuccess\x1a\xa2\x02\n\x0eSendMailReject\x12W\n\x0frecipient_limit\x18\x01 \x01(\x0b\x32<.dialog.SendMailResponse.SendMailReject.RejectRecipientLimitH\x00\x12R\n\rto_many_sends\x18\x02 \x01(\x0b\x32\x39.dialog.SendMailResponse.SendMailReject.RejectToManySendsH\x00\x1a-\n\x14RejectRecipientLimit\x12\x15\n\rblocked_until\x18\x01 \x01(\x03\x1a*\n\x11RejectToManySends\x12\x15\n\rblocked_until\x18\x01 \x01(\x03\x42\x08\n\x06rejectB\x08\n\x06result2Q\n\x0cNotification\x12\x41\n\x08SendMail\x12\x19.dialog.SendByUserOutPeer\x1a\x18.dialog.SendMailResponse\"\x00\x42\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,peers__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_SENDBYUSEROUTPEER = _descriptor.Descriptor(
  name='SendByUserOutPeer',
  full_name='dialog.SendByUserOutPeer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_out_peer', full_name='dialog.SendByUserOutPeer.user_out_peer', index=0,
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
  serialized_start=98,
  serialized_end=161,
)


_SENDMAILRESPONSE_SENDMAILSUCCESS = _descriptor.Descriptor(
  name='SendMailSuccess',
  full_name='dialog.SendMailResponse.SendMailSuccess',
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
  serialized_start=304,
  serialized_end=321,
)

_SENDMAILRESPONSE_SENDMAILREJECT_REJECTRECIPIENTLIMIT = _descriptor.Descriptor(
  name='RejectRecipientLimit',
  full_name='dialog.SendMailResponse.SendMailReject.RejectRecipientLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocked_until', full_name='dialog.SendMailResponse.SendMailReject.RejectRecipientLimit.blocked_until', index=0,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=515,
  serialized_end=560,
)

_SENDMAILRESPONSE_SENDMAILREJECT_REJECTTOMANYSENDS = _descriptor.Descriptor(
  name='RejectToManySends',
  full_name='dialog.SendMailResponse.SendMailReject.RejectToManySends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='blocked_until', full_name='dialog.SendMailResponse.SendMailReject.RejectToManySends.blocked_until', index=0,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=604,
)

_SENDMAILRESPONSE_SENDMAILREJECT = _descriptor.Descriptor(
  name='SendMailReject',
  full_name='dialog.SendMailResponse.SendMailReject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipient_limit', full_name='dialog.SendMailResponse.SendMailReject.recipient_limit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_many_sends', full_name='dialog.SendMailResponse.SendMailReject.to_many_sends', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SENDMAILRESPONSE_SENDMAILREJECT_REJECTRECIPIENTLIMIT, _SENDMAILRESPONSE_SENDMAILREJECT_REJECTTOMANYSENDS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='reject', full_name='dialog.SendMailResponse.SendMailReject.reject',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=324,
  serialized_end=614,
)

_SENDMAILRESPONSE = _descriptor.Descriptor(
  name='SendMailResponse',
  full_name='dialog.SendMailResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='dialog.SendMailResponse.success', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reject', full_name='dialog.SendMailResponse.reject', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SENDMAILRESPONSE_SENDMAILSUCCESS, _SENDMAILRESPONSE_SENDMAILREJECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='result', full_name='dialog.SendMailResponse.result',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=164,
  serialized_end=624,
)

_SENDBYUSEROUTPEER.fields_by_name['user_out_peer'].message_type = peers__pb2._USEROUTPEER
_SENDMAILRESPONSE_SENDMAILSUCCESS.containing_type = _SENDMAILRESPONSE
_SENDMAILRESPONSE_SENDMAILREJECT_REJECTRECIPIENTLIMIT.containing_type = _SENDMAILRESPONSE_SENDMAILREJECT
_SENDMAILRESPONSE_SENDMAILREJECT_REJECTTOMANYSENDS.containing_type = _SENDMAILRESPONSE_SENDMAILREJECT
_SENDMAILRESPONSE_SENDMAILREJECT.fields_by_name['recipient_limit'].message_type = _SENDMAILRESPONSE_SENDMAILREJECT_REJECTRECIPIENTLIMIT
_SENDMAILRESPONSE_SENDMAILREJECT.fields_by_name['to_many_sends'].message_type = _SENDMAILRESPONSE_SENDMAILREJECT_REJECTTOMANYSENDS
_SENDMAILRESPONSE_SENDMAILREJECT.containing_type = _SENDMAILRESPONSE
_SENDMAILRESPONSE_SENDMAILREJECT.oneofs_by_name['reject'].fields.append(
  _SENDMAILRESPONSE_SENDMAILREJECT.fields_by_name['recipient_limit'])
_SENDMAILRESPONSE_SENDMAILREJECT.fields_by_name['recipient_limit'].containing_oneof = _SENDMAILRESPONSE_SENDMAILREJECT.oneofs_by_name['reject']
_SENDMAILRESPONSE_SENDMAILREJECT.oneofs_by_name['reject'].fields.append(
  _SENDMAILRESPONSE_SENDMAILREJECT.fields_by_name['to_many_sends'])
_SENDMAILRESPONSE_SENDMAILREJECT.fields_by_name['to_many_sends'].containing_oneof = _SENDMAILRESPONSE_SENDMAILREJECT.oneofs_by_name['reject']
_SENDMAILRESPONSE.fields_by_name['success'].message_type = _SENDMAILRESPONSE_SENDMAILSUCCESS
_SENDMAILRESPONSE.fields_by_name['reject'].message_type = _SENDMAILRESPONSE_SENDMAILREJECT
_SENDMAILRESPONSE.oneofs_by_name['result'].fields.append(
  _SENDMAILRESPONSE.fields_by_name['success'])
_SENDMAILRESPONSE.fields_by_name['success'].containing_oneof = _SENDMAILRESPONSE.oneofs_by_name['result']
_SENDMAILRESPONSE.oneofs_by_name['result'].fields.append(
  _SENDMAILRESPONSE.fields_by_name['reject'])
_SENDMAILRESPONSE.fields_by_name['reject'].containing_oneof = _SENDMAILRESPONSE.oneofs_by_name['result']
DESCRIPTOR.message_types_by_name['SendByUserOutPeer'] = _SENDBYUSEROUTPEER
DESCRIPTOR.message_types_by_name['SendMailResponse'] = _SENDMAILRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SendByUserOutPeer = _reflection.GeneratedProtocolMessageType('SendByUserOutPeer', (_message.Message,), {
  'DESCRIPTOR' : _SENDBYUSEROUTPEER,
  '__module__' : 'notification_pb2'
  # @@protoc_insertion_point(class_scope:dialog.SendByUserOutPeer)
  })
_sym_db.RegisterMessage(SendByUserOutPeer)

SendMailResponse = _reflection.GeneratedProtocolMessageType('SendMailResponse', (_message.Message,), {

  'SendMailSuccess' : _reflection.GeneratedProtocolMessageType('SendMailSuccess', (_message.Message,), {
    'DESCRIPTOR' : _SENDMAILRESPONSE_SENDMAILSUCCESS,
    '__module__' : 'notification_pb2'
    # @@protoc_insertion_point(class_scope:dialog.SendMailResponse.SendMailSuccess)
    })
  ,

  'SendMailReject' : _reflection.GeneratedProtocolMessageType('SendMailReject', (_message.Message,), {

    'RejectRecipientLimit' : _reflection.GeneratedProtocolMessageType('RejectRecipientLimit', (_message.Message,), {
      'DESCRIPTOR' : _SENDMAILRESPONSE_SENDMAILREJECT_REJECTRECIPIENTLIMIT,
      '__module__' : 'notification_pb2'
      # @@protoc_insertion_point(class_scope:dialog.SendMailResponse.SendMailReject.RejectRecipientLimit)
      })
    ,

    'RejectToManySends' : _reflection.GeneratedProtocolMessageType('RejectToManySends', (_message.Message,), {
      'DESCRIPTOR' : _SENDMAILRESPONSE_SENDMAILREJECT_REJECTTOMANYSENDS,
      '__module__' : 'notification_pb2'
      # @@protoc_insertion_point(class_scope:dialog.SendMailResponse.SendMailReject.RejectToManySends)
      })
    ,
    'DESCRIPTOR' : _SENDMAILRESPONSE_SENDMAILREJECT,
    '__module__' : 'notification_pb2'
    # @@protoc_insertion_point(class_scope:dialog.SendMailResponse.SendMailReject)
    })
  ,
  'DESCRIPTOR' : _SENDMAILRESPONSE,
  '__module__' : 'notification_pb2'
  # @@protoc_insertion_point(class_scope:dialog.SendMailResponse)
  })
_sym_db.RegisterMessage(SendMailResponse)
_sym_db.RegisterMessage(SendMailResponse.SendMailSuccess)
_sym_db.RegisterMessage(SendMailResponse.SendMailReject)
_sym_db.RegisterMessage(SendMailResponse.SendMailReject.RejectRecipientLimit)
_sym_db.RegisterMessage(SendMailResponse.SendMailReject.RejectToManySends)


DESCRIPTOR._options = None

_NOTIFICATION = _descriptor.ServiceDescriptor(
  name='Notification',
  full_name='dialog.Notification',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=626,
  serialized_end=707,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendMail',
    full_name='dialog.Notification.SendMail',
    index=0,
    containing_service=None,
    input_type=_SENDBYUSEROUTPEER,
    output_type=_SENDMAILRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOTIFICATION)

DESCRIPTOR.services_by_name['Notification'] = _NOTIFICATION

# @@protoc_insertion_point(module_scope)