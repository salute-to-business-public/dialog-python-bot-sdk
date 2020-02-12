from dialog_api import peers_pb2
from dialog_api.peers_pb2 import PEERTYPE_PRIVATE, PEERTYPE_GROUP, PEERTYPE_UNKNOWN, PEERTYPE_ENCRYPTEDPRIVATE, \
    PEERTYPE_SIP


class PeerType:
    PEERTYPE_UNKNOWN = PEERTYPE_UNKNOWN
    PEERTYPE_PRIVATE = PEERTYPE_PRIVATE
    PEERTYPE_GROUP = PEERTYPE_GROUP
    PEERTYPE_ENCRYPTEDPRIVATE = PEERTYPE_ENCRYPTEDPRIVATE
    PEERTYPE_SIP = PEERTYPE_SIP


class Peer:
    def __init__(self, id: int, type: PeerType) -> None:
        self.id = id
        self.type = type

    def to_api(self) -> peers_pb2.Peer:
        return peers_pb2.Peer(id=self.id, type=self.type)

    @classmethod
    def from_api(cls, peer: peers_pb2.Peer) -> 'Peer':
        return cls(peer.id, peer.type)

    def __dict__(self):
        return {"id": self.id, "type": PeerTypeMap.self.type}

    def __str__(self):
        return "Peer({})".format(self.__dict__())
