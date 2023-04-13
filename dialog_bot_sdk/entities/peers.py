from dialog_api import peers_pb2
from dialog_api.peers_pb2 import PEERTYPE_PRIVATE, PEERTYPE_GROUP, PEERTYPE_UNKNOWN, PEERTYPE_ENCRYPTEDPRIVATE, \
    PEERTYPE_SIP, PEERTYPE_THREAD


class PeerType:
    PEERTYPE_UNKNOWN = PEERTYPE_UNKNOWN
    PEERTYPE_PRIVATE = PEERTYPE_PRIVATE
    PEERTYPE_GROUP = PEERTYPE_GROUP
    PEERTYPE_ENCRYPTEDPRIVATE = PEERTYPE_ENCRYPTEDPRIVATE
    PEERTYPE_SIP = PEERTYPE_SIP
    PEERTYPE_THREAD = PEERTYPE_THREAD


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
        return {"id": self.id, "type": self.type}

    def __str__(self):
        return "Peer({})".format(self.__dict__())

    def __eq__(self, other):
        if self.id == other.id and self.type == other.type:
            return True
        return False


class OutPeer:
    def __init__(self, id: int, type: PeerType, access_hash: int) -> None:
        self.id = id
        self.type = type
        self.access_hash = access_hash

    def to_api(self) -> peers_pb2.OutPeer:
        return peers_pb2.OutPeer(id=self.id, type=self.type, access_hash=self.access_hash)

    @classmethod
    def from_api(cls, peer: peers_pb2.OutPeer) -> 'OutPeer':
        return cls(peer.id, peer.type, peer.access_hash)

    def __dict__(self):
        return {"id": self.id, "type": self.type, "access_hash": self.access_hash}

    def __str__(self):
        return "OutPeer({})".format(self.__dict__())

    def __eq__(self, other):
        if self.id == other.id and self.type == other.type and self.access_hash == other.access_hash:
            return True
        return False


class GroupOutPeer:
    def __init__(self, group_id: int, access_hash: int) -> None:
        self.group_id = group_id
        self.access_hash = access_hash

    def to_api(self) -> peers_pb2.GroupOutPeer:
        return peers_pb2.OutPeer(group_id=self.group_id, access_hash=self.access_hash)

    @classmethod
    def from_api(cls, peer: peers_pb2.GroupOutPeer) -> 'GroupOutPeer':
        return cls(peer.group_id, peer.access_hash)

    def __dict__(self):
        return {"group_id": self.group_id, "access_hash": self.access_hash}

    def __str__(self):
        return "GroupOutPeer({})".format(self.__dict__())


class UserOutPeer:
    def __init__(self, uid: int, access_hash: int) -> None:
        self.uid = uid
        self.access_hash = access_hash

    def to_api(self) -> peers_pb2.UserOutPeer:
        return peers_pb2.UserOutPeer(uid=self.uid, access_hash=self.access_hash)

    @classmethod
    def from_api(cls, peer: peers_pb2.UserOutPeer) -> 'UserOutPeer':
        return cls(peer.uid, peer.access_hash)

    def __dict__(self):
        return {"uid": self.uid, "access_hash": self.access_hash}

    def __str__(self):
        return "UserOutPeer({})".format(self.__dict__())
