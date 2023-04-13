from typing import List
from dialog_api import sequence_and_updates_pb2

from dialog_bot_sdk.entities.draft_messages import UpdateDraftMessageChanged
from dialog_bot_sdk.entities.authentication import UpdateForceReloadState
from dialog_bot_sdk.entities.config_sync import UpdateParameterChanged, UpdateFeatureFlagChanged
from dialog_bot_sdk.entities.contacts import UpdateContactRegistered, UpdateContactsAdded, \
    UpdateContactsAddTaskSuspended, UpdateContactsRemoved
from dialog_bot_sdk.entities.counters import UpdateCountersChanged
from dialog_bot_sdk.entities.dialog_folder import UpdateDialogFolderChanged, UpdateDialogFolderDeleted, \
    UpdateDialogFoldersOrderChanged
from dialog_bot_sdk.entities.event_bus import UpdateEventBusDeviceConnected, UpdateEventBusDeviceDisconnected, \
    UpdateEventBusMessage, UpdateEventBusDisposed
from dialog_bot_sdk.entities.favourites_messages import UpdateFavouritesMessagesChanged
from dialog_bot_sdk.entities.groups import Group, UpdateGroupTitleChanged, UpdateGroupAvatarChanged, \
    UpdateGroupAboutChanged, UpdateGroupOwnerChanged, UpdateGroupMembersUpdated, UpdateGroupMemberDiff, \
    UpdateGroupMembersCountChanged, UpdateGroupMemberPermissionsChanged, UpdateGroupInviteObsolete, \
    UpdateGroupUserInvitedObsolete, UpdateGroupUserLeaveObsolete, UpdateGroupUserKickObsolete, \
    UpdateGroupMembersUpdateObsolete, UpdateGroupTitleChangedObsolete, UpdateGroupAboutChangedObsolete, \
    UpdateGroupShortnameChanged, UpdateGroup, UpdateGroupMemberInvited, UpdateGroupAvatarChangedObsolete, \
    UpdateGroupShortnameRemoved
from dialog_bot_sdk.entities.messaging import Message, UpdateInteractiveMediaEvent, UpdateMessage, \
    UpdateMessageContentChanged, UpdateMessageSent, UpdateMessageReceived, UpdateMessageRead, UpdateMessageReadByMe, \
    UpdateMessageDelete, UpdateChatClear, UpdateChatDelete, UpdateChatArchive, UpdateChatGroupsChanged, \
    UpdateReactionsUpdate, UpdateDialogFavouriteChanged, UpdateMessageRejectedByHook, UpdateMessageEditRejectedByHook, \
    UpdateDialogReadLaterChanged
from dialog_bot_sdk.entities.miscellaneous import UpdateConfig, Config
from dialog_bot_sdk.entities.peers import Peer, PeerType, UserOutPeer, GroupOutPeer
from dialog_bot_sdk.entities.permissions import UpdatePermissionsChange
from dialog_bot_sdk.entities.pinned_messages import UpdatePinnedMessagesChanged
from dialog_bot_sdk.entities.presence import UpdateTyping, UpdateTypingStop, UpdateUserOnline, UpdateUserOffline, \
    UpdateUserLastSeen, UpdateGroupOnline, UpdateGroupTyping, UpdateThreadTyping
from dialog_bot_sdk.entities.privacy import UpdateUserBlocked, UpdateUserUnblocked
from dialog_bot_sdk.entities.reactions import MessageReactionsUpdate
from dialog_bot_sdk.entities.spaces import UpdateSpaceModified, UpdateSpaceMemberModified
from dialog_bot_sdk.entities.stickers import UpdateStickerCollectionsChanged, UpdateStickerPackRemoved, \
    UpdateStickerPackAdded, UpdateUserStickerPackCollectionChanged
from dialog_bot_sdk.entities.threads import UpdateThreadCreated, UpdateSubscribedToThread, UpdateUnsubscribedFromThread
from dialog_bot_sdk.entities.users import User, UpdateUserAvatarChanged, UpdateUserNameChanged, \
    UpdateUserLocalNameChanged, UpdateUserContactsChanged, UpdateUserNickChanged, UpdateUserAboutChanged, \
    UpdateUserPreferredLanguagesChanged, UpdateUserTimeZoneChanged, UpdateUserBotCommandsChanged, UpdateUserSexChanged, \
    UpdateUserCustomProfileChanged, UpdateUserStatusChanged, UpdateUser, UpdateUserRestrictionsChanged, \
    UpdateUserExtChanged
from dialog_bot_sdk.entities.web_rtc import UpdateIncomingCallDeprecated, UpdateIncomingCall, UpdateCallHandled, \
    UpdateCallDisposed


