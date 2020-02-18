from dialog_api import users_pb2
from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.Peer import PeerType, Peer


class UserData:
    def __init__(self, name: str, avatar: Avatar, about: str, nick: str) -> None:
        self.name = name
        self.avatar = avatar
        self.about = about
        self.nick = nick

    @classmethod
    def from_api(cls, data: users_pb2.UserData) -> 'UserData':
        if data:
            return cls(data.name, Avatar.from_api(data.avatar), data.about.value, data.nick.value)

    def __dict__(self):
        return {"name": self.name, "avatar": self.avatar.__dict__(), "about": self.about, "nick": self.nick}

    def __str__(self):
        return "{}".format(self.__dict__())


class User:
    def __init__(self, id: int, data: UserData = None) -> None:
        self.data = data
        self.peer = Peer(id, PeerType.PEERTYPE_PRIVATE)

    @classmethod
    def from_api(cls, user: users_pb2.User) -> 'User':
        return cls(user.id, UserData.from_api(user.data))

    def __dict__(self):
        return {"data": self.data.__dict__(), "peer": self.peer.__dict__()}

    def __str__(self):
        return "User({})".format(self.__dict__())
