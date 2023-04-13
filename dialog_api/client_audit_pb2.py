# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client_audit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from . import peers_pb2 as peers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='client_audit.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=b'\n\024im.dlg.grpc.servicesZ\006dialog',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x63lient_audit.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x15scalapb/scalapb.proto\x1a\x0bpeers.proto\"=\n\x0e\x46ilesavedEvent\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\x03\x12\x1a\n\x04peer\x18\x02 \x01(\x0b\x32\x0c.dialog.Peer\"\x8d\x08\n\x0fScreenshotEvent\x12?\n\x0b\x64ialog_list\x18\x01 \x01(\x0b\x32(.dialog.ScreenshotEvent.DialogListScreenH\x00\x12:\n\x08\x63ontacts\x18\x02 \x01(\x0b\x32&.dialog.ScreenshotEvent.ContactsScreenH\x00\x12\x41\n\x0c\x63\x61ll_history\x18\x03 \x01(\x0b\x32).dialog.ScreenshotEvent.CallHistoryScreenH\x00\x12\x42\n\x0c\x63onversation\x18\x04 \x01(\x0b\x32*.dialog.ScreenshotEvent.ConversationScreenH\x00\x12\x41\n\x0cuser_profile\x18\x05 \x01(\x0b\x32).dialog.ScreenshotEvent.UserProfileScreenH\x00\x12=\n\ngroup_info\x18\x06 \x01(\x0b\x32\'.dialog.ScreenshotEvent.GroupInfoScreenH\x00\x12<\n\tassistant\x18\x07 \x01(\x0b\x32\'.dialog.ScreenshotEvent.AssistantScreenH\x00\x12M\n\x12\x63onversation_files\x18\x08 \x01(\x0b\x32/.dialog.ScreenshotEvent.ConversationFilesScreenH\x00\x12\x41\n\x0c\x66ile_preview\x18\t \x01(\x0b\x32).dialog.ScreenshotEvent.FilePreviewScreenH\x00\x12>\n\nconference\x18\n \x01(\x0b\x32(.dialog.ScreenshotEvent.ConferenceScreenH\x00\x1a\x12\n\x10\x44ialogListScreen\x1a\x10\n\x0e\x43ontactsScreen\x1a\x13\n\x11\x43\x61llHistoryScreen\x1a\x30\n\x12\x43onversationScreen\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x1a$\n\x11UserProfileScreen\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x1a#\n\x0fGroupInfoScreen\x12\x10\n\x08group_id\x18\x01 \x01(\x05\x1a\x11\n\x0f\x41ssistantScreen\x1a\x35\n\x17\x43onversationFilesScreen\x12\x1a\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.Peer\x1a@\n\x11\x46ilePreviewScreen\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\x03\x12\x1a\n\x04peer\x18\x02 \x01(\x0b\x32\x0c.dialog.Peer\x1a\x12\n\x10\x43onferenceScreenB\x0c\n\napp_screen\"y\n\x12RecordEventRequest\x12-\n\nscreenshot\x18\x01 \x01(\x0b\x32\x17.dialog.ScreenshotEventH\x00\x12+\n\tfilesaved\x18\x02 \x01(\x0b\x32\x16.dialog.FilesavedEventH\x00\x42\x07\n\x05\x65vent\"\x15\n\x13RecordEventResponse2v\n\x05\x41udit\x12m\n\x0bRecordEvent\x12\x1a.dialog.RecordEventRequest\x1a\x1b.dialog.RecordEventResponse\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/grpc/Audit/RecordEvent:\x01*B\x1e\n\x14im.dlg.grpc.servicesZ\x06\x64ialogb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,peers__pb2.DESCRIPTOR,])




_FILESAVEDEVENT = _descriptor.Descriptor(
  name='FilesavedEvent',
  full_name='dialog.FilesavedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_id', full_name='dialog.FilesavedEvent.file_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.FilesavedEvent.peer', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=157,
  serialized_end=218,
)


_SCREENSHOTEVENT_DIALOGLISTSCREEN = _descriptor.Descriptor(
  name='DialogListScreen',
  full_name='dialog.ScreenshotEvent.DialogListScreen',
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
  serialized_start=902,
  serialized_end=920,
)

_SCREENSHOTEVENT_CONTACTSSCREEN = _descriptor.Descriptor(
  name='ContactsScreen',
  full_name='dialog.ScreenshotEvent.ContactsScreen',
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
  serialized_start=922,
  serialized_end=938,
)

_SCREENSHOTEVENT_CALLHISTORYSCREEN = _descriptor.Descriptor(
  name='CallHistoryScreen',
  full_name='dialog.ScreenshotEvent.CallHistoryScreen',
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
  serialized_start=940,
  serialized_end=959,
)

