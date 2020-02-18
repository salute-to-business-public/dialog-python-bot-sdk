from typing import List

from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.Peer import Peer, PeerType
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.message.Message import MessageContent


class UpdateMessage:
    def __init__(self, peer: Peer, sender_peer: Peer, mid: UUID, message: MessageContent, forward: List[UUID],
                 reply: List[UUID], previous_mid: UUID, date: int) -> None:
        self.peer = peer
        self.sender_peer = sender_peer
        self.mid = mid
        self.message = message
        self.forward = forward
        self.reply = reply
        self.previous_mid = previous_mid
        self.date = date

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessage) -> 'UpdateMessage':
        return cls(Peer.from_api(update.peer), Peer(update.sender_uid, PeerType.PEERTYPE_PRIVATE),
                   UUID.from_api(update.mid), MessageContent.from_api(update.message),
                   [UUID.from_api(x) for x in update.forward.mids], [UUID.from_api(x) for x in update.reply.mids],
                   UUID.from_api(update.previous_mid), update.date)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "sender_peer": self.sender_peer.__dict__(),
                "mid": self.mid.__str__(), "message": self.message.__dict__(),
                "forward": [x.__str__() for x in self.forward], "reply": [x.__str__() for x in self.reply],
                "previous_mid": self.previous_mid.__str__(), "date": self.date}

    def __str__(self):
        return "UpdateMessage({})".format(self.__dict__())
