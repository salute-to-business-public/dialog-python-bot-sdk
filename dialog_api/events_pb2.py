# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: events.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import peers_pb2 as peers__pb2
from . import definitions_pb2 as definitions__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='events.proto',
  package='dialog.events',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x65vents.proto\x12\rdialog.events\x1a\x1cgoogle/api/annotations.proto\x1a\x0bpeers.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x15scalapb/scalapb.proto\"\xb8\x06\n\x05\x45vent\x12\r\n\x05\x63lock\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12/\n\x07mention\x18\x03 \x01(\x0b\x32\x1c.dialog.events.Event.MentionH\x00\x12\x33\n\treactions\x18\x04 \x01(\x0b\x32\x1e.dialog.events.Event.ReactionsH\x00\x12+\n\x05reply\x18\x05 \x01(\x0b\x32\x1a.dialog.events.Event.ReplyH\x00\x12-\n\x06invite\x18\x06 \x01(\x0b\x32\x1b.dialog.events.Event.InviteH\x00\x12)\n\x04kick\x18\x07 \x01(\x0b\x32\x19.dialog.events.Event.KickH\x00\x1aS\n\x07Mention\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x12\x1e\n\x03mid\x18\x02 \x01(\x0b\x32\x11.dialog.UUIDValue\x12\x0c\n\x04user\x18\x03 \x01(\x05\x1a\x8f\x02\n\tReactions\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x12\x1e\n\x03mid\x18\x02 \x01(\x0b\x32\x11.dialog.UUIDValue\x12:\n\treactions\x18\x03 \x03(\x0b\x32\'.dialog.events.Event.Reactions.Reaction\x1a\x89\x01\n\x08Reaction\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x41\n\x05users\x18\x02 \x03(\x0b\x32\x32.dialog.events.Event.Reactions.Reaction.UsersEntry\x1a,\n\nUsersEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\x1aQ\n\x05Reply\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x12\x1e\n\x03mid\x18\x02 \x01(\x0b\x32\x11.dialog.UUIDValue\x12\x0c\n\x04user\x18\x03 \x01(\x05\x1a\x32\n\x06Invite\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x12\x0c\n\x04user\x18\x02 \x01(\x05\x1a\x30\n\x04Kick\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x12\x0c\n\x04user\x18\x02 \x01(\x05\x42\x07\n\x05\x65vent\"F\n\x0bUpdateEvent\x12#\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x14.dialog.events.Event\x12\x12\n\nprev_clock\x18\x02 \x01(\x03\"b\n\x11LoadEventsRequest\x12\x12\n\nfrom_clock\x18\x01 \x01(\x03\x12*\n\tload_mode\x18\x02 \x01(\x0e\x32\x17.dialog.events.LoadMode\x12\r\n\x05limit\x18\x03 \x01(\x05\"\x80\x01\n\x12LoadEventsResponse\x12$\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x14.dialog.events.Event\x12\r\n\x05\x63lock\x18\x02 \x01(\x03\x12\x16\n\x0enext_available\x18\x03 \x01(\x08:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse*M\n\x08LoadMode\x12\x14\n\x10LOADMODE_UNKNOWN\x10\x00\x12\x14\n\x10LOADMODE_FORWARD\x10\x01\x12\x15\n\x11LOADMODE_BACKWARD\x10\x02\x32\x82\x01\n\x06\x45vents\x12x\n\nLoadEvents\x12 .dialog.events.LoadEventsRequest\x1a!.dialog.events.LoadEventsResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/grpc/Events/LoadEvents:\x01*B\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,peers__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])

_LOADMODE = _descriptor.EnumDescriptor(
  name='LoadMode',
  full_name='dialog.events.LoadMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOADMODE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOADMODE_FORWARD', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOADMODE_BACKWARD', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1246,
  serialized_end=1323,
)
_sym_db.RegisterEnumDescriptor(_LOADMODE)

LoadMode = enum_type_wrapper.EnumTypeWrapper(_LOADMODE)
LOADMODE_UNKNOWN = 0
LOADMODE_FORWARD = 1
LOADMODE_BACKWARD = 2



_EVENT_MENTION = _descriptor.Descriptor(
  name='Mention',
  full_name='dialog.events.Event.Mention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.events.Event.Mention.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mid', full_name='dialog.events.Event.Mention.mid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='dialog.events.Event.Mention.user', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=390,
  serialized_end=473,
)

_EVENT_REACTIONS_REACTION_USERSENTRY = _descriptor.Descriptor(
  name='UsersEntry',
  full_name='dialog.events.Event.Reactions.Reaction.UsersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='dialog.events.Event.Reactions.Reaction.UsersEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='dialog.events.Event.Reactions.Reaction.UsersEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=703,
  serialized_end=747,
)

