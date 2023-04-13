from typing import List

from dialog_api import presence_pb2
from dialog_api.presence_pb2 import DEVICETYPE_UNKNOWN, DEVICETYPE_GENERIC, DEVICETYPE_PC, DEVICETYPE_MOBILE, \
    DEVICETYPE_TABLET, DEVICETYPE_WATCH, DEVICETYPE_MIRROR, DEVICETYPE_CAR, DEVICETYPE_TABLE
from dialog_api.presence_pb2 import TYPINGTYPE_UNKNOWN, TYPINGTYPE_TEXT, TYPINGTYPE_VOICE

from dialog_bot_sdk.entities.peers import Peer, PeerType


class DeviceType:
    DEVICETYPE_UNKNOWN = DEVICETYPE_UNKNOWN
    DEVICETYPE_GENERIC = DEVICETYPE_GENERIC
    DEVICETYPE_PC = DEVICETYPE_PC
    DEVICETYPE_MOBILE = DEVICETYPE_MOBILE
    DEVICETYPE_TABLET = DEVICETYPE_TABLET
    DEVICETYPE_WATCH = DEVICETYPE_WATCH
    DEVICETYPE_MIRROR = DEVICETYPE_MIRROR
    DEVICETYPE_CAR = DEVICETYPE_CAR
    DEVICETYPE_TABLE = DEVICETYPE_TABLE


class TypingType:
    TYPINGTYPE_UNKNOWN = TYPINGTYPE_UNKNOWN
    TYPINGTYPE_TEXT = TYPINGTYPE_TEXT
    TYPINGTYPE_VOICE = TYPINGTYPE_VOICE


class UserTyping:
    def __init__(self, peer: Peer, typing_type: TypingType) -> None:
        self.peer = peer
        self.typing_type = typing_type

    @classmethod
    def from_api(cls, typing: presence_pb2.UpdateGroupTyping.UserTyping) -> 'UserTyping':
        return cls(Peer(typing.user_id, PeerType.PEERTYPE_PRIVATE), typing.typing_type)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "typing_type": self.typing_type}

    def __str__(self):
        return "UpdateTyping({})".format(self.__dict__())


# updates
class UpdateTyping:
    def __init__(self, peer: Peer, user_peer: Peer, typing_type: TypingType) -> None:
        self.peer = peer
        self.user_peer = user_peer
        self.typing_type = typing_type

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateTyping) -> 'UpdateTyping':
        return cls(Peer.from_api(update.peer), Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.typing_type)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "user_peer": self.user_peer.__dict__(), "typing_type": self.typing_type}

    def __str__(self):
        return "UpdateTyping({})".format(self.__dict__())


class UpdateTypingStop:
    def __init__(self, peer: Peer, user_peer: Peer, typing_type: TypingType) -> None:
        self.peer = peer
        self.user_peer = user_peer
        self.typing_type = typing_type

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateTypingStop) -> 'UpdateTypingStop':
        return cls(Peer.from_api(update.peer), Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.typing_type)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "user_peer": self.user_peer.__dict__(), "typing_type": self.typing_type}

    def __str__(self):
        return "UpdateTypingStop({})".format(self.__dict__())


class UpdateUserOnline:
    def __init__(self, peer: Peer, device_type: DeviceType) -> None:
        self.peer = peer
        self.device_type = device_type

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateUserOnline) -> 'UpdateUserOnline':
        return cls(Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.device_type)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "device_type": self.device_type}

    def __str__(self):
        return "UpdateUserOnline({})".format(self.__dict__())


class UpdateUserOffline:
    def __init__(self, peer: Peer, device_type: DeviceType) -> None:
        self.peer = peer
        self.device_type = device_type

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateUserOffline) -> 'UpdateUserOffline':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.device_type)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "device_type": self.device_type}

    def __str__(self):
        return "UpdateUserOffline({})".format(self.__dict__())


class UpdateUserLastSeen:
    def __init__(self, peer: Peer, last_seen_at: int, device_type: DeviceType, current_time: int) -> None:
        self.peer = peer
        self.last_seen_at = last_seen_at
        self.device_type = device_type
        self.current_time = current_time

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateUserLastSeen) -> 'UpdateUserLastSeen':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.last_seen_at, update.device_type, update.current_time)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "last_seen_at": self.last_seen_at,
            "device_type": self.device_type,
            "current_time": self.current_time
        }

    def __str__(self):
        return "UpdateUserLastSeen({})".format(self.__dict__())


class UpdateGroupOnline:
    def __init__(self, peer: Peer, count: int, user_peers: List[Peer]) -> None:
        self.peer = peer
        self.count = count
        self.user_peers = user_peers

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateGroupOnline) -> 'UpdateGroupOnline':
        return cls(Peer(update.group_id, PeerType.PEERTYPE_GROUP), update.count,
                   [Peer(x, PeerType.PEERTYPE_PRIVATE) for x in update.users_id])

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "count": self.count,
            "user_peers": [x.__dict__() for x in self.user_peers],
        }

    def __str__(self):
        return "UpdateGroupOnline({})".format(self.__dict__())


class UpdateGroupTyping:
    def __init__(self, peer: Peer, users_typing: List[UserTyping]) -> None:
        self.peer = peer
        self.users_typing = users_typing

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateGroupTyping) -> 'UpdateGroupTyping':
        return cls(Peer(update.group_id, PeerType.PEERTYPE_GROUP), [UserTyping.from_api(x) for x in update.users_typing])

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "users_typing": [x.__dict__() for x in self.users_typing],
        }

    def __str__(self):
        return "UpdateGroupTyping({})".format(self.__dict__())


class UpdateThreadTyping:
    def __init__(self, peer: Peer, users_typing: List[UserTyping]) -> None:
        self.peer = peer
        self.users_typing = users_typing

    @classmethod
    def from_api(cls, update: presence_pb2.UpdateThreadTyping) -> 'UpdateThreadTyping':
        return cls(Peer(update.thread_id, PeerType.PEERTYPE_THREAD), [UserTyping.from_api(x) for x in update.users_typing])

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "users_typing": [x.__dict__() for x in self.users_typing],
        }

    def __str__(self):
        return "UpdateThreadTyping({})".format(self.__dict__())
