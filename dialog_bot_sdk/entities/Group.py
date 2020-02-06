from dialog_api import groups_pb2

from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.peers.OutPeer import OutPeer
from dialog_bot_sdk.entities.peers.Peer import PeerType


class GroupType:
    GROUPTYPE_UNKNOWN = 0
    GROUPTYPE_GROUP = 1
    GROUPTYPE_CHANNEL = 2
    GROUPTYPE_THREAD = 4


class GroupData:
    def __init__(self, about: str, avatar: Avatar, name: str, title: str, type_: int) -> None:
        self.about = about
        self.avatar = avatar
        self.name = name
        self.title = title
        self.type = type_

    @classmethod
    def from_api(cls, data: groups_pb2.GroupData) -> 'GroupData':
        return cls(data.about.value, Avatar.from_api(data.avatar), data.shortname.value, data.title, data.group_type)


class Group:
    def __init__(self, id_: int, access_hash: int, data: GroupData) -> None:
        self.id = id_
        self.access_hash = access_hash
        self.data = data
        self.out_peer = OutPeer(id_, access_hash, PeerType.PEERTYPE_GROUP)

    @classmethod
    def from_api(cls, group: groups_pb2.Group) -> 'Group':
        return cls(group.id, group.access_hash, GroupData.from_api(group.data))
