from typing import List

from dialog_bot_sdk.entities.Peer import PeerType, Peer
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.message.DocumentMessage import DocumentMessage
from dialog_bot_sdk.entities.message.ServiceMessage import ServiceMessage
from dialog_bot_sdk.entities.message.TextMessage import TextMessage
from dialog_api import messaging_pb2


class DeletedMessage:
    def __init__(self, is_local: bool) -> None:
        self.is_local = is_local

    @classmethod
    def from_api(cls, deleted: messaging_pb2.DeletedMessage) -> 'DeletedMessage':
        return cls(deleted.is_local)

    def __dict__(self):
        return {"is_local": self.is_local}

    def __str__(self):
        return "DeleteMessage({})".format(self.__dict__())


class JsonMessage:
    def __init__(self, raw_json: str) -> None:
        self.raw_json = raw_json

    @classmethod
    def from_api(cls, json_: messaging_pb2.JsonMessage) -> 'JsonMessage':
        return cls(json_.raw_json)

    def __dict__(self):
        return {"raw_json": self.raw_json}

    def __str__(self):
        return "JsonMessage({})".format(self.__dict__())


class MessageContent:
    def __init__(self, deleted: DeletedMessage, document: DocumentMessage, json_: JsonMessage,
                 service: ServiceMessage, text: TextMessage) -> None:
        self.deleted_message = deleted
        self.document_message = document
        self.json_message = json_
        self.service_message = service
        self.text_message = text

    @classmethod
    def from_api(cls, content: messaging_pb2.MessageContent) -> 'MessageContent':
        return cls(DeletedMessage.from_api(content.deletedMessage), DocumentMessage.from_api(content.documentMessage),
                   JsonMessage.from_api(content.jsonMessage), ServiceMessage.from_api(content.serviceMessage),
                   TextMessage.from_api(content.textMessage))

    def __dict__(self):
        return {"deleted_message": self.deleted_message.__dict__(), "document_message": self.document_message.__dict__(),
                "json_message": self.json_message.__dict__(),
                "service_message": self.service_message.__dict__(), "text_message": self.text_message.__dict__()}

    def __str__(self):
        return "MessageContent({})".format(self.__dict__())


class Message:
    def __init__(self, mid: UUID, prev_mid: UUID, sender_peer: Peer, message: MessageContent, reply: List[UUID],
                 forward: List[UUID], date: int, edited_at: int) -> None:
        self.mid = mid
        self.prev_mid = prev_mid
        self.sender_peer = sender_peer
        self.message = message
        self.reply = reply
        self.forward = forward
        self.date = date
        self.edited_at = edited_at

    @classmethod
    def from_api(cls, message: messaging_pb2.HistoryMessage) -> 'Message':
        return cls(UUID.from_api(message.mid), UUID.from_api(message.prev_mid),
                   Peer(message.sender_peer.id, PeerType.PEERTYPE_PRIVATE),
                   MessageContent.from_api(message.message), [UUID.from_api(x.mid) for x in message.reply],
                   [UUID.from_api(x.mid) for x in message.forward], message.date, message.edited_at.value)

    def __dict__(self):
        return {"mid": self.mid.__str__(), "prev_mid": self.prev_mid.__str__(),
                "sender_peer": self.sender_peer.__dict__(),
                "message": self.message.__dict__(), "reply": [x.__str__() for x in self.reply],
                "forward": [x.__str__() for x in self.forward], "date": self.date, "edited_at": self.edited_at}

    def __str__(self):
        return "Message({})".format(self.__dict__())
