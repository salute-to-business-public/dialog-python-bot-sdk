from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.Peer import Peer, PeerType
from dialog_bot_sdk.entities.UUID import UUID


class UpdateInteractiveMediaEvent:
    def __init__(self, mid: UUID, id_: str, value: str, peer: Peer) -> None:
        self.mid = mid
        self.id = id_
        self.value = value
        self.peer = peer

    @classmethod
    def from_api(cls, event: messaging_pb2.UpdateInteractiveMediaEvent) -> 'UpdateInteractiveMediaEvent':
        return cls(UUID.from_api(event.mid), event.id, event.value, Peer(event.uid, PeerType.PEERTYPE_PRIVATE))

    def __dict__(self):
        return {"mid": self.mid.__str__(), "id": self.id, "value": self.value, "peer": self.peer.__dict__()}

    def __str__(self):
        return "UpdateInteractiveMediaEvent({})".format(self.__dict__())
