from typing import List

from dialog_api import groups_pb2
from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.media_and_files import Avatar
from dialog_bot_sdk.entities.peers import Peer, PeerType
from dialog_api.groups_pb2 import GROUPADMINPERMISSION_EDITSHORTNAME, GROUPADMINPERMISSION_INVITE, \
    GROUPADMINPERMISSION_KICK, GROUPADMINPERMISSION_UPDATEINFO, GROUPADMINPERMISSION_SETPERMISSIONS, \
    GROUPADMINPERMISSION_EDITMESSAGE, GROUPADMINPERMISSION_DELETEMESSAGE, GROUPADMINPERMISSION_GETINTEGRATIONTOKEN, \
    GROUPADMINPERMISSION_SENDMESSAGE, GROUPADMINPERMISSION_PINMESSAGE, GROUPADMINPERMISSION_VIEWMEMBERS, \
    GROUPADMINPERMISSION_LEAVE, GROUPADMINPERMISSION_TARGETING, GROUPADMINPERMISSION_UNKNOWN, \
    GROUPADMINPERMISSION_DELETE, GROUPADMINPERMISSION_MANAGE_CONFERENCE, GROUPADMINPERMISSION_VIEW_STATISTICS, \
    GROUPADMINPERMISSION_MANAGE_THREADS, GROUPADMINPERMISSION_READ_THREADS, GROUPADMINPERMISSION_WRITE_THREADS, \
    GROUPADMINPERMISSION_MANAGE_POLLS


PERMISSION_TO_STRING = {
    GROUPADMINPERMISSION_UNKNOWN: "unknown",
    GROUPADMINPERMISSION_EDITSHORTNAME: "edit short_name",
    GROUPADMINPERMISSION_INVITE: "invite",
    GROUPADMINPERMISSION_KICK: "kick",
    GROUPADMINPERMISSION_UPDATEINFO: "update info",
    GROUPADMINPERMISSION_SETPERMISSIONS: "set permissions",
    GROUPADMINPERMISSION_EDITMESSAGE: "edit message",
    GROUPADMINPERMISSION_DELETEMESSAGE: "delete message",
    GROUPADMINPERMISSION_GETINTEGRATIONTOKEN: "get integration token",
    GROUPADMINPERMISSION_SENDMESSAGE: "send message",
    GROUPADMINPERMISSION_PINMESSAGE: "pin message",
    GROUPADMINPERMISSION_VIEWMEMBERS: "view members",
    GROUPADMINPERMISSION_LEAVE: "leave",
    GROUPADMINPERMISSION_TARGETING: "targeting",
    GROUPADMINPERMISSION_DELETE: "delete",
    GROUPADMINPERMISSION_MANAGE_CONFERENCE: "manage conference",
    GROUPADMINPERMISSION_VIEW_STATISTICS: "view_statistics",
    GROUPADMINPERMISSION_MANAGE_THREADS: "manage_threads",
    GROUPADMINPERMISSION_READ_THREADS: "read_threads",
    GROUPADMINPERMISSION_WRITE_THREADS: "write_threads",
    GROUPADMINPERMISSION_MANAGE_POLLS: "manage_polls"
}


