from dialog_api import privacy_pb2
from dialog_bot_sdk.entities.peers import Peer, PeerType


# updates
class UpdateUserBlocked:
    def __init__(self, peer: Peer) -> None:
        self.peer = peer

    @classmethod
    def from_api(cls, update: privacy_pb2.UpdateUserBlocked) -> 'UpdateUserBlocked':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE))

    def __dict__(self):
        return {"peer": self.peer}

    def __str__(self):
        return "UpdateUserBlocked({})".format(self.__dict__())


class UpdateUserUnblocked:
    def __init__(self, peer: Peer) -> None:
        self.peer = peer

    @classmethod
    def from_api(cls, update: privacy_pb2.UpdateUserUnblocked) -> 'UpdateUserUnblocked':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE))

    def __dict__(self):
        return {"peer": self.peer}

    def __str__(self):
        return "UpdateUserUnblocked({})".format(self.__dict__())
