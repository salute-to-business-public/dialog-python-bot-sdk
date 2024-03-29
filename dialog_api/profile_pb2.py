# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import definitions_pb2 as definitions__pb2
from . import miscellaneous_pb2 as miscellaneous__pb2
from . import media_and_files_pb2 as media__and__files__pb2
from . import users_pb2 as users__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='profile.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rprofile.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x15media_and_files.proto\x1a\x0busers.proto\x1a\x15scalapb/scalapb.proto\"K\n\x0fRequestEditName\x12\x1a\n\x04name\x18\x01 \x01(\tB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"r\n\x13RequestEditNickName\x12=\n\x08nickname\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"U\n\x14RequestCheckNickName\x12\x1f\n\x08nickname\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"k\n\x10RequestEditAbout\x12\x39\n\x05\x61\x62out\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"m\n\x11RequestEditAvatar\x12:\n\rfile_location\x18\x01 \x01(\x0b\x32\x14.dialog.FileLocationB\r\x8a\xea\x30\t\n\x07\x63ompact:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"o\n\x12ResponseEditAvatar\x12\x1e\n\x06\x61vatar\x18\x01 \x01(\x0b\x32\x0e.dialog.Avatar\x12\x0b\n\x03seq\x18\x02 \x01(\x05\x12\r\n\x05state\x18\x03 \x01(\x0c:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse\"3\n\x13RequestRemoveAvatar:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"P\n\x15RequestEditMyTimeZone\x12\x19\n\x02tz\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"k\n\x1fRequestEditMyPreferredLanguages\x12*\n\x13preferred_languages\x18\x01 \x03(\tB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"V\n\x0eRequestEditSex\x12&\n\x03sex\x18\x01 \x01(\x0e\x32\x0b.dialog.SexB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"_\n\x18RequestEditCustomProfile\x12%\n\x0e\x63ustom_profile\x18\x01 \x01(\tB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"j\n\x17RequestChangeUserStatus\x12\x31\n\x06status\x18\x01 \x01(\x0b\x32\x12.dialog.UserStatusB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"q\n\x18RequestUpdateBotCommands\x12\x37\n\x0c\x62ot_commands\x18\x01 \x03(\x0b\x32\x12.dialog.BotCommandB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest2\xd2\n\n\x07Profile\x12^\n\x08\x45\x64itName\x12\x17.dialog.RequestEditName\x1a\x13.dialog.ResponseSeq\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/grpc/Profile/EditName:\x01*\x12j\n\x0c\x45\x64itNickName\x12\x1b.dialog.RequestEditNickName\x1a\x13.dialog.ResponseSeq\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v1/grpc/Profile/EditNickName:\x01*\x12n\n\rCheckNickName\x12\x1c.dialog.RequestCheckNickName\x1a\x14.dialog.ResponseBool\")\x82\xd3\xe4\x93\x02#\"\x1e/v1/grpc/Profile/CheckNickName:\x01*\x12\x61\n\tEditAbout\x12\x18.dialog.RequestEditAbout\x1a\x13.dialog.ResponseSeq\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/grpc/Profile/EditAbout:\x01*\x12k\n\nEditAvatar\x12\x19.dialog.RequestEditAvatar\x1a\x1a.dialog.ResponseEditAvatar\"&\x82\xd3\xe4\x93\x02 \"\x1b/v1/grpc/Profile/EditAvatar:\x01*\x12j\n\x0cRemoveAvatar\x12\x1b.dialog.RequestRemoveAvatar\x1a\x13.dialog.ResponseSeq\"(\x82\xd3\xe4\x93\x02\"\"\x1d/v1/grpc/Profile/RemoveAvatar:\x01*\x12p\n\x0e\x45\x64itMyTimeZone\x12\x1d.dialog.RequestEditMyTimeZone\x1a\x13.dialog.ResponseSeq\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/grpc/Profile/EditMyTimeZone:\x01*\x12\x8e\x01\n\x18\x45\x64itMyPreferredLanguages\x12\'.dialog.RequestEditMyPreferredLanguages\x1a\x13.dialog.ResponseSeq\"4\x82\xd3\xe4\x93\x02.\")/v1/grpc/Profile/EditMyPreferredLanguages:\x01*\x12[\n\x07\x45\x64itSex\x12\x16.dialog.RequestEditSex\x1a\x13.dialog.ResponseSeq\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/v1/grpc/Profile/EditSex:\x01*\x12y\n\x11\x45\x64itCustomProfile\x12 .dialog.RequestEditCustomProfile\x1a\x13.dialog.ResponseSeq\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/grpc/Profile/EditCustomProfile:\x01*\x12v\n\x10\x43hangeUserStatus\x12\x1f.dialog.RequestChangeUserStatus\x1a\x13.dialog.ResponseSeq\",\x82\xd3\xe4\x93\x02&\"!/v1/grpc/Profile/ChangeUserStatus:\x01*\x12|\n\x11UpdateBotCommands\x12 .dialog.RequestUpdateBotCommands\x1a\x16.google.protobuf.Empty\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/grpc/Profile/UpdateBotCommands:\x01*B\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,media__and__files__pb2.DESCRIPTOR,users__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_REQUESTEDITNAME = _descriptor.Descriptor(
  name='RequestEditName',
  full_name='dialog.RequestEditName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='dialog.RequestEditName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=215,
  serialized_end=290,
)