class UpdateType:
    UPDATE_FORCE_RELOAD_STATE = "update_force_reload_state"
    UPDATE_USER_AVATAR_CHANGED = "update_user_avatar_changed"
    UPDATE_USER_NAME_CHANGED = "update_user_name_changed"
    UPDATE_USER_LOCAL_NAME_CHANGED = "update_user_local_name_changed"
    UPDATE_USER_CONTACTS_CHANGED = "update_user_contacts_changed"
    UPDATE_USER_NICK_CHANGED = "update_user_nick_changed"
    UPDATE_USER_ABOUT_CHANGED = "update_user_about_changed"
    UPDATE_USER_PREFERRED_LANGUAGES_CHANGED = "update_user_preferred_languages_changed"
    UPDATE_USER_TIME_ZONE_CHANGED = "update_user_time_zone_changed"
    UPDATE_USER_BOT_COMMANDS_CHANGED = "update_user_bot_commands_changed"
    UPDATE_USER_EXT_CHANGED = "update_user_ext_changed"
    UPDATE_USER_SEX_CHANGED = "update_user_sex_changed"
    UPDATE_USER_CUSTOM_PROFILE_CHANGED = "update_user_custom_profile_changed"
    UPDATE_USER_STATUS_CHANGED = "update_user_status_changed"
    UPDATE_CONTACT_REGISTERED = "update_contact_registered"
    UPDATE_CONTACTS_ADDED = "update_contacts_added"
    UPDATE_CONTACTS_ADD_TASK_SUSPENDED = "update_contacts_add_task_suspended"
    UPDATE_CONTACTS_REMOVED = "update_contacts_removed"
    UPDATE_USER_BLOCKED = "update_user_blocked"
    UPDATE_USER_UNBLOCKED = "update_user_unblocked"
    UPDATE_INTERACTIVE_MEDIA_EVENT = "update_interactive_media_event"
    UPDATE_MESSAGE = "update_message"
    UPDATE_MESSAGE_CONTENT_CHANGED = "update_message_content_changed"
    UPDATE_MESSAGE_SENT = "update_message_sent"
    UPDATE_MESSAGE_RECEIVED = "update_message_received"
    UPDATE_MESSAGE_READ = "update_message_read"
    UPDATE_MESSAGE_READ_BY_ME = "update_message_read_by_me"
    UPDATE_MESSAGE_DELETE = "update_message_delete"
    UPDATE_CHAT_CLEAR = "update_chat_clear"
    UPDATE_CHAT_DELETE = "update_chat_delete"
    UPDATE_CHAT_ARCHIVE = "update_chat_archive"
    UPDATE_CHAT_GROUPS_CHANGED = "update_chat_groups_changed"
    UPDATE_REACTIONS_UPDATE = "update_reactions_update"
    UPDATE_DIALOG_FAVOURITE_CHANGED = "update_dialog_favourite_changed"
    UPDATE_PINNED_MESSAGES_CHANGED = "update_pinned_messages_changed"
    UPDATE_GROUP_TITLE_CHANGED = "update_group_title_changed"
    UPDATE_GROUP_AVATAR_CHANGED = "update_group_avatar_changed"
    UPDATE_GROUP_ABOUT_CHANGED = "update_group_about_changed"
    UPDATE_GROUP_OWNER_CHANGED = "update_group_owner_changed"
    UPDATE_GROUP_MEMBERS_UPDATED = "update_group_members_updated"
    UPDATE_GROUP_MEMBER_DIFF = "update_group_member_diff"
    UPDATE_GROUP_MEMBERS_COUNT_CHANGED = "update_group_members_count_changed"
    UPDATE_GROUP_MEMBER_PERMISSIONS_CHANGED = "update_group_member_permissions_changed"
    UPDATE_GROUP_INVITE_OBSOLETE = "update_group_invite_obsolete"
    UPDATE_GROUP_USER_INVITED_OBSOLETE = "update_group_user_invited_obsolete"
    UPDATE_GROUP_USER_LEAVE_OBSOLETE = "update_group_user_leave_obsolete"
    UPDATE_GROUP_USER_KICK_OBSOLETE = "update_group_user_kick_obsolete"
    UPDATE_GROUP_MEMBERS_UPDATE_OBSOLETE = "update_group_members_update_obsolete"
    UPDATE_GROUP_TITLE_CHANGED_OBSOLETE = "update_group_title_changed_obsolete"
    UPDATE_GROUP_ABOUT_CHANGED_OBSOLETE = "update_group_about_changed_obsolete"
    UPDATE_GROUP_AVATAR_CHANGED_OBSOLETE = "update_group_avatar_changed_obsolete"
    UPDATE_GROUP_SHORTNAME_CHANGED = "update_group_shortname_changed"
    UPDATE_STICKER_COLLECTIONS_CHANGED = "update_sticker_collections_changed"
    UPDATE_STICKER_PACK_REMOVED = "update_sticker_pack_removed"
    UPDATE_STICKER_PACK_ADDED = "update_sticker_pack_added"
    UPDATE_USER_STICKER_PACK_COLLECTION_CHANGED = "update_user_sticker_pack_collection_changed"
    UPDATE_TYPING = "update_typing"
    UPDATE_TYPING_STOP = "update_typing_stop"
    UPDATE_USER_ONLINE = "update_user_online"
    UPDATE_USER_OFFLINE = "update_user_offline"
    UPDATE_USER_LAST_SEEN = "update_user_last_seen"
    UPDATE_GROUP_ONLINE = "update_group_online"
    UPDATE_EVENT_BUS_DEVICE_CONNECTED = "update_event_bus_device_connected"
    UPDATE_EVENT_BUS_DEVICE_DISCONNECTED = "update_event_bus_device_disconnected"
    UPDATE_EVENT_BUS_MESSAGE = "update_event_bus_message"
    UPDATE_EVENT_BUS_DISPOSED = "update_event_bus_disposed"
    UPDATE_INCOMING_CALL_DEPRECATED = "update_incoming_call_deprecated"
    UPDATE_INCOMING_CALL = "update_incoming_call"
    UPDATE_CALL_HANDLED = "update_call_handled"
    UPDATE_CALL_DISPOSED = "update_call_disposed"
    UPDATE_PARAMETER_CHANGED = "update_parameter_changed"
    UPDATE_RAW_UPDATE = "update_raw_update"
    UPDATE_EMPTY_UPDATE = "update_empty_update"
    UPDATE_COUNTERS_CHANGED = "update_counters_changed"
    UPDATE_CONFIG = "update_config"
    UPDATE_SPACE_MODIFIED = "update_space_modified"
    UPDATE_SPACE_MEMBER_MODIFIED = "update_space_member_modified"
    UPDATE_MESSAGE_REJECTED_BY_HOOK = "update_message_rejected_by_hook"
    UPDATE_MESSAGE_EDIT_REJECTED_BY_HOOK = "update_message_edit_rejected_by_hook"
    UPDATE_USER = "update_user"
    UPDATE_FEATURE_FLAG_CHANGED = "update_feature_flag_changed"
    UPDATE_GROUP = "update_group"
    UPDATE_GROUP_MEMBER_INVITED = "update_group_member_invited"
    MESSAGE_REACTIONS_UPDATE = "message_reactions_update"
    UPDATE_PERMISSIONS_CHANGE = "update_permissions_change"
    UPDATE_GROUP_TYPING = "update_group_typing"
    UPDATE_DIALOG_READ_LATER_CHANGED = "update_dialog_read_later_changed"
    UPDATE_DIALOG_FOLDER_CHANGED = "update_dialog_folder_changed"
    UPDATE_DIALOG_FOLDER_DELETED = "update_dialog_folder_deleted"
    UPDATE_DIALOG_FOLDER_ORDER_CHANGED = "update_dialog_folder_order_changed"
    UPDATE_FAVOURITES_MESSAGES_CHANGED = "update_favourites_messages_changed"
    UPDATE_USER_RESTRICTIONS_CHANGED = "update_user_restrictions_changed"
    CONFERENCE_ONLINE = "conference_online"
    CONFERENCE_INVITE = "conference_invite"
    UPDATE_THREAD_CREATED = "update_thread_created"
    UPDATE_SUBSCRIBED_TO_THREAD = "update_subscribed_to_thread"
    UPDATE_UNSUBSCRIBED_FROM_THREAD = "update_unsubscribed_from_thread"
    UPDATE_THREAD_TYPING = "update_thread_typing"
    UPDATE_DRAFT_MESSAGE_CHANGED = "update_draft_message_changed"
    UPDATE_GROUP_SHORTNAME_REMOVED = "update_group_shortname_removed"
    CONFERENCE_STATUSES = "conference_statuses"


