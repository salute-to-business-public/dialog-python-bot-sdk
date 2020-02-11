from dialog_api import groups_pb2

from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.Peer import PeerType, Peer


class GroupType:
    GROUPTYPE_UNKNOWN = groups_pb2.GROUPTYPE_UNKNOWN
    GROUPTYPE_GROUP = groups_pb2.GROUPTYPE_GROUP
    GROUPTYPE_CHANNEL = groups_pb2.GROUPTYPE_CHANNEL
    GROUPTYPE_THREAD = groups_pb2.GROUPTYPE_THREAD


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

    def __dict__(self):
        return {"about": self.about, "avatar": self.avatar.__dict__(), "name": self.name, "title": self.title,
                "type": self.type}

    def __str__(self):
        return "{}".format(self.__dict__())


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
        return "group: {}".format(self.__dict__())