class GroupPermission:
    GROUPADMINPERMISSION_UNKNOWN = GROUPADMINPERMISSION_UNKNOWN
    GROUPADMINPERMISSION_EDITSHORTNAME = GROUPADMINPERMISSION_EDITSHORTNAME
    GROUPADMINPERMISSION_INVITE = GROUPADMINPERMISSION_INVITE
    GROUPADMINPERMISSION_KICK = GROUPADMINPERMISSION_KICK
    GROUPADMINPERMISSION_UPDATEINFO = GROUPADMINPERMISSION_UPDATEINFO
    GROUPADMINPERMISSION_SETPERMISSIONS = GROUPADMINPERMISSION_SETPERMISSIONS
    GROUPADMINPERMISSION_EDITMESSAGE = GROUPADMINPERMISSION_EDITMESSAGE
    GROUPADMINPERMISSION_DELETEMESSAGE = GROUPADMINPERMISSION_DELETEMESSAGE
    GROUPADMINPERMISSION_GETINTEGRATIONTOKEN = GROUPADMINPERMISSION_GETINTEGRATIONTOKEN
    GROUPADMINPERMISSION_SENDMESSAGE = GROUPADMINPERMISSION_SENDMESSAGE
    GROUPADMINPERMISSION_PINMESSAGE = GROUPADMINPERMISSION_PINMESSAGE
    GROUPADMINPERMISSION_VIEWMEMBERS = GROUPADMINPERMISSION_VIEWMEMBERS
    GROUPADMINPERMISSION_LEAVE = GROUPADMINPERMISSION_LEAVE
    GROUPADMINPERMISSION_TARGETING = GROUPADMINPERMISSION_TARGETING
    GROUPADMINPERMISSION_DELETE = GROUPADMINPERMISSION_DELETE
    GROUPADMINPERMISSION_MANAGE_CONFERENCE = GROUPADMINPERMISSION_MANAGE_CONFERENCE
    GROUPADMINPERMISSION_VIEW_STATISTICS = GROUPADMINPERMISSION_VIEW_STATISTICS
    GROUPADMINPERMISSION_MANAGE_THREADS = GROUPADMINPERMISSION_MANAGE_THREADS
    GROUPADMINPERMISSION_READ_THREADS = GROUPADMINPERMISSION_READ_THREADS
    GROUPADMINPERMISSION_WRITE_THREADS = GROUPADMINPERMISSION_WRITE_THREADS
    GROUPADMINPERMISSION_MANAGE_POLLS = GROUPADMINPERMISSION_MANAGE_POLLS


class GroupType:
    GROUPTYPE_UNKNOWN = groups_pb2.GROUPTYPE_UNKNOWN
    GROUPTYPE_GROUP = groups_pb2.GROUPTYPE_GROUP
    GROUPTYPE_CHANNEL = groups_pb2.GROUPTYPE_CHANNEL


class Permissions:
    def __init__(self, user_id: int, permissions: List[GroupPermission]) -> None:
        self.user_id = user_id
        self.permissions = permissions

    @classmethod
    def from_api(cls, permissions: groups_pb2.GroupMemberPermission) -> 'Permissions':
        return cls(permissions.user_id, [x for x in permissions.permissions])

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "permissions": [PERMISSION_TO_STRING[x] if x in PERMISSION_TO_STRING else str(x) for x in self.permissions]
        }

    def __str__(self):
        return "Permissions({})".format(self.__dict__())


class GroupData:
    def __init__(
            self,
            space_id: UUID,
            title: str,
            avatar: Avatar,
            members_amount: int,
            type: GroupType,
            created_at: int,
            about: str,
            shortname: str,
            base_permissions: List[GroupPermission],
            clock: int,
            pinned_at: int,
            conference_link: str,
            members_count_limit: int,
            deleted_at: int,
            owner_user_id: int,
            threads_enabled: bool
    ) -> None:
        self.space_id = space_id
        self.title = title
        self.avatar = avatar
        self.members_amount = members_amount
        self.type = type
        self.created_at = created_at
        self.about = about
        self.shortname = shortname
        self.base_permissions = base_permissions
        self.clock = clock
        self.pinned_at = pinned_at
        self.conference_link = conference_link
        self.members_count_limit = members_count_limit
        self.deleted_at = deleted_at
        self.owner_user_id = owner_user_id
        self.name = shortname
        self.threads_enabled = threads_enabled

    @classmethod
    def from_api(cls, data: groups_pb2.GroupData) -> 'GroupData':
        return cls(
            UUID.from_api(data.space_id),
            data.title,
            Avatar.from_api(data.avatar),
            data.members_amount,
            data.group_type,
            data.created_at.seconds,
            data.about.value,
            data.shortname.value,
            data.base_permissions,
            data.clock,
            data.pinned_at.value,
            data.conference_link.value,
            data.members_count_limit.value,
            data.deleted_at.value,
            data.owner_user_id.value,
            data.threads_enabled.value
        )

    def __dict__(self):
        return {
            "space_id": self.space_id.__dict__(),
            "title": self.title,
            "avatar": self.avatar.__dict__(),
            "members_amount": self.members_amount,
            "type": self.type,
            "created_at": self.created_at,
            "about": self.about,
            "shortname": self.shortname,
            "base_permissions": self.base_permissions,
            "clock": self.clock,
            "pinned_at": self.pinned_at,
            "conference_link": self.conference_link,
            "members_count_limit": self.members_count_limit,
            "deleted_at": self.deleted_at,
            "owner_user_id": self.owner_user_id,
            "name": self.name,
            "threads_enabled": self.threads_enabled
        }

    def __str__(self):
        return "GroupData({})".format(self.__dict__())