update_type_mapper = {
    "updateForceReloadState": UpdateType.UPDATE_FORCE_RELOAD_STATE,
    "updateUserAvatarChanged": UpdateType.UPDATE_USER_AVATAR_CHANGED,
    "updateUserNameChanged": UpdateType.UPDATE_USER_NAME_CHANGED,
    "updateUserLocalNameChanged": UpdateType.UPDATE_USER_LOCAL_NAME_CHANGED,
    "updateUserContactsChanged": UpdateType.UPDATE_USER_CONTACTS_CHANGED,
    "updateUserNickChanged": UpdateType.UPDATE_USER_NICK_CHANGED,
    "updateUserAboutChanged": UpdateType.UPDATE_USER_ABOUT_CHANGED,
    "updateUserPreferredLanguagesChanged": UpdateType.UPDATE_USER_PREFERRED_LANGUAGES_CHANGED,
    "updateUserTimeZoneChanged": UpdateType.UPDATE_USER_TIME_ZONE_CHANGED,
    "updateUserBotCommandsChanged": UpdateType.UPDATE_USER_BOT_COMMANDS_CHANGED,
    "updateUserExtChanged": UpdateType.UPDATE_USER_EXT_CHANGED,
    "updateUserSexChanged": UpdateType.UPDATE_USER_SEX_CHANGED,
    "updateUserCustomProfileChanged": UpdateType.UPDATE_USER_CUSTOM_PROFILE_CHANGED,
    "updateUserStatusChanged": UpdateType.UPDATE_USER_STATUS_CHANGED,
    "updateContactRegistered": UpdateType.UPDATE_CONTACT_REGISTERED,
    "updateContactsAdded": UpdateType.UPDATE_CONTACTS_ADDED,
    "updateContactsAddTaskSuspended": UpdateType.UPDATE_CONTACTS_ADD_TASK_SUSPENDED,
    "updateContactsRemoved": UpdateType.UPDATE_CONTACTS_REMOVED,
    "updateUserBlocked": UpdateType.UPDATE_USER_BLOCKED,
    "updateUserUnblocked": UpdateType.UPDATE_USER_UNBLOCKED,
    "updateInteractiveMediaEvent": UpdateType.UPDATE_INTERACTIVE_MEDIA_EVENT,
    "updateMessage": UpdateType.UPDATE_MESSAGE,
    "updateMessageContentChanged": UpdateType.UPDATE_MESSAGE_CONTENT_CHANGED,
    "updateMessageSent": UpdateType.UPDATE_MESSAGE_SENT,
    "updateMessageReceived": UpdateType.UPDATE_MESSAGE_RECEIVED,
    "updateMessageRead": UpdateType.UPDATE_MESSAGE_READ,
    "updateMessageReadByMe": UpdateType.UPDATE_MESSAGE_READ_BY_ME,
    "updateMessageDelete": UpdateType.UPDATE_MESSAGE_DELETE,
    "updateChatClear": UpdateType.UPDATE_CHAT_CLEAR,
    "updateChatDelete": UpdateType.UPDATE_CHAT_DELETE,
    "updateChatArchive": UpdateType.UPDATE_CHAT_ARCHIVE,
    "updateChatGroupsChanged": UpdateType.UPDATE_CHAT_GROUPS_CHANGED,
    "updateReactionsUpdate": UpdateType.UPDATE_REACTIONS_UPDATE,
    "updateDialogFavouriteChanged": UpdateType.UPDATE_DIALOG_FAVOURITE_CHANGED,
    "updatePinnedMessagesChanged": UpdateType.UPDATE_PINNED_MESSAGES_CHANGED,
    "updateGroupTitleChanged": UpdateType.UPDATE_GROUP_TITLE_CHANGED,
    "updateGroupAvatarChanged": UpdateType.UPDATE_GROUP_AVATAR_CHANGED,
    "updateGroupAboutChanged": UpdateType.UPDATE_GROUP_ABOUT_CHANGED,
    "updateGroupOwnerChanged": UpdateType.UPDATE_GROUP_OWNER_CHANGED,
    "updateGroupMembersUpdated": UpdateType.UPDATE_GROUP_MEMBERS_UPDATED,
    "updateGroupMemberDiff": UpdateType.UPDATE_GROUP_MEMBER_DIFF,
    "updateGroupMembersCountChanged": UpdateType.UPDATE_GROUP_MEMBERS_COUNT_CHANGED,
    "updateGroupMemberPermissionsChanged": UpdateType.UPDATE_GROUP_MEMBER_PERMISSIONS_CHANGED,
    "updateGroupInviteObsolete": UpdateType.UPDATE_GROUP_INVITE_OBSOLETE,
    "updateGroupUserInvitedObsolete": UpdateType.UPDATE_GROUP_USER_INVITED_OBSOLETE,
    "updateGroupUserLeaveObsolete": UpdateType.UPDATE_GROUP_USER_LEAVE_OBSOLETE,
    "updateGroupUserKickObsolete": UpdateType.UPDATE_GROUP_USER_KICK_OBSOLETE,
    "updateGroupMembersUpdateObsolete": UpdateType.UPDATE_GROUP_MEMBERS_UPDATE_OBSOLETE,
    "updateGroupTitleChangedObsolete": UpdateType.UPDATE_GROUP_TITLE_CHANGED_OBSOLETE,
    "updateGroupAboutChangedObsolete": UpdateType.UPDATE_GROUP_ABOUT_CHANGED_OBSOLETE,
    "updateGroupAvatarChangedObsolete": UpdateType.UPDATE_GROUP_AVATAR_CHANGED_OBSOLETE,
    "updateGroupShortnameChanged": UpdateType.UPDATE_GROUP_SHORTNAME_CHANGED,
    "updateStickerCollectionsChanged": UpdateType.UPDATE_STICKER_COLLECTIONS_CHANGED,
    "updateStickerPackRemoved": UpdateType.UPDATE_STICKER_PACK_REMOVED,
    "updateStickerPackAdded": UpdateType.UPDATE_STICKER_PACK_ADDED,
    "updateUserStickerPackCollectionChanged": UpdateType.UPDATE_USER_STICKER_PACK_COLLECTION_CHANGED,
    "updateTyping": UpdateType.UPDATE_TYPING,
    "updateTypingStop": UpdateType.UPDATE_TYPING_STOP,
    "updateUserOnline": UpdateType.UPDATE_USER_ONLINE,
    "updateUserOffline": UpdateType.UPDATE_USER_OFFLINE,
    "updateUserLastSeen": UpdateType.UPDATE_USER_LAST_SEEN,
    "updateGroupOnline": UpdateType.UPDATE_GROUP_ONLINE,
    "updateEventBusDeviceConnected": UpdateType.UPDATE_EVENT_BUS_DEVICE_CONNECTED,
    "updateEventBusDeviceDisconnected": UpdateType.UPDATE_EVENT_BUS_DEVICE_DISCONNECTED,
    "updateEventBusMessage": UpdateType.UPDATE_EVENT_BUS_MESSAGE,
    "updateEventBusDisposed": UpdateType.UPDATE_EVENT_BUS_DISPOSED,
    "updateIncomingCallDeprecated": UpdateType.UPDATE_INCOMING_CALL_DEPRECATED,
    "updateIncomingCall": UpdateType.UPDATE_INCOMING_CALL,
    "updateCallHandled": UpdateType.UPDATE_CALL_HANDLED,
    "updateCallDisposed": UpdateType.UPDATE_CALL_DISPOSED,
    "updateParameterChanged": UpdateType.UPDATE_PARAMETER_CHANGED,
    "updateRawUpdate": UpdateType.UPDATE_RAW_UPDATE,
    "updateEmptyUpdate": UpdateType.UPDATE_EMPTY_UPDATE,
    "updateCountersChanged": UpdateType.UPDATE_COUNTERS_CHANGED,
    "updateConfig": UpdateType.UPDATE_CONFIG,
    "updateSpaceModified": UpdateType.UPDATE_SPACE_MODIFIED,
    "updateSpaceMemberModified": UpdateType.UPDATE_SPACE_MEMBER_MODIFIED,
    "updateMessageRejectedByHook": UpdateType.UPDATE_MESSAGE_REJECTED_BY_HOOK,
    "updateMessageEditRejectedByHook": UpdateType.UPDATE_MESSAGE_EDIT_REJECTED_BY_HOOK,
    "updateUser": UpdateType.UPDATE_USER,
    "updateFeatureFlagChanged": UpdateType.UPDATE_FEATURE_FLAG_CHANGED,
    "updateGroup": UpdateType.UPDATE_GROUP,
    "updateGroupMemberInvited": UpdateType.UPDATE_GROUP_MEMBER_INVITED,
    "messageReactionsUpdate": UpdateType.MESSAGE_REACTIONS_UPDATE,
    "updatePermissionsChange": UpdateType.UPDATE_PERMISSIONS_CHANGE,
    "updateGroupTyping": UpdateType.UPDATE_GROUP_TYPING,
    "updateDialogReadLaterChanged": UpdateType.UPDATE_DIALOG_READ_LATER_CHANGED,
    "updateDialogFolderChanged": UpdateType.UPDATE_DIALOG_FOLDER_CHANGED,
    "updateDialogFolderDeleted": UpdateType.UPDATE_DIALOG_FOLDER_DELETED,
    "updateDialogFolderOrderChanged": UpdateType.UPDATE_DIALOG_FOLDER_ORDER_CHANGED,
    "updateFavouritesMessagesChanged": UpdateType.UPDATE_FAVOURITES_MESSAGES_CHANGED,
    "updateUserRestrictionsChanged": UpdateType.UPDATE_USER_RESTRICTIONS_CHANGED,
    "conference_online": UpdateType.CONFERENCE_ONLINE,
    "conference_invite": UpdateType.CONFERENCE_INVITE,
    "updateThreadCreated": UpdateType.UPDATE_THREAD_CREATED,
    "updateSubscribedToThread": UpdateType.UPDATE_SUBSCRIBED_TO_THREAD,
    "updateUnsubscribedFromThread": UpdateType.UPDATE_UNSUBSCRIBED_FROM_THREAD,
    "updateThreadTyping": UpdateType.UPDATE_THREAD_TYPING,
    "updateDraftMessageChanged": UpdateType.UPDATE_DRAFT_MESSAGE_CHANGED,
    "updateGroupShortnameRemoved": UpdateType.UPDATE_GROUP_SHORTNAME_REMOVED,
    "conference_statuses": UpdateType.CONFERENCE_STATUSES
}


class ParticipantStatus:
    INITIAL = sequence_and_updates_pb2.INITIAL
    ANSWERED = sequence_and_updates_pb2.ANSWERED
    JOINED = sequence_and_updates_pb2.JOINED
    HANGED = sequence_and_updates_pb2.HANGED


class UpdateHandler:
    def __init__(self, function: callable, update_type: UpdateType, ignored_sleep: bool = False) -> None:
        self.function = function
        self.update_type = update_type
        self.ignored_sleep = ignored_sleep


class ReferencedEntities:
    def __init__(self, users: List[User], groups: List[Group], messages: List[Message]) -> None:
        self.users = users
        self.groups = groups
        self.messages = messages

    @classmethod
    def from_api(cls, entities: sequence_and_updates_pb2.ResponseGetReferencedEntitites) -> 'ReferencedEntities':
        return cls(
            [User.from_api(x) for x in entities.users],
            [Group.from_api(x) for x in entities.groups],
            [Message.from_api(x) for x in entities.messages]
        )

    def __dict__(self):
        return {
            "users": [x.__dict__() for x in self.users],
            "groups": [x.__dict__() for x in self.groups],
            "messages": [x.__dict__() for x in self.messages],
        }

    def __str__(self):
        return "ReferencedEntities({})".format(self.__dict__())


class VKS_info:
    def __init__(self, room_link: str, room_id: str, room_password: str, binded_group_id: int) -> None:
        self.room_link = room_link
        self.room_id = room_id
        self.room_password = room_password
        self.binded_group_id = binded_group_id

    @classmethod
    def from_api(cls, vks: sequence_and_updates_pb2.UpdateConferenceInvite.VKS_info) -> 'VKS_info':
        return cls(vks.room_link, vks.room_id, vks.room_password, vks.binded_group_id.value)

    def __dict__(self):
        return {
            "room_link": self.room_link,
            "room_id": self.room_id,
            "binded_group_id": self.binded_group_id,
        }

    def __str__(self):
        return "VKS_info({})".format(self.__dict__())


# updates
class UpdateRawUpdate:
    def __init__(self, type: str, bytes_: bytes) -> None:
        self.type = type
        self.bytes = bytes_

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.UpdateRawUpdate) -> 'UpdateRawUpdate':
        return cls(update.type.value, update.bytes)

    def __dict__(self):
        return {
            "type": self.type,
            "bytes": self.bytes,
        }

    def __str__(self):
        return "UpdateRawUpdate({})".format(self.__dict__())