_REQUESTEDITNICKNAME = _descriptor.Descriptor(
  name='RequestEditNickName',
  full_name='dialog.RequestEditNickName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dialog.RequestEditNickName.nickname', index=0,
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
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=406,
)


_REQUESTCHECKNICKNAME = _descriptor.Descriptor(
  name='RequestCheckNickName',
  full_name='dialog.RequestCheckNickName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='nickname', full_name='dialog.RequestCheckNickName.nickname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=408,
  serialized_end=493,
)


_REQUESTEDITABOUT = _descriptor.Descriptor(
  name='RequestEditAbout',
  full_name='dialog.RequestEditAbout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='about', full_name='dialog.RequestEditAbout.about', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=495,
  serialized_end=602,
)


_REQUESTEDITAVATAR = _descriptor.Descriptor(
  name='RequestEditAvatar',
  full_name='dialog.RequestEditAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_location', full_name='dialog.RequestEditAvatar.file_location', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\t\n\007compact', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=604,
  serialized_end=713,
)


_RESPONSEEDITAVATAR = _descriptor.Descriptor(
  name='ResponseEditAvatar',
  full_name='dialog.ResponseEditAvatar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar', full_name='dialog.ResponseEditAvatar.avatar', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='seq', full_name='dialog.ResponseEditAvatar.seq', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='dialog.ResponseEditAvatar.state', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=715,
  serialized_end=826,
)


_REQUESTREMOVEAVATAR = _descriptor.Descriptor(
  name='RequestRemoveAvatar',
  full_name='dialog.RequestRemoveAvatar',
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
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=828,
  serialized_end=879,
)


_REQUESTEDITMYTIMEZONE = _descriptor.Descriptor(
  name='RequestEditMyTimeZone',
  full_name='dialog.RequestEditMyTimeZone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tz', full_name='dialog.RequestEditMyTimeZone.tz', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=881,
  serialized_end=961,
)


_REQUESTEDITMYPREFERREDLANGUAGES = _descriptor.Descriptor(
  name='RequestEditMyPreferredLanguages',
  full_name='dialog.RequestEditMyPreferredLanguages',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='preferred_languages', full_name='dialog.RequestEditMyPreferredLanguages.preferred_languages', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=963,
  serialized_end=1070,
)


_REQUESTEDITSEX = _descriptor.Descriptor(
  name='RequestEditSex',
  full_name='dialog.RequestEditSex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sex', full_name='dialog.RequestEditSex.sex', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\3520\010\n\006hidden', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1072,
  serialized_end=1158,
)