class Group:
    def __init__(self, id_: int, data: GroupData) -> None:
        self.data = data
        self.peer = Peer(id_, PeerType.PEERTYPE_GROUP)

    @classmethod
    def from_api(cls, group: groups_pb2.Group) -> 'Group':
        return cls(group.id, GroupData.from_api(group.data))

    def __dict__(self):
        return {"data": self.data.__dict__(), "peer": self.peer.__dict__()}

    def __str__(self):
        return "Group({})".format(self.__dict__())


class Member:
    def __init__(self, peer: Peer, invited_at: int, permissions: List[Permissions], clock: int, deleted_at: int) -> None:
        self.peer = peer
        self.invited_at = invited_at
        self.permissions = permissions
        self.clock = clock
        self.deleted_at = deleted_at

    @classmethod
    def from_api(cls, member: groups_pb2.Member) -> 'Member':
        return cls(
            Peer(member.uid, PeerType.PEERTYPE_PRIVATE),
            member.invited_at,
            member.permissions,
            member.clock,
            member.deleted_at.seconds
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "invited_at": self.invited_at,
            "permissions": self.permissions,
            "clock": self.clock,
            "deleted_at": self.deleted_at,
        }

    def __str__(self):
        return "Member({})".format(self.__dict__())


# updates
class UpdateGroupTitleChanged:
    def __init__(self, peer: Peer, title: str) -> None:
        self.peer = peer
        self.title = title

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupTitleChanged) -> 'UpdateGroupTitleChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.title,
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "title": self.title,
        }

    def __str__(self):
        return "UpdateGroupTitleChanged({})".format(self.__dict__())


class UpdateGroupAvatarChanged:
    def __init__(self, peer: Peer, avatar: Avatar) -> None:
        self.peer = peer
        self.avatar = avatar

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupAvatarChanged) -> 'UpdateGroupAvatarChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            Avatar.from_api(update.avatar),
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "avatar": self.avatar.__dict__(),
        }

    def __str__(self):
        return "UpdateGroupAvatarChanged({})".format(self.__dict__())


class UpdateGroupAboutChanged:
    def __init__(self, peer: Peer, about: str) -> None:
        self.peer = peer
        self.about = about

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupAboutChanged) -> 'UpdateGroupAboutChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.about.value,
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "about": self.about,
        }

    def __str__(self):
        return "UpdateGroupAboutChanged({})".format(self.__dict__())


class UpdateGroupOwnerChanged:
    def __init__(self, peer: Peer, user_peer: Peer) -> None:
        self.peer = peer
        self.user_peer = user_peer

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupOwnerChanged) -> 'UpdateGroupOwnerChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            Peer(update.user_id, PeerType.PEERTYPE_PRIVATE),
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "user_peer": self.user_peer.__dict__(),
        }

    def __str__(self):
        return "UpdateGroupOwnerChanged({})".format(self.__dict__())


class UpdateGroupMembersUpdated:
    def __init__(self, peer: Peer, members: List[Member]) -> None:
        self.peer = peer
        self.members = members

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupMembersUpdated) -> 'UpdateGroupMembersUpdated':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            [Member.from_api(x) for x in update.members],
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "members": [x.__dict__() for x in self.members],
        }

    def __str__(self):
        return "UpdateGroupMembersUpdated({})".format(self.__dict__())


class UpdateGroupMemberDiff:
    def __init__(self, removed_users: List[Peer], added_members: List[Member], members_count: int) -> None:
        self.removed_users = removed_users
        self.added_members = added_members
        self.members_count = members_count

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupMemberDiff) -> 'UpdateGroupMemberDiff':
        return cls(
            [Peer(x, PeerType.PEERTYPE_GROUP) for x in update.removed_users],
            [Member.from_api(x) for x in update.added_members],
            update.members_count
        )

    def __dict__(self):
        return {
            "removed_users": [x.__dict__() for x in self.removed_users],
            "added_members": [x.__dict__() for x in self.added_members],
            "members_count": self.members_count
        }

    def __str__(self):
        return "UpdateGroupMemberDiff({})".format(self.__dict__())


