from dialog_api import peers_pb2


class PeerType:
    PEERTYPE_UNKNOWN = 0
    PEERTYPE_PRIVATE = 1
    PEERTYPE_GROUP = 2
    PEERTYPE_ENCRYPTEDPRIVATE = 3
    PEERTYPE_SIP = 4


class Peer:
    def __init__(self, id_: int, type_: PeerType) -> None:
        self.id = id_
        self.type = type_

    def to_api(self) -> peers_pb2.Peer:
        return peers_pb2.Peer(id=self.id, type=self.type)

    @classmethod
    def from_api(cls, peer: peers_pb2.Peer) -> 'Peer':
        return cls(peer.id, peer.type)

    def __dict__(self):
        return {"id": self.id, "type": self.type}

    def __str__(self):
        return "{}".format(self.__dict__())