_EVENT_REACTIONS_REACTION = _descriptor.Descriptor(
  name='Reaction',
  full_name='dialog.events.Event.Reactions.Reaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='dialog.events.Event.Reactions.Reaction.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='users', full_name='dialog.events.Event.Reactions.Reaction.users', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_REACTIONS_REACTION_USERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=610,
  serialized_end=747,
)

_EVENT_REACTIONS = _descriptor.Descriptor(
  name='Reactions',
  full_name='dialog.events.Event.Reactions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.events.Event.Reactions.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mid', full_name='dialog.events.Event.Reactions.mid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reactions', full_name='dialog.events.Event.Reactions.reactions', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_REACTIONS_REACTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=747,
)

_EVENT_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='dialog.events.Event.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.events.Event.Reply.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mid', full_name='dialog.events.Event.Reply.mid', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='dialog.events.Event.Reply.user', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=749,
  serialized_end=830,
)

_EVENT_INVITE = _descriptor.Descriptor(
  name='Invite',
  full_name='dialog.events.Event.Invite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.events.Event.Invite.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='dialog.events.Event.Invite.user', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=832,
  serialized_end=882,
)

_EVENT_KICK = _descriptor.Descriptor(
  name='Kick',
  full_name='dialog.events.Event.Kick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.events.Event.Kick.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='dialog.events.Event.Kick.user', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=884,
  serialized_end=932,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='dialog.events.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='clock', full_name='dialog.events.Event.clock', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='dialog.events.Event.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mention', full_name='dialog.events.Event.mention', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reactions', full_name='dialog.events.Event.reactions', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply', full_name='dialog.events.Event.reply', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invite', full_name='dialog.events.Event.invite', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kick', full_name='dialog.events.Event.kick', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_MENTION, _EVENT_REACTIONS, _EVENT_REPLY, _EVENT_INVITE, _EVENT_KICK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event', full_name='dialog.events.Event.event',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=117,
  serialized_end=941,
)


_UPDATEEVENT = _descriptor.Descriptor(
  name='UpdateEvent',
  full_name='dialog.events.UpdateEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='dialog.events.UpdateEvent.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='prev_clock', full_name='dialog.events.UpdateEvent.prev_clock', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=943,
  serialized_end=1013,
)


_LOADEVENTSREQUEST = _descriptor.Descriptor(
  name='LoadEventsRequest',
  full_name='dialog.events.LoadEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_clock', full_name='dialog.events.LoadEventsRequest.from_clock', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_mode', full_name='dialog.events.LoadEventsRequest.load_mode', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='dialog.events.LoadEventsRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=1015,
  serialized_end=1113,
)


_LOADEVENTSRESPONSE = _descriptor.Descriptor(
  name='LoadEventsResponse',
  full_name='dialog.events.LoadEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='dialog.events.LoadEventsResponse.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clock', full_name='dialog.events.LoadEventsResponse.clock', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_available', full_name='dialog.events.LoadEventsResponse.next_available', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_options=b'\342?\032\n\030im.dlg.grpc.GrpcResponse',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1116,
  serialized_end=1244,
)