class UpdateEmptyUpdate:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.UpdateEmptyUpdate) -> 'UpdateEmptyUpdate':
        return cls()

    def __dict__(self):
        return {}

    def __str__(self):
        return "UpdateRawUpdate({})".format(self.__dict__())


class UpdateConferenceOnline:
    def __init__(self, peer: Peer, count: int, user_peers: List[Peer]) -> None:
        self.peer = peer
        self.count = count
        self.user_peers = user_peers

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.UpdateConferenceOnline) -> 'UpdateConferenceOnline':
        return cls(Peer.from_api(update.peer), update.count, [Peer(x, PeerType.PEERTYPE_PRIVATE) for x in update.users_id])

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "count": self.count,
            "user_peers": [x.__dict__() for x in self.user_peers],
        }

    def __str__(self):
        return "UpdateConferenceOnline({})".format(self.__dict__())


class UpdateConferenceInvite:
    def __init__(self, initiator_id: int, vks_info: VKS_info) -> None:
        self.initiator_id = initiator_id
        self.vks_info = vks_info

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.UpdateConferenceInvite) -> 'UpdateConferenceInvite':
        return cls(update.initiator_id, VKS_info.from_api(update.vks_info))

    def __dict__(self):
        return {
            "initiator_id": self.initiator_id,
            "vks_info": self.vks_info.__dict__(),
        }

    def __str__(self):
        return "UpdateConferenceInvite({})".format(self.__dict__())


class Participant:
    def __init__(self, peer: Peer, status: ParticipantStatus) -> None:
        self.peer = peer
        self.status = status

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.Participant) -> 'Participant':
        return cls(Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.status)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "status": self.status,
        }

    def __str__(self):
        return "Participant({})".format(self.__dict__())


class UpdateConferenceStatuses:
    def __init__(self, room_id: str, participants: List[Participant]) -> None:
        self.room_id = room_id
        self.participants = participants

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.UpdateConferenceStatuses) -> 'UpdateConferenceStatuses':
        return cls(update.room_id, [Participant.from_api(x) for x in update.participants])

    def __dict__(self):
        return {
            "room_id": self.room_id,
            "participants": [x.__dict__() for x in self.participants],
        }

    def __str__(self):
        return "UpdateConferenceStatuses({})".format(self.__dict__())


update_entity_mapper = {
    "updateForceReloadState": UpdateForceReloadState,
    "updateUserAvatarChanged": UpdateUserAvatarChanged,
    "updateUserNameChanged": UpdateUserNameChanged,
    "updateUserLocalNameChanged": UpdateUserLocalNameChanged,
    "updateUserContactsChanged": UpdateUserContactsChanged,
    "updateUserNickChanged": UpdateUserNickChanged,
    "updateUserAboutChanged": UpdateUserAboutChanged,
    "updateUserPreferredLanguagesChanged": UpdateUserPreferredLanguagesChanged,
    "updateUserTimeZoneChanged": UpdateUserTimeZoneChanged,
    "updateUserBotCommandsChanged": UpdateUserBotCommandsChanged,
    "updateUserExtChanged": UpdateUserExtChanged,
    "updateUserSexChanged": UpdateUserSexChanged,
    "updateUserCustomProfileChanged": UpdateUserCustomProfileChanged,
    "updateUserStatusChanged": UpdateUserStatusChanged,
    "updateContactRegistered": UpdateContactRegistered,
    "updateContactsAdded": UpdateContactsAdded,
    "updateContactsAddTaskSuspended": UpdateContactsAddTaskSuspended,
    "updateContactsRemoved": UpdateContactsRemoved,
    "updateUserBlocked": UpdateUserBlocked,
    "updateUserUnblocked": UpdateUserUnblocked,
    "updateInteractiveMediaEvent": UpdateInteractiveMediaEvent,
    "updateMessage": UpdateMessage,
    "updateMessageContentChanged": UpdateMessageContentChanged,
    "updateMessageSent": UpdateMessageSent,
    "updateMessageReceived": UpdateMessageReceived,
    "updateMessageRead": UpdateMessageRead,
    "updateMessageReadByMe": UpdateMessageReadByMe,
    "updateMessageDelete": UpdateMessageDelete,
    "updateChatClear": UpdateChatClear,
    "updateChatDelete": UpdateChatDelete,
    "updateChatArchive": UpdateChatArchive,
    "updateChatGroupsChanged": UpdateChatGroupsChanged,
    "updateReactionsUpdate": UpdateReactionsUpdate,
    "updateDialogFavouriteChanged": UpdateDialogFavouriteChanged,
    "updatePinnedMessagesChanged": UpdatePinnedMessagesChanged,
    "updateGroupTitleChanged": UpdateGroupTitleChanged,
    "updateGroupAvatarChanged": UpdateGroupAvatarChanged,
    "updateGroupAboutChanged": UpdateGroupAboutChanged,
    "updateGroupOwnerChanged": UpdateGroupOwnerChanged,
    "updateGroupMembersUpdated": UpdateGroupMembersUpdated,
    "updateGroupMemberDiff": UpdateGroupMemberDiff,
    "updateGroupMembersCountChanged": UpdateGroupMembersCountChanged,
    "updateGroupMemberPermissionsChanged": UpdateGroupMemberPermissionsChanged,
    "updateGroupInviteObsolete": UpdateGroupInviteObsolete,
    "updateGroupUserInvitedObsolete": UpdateGroupUserInvitedObsolete,
    "updateGroupUserLeaveObsolete": UpdateGroupUserLeaveObsolete,
    "updateGroupUserKickObsolete": UpdateGroupUserKickObsolete,
    "updateGroupMembersUpdateObsolete": UpdateGroupMembersUpdateObsolete,
    "updateGroupTitleChangedObsolete": UpdateGroupTitleChangedObsolete,
    "updateGroupAboutChangedObsolete": UpdateGroupAboutChangedObsolete,
    "updateGroupAvatarChangedObsolete": UpdateGroupAvatarChangedObsolete,
    "updateGroupShortnameChanged": UpdateGroupShortnameChanged,
    "updateStickerCollectionsChanged": UpdateStickerCollectionsChanged,
    "updateStickerPackRemoved": UpdateStickerPackRemoved,
    "updateStickerPackAdded": UpdateStickerPackAdded,
    "updateUserStickerPackCollectionChanged": UpdateUserStickerPackCollectionChanged,
    "updateTyping": UpdateTyping,
    "updateTypingStop": UpdateTypingStop,
    "updateUserOnline": UpdateUserOnline,
    "updateUserOffline": UpdateUserOffline,
    "updateUserLastSeen": UpdateUserLastSeen,
    "updateGroupOnline": UpdateGroupOnline,
    "updateEventBusDeviceConnected": UpdateEventBusDeviceConnected,
    "updateEventBusDeviceDisconnected": UpdateEventBusDeviceDisconnected,
    "updateEventBusMessage": UpdateEventBusMessage,
    "updateEventBusDisposed": UpdateEventBusDisposed,
    "updateIncomingCallDeprecated": UpdateIncomingCallDeprecated,
    "updateIncomingCall": UpdateIncomingCall,
    "updateCallHandled": UpdateCallHandled,
    "updateCallDisposed": UpdateCallDisposed,
    "updateParameterChanged": UpdateParameterChanged,
    "updateRawUpdate": UpdateRawUpdate,
    "updateEmptyUpdate": UpdateEmptyUpdate,
    "updateCountersChanged": UpdateCountersChanged,
    "updateConfig": UpdateConfig,
    "updateSpaceModified": UpdateSpaceModified,
    "updateSpaceMemberModified": UpdateSpaceMemberModified,
    "updateMessageRejectedByHook": UpdateMessageRejectedByHook,
    "updateMessageEditRejectedByHook": UpdateMessageEditRejectedByHook,
    "updateUser": UpdateUser,
    "updateFeatureFlagChanged": UpdateFeatureFlagChanged,
    "updateGroup": UpdateGroup,
    "updateGroupMemberInvited": UpdateGroupMemberInvited,
    "messageReactionsUpdate": MessageReactionsUpdate,
    "updatePermissionsChange": UpdatePermissionsChange,
    "updateGroupTyping": UpdateGroupTyping,
    "updateDialogReadLaterChanged": UpdateDialogReadLaterChanged,
    "updateDialogFolderChanged": UpdateDialogFolderChanged,
    "updateDialogFolderDeleted": UpdateDialogFolderDeleted,
    "updateDialogFolderOrderChanged": UpdateDialogFoldersOrderChanged,
    "updateFavouritesMessagesChanged": UpdateFavouritesMessagesChanged,
    "updateUserRestrictionsChanged": UpdateUserRestrictionsChanged,
    "conference_online": UpdateConferenceOnline,
    "conference_invite": UpdateConferenceInvite,
    "updateThreadCreated": UpdateThreadCreated,
    "updateSubscribedToThread": UpdateSubscribedToThread,
    "updatedUnsubscribedFromThread": UpdateUnsubscribedFromThread,
    "updateThreadTyping": UpdateThreadTyping,
    "draftMessageChanged": UpdateDraftMessageChanged,
    "groupShortnameRemoved": UpdateGroupShortnameRemoved,
    "conference_statuses": UpdateConferenceStatuses
}