_SCREENSHOTEVENT_CONVERSATIONSCREEN = _descriptor.Descriptor(
  name='ConversationScreen',
  full_name='dialog.ScreenshotEvent.ConversationScreen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.ScreenshotEvent.ConversationScreen.peer', index=0,
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
  serialized_start=961,
  serialized_end=1009,
)

_SCREENSHOTEVENT_USERPROFILESCREEN = _descriptor.Descriptor(
  name='UserProfileScreen',
  full_name='dialog.ScreenshotEvent.UserProfileScreen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='dialog.ScreenshotEvent.UserProfileScreen.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1011,
  serialized_end=1047,
)

_SCREENSHOTEVENT_GROUPINFOSCREEN = _descriptor.Descriptor(
  name='GroupInfoScreen',
  full_name='dialog.ScreenshotEvent.GroupInfoScreen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='dialog.ScreenshotEvent.GroupInfoScreen.group_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=1049,
  serialized_end=1084,
)

_SCREENSHOTEVENT_ASSISTANTSCREEN = _descriptor.Descriptor(
  name='AssistantScreen',
  full_name='dialog.ScreenshotEvent.AssistantScreen',
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
  serialized_start=1086,
  serialized_end=1103,
)

_SCREENSHOTEVENT_CONVERSATIONFILESSCREEN = _descriptor.Descriptor(
  name='ConversationFilesScreen',
  full_name='dialog.ScreenshotEvent.ConversationFilesScreen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.ScreenshotEvent.ConversationFilesScreen.peer', index=0,
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
  serialized_start=1105,
  serialized_end=1158,
)

_SCREENSHOTEVENT_FILEPREVIEWSCREEN = _descriptor.Descriptor(
  name='FilePreviewScreen',
  full_name='dialog.ScreenshotEvent.FilePreviewScreen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_id', full_name='dialog.ScreenshotEvent.FilePreviewScreen.file_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.ScreenshotEvent.FilePreviewScreen.peer', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1160,
  serialized_end=1224,
)

_SCREENSHOTEVENT_CONFERENCESCREEN = _descriptor.Descriptor(
  name='ConferenceScreen',
  full_name='dialog.ScreenshotEvent.ConferenceScreen',
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
  serialized_start=1226,
  serialized_end=1244,
)

_SCREENSHOTEVENT = _descriptor.Descriptor(
  name='ScreenshotEvent',
  full_name='dialog.ScreenshotEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dialog_list', full_name='dialog.ScreenshotEvent.dialog_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contacts', full_name='dialog.ScreenshotEvent.contacts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='call_history', full_name='dialog.ScreenshotEvent.call_history', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversation', full_name='dialog.ScreenshotEvent.conversation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_profile', full_name='dialog.ScreenshotEvent.user_profile', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_info', full_name='dialog.ScreenshotEvent.group_info', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='assistant', full_name='dialog.ScreenshotEvent.assistant', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conversation_files', full_name='dialog.ScreenshotEvent.conversation_files', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_preview', full_name='dialog.ScreenshotEvent.file_preview', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='conference', full_name='dialog.ScreenshotEvent.conference', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SCREENSHOTEVENT_DIALOGLISTSCREEN, _SCREENSHOTEVENT_CONTACTSSCREEN, _SCREENSHOTEVENT_CALLHISTORYSCREEN, _SCREENSHOTEVENT_CONVERSATIONSCREEN, _SCREENSHOTEVENT_USERPROFILESCREEN, _SCREENSHOTEVENT_GROUPINFOSCREEN, _SCREENSHOTEVENT_ASSISTANTSCREEN, _SCREENSHOTEVENT_CONVERSATIONFILESSCREEN, _SCREENSHOTEVENT_FILEPREVIEWSCREEN, _SCREENSHOTEVENT_CONFERENCESCREEN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='app_screen', full_name='dialog.ScreenshotEvent.app_screen',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=221,
  serialized_end=1258,
)


_RECORDEVENTREQUEST = _descriptor.Descriptor(
  name='RecordEventRequest',
  full_name='dialog.RecordEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='screenshot', full_name='dialog.RecordEventRequest.screenshot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filesaved', full_name='dialog.RecordEventRequest.filesaved', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='event', full_name='dialog.RecordEventRequest.event',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1260,
  serialized_end=1381,
)


_RECORDEVENTRESPONSE = _descriptor.Descriptor(
  name='RecordEventResponse',
  full_name='dialog.RecordEventResponse',
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
  serialized_start=1383,
  serialized_end=1404,
)