class UpdateGroupMembersCountChanged:
    def __init__(self, peer: Peer, members_count: int) -> None:
        self.peer = peer
        self.members_count = members_count

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupMembersCountChanged) -> 'UpdateGroupMembersCountChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.members_count,
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "members_count": self.members_count,
        }

    def __str__(self):
        return "UpdateGroupMembersCountChanged({})".format(self.__dict__())


class UpdateGroupMemberPermissionsChanged:
    def __init__(self, peer: Peer, user_peer: Peer, permissions: List[GroupPermission]) -> None:
        self.peer = peer
        self.user_peer = user_peer
        self.permissions = permissions

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupMemberPermissionsChanged) -> 'UpdateGroupMemberPermissionsChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            Peer(update.user_id, PeerType.PEERTYPE_PRIVATE),
            update.permissions
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "user_peer": self.user_peer.__dict__(),
            "permissions": self.permissions
        }

    def __str__(self):
        return "UpdateGroupMemberPermissionsChanged({})".format(self.__dict__())


class UpdateGroupInviteObsolete:
    def __init__(self, peer: Peer, rid: int, mid: UUID, invite_uid: int, date: int) -> None:
        self.peer = peer
        self.rid = rid
        self.mid = mid
        self.invite_uid = invite_uid
        self.date = date

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupInviteObsolete) -> 'UpdateGroupInviteObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.rid,
            UUID.from_api(update.mid),
            update.invite_uid,
            update.date
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "rid": self.rid,
            "mid": self.mid.__dict__(),
            "invite_uid": self.invite_uid,
            "date": self.date
        }

    def __str__(self):
        return "UpdateGroupInviteObsolete({})".format(self.__dict__())


class UpdateGroupUserInvitedObsolete:
    def __init__(self, peer: Peer, rid: int, mid: UUID, user_peer: Peer, inviter_peer: Peer, date: int) -> None:
        self.peer = peer
        self.rid = rid
        self.mid = mid
        self.user_peer = user_peer
        self.inviter_peer = inviter_peer
        self.date = date

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupUserInvitedObsolete) -> 'UpdateGroupUserInvitedObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.rid,
            UUID.from_api(update.mid),
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
            Peer(update.inviter_uid, PeerType.PEERTYPE_PRIVATE),
            update.date
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "rid": self.rid,
            "mid": self.mid.__dict__(),
            "user_peer": self.user_peer.__dict__(),
            "inviter_peer": self.inviter_peer.__dict__(),
            "date": self.date
        }

    def __str__(self):
        return "UpdateGroupUserInvitedObsolete({})".format(self.__dict__())


class UpdateGroupUserLeaveObsolete:
    def __init__(self, peer: Peer, mid: UUID, user_peer: Peer, date: int) -> None:
        self.peer = peer
        self.mid = mid
        self.user_peer = user_peer
        self.date = date

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupUserLeaveObsolete) -> 'UpdateGroupUserLeaveObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            UUID.from_api(update.mid),
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
            update.date
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "user_peer": self.user_peer.__dict__(),
            "date": self.date
        }

    def __str__(self):
        return "UpdateGroupUserLeaveObsolete({})".format(self.__dict__())


class UpdateGroupUserKickObsolete:
    def __init__(self, peer: Peer, mid: UUID, user_peer: Peer, kicker_peer: Peer, date: int) -> None:
        self.peer = peer
        self.mid = mid
        self.user_peer = user_peer
        self.kicker_peer = kicker_peer
        self.date = date

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupUserKickObsolete) -> 'UpdateGroupUserKickObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            UUID.from_api(update.mid),
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
            Peer(update.kicker_uid, PeerType.PEERTYPE_PRIVATE),
            update.date
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "user_peer": self.user_peer.__dict__(),
            "kicker_peer": self.kicker_peer.__dict__(),
            "date": self.date
        }

    def __str__(self):
        return "UpdateGroupUserKickObsolete({})".format(self.__dict__())


