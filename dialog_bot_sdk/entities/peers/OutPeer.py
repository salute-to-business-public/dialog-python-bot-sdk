from dialog_api import peers_pb2

from dialog_bot_sdk.entities.peers.Peer import PeerType


class OutPeer:
    def __init__(self, id_: int, access_hash: int, type_: PeerType) -> None:
        self.id = id_
        self.access_hash = access_hash
        self.type = type_

    def to_api(self) -> peers_pb2.OutPeer:
        return peers_pb2.OutPeer(id=self.id, access_hash=self.access_hash, type=self.type)

    @classmethod
    def from_api(cls, out_peer: peers_pb2.OutPeer) -> 'OutPeer':
        return cls(out_peer.id, out_peer.access_hash, out_peer.type)