_REQUESTEDITCUSTOMPROFILE = _descriptor.Descriptor(
  name='RequestEditCustomProfile',
  full_name='dialog.RequestEditCustomProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='custom_profile', full_name='dialog.RequestEditCustomProfile.custom_profile', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1160,
  serialized_end=1255,
)


_REQUESTCHANGEUSERSTATUS = _descriptor.Descriptor(
  name='RequestChangeUserStatus',
  full_name='dialog.RequestChangeUserStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='dialog.RequestChangeUserStatus.status', index=0,
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
  serialized_options=b'\342?\031\n\027im.dlg.grpc.GrpcRequest',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1257,
  serialized_end=1363,
)


_REQUESTUPDATEBOTCOMMANDS = _descriptor.Descriptor(
  name='RequestUpdateBotCommands',
  full_name='dialog.RequestUpdateBotCommands',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bot_commands', full_name='dialog.RequestUpdateBotCommands.bot_commands', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1365,
  serialized_end=1478,
)

_REQUESTEDITNICKNAME.fields_by_name['nickname'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_REQUESTEDITABOUT.fields_by_name['about'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_REQUESTEDITAVATAR.fields_by_name['file_location'].message_type = media__and__files__pb2._FILELOCATION
_RESPONSEEDITAVATAR.fields_by_name['avatar'].message_type = media__and__files__pb2._AVATAR
_REQUESTEDITSEX.fields_by_name['sex'].enum_type = users__pb2._SEX
_REQUESTCHANGEUSERSTATUS.fields_by_name['status'].message_type = users__pb2._USERSTATUS
_REQUESTUPDATEBOTCOMMANDS.fields_by_name['bot_commands'].message_type = users__pb2._BOTCOMMAND
DESCRIPTOR.message_types_by_name['RequestEditName'] = _REQUESTEDITNAME
DESCRIPTOR.message_types_by_name['RequestEditNickName'] = _REQUESTEDITNICKNAME
DESCRIPTOR.message_types_by_name['RequestCheckNickName'] = _REQUESTCHECKNICKNAME
DESCRIPTOR.message_types_by_name['RequestEditAbout'] = _REQUESTEDITABOUT
DESCRIPTOR.message_types_by_name['RequestEditAvatar'] = _REQUESTEDITAVATAR
DESCRIPTOR.message_types_by_name['ResponseEditAvatar'] = _RESPONSEEDITAVATAR
DESCRIPTOR.message_types_by_name['RequestRemoveAvatar'] = _REQUESTREMOVEAVATAR
DESCRIPTOR.message_types_by_name['RequestEditMyTimeZone'] = _REQUESTEDITMYTIMEZONE
DESCRIPTOR.message_types_by_name['RequestEditMyPreferredLanguages'] = _REQUESTEDITMYPREFERREDLANGUAGES
DESCRIPTOR.message_types_by_name['RequestEditSex'] = _REQUESTEDITSEX
DESCRIPTOR.message_types_by_name['RequestEditCustomProfile'] = _REQUESTEDITCUSTOMPROFILE
DESCRIPTOR.message_types_by_name['RequestChangeUserStatus'] = _REQUESTCHANGEUSERSTATUS
DESCRIPTOR.message_types_by_name['RequestUpdateBotCommands'] = _REQUESTUPDATEBOTCOMMANDS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestEditName = _reflection.GeneratedProtocolMessageType('RequestEditName', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITNAME,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditName)
  })
_sym_db.RegisterMessage(RequestEditName)

RequestEditNickName = _reflection.GeneratedProtocolMessageType('RequestEditNickName', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITNICKNAME,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditNickName)
  })
_sym_db.RegisterMessage(RequestEditNickName)

RequestCheckNickName = _reflection.GeneratedProtocolMessageType('RequestCheckNickName', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCHECKNICKNAME,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestCheckNickName)
  })