class UpdateGroupMembersUpdateObsolete:
    def __init__(self, peer: Peer, members: List[Member]) -> None:
        self.peer = peer
        self.members = members

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupMembersUpdateObsolete) -> 'UpdateGroupMembersUpdateObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            [Member.from_api(x) for x in update.members],
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "members": [x.__dict__() for x in self.members],
        }

    def __str__(self):
        return "UpdateGroupMembersUpdateObsolete({})".format(self.__dict__())


class UpdateGroupTitleChangedObsolete:
    def __init__(self, peer: Peer, mid: UUID, user_peer: Peer, title: str, date: int) -> None:
        self.peer = peer
        self.mid = mid
        self.user_peer = user_peer
        self.title = title
        self.date = date

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupTitleChangedObsolete) -> 'UpdateGroupTitleChangedObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            UUID.from_api(update.mid),
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
            update.title,
            update.date
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "user_peer": self.user_peer.__dict__(),
            "title": self.title,
            "date": self.date
        }

    def __str__(self):
        return "UpdateGroupTitleChangedObsolete({})".format(self.__dict__())


class UpdateGroupAboutChangedObsolete:
    def __init__(self, peer: Peer, about: str) -> None:
        self.peer = peer
        self.about = about

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupAboutChangedObsolete) -> 'UpdateGroupAboutChangedObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.about.value,
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "about": self.about,
        }

    def __str__(self):
        return "UpdateGroupAboutChangedObsolete({})".format(self.__dict__())


class UpdateGroupAvatarChangedObsolete:
    def __init__(self, peer: Peer, mid: UUID, user_peer: Peer, avatar: Avatar, date: int) -> None:
        self.peer = peer
        self.mid = mid
        self.user_peer = user_peer
        self.avatar = avatar
        self.date = date

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupAvatarChangedObsolete) -> 'UpdateGroupAvatarChangedObsolete':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            UUID.from_api(update.mid),
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
            Avatar.from_api(update.avatar),
            update.date
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "user_peer": self.user_peer.__dict__(),
            "avatar": self.avatar.__dict__(),
            "date": self.date
        }

    def __str__(self):
        return "UpdateGroupAvatarChangedObsolete({})".format(self.__dict__())


class UpdateGroupShortnameChanged:
    def __init__(self, peer: Peer, shortname: str, user_peer: Peer) -> None:
        self.peer = peer
        self.shortname = shortname
        self.user_peer = user_peer

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupShortnameChanged) -> 'UpdateGroupShortnameChanged':
        return cls(
            Peer(update.group_id, PeerType.PEERTYPE_GROUP),
            update.shortname,
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "shortname": self.shortname,
            "user_peer": self.user_peer.__dict__(),
        }

    def __str__(self):
        return "UpdateGroupShortnameChanged({})".format(self.__dict__())


class UpdateGroup:
    def __init__(self, peer: Peer, data: GroupData) -> None:
        self.peer = peer
        self.data = data

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroup) -> 'UpdateGroup':
        group = Group.from_api(update)
        return cls(group.peer, group.data)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "data": self.data.__dict__(),
        }

    def __str__(self):
        return "UpdateGroup({})".format(self.__dict__())


class UpdateGroupMemberInvited:
    def __init__(self, peer: Peer, member: Member) -> None:
        self.peer = peer
        self.member = member

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupMemberInvited) -> 'UpdateGroupMemberInvited':
        return cls(Peer(update.group_id, PeerType.PEERTYPE_GROUP), Member.from_api(update.member))

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "member": self.member.__dict__(),
        }

    def __str__(self):
        return "UpdateGroupMemberInvited({})".format(self.__dict__())


class UpdateGroupShortnameRemoved:
    def __init__(self, peer: Peer, user_peer: Peer) -> None:
        self.peer = peer
        self.user_peer = user_peer

    @classmethod
    def from_api(cls, update: groups_pb2.UpdateGroupShortnameRemoved) -> 'UpdateGroupShortnameRemoved':
        return cls(Peer(update.group_id, PeerType.PEERTYPE_GROUP), Peer(update.uid, PeerType.PEERTYPE_PRIVATE))

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "user_peer": self.user_peer.__dict__(),
        }

    def __str__(self):
        return "UpdateGroupShortnameRemoved({})".format(self.__dict__())
