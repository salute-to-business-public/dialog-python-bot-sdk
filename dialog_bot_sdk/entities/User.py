from dialog_api import users_pb2
from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.peers.OutPeer import OutPeer
from dialog_bot_sdk.entities.peers.Peer import PeerType


class UserData:
    def __init_(self, name: str, avatar: Avatar, about: str, nick: str) -> None:
        self.name = name
        self.avatar = avatar
        self.about = about
        self.nick = nick

    @classmethod
    def from_api(cls, data: users_pb2.UserData) -> 'UserData':
        return cls(data.name, Avatar.from_api(data.avatar), data.about.value, data.nick.value)


class User:
    def __init__(self, id_: int, access_hash: int, user_data: UserData) -> None:
        self.id = id_
        self.access_hash = access_hash
        self.user_data = user_data
        self.out_peer = OutPeer(self.id, self.access_hash, PeerType.PEERTYPE_PRIVATE)

    @classmethod
    def from_api(cls, user: users_pb2.User) -> 'User':
        return cls(user.id, user.access_hash, UserData.from_api(user.data))