_sym_db.RegisterMessage(RequestCheckNickName)

RequestEditAbout = _reflection.GeneratedProtocolMessageType('RequestEditAbout', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITABOUT,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditAbout)
  })
_sym_db.RegisterMessage(RequestEditAbout)

RequestEditAvatar = _reflection.GeneratedProtocolMessageType('RequestEditAvatar', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITAVATAR,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditAvatar)
  })
_sym_db.RegisterMessage(RequestEditAvatar)

ResponseEditAvatar = _reflection.GeneratedProtocolMessageType('ResponseEditAvatar', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEEDITAVATAR,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseEditAvatar)
  })
_sym_db.RegisterMessage(ResponseEditAvatar)

RequestRemoveAvatar = _reflection.GeneratedProtocolMessageType('RequestRemoveAvatar', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTREMOVEAVATAR,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRemoveAvatar)
  })
_sym_db.RegisterMessage(RequestRemoveAvatar)

RequestEditMyTimeZone = _reflection.GeneratedProtocolMessageType('RequestEditMyTimeZone', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITMYTIMEZONE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditMyTimeZone)
  })
_sym_db.RegisterMessage(RequestEditMyTimeZone)

RequestEditMyPreferredLanguages = _reflection.GeneratedProtocolMessageType('RequestEditMyPreferredLanguages', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITMYPREFERREDLANGUAGES,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditMyPreferredLanguages)
  })
_sym_db.RegisterMessage(RequestEditMyPreferredLanguages)

RequestEditSex = _reflection.GeneratedProtocolMessageType('RequestEditSex', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITSEX,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditSex)
  })
_sym_db.RegisterMessage(RequestEditSex)

RequestEditCustomProfile = _reflection.GeneratedProtocolMessageType('RequestEditCustomProfile', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTEDITCUSTOMPROFILE,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestEditCustomProfile)
  })
_sym_db.RegisterMessage(RequestEditCustomProfile)

RequestChangeUserStatus = _reflection.GeneratedProtocolMessageType('RequestChangeUserStatus', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCHANGEUSERSTATUS,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestChangeUserStatus)
  })
_sym_db.RegisterMessage(RequestChangeUserStatus)

RequestUpdateBotCommands = _reflection.GeneratedProtocolMessageType('RequestUpdateBotCommands', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTUPDATEBOTCOMMANDS,
  '__module__' : 'profile_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestUpdateBotCommands)
  })
_sym_db.RegisterMessage(RequestUpdateBotCommands)


DESCRIPTOR._options = None
_REQUESTEDITNAME.fields_by_name['name']._options = None
_REQUESTEDITNAME._options = None
_REQUESTEDITNICKNAME.fields_by_name['nickname']._options = None
_REQUESTEDITNICKNAME._options = None
_REQUESTCHECKNICKNAME.fields_by_name['nickname']._options = None
_REQUESTCHECKNICKNAME._options = None
_REQUESTEDITABOUT.fields_by_name['about']._options = None
_REQUESTEDITABOUT._options = None
_REQUESTEDITAVATAR.fields_by_name['file_location']._options = None
_REQUESTEDITAVATAR._options = None
_RESPONSEEDITAVATAR._options = None
_REQUESTREMOVEAVATAR._options = None
_REQUESTEDITMYTIMEZONE.fields_by_name['tz']._options = None
_REQUESTEDITMYTIMEZONE._options = None
_REQUESTEDITMYPREFERREDLANGUAGES.fields_by_name['preferred_languages']._options = None
_REQUESTEDITMYPREFERREDLANGUAGES._options = None
_REQUESTEDITSEX.fields_by_name['sex']._options = None
_REQUESTEDITSEX._options = None
_REQUESTEDITCUSTOMPROFILE.fields_by_name['custom_profile']._options = None
_REQUESTEDITCUSTOMPROFILE._options = None
_REQUESTCHANGEUSERSTATUS.fields_by_name['status']._options = None
_REQUESTCHANGEUSERSTATUS._options = None
_REQUESTUPDATEBOTCOMMANDS.fields_by_name['bot_commands']._options = None
_REQUESTUPDATEBOTCOMMANDS._options = None

