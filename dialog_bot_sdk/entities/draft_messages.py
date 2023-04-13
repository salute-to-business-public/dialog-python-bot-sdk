from typing import List

from dialog_api import draft_messages_pb2

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.messaging import MessageContent
from dialog_bot_sdk.entities.peers import Peer


class DraftMessageStatus:
    DRAFT_MESSAGE_UNKNOWN = draft_messages_pb2.DRAFT_MESSAGE_UNKNOWN
    DRAFT_MESSAGE_SAVED = draft_messages_pb2.DRAFT_MESSAGE_SAVED
    DRAFT_MESSAGE_DELETED = draft_messages_pb2.DRAFT_MESSAGE_DELETED
    DRAFT_MESSAGE_REJECTED = draft_messages_pb2.DRAFT_MESSAGE_REJECTED
    DRAFT_MESSAGE_FAILED = draft_messages_pb2.DRAFT_MESSAGE_FAILED


class DraftMessage:
    def __init__(self, message: MessageContent, forward: List[UUID], reply: List[UUID], clock: int) -> None:
        self.message = message
        self.forward = forward
        self.reply = reply
        self.clock = clock

    @classmethod
    def from_api(cls, draft_message: draft_messages_pb2.DraftMessage) -> 'DraftMessage':
        return cls(
            MessageContent.from_api(draft_message.message),
            [UUID.from_api(x) for x in draft_message.forward.mids],
            [UUID.from_api(x) for x in draft_message.reply.mids],
            draft_message.clock,
        )

    def __dict__(self):
        return {
            "message": self.message.__dict__(),
            "forward": [x.__dict__() for x in self.forward],
            "reply": [x.__dict__() for x in self.reply],
            "clock": self.clock,
        }

    def __str__(self):
        return "DraftMessage({})".format(self.__dict__())


class UpdateDraftMessageChanged:
    def __init__(self, status: DraftMessageStatus, peer: Peer, message: DraftMessage) -> None:
        self.status = status
        self.peer = peer
        self.message = message

    @classmethod
    def from_api(cls, update: draft_messages_pb2.UpdateDraftMessageChanged) -> 'UpdateDraftMessageChanged':
        return cls(
            update.status,
            Peer.from_api(update.peer),
            DraftMessage.from_api(update.message),
        )

    def __dict__(self):
        return {
            "status": self.status,
            "peer": self.peer.__dict__(),
            "message": self.message.__dict__(),
        }

    def __str__(self):
        return "UpdateDraftMessageChanged({})".format(self.__dict__())