_EVENT_MENTION.fields_by_name['peer'].message_type = peers__pb2._PEER
_EVENT_MENTION.fields_by_name['mid'].message_type = definitions__pb2._UUIDVALUE
_EVENT_MENTION.containing_type = _EVENT
_EVENT_REACTIONS_REACTION_USERSENTRY.containing_type = _EVENT_REACTIONS_REACTION
_EVENT_REACTIONS_REACTION.fields_by_name['users'].message_type = _EVENT_REACTIONS_REACTION_USERSENTRY
_EVENT_REACTIONS_REACTION.containing_type = _EVENT_REACTIONS
_EVENT_REACTIONS.fields_by_name['peer'].message_type = peers__pb2._PEER
_EVENT_REACTIONS.fields_by_name['mid'].message_type = definitions__pb2._UUIDVALUE
_EVENT_REACTIONS.fields_by_name['reactions'].message_type = _EVENT_REACTIONS_REACTION
_EVENT_REACTIONS.containing_type = _EVENT
_EVENT_REPLY.fields_by_name['peer'].message_type = peers__pb2._PEER
_EVENT_REPLY.fields_by_name['mid'].message_type = definitions__pb2._UUIDVALUE
_EVENT_REPLY.containing_type = _EVENT
_EVENT_INVITE.fields_by_name['peer'].message_type = peers__pb2._PEER
_EVENT_INVITE.containing_type = _EVENT
_EVENT_KICK.fields_by_name['peer'].message_type = peers__pb2._PEER
_EVENT_KICK.containing_type = _EVENT
_EVENT.fields_by_name['mention'].message_type = _EVENT_MENTION
_EVENT.fields_by_name['reactions'].message_type = _EVENT_REACTIONS
_EVENT.fields_by_name['reply'].message_type = _EVENT_REPLY
_EVENT.fields_by_name['invite'].message_type = _EVENT_INVITE
_EVENT.fields_by_name['kick'].message_type = _EVENT_KICK
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['mention'])
_EVENT.fields_by_name['mention'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['reactions'])
_EVENT.fields_by_name['reactions'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['reply'])
_EVENT.fields_by_name['reply'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['invite'])
_EVENT.fields_by_name['invite'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['kick'])
_EVENT.fields_by_name['kick'].containing_oneof = _EVENT.oneofs_by_name['event']
_UPDATEEVENT.fields_by_name['event'].message_type = _EVENT
_LOADEVENTSREQUEST.fields_by_name['load_mode'].enum_type = _LOADMODE
_LOADEVENTSRESPONSE.fields_by_name['events'].message_type = _EVENT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['UpdateEvent'] = _UPDATEEVENT
DESCRIPTOR.message_types_by_name['LoadEventsRequest'] = _LOADEVENTSREQUEST
DESCRIPTOR.message_types_by_name['LoadEventsResponse'] = _LOADEVENTSRESPONSE
DESCRIPTOR.enum_types_by_name['LoadMode'] = _LOADMODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'Mention' : _reflection.GeneratedProtocolMessageType('Mention', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_MENTION,
    '__module__' : 'events_pb2'
    # @@protoc_insertion_point(class_scope:dialog.events.Event.Mention)
    })
  ,

  'Reactions' : _reflection.GeneratedProtocolMessageType('Reactions', (_message.Message,), {

    'Reaction' : _reflection.GeneratedProtocolMessageType('Reaction', (_message.Message,), {

      'UsersEntry' : _reflection.GeneratedProtocolMessageType('UsersEntry', (_message.Message,), {
        'DESCRIPTOR' : _EVENT_REACTIONS_REACTION_USERSENTRY,
        '__module__' : 'events_pb2'
        # @@protoc_insertion_point(class_scope:dialog.events.Event.Reactions.Reaction.UsersEntry)
        })
      ,
      'DESCRIPTOR' : _EVENT_REACTIONS_REACTION,
      '__module__' : 'events_pb2'
      # @@protoc_insertion_point(class_scope:dialog.events.Event.Reactions.Reaction)
      })
    ,
    'DESCRIPTOR' : _EVENT_REACTIONS,
    '__module__' : 'events_pb2'
    # @@protoc_insertion_point(class_scope:dialog.events.Event.Reactions)
    })
  ,

  'Reply' : _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_REPLY,
    '__module__' : 'events_pb2'
    # @@protoc_insertion_point(class_scope:dialog.events.Event.Reply)
    })
  ,

  'Invite' : _reflection.GeneratedProtocolMessageType('Invite', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_INVITE,
    '__module__' : 'events_pb2'
    # @@protoc_insertion_point(class_scope:dialog.events.Event.Invite)
    })
  ,

  'Kick' : _reflection.GeneratedProtocolMessageType('Kick', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_KICK,
    '__module__' : 'events_pb2'
    # @@protoc_insertion_point(class_scope:dialog.events.Event.Kick)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:dialog.events.Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.Mention)
_sym_db.RegisterMessage(Event.Reactions)
_sym_db.RegisterMessage(Event.Reactions.Reaction)
_sym_db.RegisterMessage(Event.Reactions.Reaction.UsersEntry)
_sym_db.RegisterMessage(Event.Reply)
_sym_db.RegisterMessage(Event.Invite)
_sym_db.RegisterMessage(Event.Kick)

UpdateEvent = _reflection.GeneratedProtocolMessageType('UpdateEvent', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEEVENT,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:dialog.events.UpdateEvent)
  })
_sym_db.RegisterMessage(UpdateEvent)

LoadEventsRequest = _reflection.GeneratedProtocolMessageType('LoadEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOADEVENTSREQUEST,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:dialog.events.LoadEventsRequest)
  })
_sym_db.RegisterMessage(LoadEventsRequest)

LoadEventsResponse = _reflection.GeneratedProtocolMessageType('LoadEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOADEVENTSRESPONSE,
  '__module__' : 'events_pb2'
  # @@protoc_insertion_point(class_scope:dialog.events.LoadEventsResponse)
  })
_sym_db.RegisterMessage(LoadEventsResponse)


DESCRIPTOR._options = None
_EVENT_REACTIONS_REACTION_USERSENTRY._options = None
_LOADEVENTSRESPONSE._options = None

_EVENTS = _descriptor.ServiceDescriptor(
  name='Events',
  full_name='dialog.events.Events',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1326,
  serialized_end=1456,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoadEvents',
    full_name='dialog.events.Events.LoadEvents',
    index=0,
    containing_service=None,
    input_type=_LOADEVENTSREQUEST,
    output_type=_LOADEVENTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\"\032/v1/grpc/Events/LoadEvents:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTS)

DESCRIPTOR.services_by_name['Events'] = _EVENTS

# @@protoc_insertion_point(module_scope)