_FILESAVEDEVENT.fields_by_name['peer'].message_type = peers__pb2._PEER
_SCREENSHOTEVENT_DIALOGLISTSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_CONTACTSSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_CALLHISTORYSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_CONVERSATIONSCREEN.fields_by_name['peer'].message_type = peers__pb2._PEER
_SCREENSHOTEVENT_CONVERSATIONSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_USERPROFILESCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_GROUPINFOSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_ASSISTANTSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_CONVERSATIONFILESSCREEN.fields_by_name['peer'].message_type = peers__pb2._PEER
_SCREENSHOTEVENT_CONVERSATIONFILESSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_FILEPREVIEWSCREEN.fields_by_name['peer'].message_type = peers__pb2._PEER
_SCREENSHOTEVENT_FILEPREVIEWSCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT_CONFERENCESCREEN.containing_type = _SCREENSHOTEVENT
_SCREENSHOTEVENT.fields_by_name['dialog_list'].message_type = _SCREENSHOTEVENT_DIALOGLISTSCREEN
_SCREENSHOTEVENT.fields_by_name['contacts'].message_type = _SCREENSHOTEVENT_CONTACTSSCREEN
_SCREENSHOTEVENT.fields_by_name['call_history'].message_type = _SCREENSHOTEVENT_CALLHISTORYSCREEN
_SCREENSHOTEVENT.fields_by_name['conversation'].message_type = _SCREENSHOTEVENT_CONVERSATIONSCREEN
_SCREENSHOTEVENT.fields_by_name['user_profile'].message_type = _SCREENSHOTEVENT_USERPROFILESCREEN
_SCREENSHOTEVENT.fields_by_name['group_info'].message_type = _SCREENSHOTEVENT_GROUPINFOSCREEN
_SCREENSHOTEVENT.fields_by_name['assistant'].message_type = _SCREENSHOTEVENT_ASSISTANTSCREEN
_SCREENSHOTEVENT.fields_by_name['conversation_files'].message_type = _SCREENSHOTEVENT_CONVERSATIONFILESSCREEN
_SCREENSHOTEVENT.fields_by_name['file_preview'].message_type = _SCREENSHOTEVENT_FILEPREVIEWSCREEN
_SCREENSHOTEVENT.fields_by_name['conference'].message_type = _SCREENSHOTEVENT_CONFERENCESCREEN
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['dialog_list'])
_SCREENSHOTEVENT.fields_by_name['dialog_list'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['contacts'])
_SCREENSHOTEVENT.fields_by_name['contacts'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['call_history'])
_SCREENSHOTEVENT.fields_by_name['call_history'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['conversation'])
_SCREENSHOTEVENT.fields_by_name['conversation'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['user_profile'])
_SCREENSHOTEVENT.fields_by_name['user_profile'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['group_info'])
_SCREENSHOTEVENT.fields_by_name['group_info'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['assistant'])
_SCREENSHOTEVENT.fields_by_name['assistant'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['conversation_files'])
_SCREENSHOTEVENT.fields_by_name['conversation_files'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['file_preview'])
_SCREENSHOTEVENT.fields_by_name['file_preview'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_SCREENSHOTEVENT.oneofs_by_name['app_screen'].fields.append(
  _SCREENSHOTEVENT.fields_by_name['conference'])
_SCREENSHOTEVENT.fields_by_name['conference'].containing_oneof = _SCREENSHOTEVENT.oneofs_by_name['app_screen']
_RECORDEVENTREQUEST.fields_by_name['screenshot'].message_type = _SCREENSHOTEVENT
_RECORDEVENTREQUEST.fields_by_name['filesaved'].message_type = _FILESAVEDEVENT
_RECORDEVENTREQUEST.oneofs_by_name['event'].fields.append(
  _RECORDEVENTREQUEST.fields_by_name['screenshot'])
_RECORDEVENTREQUEST.fields_by_name['screenshot'].containing_oneof = _RECORDEVENTREQUEST.oneofs_by_name['event']
_RECORDEVENTREQUEST.oneofs_by_name['event'].fields.append(
  _RECORDEVENTREQUEST.fields_by_name['filesaved'])
_RECORDEVENTREQUEST.fields_by_name['filesaved'].containing_oneof = _RECORDEVENTREQUEST.oneofs_by_name['event']
DESCRIPTOR.message_types_by_name['FilesavedEvent'] = _FILESAVEDEVENT
DESCRIPTOR.message_types_by_name['ScreenshotEvent'] = _SCREENSHOTEVENT
DESCRIPTOR.message_types_by_name['RecordEventRequest'] = _RECORDEVENTREQUEST
DESCRIPTOR.message_types_by_name['RecordEventResponse'] = _RECORDEVENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FilesavedEvent = _reflection.GeneratedProtocolMessageType('FilesavedEvent', (_message.Message,), {
  'DESCRIPTOR' : _FILESAVEDEVENT,
  '__module__' : 'client_audit_pb2'
  # @@protoc_insertion_point(class_scope:dialog.FilesavedEvent)
  })
_sym_db.RegisterMessage(FilesavedEvent)

ScreenshotEvent = _reflection.GeneratedProtocolMessageType('ScreenshotEvent', (_message.Message,), {

  'DialogListScreen' : _reflection.GeneratedProtocolMessageType('DialogListScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_DIALOGLISTSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.DialogListScreen)
    })
  ,

  'ContactsScreen' : _reflection.GeneratedProtocolMessageType('ContactsScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_CONTACTSSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.ContactsScreen)
    })
  ,

  'CallHistoryScreen' : _reflection.GeneratedProtocolMessageType('CallHistoryScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_CALLHISTORYSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.CallHistoryScreen)
    })
  ,

  'ConversationScreen' : _reflection.GeneratedProtocolMessageType('ConversationScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_CONVERSATIONSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.ConversationScreen)
    })
  ,

  'UserProfileScreen' : _reflection.GeneratedProtocolMessageType('UserProfileScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_USERPROFILESCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.UserProfileScreen)
    })
  ,

  'GroupInfoScreen' : _reflection.GeneratedProtocolMessageType('GroupInfoScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_GROUPINFOSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.GroupInfoScreen)
    })
  ,

  'AssistantScreen' : _reflection.GeneratedProtocolMessageType('AssistantScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_ASSISTANTSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.AssistantScreen)
    })
  ,

  'ConversationFilesScreen' : _reflection.GeneratedProtocolMessageType('ConversationFilesScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_CONVERSATIONFILESSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.ConversationFilesScreen)
    })
  ,

  'FilePreviewScreen' : _reflection.GeneratedProtocolMessageType('FilePreviewScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_FILEPREVIEWSCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.FilePreviewScreen)
    })
  ,

  'ConferenceScreen' : _reflection.GeneratedProtocolMessageType('ConferenceScreen', (_message.Message,), {
    'DESCRIPTOR' : _SCREENSHOTEVENT_CONFERENCESCREEN,
    '__module__' : 'client_audit_pb2'
    # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent.ConferenceScreen)
    })
  ,
  'DESCRIPTOR' : _SCREENSHOTEVENT,
  '__module__' : 'client_audit_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ScreenshotEvent)
  })