_PROFILE = _descriptor.ServiceDescriptor(
  name='Profile',
  full_name='dialog.Profile',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1481,
  serialized_end=2843,
  methods=[
  _descriptor.MethodDescriptor(
    name='EditName',
    full_name='dialog.Profile.EditName',
    index=0,
    containing_service=None,
    input_type=_REQUESTEDITNAME,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002\036\"\031/v1/grpc/Profile/EditName:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditNickName',
    full_name='dialog.Profile.EditNickName',
    index=1,
    containing_service=None,
    input_type=_REQUESTEDITNICKNAME,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002\"\"\035/v1/grpc/Profile/EditNickName:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckNickName',
    full_name='dialog.Profile.CheckNickName',
    index=2,
    containing_service=None,
    input_type=_REQUESTCHECKNICKNAME,
    output_type=miscellaneous__pb2._RESPONSEBOOL,
    serialized_options=b'\202\323\344\223\002#\"\036/v1/grpc/Profile/CheckNickName:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditAbout',
    full_name='dialog.Profile.EditAbout',
    index=3,
    containing_service=None,
    input_type=_REQUESTEDITABOUT,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002\037\"\032/v1/grpc/Profile/EditAbout:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditAvatar',
    full_name='dialog.Profile.EditAvatar',
    index=4,
    containing_service=None,
    input_type=_REQUESTEDITAVATAR,
    output_type=_RESPONSEEDITAVATAR,
    serialized_options=b'\202\323\344\223\002 \"\033/v1/grpc/Profile/EditAvatar:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveAvatar',
    full_name='dialog.Profile.RemoveAvatar',
    index=5,
    containing_service=None,
    input_type=_REQUESTREMOVEAVATAR,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002\"\"\035/v1/grpc/Profile/RemoveAvatar:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditMyTimeZone',
    full_name='dialog.Profile.EditMyTimeZone',
    index=6,
    containing_service=None,
    input_type=_REQUESTEDITMYTIMEZONE,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002$\"\037/v1/grpc/Profile/EditMyTimeZone:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditMyPreferredLanguages',
    full_name='dialog.Profile.EditMyPreferredLanguages',
    index=7,
    containing_service=None,
    input_type=_REQUESTEDITMYPREFERREDLANGUAGES,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002.\")/v1/grpc/Profile/EditMyPreferredLanguages:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditSex',
    full_name='dialog.Profile.EditSex',
    index=8,
    containing_service=None,
    input_type=_REQUESTEDITSEX,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002\035\"\030/v1/grpc/Profile/EditSex:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditCustomProfile',
    full_name='dialog.Profile.EditCustomProfile',
    index=9,
    containing_service=None,
    input_type=_REQUESTEDITCUSTOMPROFILE,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002\'\"\"/v1/grpc/Profile/EditCustomProfile:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ChangeUserStatus',
    full_name='dialog.Profile.ChangeUserStatus',
    index=10,
    containing_service=None,
    input_type=_REQUESTCHANGEUSERSTATUS,
    output_type=miscellaneous__pb2._RESPONSESEQ,
    serialized_options=b'\202\323\344\223\002&\"!/v1/grpc/Profile/ChangeUserStatus:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBotCommands',
    full_name='dialog.Profile.UpdateBotCommands',
    index=11,
    containing_service=None,
    input_type=_REQUESTUPDATEBOTCOMMANDS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\'\"\"/v1/grpc/Profile/UpdateBotCommands:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROFILE)

DESCRIPTOR.services_by_name['Profile'] = _PROFILE

# @@protoc_insertion_point(module_scope)
