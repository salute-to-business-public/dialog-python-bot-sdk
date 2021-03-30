from dialog_api import groups_pb2
from dialog_api.groups_pb2 import GROUPTYPE_GROUP, GROUPTYPE_UNKNOWN, GROUPTYPE_CHANNEL, GROUPTYPE_THREAD

from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.Peer import PeerType, Peer


class GroupType:
    GROUPTYPE_UNKNOWN = GROUPTYPE_UNKNOWN
    GROUPTYPE_GROUP = GROUPTYPE_GROUP
    GROUPTYPE_CHANNEL = GROUPTYPE_CHANNEL
    GROUPTYPE_THREAD = GROUPTYPE_THREAD


class GroupData:
    def __init__(self, about: str, avatar: Avatar, name: str, title: str, type: int, owner_user_id: int,
                 conference_link: str, members_amount: int, members_count_limit: int, shortname: str) -> None:
        self.about = about
        self.avatar = avatar
        self.name = name
        self.title = title
        self.type = type
        self.owner_user_id = owner_user_id
        self.conference_link = conference_link
        self.members_amount = members_amount
        self.members_count_limit = members_count_limit
        self.shortname = shortname

    @classmethod
    def from_api(cls, data: groups_pb2.GroupData) -> 'GroupData':
        return cls(data.about.value, Avatar.from_api(data.avatar), data.shortname.value, data.title, data.group_type,
                   data.owner_user_id, data.conference_link.value, data.members_amount, data.members_count_limit.value,
                   data.shortname.value)

    def __dict__(self):
        return {"about": self.about, "avatar": self.avatar.__dict__(), "name": self.name, "title": self.title,
                "type": self.type, "owner_user_id": self.owner_user_id, "conference_link": self.conference_link,
                "members_amount": self.members_amount, "members_count_limit": self.members_count_limit,
                "shortname": self.shortname}

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