_sym_db.RegisterMessage(ScreenshotEvent)
_sym_db.RegisterMessage(ScreenshotEvent.DialogListScreen)
_sym_db.RegisterMessage(ScreenshotEvent.ContactsScreen)
_sym_db.RegisterMessage(ScreenshotEvent.CallHistoryScreen)
_sym_db.RegisterMessage(ScreenshotEvent.ConversationScreen)
_sym_db.RegisterMessage(ScreenshotEvent.UserProfileScreen)
_sym_db.RegisterMessage(ScreenshotEvent.GroupInfoScreen)
_sym_db.RegisterMessage(ScreenshotEvent.AssistantScreen)
_sym_db.RegisterMessage(ScreenshotEvent.ConversationFilesScreen)
_sym_db.RegisterMessage(ScreenshotEvent.FilePreviewScreen)
_sym_db.RegisterMessage(ScreenshotEvent.ConferenceScreen)

RecordEventRequest = _reflection.GeneratedProtocolMessageType('RecordEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECORDEVENTREQUEST,
  '__module__' : 'client_audit_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RecordEventRequest)
  })
_sym_db.RegisterMessage(RecordEventRequest)

RecordEventResponse = _reflection.GeneratedProtocolMessageType('RecordEventResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECORDEVENTRESPONSE,
  '__module__' : 'client_audit_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RecordEventResponse)
  })
_sym_db.RegisterMessage(RecordEventResponse)


DESCRIPTOR._options = None

_AUDIT = _descriptor.ServiceDescriptor(
  name='Audit',
  full_name='dialog.Audit',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1406,
  serialized_end=1524,
  methods=[
  _descriptor.MethodDescriptor(
    name='RecordEvent',
    full_name='dialog.Audit.RecordEvent',
    index=0,
    containing_service=None,
    input_type=_RECORDEVENTREQUEST,
    output_type=_RECORDEVENTRESPONSE,
    serialized_options=b'\202\323\344\223\002\037\"\032/v1/grpc/Audit/RecordEvent:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUDIT)

DESCRIPTOR.services_by_name['Audit'] = _AUDIT

# @@protoc_insertion_point(module_scope)