class UpdateSeqUpdate:
    def __init__(
            self,
            update_type: UpdateType,
            seq: int,
            state: bytes,
            update_header: int,
            update_force_reload_state: UpdateForceReloadState,
            update_user_avatar_changed: UpdateUserAvatarChanged,
            update_user_name_changed: UpdateUserNameChanged,
            update_user_local_name_changed: UpdateUserLocalNameChanged,
            update_user_contacts_changed: UpdateUserContactsChanged,
            update_user_nick_changed: UpdateUserNickChanged,
            update_user_about_changed: UpdateUserAboutChanged,
            update_user_preferred_languages_changed: UpdateUserPreferredLanguagesChanged,
            update_user_time_zone_changed: UpdateUserTimeZoneChanged,
            update_user_bot_commands_changed: UpdateUserBotCommandsChanged,
            update_user_ext_changed: UpdateUserExtChanged,
            update_user_sex_changed: UpdateUserSexChanged,
            update_user_custom_profile_changed: UpdateUserCustomProfileChanged,
            update_user_status_changed: UpdateUserStatusChanged,
            update_contact_registered: UpdateContactRegistered,
            update_contacts_added: UpdateContactsAdded,
            update_contacts_add_task_suspended: UpdateContactsAddTaskSuspended,
            update_contacts_removed: UpdateContactsRemoved,
            update_user_blocked: UpdateUserBlocked,
            update_user_unblocked: UpdateUserUnblocked,
            update_interactive_media_event: UpdateInteractiveMediaEvent,
            update_message: UpdateMessage,
            update_message_content_changed: UpdateMessageContentChanged,
            update_message_sent: UpdateMessageSent,
            update_message_received: UpdateMessageReceived,
            update_message_read: UpdateMessageRead,
            update_message_read_by_me: UpdateMessageReadByMe,
            update_message_delete: UpdateMessageDelete,
            update_chat_clear: UpdateChatClear,
            update_chat_delete: UpdateChatDelete,
            update_chat_archive: UpdateChatArchive,
            update_chat_groups_changed: UpdateChatGroupsChanged,
            update_reactions_update: UpdateReactionsUpdate,
            update_dialog_favourite_changed: UpdateDialogFavouriteChanged,
            update_pinned_messages_changed: UpdatePinnedMessagesChanged,
            update_group_title_changed: UpdateGroupTitleChanged,
            update_group_avatar_changed: UpdateGroupAvatarChanged,
            update_group_about_changed: UpdateGroupAboutChanged,
            update_group_owner_changed: UpdateGroupOwnerChanged,
            update_group_members_updated: UpdateGroupMembersUpdated,
            update_group_member_diff: UpdateGroupMemberDiff,
            update_group_members_count_changed: UpdateGroupMembersCountChanged,
            update_group_member_permissions_changed: UpdateGroupMemberPermissionsChanged,
            update_group_invite_obsolete: UpdateGroupInviteObsolete,
            update_group_user_invited_obsolete: UpdateGroupUserInvitedObsolete,
            update_group_user_leave_obsolete: UpdateGroupUserLeaveObsolete,
            update_group_user_kick_obsolete: UpdateGroupUserKickObsolete,
            update_group_members_update_obsolete: UpdateGroupMembersUpdateObsolete,
            update_group_title_changed_obsolete: UpdateGroupTitleChangedObsolete,
            update_group_about_changed_obsolete: UpdateGroupAboutChangedObsolete,
            update_group_avatar_changed_obsolete: UpdateGroupAvatarChangedObsolete,
            update_group_shortname_changed: UpdateGroupShortnameChanged,
            update_sticker_collections_changed: UpdateStickerCollectionsChanged,
            update_sticker_pack_removed: UpdateStickerPackRemoved,
            update_sticker_pack_added: UpdateStickerPackAdded,
            update_user_sticker_pack_collection_changed: UpdateUserStickerPackCollectionChanged,
            update_typing: UpdateTyping,
            update_typing_stop: UpdateTypingStop,
            update_user_online: UpdateUserOnline,
            update_user_offline: UpdateUserOffline,
            update_user_last_seen: UpdateUserLastSeen,
            update_group_online: UpdateGroupOnline,
            update_event_bus_device_connected: UpdateEventBusDeviceConnected,
            update_event_bus_device_disconnected: UpdateEventBusDeviceDisconnected,
            update_event_bus_message: UpdateEventBusMessage,
            update_event_bus_disposed: UpdateEventBusDisposed,
            update_incoming_call_deprecated: UpdateIncomingCallDeprecated,
            update_incoming_call: UpdateIncomingCall,
            update_call_handled: UpdateCallHandled,
            update_call_disposed: UpdateCallDisposed,
            update_parameter_changed: UpdateParameterChanged,
            update_raw_update: UpdateRawUpdate,
            update_empty_update: UpdateEmptyUpdate,
            update_counters_changed: UpdateCountersChanged,
            update_config: UpdateConfig,
            update_space_modified: UpdateSpaceModified,
            update_space_member_modified: UpdateSpaceMemberModified,
            update_message_rejected_by_hook: UpdateMessageRejectedByHook,
            update_message_edit_rejected_by_hook: UpdateMessageEditRejectedByHook,
            update_user: UpdateUser,
            update_feature_flag_changed: UpdateFeatureFlagChanged,
            update_group: UpdateGroup,
            update_group_member_invited: UpdateGroupMemberInvited,
            message_reactions_update: MessageReactionsUpdate,
            update_permissions_change: UpdatePermissionsChange,
            update_group_typing: UpdateGroupTyping,
            update_dialog_read_later_changed: UpdateDialogReadLaterChanged,
            update_dialog_folder_changed: UpdateDialogFolderChanged,
            update_dialog_folder_deleted: UpdateDialogFolderDeleted,
            update_dialog_folder_order_changed: UpdateDialogFoldersOrderChanged,
            update_favourites_messages_changed: UpdateFavouritesMessagesChanged,
            update_user_restrictions_changed: UpdateUserRestrictionsChanged,
            conference_online: UpdateConferenceOnline,
            conference_invite: UpdateConferenceInvite,
            update_thread_created: UpdateThreadCreated,
            update_subscribed_to_thread: UpdateSubscribedToThread,
            update_unsubscribed_from_thread: UpdateUnsubscribedFromThread,
            update_thread_typing: UpdateThreadTyping,
            update_draft_message_changed: UpdateDraftMessageChanged,
            update_group_shortname_removed: UpdateGroupShortnameRemoved,
            update_conference_statuses: UpdateConferenceStatuses
    ) -> None:
        self.type = update_type
        self.seq = seq
        self.state = state
        self.update_header = update_header
        self.update_force_reload_state = update_force_reload_state
        self.update_user_avatar_changed = update_user_avatar_changed
        self.update_user_name_changed = update_user_name_changed
        self.update_user_local_name_changed = update_user_local_name_changed
        self.update_user_contacts_changed = update_user_contacts_changed
        self.update_user_nick_changed = update_user_nick_changed
        self.update_user_about_changed = update_user_about_changed
        self.update_user_preferred_languages_changed = update_user_preferred_languages_changed
        self.update_user_time_zone_changed = update_user_time_zone_changed
        self.update_user_bot_commands_changed = update_user_bot_commands_changed
        self.update_user_ext_changed = update_user_ext_changed
        self.update_user_sex_changed = update_user_sex_changed
        self.update_user_custom_profile_changed = update_user_custom_profile_changed
        self.update_user_status_changed = update_user_status_changed
        self.update_contact_registered = update_contact_registered
        self.update_contacts_added = update_contacts_added
        self.update_contacts_add_task_suspended = update_contacts_add_task_suspended
        self.update_contacts_removed = update_contacts_removed
        self.update_user_blocked = update_user_blocked
        self.update_user_unblocked = update_user_unblocked
        self.update_interactive_media_event = update_interactive_media_event
        self.update_message = update_message
        self.update_message_content_changed = update_message_content_changed
        self.update_message_sent = update_message_sent
        self.update_message_received = update_message_received
        self.update_message_read = update_message_read
        self.update_message_read_by_me = update_message_read_by_me
        self.update_message_delete = update_message_delete
        self.update_chat_clear = update_chat_clear
        self.update_chat_delete = update_chat_delete
        self.update_chat_archive = update_chat_archive
        self.update_chat_groups_changed = update_chat_groups_changed
        self.update_reactions_update = update_reactions_update
        self.update_dialog_favourite_changed = update_dialog_favourite_changed
        self.update_pinned_messages_changed = update_pinned_messages_changed
        self.update_group_title_changed = update_group_title_changed
        self.update_group_avatar_changed = update_group_avatar_changed
        self.update_group_about_changed = update_group_about_changed
        self.update_group_owner_changed = update_group_owner_changed
        self.update_group_members_updated = update_group_members_updated
        self.update_group_member_diff = update_group_member_diff
        self.update_group_members_count_changed = update_group_members_count_changed
        self.update_group_member_permissions_changed = update_group_member_permissions_changed
        self.update_group_invite_obsolete = update_group_invite_obsolete
        self.update_group_user_invited_obsolete = update_group_user_invited_obsolete
        self.update_group_user_leave_obsolete = update_group_user_leave_obsolete
        self.update_group_user_kick_obsolete = update_group_user_kick_obsolete
        self.update_group_members_update_obsolete = update_group_members_update_obsolete
        self.update_group_title_changed_obsolete = update_group_title_changed_obsolete
        self.update_group_about_changed_obsolete = update_group_about_changed_obsolete
        self.update_group_avatar_changed_obsolete = update_group_avatar_changed_obsolete
        self.update_group_shortname_changed = update_group_shortname_changed
        self.update_sticker_collections_changed = update_sticker_collections_changed
        self.update_sticker_pack_removed = update_sticker_pack_removed
        self.update_sticker_pack_added = update_sticker_pack_added
        self.update_user_sticker_pack_collection_changed = update_user_sticker_pack_collection_changed
        self.update_typing = update_typing
        self.update_typing_stop = update_typing_stop
        self.update_user_online = update_user_online
        self.update_user_offline = update_user_offline
        self.update_user_last_seen = update_user_last_seen
        self.update_group_online = update_group_online
        self.update_event_bus_device_connected = update_event_bus_device_connected
        self.update_event_bus_device_disconnected = update_event_bus_device_disconnected
        self.update_event_bus_message = update_event_bus_message
        self.update_event_bus_disposed = update_event_bus_disposed
        self.update_incoming_call_deprecated = update_incoming_call_deprecated
        self.update_incoming_call = update_incoming_call
        self.update_call_handled = update_call_handled
        self.update_call_disposed = update_call_disposed
        self.update_parameter_changed = update_parameter_changed
        self.update_raw_update = update_raw_update
        self.update_empty_update = update_empty_update
        self.update_counters_changed = update_counters_changed
        self.update_config = update_config
        self.update_space_modified = update_space_modified
        self.update_space_member_modified = update_space_member_modified
        self.update_message_rejected_by_hook = update_message_rejected_by_hook
        self.update_message_edit_rejected_by_hook = update_message_edit_rejected_by_hook
        self.update_user = update_user
        self.update_feature_flag_changed = update_feature_flag_changed
        self.update_group = update_group
        self.update_group_member_invited = update_group_member_invited
        self.message_reactions_update = message_reactions_update
        self.update_permissions_change = update_permissions_change
        self.update_group_typing = update_group_typing
        self.update_dialog_read_later_changed = update_dialog_read_later_changed
        self.update_dialog_folder_changed = update_dialog_folder_changed
        self.update_dialog_folder_deleted = update_dialog_folder_deleted
        self.update_dialog_folder_order_changed = update_dialog_folder_order_changed
        self.update_favourites_messages_changed = update_favourites_messages_changed
        self.update_user_restrictions_changed = update_user_restrictions_changed
        self.conference_online = conference_online
        self.conference_invite = conference_invite
        self.update_thread_created = update_thread_created
        self.update_subscribed_to_thread = update_subscribed_to_thread
        self.update_unsubscribed_from_thread = update_unsubscribed_from_thread
        self.update_thread_typing = update_thread_typing
        self.update_draft_message_changed = update_draft_message_changed
        self.update_group_shortname_removed = update_group_shortname_removed
        self.update_conference_statuses = update_conference_statuses

    @classmethod
    def from_api(cls, update: sequence_and_updates_pb2.UpdateSeqUpdate) -> 'UpdateSeqUpdate':
        if hasattr(update, "unboxed_update"):
            update = update.unboxed_update
        return cls(
            update_type_mapper.get(update.WhichOneof('update')),
            update.seq,
            update.state,
            update.update_header,
            UpdateForceReloadState.from_api(update.updateForceReloadState),
            UpdateUserAvatarChanged.from_api(update.updateUserAvatarChanged),
            UpdateUserNameChanged.from_api(update.updateUserNameChanged),
            UpdateUserLocalNameChanged.from_api(update.updateUserLocalNameChanged),
            UpdateUserContactsChanged.from_api(update.updateUserContactsChanged),
            UpdateUserNickChanged.from_api(update.updateUserNickChanged),
            UpdateUserAboutChanged.from_api(update.updateUserAboutChanged),
            UpdateUserPreferredLanguagesChanged.from_api(update.updateUserPreferredLanguagesChanged),
            UpdateUserTimeZoneChanged.from_api(update.updateUserTimeZoneChanged),
            UpdateUserBotCommandsChanged.from_api(update.updateUserBotCommandsChanged),
            UpdateUserExtChanged.from_api(update.updateUserExtChanged),
            UpdateUserSexChanged.from_api(update.updateUserSexChanged),
            UpdateUserCustomProfileChanged.from_api(update.updateUserCustomProfileChanged),
            UpdateUserStatusChanged.from_api(update.updateUserStatusChanged),
            UpdateContactRegistered.from_api(update.updateContactRegistered),
            UpdateContactsAdded.from_api(update.updateContactsAdded),
            UpdateContactsAddTaskSuspended.from_api(update.updateContactsAddTaskSuspended),
            UpdateContactsRemoved.from_api(update.updateContactsRemoved),
            UpdateUserBlocked.from_api(update.updateUserBlocked),
            UpdateUserUnblocked.from_api(update.updateUserUnblocked),
            UpdateInteractiveMediaEvent.from_api(update.updateInteractiveMediaEvent),
            UpdateMessage.from_api(update.updateMessage),
            UpdateMessageContentChanged.from_api(update.updateMessageContentChanged),
            UpdateMessageSent.from_api(update.updateMessageSent),
            UpdateMessageReceived.from_api(update.updateMessageReceived),
            UpdateMessageRead.from_api(update.updateMessageRead),
            UpdateMessageReadByMe.from_api(update.updateMessageReadByMe),
            UpdateMessageDelete.from_api(update.updateMessageDelete),
            UpdateChatClear.from_api(update.updateChatClear),
            UpdateChatDelete.from_api(update.updateChatDelete),
            UpdateChatArchive.from_api(update.updateChatArchive),
            UpdateChatGroupsChanged.from_api(update.updateChatGroupsChanged),
            UpdateReactionsUpdate.from_api(update.updateReactionsUpdate),
            UpdateDialogFavouriteChanged.from_api(update.updateDialogFavouriteChanged),
            UpdatePinnedMessagesChanged.from_api(update.updatePinnedMessagesChanged),
            UpdateGroupTitleChanged.from_api(update.updateGroupTitleChanged),
            UpdateGroupAvatarChanged.from_api(update.updateGroupAvatarChanged),
            UpdateGroupAboutChanged.from_api(update.updateGroupAboutChanged),
            UpdateGroupOwnerChanged.from_api(update.updateGroupOwnerChanged),
            UpdateGroupMembersUpdated.from_api(update.updateGroupMembersUpdated),
            UpdateGroupMemberDiff.from_api(update.updateGroupMemberDiff),
            UpdateGroupMembersCountChanged.from_api(update.updateGroupMembersCountChanged),
            UpdateGroupMemberPermissionsChanged.from_api(update.updateGroupMemberPermissionsChanged),
            UpdateGroupInviteObsolete.from_api(update.updateGroupInviteObsolete),
            UpdateGroupUserInvitedObsolete.from_api(update.updateGroupUserInvitedObsolete),
            UpdateGroupUserLeaveObsolete.from_api(update.updateGroupUserLeaveObsolete),
            UpdateGroupUserKickObsolete.from_api(update.updateGroupUserKickObsolete),
            UpdateGroupMembersUpdateObsolete.from_api(update.updateGroupMembersUpdateObsolete),
            UpdateGroupTitleChangedObsolete.from_api(update.updateGroupTitleChangedObsolete),
            UpdateGroupAboutChangedObsolete.from_api(update.updateGroupAboutChangedObsolete),
            UpdateGroupAvatarChangedObsolete.from_api(update.updateGroupAvatarChangedObsolete),
            UpdateGroupShortnameChanged.from_api(update.updateGroupShortnameChanged),
            UpdateStickerCollectionsChanged.from_api(update.updateStickerCollectionsChanged),
            UpdateStickerPackRemoved.from_api(update.updateStickerPackRemoved),
            UpdateStickerPackAdded.from_api(update.updateStickerPackAdded),
            UpdateUserStickerPackCollectionChanged.from_api(update.updateUserStickerPackCollectionChanged),
            UpdateTyping.from_api(update.updateTyping),
            UpdateTypingStop.from_api(update.updateTypingStop),
            UpdateUserOnline.from_api(update.updateUserOnline),
            UpdateUserOffline.from_api(update.updateUserOffline),
            UpdateUserLastSeen.from_api(update.updateUserLastSeen),
            UpdateGroupOnline.from_api(update.updateGroupOnline),
            UpdateEventBusDeviceConnected.from_api(update.updateEventBusDeviceConnected),
            UpdateEventBusDeviceDisconnected.from_api(update.updateEventBusDeviceDisconnected),
            UpdateEventBusMessage.from_api(update.updateEventBusMessage),
            UpdateEventBusDisposed.from_api(update.updateEventBusDisposed),
            UpdateIncomingCallDeprecated.from_api(update.updateIncomingCallDeprecated),
            UpdateIncomingCall.from_api(update.updateIncomingCall),
            UpdateCallHandled.from_api(update.updateCallHandled),
            UpdateCallDisposed.from_api(update.updateCallDisposed),
            UpdateParameterChanged.from_api(update.updateParameterChanged),
            UpdateRawUpdate.from_api(update.updateRawUpdate),
            UpdateEmptyUpdate.from_api(update.updateEmptyUpdate),
            UpdateCountersChanged.from_api(update.updateCountersChanged),
            UpdateConfig.from_api(update.updateConfig),
            UpdateSpaceModified.from_api(update.updateSpaceModified),
            UpdateSpaceMemberModified.from_api(update.updateSpaceMemberModified),
            UpdateMessageRejectedByHook.from_api(update.updateMessageRejectedByHook),
            UpdateMessageEditRejectedByHook.from_api(update.updateMessageEditRejectedByHook),
            UpdateUser.from_api(update.updateUser),
            UpdateFeatureFlagChanged.from_api(update.updateFeatureFlagChanged),
            UpdateGroup.from_api(update.updateGroup),
            UpdateGroupMemberInvited.from_api(update.updateGroupMemberInvited),
            MessageReactionsUpdate.from_api(update.messageReactionsUpdate),
            UpdatePermissionsChange.from_api(update.updatePermissionsChange),
            UpdateGroupTyping.from_api(update.updateGroupTyping),
            UpdateDialogReadLaterChanged.from_api(update.updateDialogReadLaterChanged),
            UpdateDialogFolderChanged.from_api(update.updateDialogFolderChanged),
            UpdateDialogFolderDeleted.from_api(update.updateDialogFolderDeleted),
            UpdateDialogFoldersOrderChanged.from_api(update.updateDialogFolderOrderChanged),
            UpdateFavouritesMessagesChanged.from_api(update.updateFavouritesMessagesChanged),
            UpdateUserRestrictionsChanged.from_api(update.updateUserRestrictionsChanged),
            UpdateConferenceOnline.from_api(update.conference_online),
            UpdateConferenceInvite.from_api(update.conference_invite),
            UpdateThreadCreated.from_api(update.updateThreadCreated),
            UpdateSubscribedToThread.from_api(update.updateSubscribedToThread),
            UpdateUnsubscribedFromThread.from_api(update.updatedUnsubscribedFromThread),
            UpdateThreadTyping.from_api(update.updateThreadTyping),
            UpdateDraftMessageChanged.from_api(update.draftMessageChanged),
            UpdateGroupShortnameRemoved.from_api(update.groupShortnameRemoved),
            UpdateConferenceStatuses.from_api(update.conference_statuses)
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            "seq": self.seq,
            "state": self.state,
            "update_header": self.update_header,
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == UpdateType.UPDATE_FORCE_RELOAD_STATE:
            return self.update_force_reload_state
        if self.type == UpdateType.UPDATE_USER_AVATAR_CHANGED:
            return self.update_user_avatar_changed
        if self.type == UpdateType.UPDATE_USER_NAME_CHANGED:
            return self.update_user_name_changed
        if self.type == UpdateType.UPDATE_USER_LOCAL_NAME_CHANGED:
            return self.update_user_local_name_changed
        if self.type == UpdateType.UPDATE_USER_CONTACTS_CHANGED:
            return self.update_user_contacts_changed
        if self.type == UpdateType.UPDATE_USER_NICK_CHANGED:
            return self.update_user_nick_changed
        if self.type == UpdateType.UPDATE_USER_ABOUT_CHANGED:
            return self.update_user_about_changed
        if self.type == UpdateType.UPDATE_USER_PREFERRED_LANGUAGES_CHANGED:
            return self.update_user_preferred_languages_changed
        if self.type == UpdateType.UPDATE_USER_TIME_ZONE_CHANGED:
            return self.update_user_time_zone_changed
        if self.type == UpdateType.UPDATE_USER_BOT_COMMANDS_CHANGED:
            return self.update_user_bot_commands_changed
        if self.type == UpdateType.UPDATE_USER_EXT_CHANGED:
            return self.update_user_ext_changed
        if self.type == UpdateType.UPDATE_USER_SEX_CHANGED:
            return self.update_user_sex_changed
        if self.type == UpdateType.UPDATE_USER_CUSTOM_PROFILE_CHANGED:
            return self.update_user_custom_profile_changed
        if self.type == UpdateType.UPDATE_USER_STATUS_CHANGED:
            return self.update_user_status_changed
        if self.type == UpdateType.UPDATE_CONTACT_REGISTERED:
            return self.update_contact_registered
        if self.type == UpdateType.UPDATE_CONTACTS_ADDED:
            return self.update_contacts_added
        if self.type == UpdateType.UPDATE_CONTACTS_ADD_TASK_SUSPENDED:
            return self.update_contacts_add_task_suspended
        if self.type == UpdateType.UPDATE_CONTACTS_REMOVED:
            return self.update_contacts_removed
        if self.type == UpdateType.UPDATE_USER_BLOCKED:
            return self.update_user_blocked
        if self.type == UpdateType.UPDATE_USER_UNBLOCKED:
            return self.update_user_unblocked
        if self.type == UpdateType.UPDATE_INTERACTIVE_MEDIA_EVENT:
            return self.update_interactive_media_event
        if self.type == UpdateType.UPDATE_MESSAGE:
            return self.update_message
        if self.type == UpdateType.UPDATE_MESSAGE_CONTENT_CHANGED:
            return self.update_message_content_changed
        if self.type == UpdateType.UPDATE_MESSAGE_SENT:
            return self.update_message_sent
        if self.type == UpdateType.UPDATE_MESSAGE_RECEIVED:
            return self.update_message_received
        if self.type == UpdateType.UPDATE_MESSAGE_READ:
            return self.update_message_read
        if self.type == UpdateType.UPDATE_MESSAGE_READ_BY_ME:
            return self.update_message_read_by_me
        if self.type == UpdateType.UPDATE_MESSAGE_DELETE:
            return self.update_message_delete
        if self.type == UpdateType.UPDATE_CHAT_CLEAR:
            return self.update_chat_clear
        if self.type == UpdateType.UPDATE_CHAT_DELETE:
            return self.update_chat_delete
        if self.type == UpdateType.UPDATE_CHAT_ARCHIVE:
            return self.update_chat_archive
        if self.type == UpdateType.UPDATE_CHAT_GROUPS_CHANGED:
            return self.update_chat_groups_changed
        if self.type == UpdateType.UPDATE_REACTIONS_UPDATE:
            return self.update_reactions_update
        if self.type == UpdateType.UPDATE_DIALOG_FAVOURITE_CHANGED:
            return self.update_dialog_favourite_changed
        if self.type == UpdateType.UPDATE_PINNED_MESSAGES_CHANGED:
            return self.update_pinned_messages_changed
        if self.type == UpdateType.UPDATE_GROUP_TITLE_CHANGED:
            return self.update_group_title_changed
        if self.type == UpdateType.UPDATE_GROUP_AVATAR_CHANGED:
            return self.update_group_avatar_changed
        if self.type == UpdateType.UPDATE_GROUP_ABOUT_CHANGED:
            return self.update_group_about_changed
        if self.type == UpdateType.UPDATE_GROUP_OWNER_CHANGED:
            return self.update_group_owner_changed
        if self.type == UpdateType.UPDATE_GROUP_MEMBERS_UPDATED:
            return self.update_group_members_updated
        if self.type == UpdateType.UPDATE_GROUP_MEMBER_DIFF:
            return self.update_group_member_diff
        if self.type == UpdateType.UPDATE_GROUP_MEMBERS_COUNT_CHANGED:
            return self.update_group_members_count_changed
        if self.type == UpdateType.UPDATE_GROUP_MEMBER_PERMISSIONS_CHANGED:
            return self.update_group_member_permissions_changed
        if self.type == UpdateType.UPDATE_GROUP_INVITE_OBSOLETE:
            return self.update_group_invite_obsolete
        if self.type == UpdateType.UPDATE_GROUP_USER_INVITED_OBSOLETE:
            return self.update_group_user_invited_obsolete
        if self.type == UpdateType.UPDATE_GROUP_USER_LEAVE_OBSOLETE:
            return self.update_group_user_leave_obsolete
        if self.type == UpdateType.UPDATE_GROUP_USER_KICK_OBSOLETE:
            return self.update_group_user_kick_obsolete
        if self.type == UpdateType.UPDATE_GROUP_MEMBERS_UPDATE_OBSOLETE:
            return self.update_group_members_update_obsolete
        if self.type == UpdateType.UPDATE_GROUP_TITLE_CHANGED_OBSOLETE:
            return self.update_group_title_changed_obsolete
        if self.type == UpdateType.UPDATE_GROUP_ABOUT_CHANGED_OBSOLETE:
            return self.update_group_about_changed_obsolete
        if self.type == UpdateType.UPDATE_GROUP_AVATAR_CHANGED_OBSOLETE:
            return self.update_group_avatar_changed_obsolete
        if self.type == UpdateType.UPDATE_GROUP_SHORTNAME_CHANGED:
            return self.update_group_shortname_changed
        if self.type == UpdateType.UPDATE_STICKER_COLLECTIONS_CHANGED:
            return self.update_sticker_collections_changed
        if self.type == UpdateType.UPDATE_STICKER_PACK_REMOVED:
            return self.update_sticker_pack_removed
        if self.type == UpdateType.UPDATE_STICKER_PACK_ADDED:
            return self.update_sticker_pack_added
        if self.type == UpdateType.UPDATE_USER_STICKER_PACK_COLLECTION_CHANGED:
            return self.update_user_sticker_pack_collection_changed
        if self.type == UpdateType.UPDATE_TYPING:
            return self.update_typing
        if self.type == UpdateType.UPDATE_TYPING_STOP:
            return self.update_typing_stop
        if self.type == UpdateType.UPDATE_USER_ONLINE:
            return self.update_user_online
        if self.type == UpdateType.UPDATE_USER_OFFLINE:
            return self.update_user_offline
        if self.type == UpdateType.UPDATE_USER_LAST_SEEN:
            return self.update_user_last_seen
        if self.type == UpdateType.UPDATE_GROUP_ONLINE:
            return self.update_group_online
        if self.type == UpdateType.UPDATE_EVENT_BUS_DEVICE_CONNECTED:
            return self.update_event_bus_device_connected
        if self.type == UpdateType.UPDATE_EVENT_BUS_DEVICE_DISCONNECTED:
            return self.update_event_bus_device_disconnected
        if self.type == UpdateType.UPDATE_EVENT_BUS_MESSAGE:
            return self.update_event_bus_message
        if self.type == UpdateType.UPDATE_EVENT_BUS_DISPOSED:
            return self.update_event_bus_disposed
        if self.type == UpdateType.UPDATE_INCOMING_CALL_DEPRECATED:
            return self.update_incoming_call_deprecated
        if self.type == UpdateType.UPDATE_INCOMING_CALL:
            return self.update_incoming_call
        if self.type == UpdateType.UPDATE_CALL_HANDLED:
            return self.update_call_handled
        if self.type == UpdateType.UPDATE_CALL_DISPOSED:
            return self.update_call_disposed
        if self.type == UpdateType.UPDATE_PARAMETER_CHANGED:
            return self.update_parameter_changed
        if self.type == UpdateType.UPDATE_RAW_UPDATE:
            return self.update_raw_update
        if self.type == UpdateType.UPDATE_EMPTY_UPDATE:
            return self.update_empty_update
        if self.type == UpdateType.UPDATE_COUNTERS_CHANGED:
            return self.update_counters_changed
        if self.type == UpdateType.UPDATE_CONFIG:
            return self.update_config
        if self.type == UpdateType.UPDATE_SPACE_MODIFIED:
            return self.update_space_modified
        if self.type == UpdateType.UPDATE_SPACE_MEMBER_MODIFIED:
            return self.update_space_member_modified
        if self.type == UpdateType.UPDATE_MESSAGE_REJECTED_BY_HOOK:
            return self.update_message_rejected_by_hook
        if self.type == UpdateType.UPDATE_MESSAGE_EDIT_REJECTED_BY_HOOK:
            return self.update_message_edit_rejected_by_hook
        if self.type == UpdateType.UPDATE_USER:
            return self.update_user
        if self.type == UpdateType.UPDATE_FEATURE_FLAG_CHANGED:
            return self.update_feature_flag_changed
        if self.type == UpdateType.UPDATE_GROUP:
            return self.update_group
        if self.type == UpdateType.UPDATE_GROUP_MEMBER_INVITED:
            return self.update_group_member_invited
        if self.type == UpdateType.MESSAGE_REACTIONS_UPDATE:
            return self.message_reactions_update
        if self.type == UpdateType.UPDATE_PERMISSIONS_CHANGE:
            return self.update_permissions_change
        if self.type == UpdateType.UPDATE_GROUP_TYPING:
            return self.update_group_typing
        if self.type == UpdateType.UPDATE_DIALOG_READ_LATER_CHANGED:
            return self.update_dialog_read_later_changed
        if self.type == UpdateType.UPDATE_DIALOG_FOLDER_CHANGED:
            return self.update_dialog_folder_changed
        if self.type == UpdateType.UPDATE_DIALOG_FOLDER_DELETED:
            return self.update_dialog_folder_deleted
        if self.type == UpdateType.UPDATE_DIALOG_FOLDER_ORDER_CHANGED:
            return self.update_dialog_folder_order_changed
        if self.type == UpdateType.UPDATE_FAVOURITES_MESSAGES_CHANGED:
            return self.update_favourites_messages_changed
        if self.type == UpdateType.UPDATE_USER_RESTRICTIONS_CHANGED:
            return self.update_user_restrictions_changed
        if self.type == UpdateType.CONFERENCE_ONLINE:
            return self.conference_online
        if self.type == UpdateType.CONFERENCE_INVITE:
            return self.conference_invite
        if self.type == UpdateType.UPDATE_THREAD_CREATED:
            return self.update_thread_created
        if self.type == UpdateType.UPDATE_SUBSCRIBED_TO_THREAD:
            return self.update_subscribed_to_thread
        if self.type == UpdateType.UPDATE_UNSUBSCRIBED_FROM_THREAD:
            return self.update_unsubscribed_from_thread
        if self.type == UpdateType.UPDATE_THREAD_TYPING:
            return self.update_thread_typing
        if self.type == UpdateType.UPDATE_DRAFT_MESSAGE_CHANGED:
            return self.update_draft_message_changed
        if self.type == UpdateType.UPDATE_GROUP_SHORTNAME_REMOVED:
            return self.update_group_shortname_removed
        if self.type == UpdateType.CONFERENCE_STATUSES:
            return self.update_conference_statuses

    def __str__(self):
        return "UpdateSeqUpdate({})".format(self.__dict__())


class GetDifference:
    def __init__(
            self,
            seq: int,
            state: bytes,
            updates: List[UpdateSeqUpdate],
            messages: List[Message],
            need_more: bool,
            users_refs: List[UserOutPeer],
            groups_refs: List[GroupOutPeer],
            config: Config,
            config_hash: int
    ) -> None:
        self.seq = seq
        self.state = state
        self.updates = updates
        self.messages = messages
        self.need_more = need_more
        self.users_refs = users_refs
        self.groups_refs = groups_refs
        self.config = config
        self.config_hash = config_hash

    @classmethod
    def from_api(cls, diff: sequence_and_updates_pb2.ResponseGetDifference) -> 'GetDifference':
        return cls(
            diff.seq,
            diff.state,
            [UpdateSeqUpdate.from_api(x) for x in diff.updates],
            [Message.from_api(x) for x in diff.messages],
            diff.need_more,
            [UserOutPeer.from_api(x) for x in diff.users_refs],
            [GroupOutPeer.from_api(x) for x in diff.groups_refs],
            Config.from_api(diff.config),
            diff.config_hash.value
        )

    def __dict__(self):
        return {
            "seq": self.seq,
            "state": self.state,
            "updates": [x.__dict__() for x in self.updates],
            "messages": [x.__dict__() for x in self.messages],
            "need_more": self.need_more,
            "users_refs": [x.__dict__() for x in self.users_refs],
            "groups_refs": [x.__dict__() for x in self.groups_refs],
            "config": self.config.__dict__(),
            "config_hash": self.config_hash,
        }

    def __str__(self):
        return "GetDifference({})".format(self.__dict__())
