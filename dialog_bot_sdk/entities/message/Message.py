from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.message.DocumentMessage import DocumentMessage
from dialog_bot_sdk.entities.message.ServiceMessage import ServiceMessage
from dialog_bot_sdk.entities.message.TextMessage import TextMessage
from dialog_bot_sdk.entities.peers.OutPeer import OutPeer
from dialog_api import messaging_pb2


class DeletedMessage:
    def __init__(self, is_local: bool) -> None:
        self.is_local = is_local

    @classmethod
    def from_api(cls, deleted: messaging_pb2.DeletedMessage) -> 'DeletedMessage':
        return cls(deleted.is_local)


class JsonMessage:
    def __init__(self, row_json: str) -> None:
        self.row_json = row_json

    @classmethod
    def from_api(cls, json_: messaging_pb2.JsonMessage) -> 'JsonMessage':
        return cls(json_.row_json)


class MessageContent:
    def __init__(self, deleted: DeletedMessage, document: DocumentMessage, json_: JsonMessage,
                 service: ServiceMessage, text: TextMessage) -> None:
        self.deletedMessage = deleted
        self.documentMessage = document
        self.jsonMessage = json_
        self.serviceMessage = service
        self.textMessage = text

    @classmethod
    def from_api(cls, content: messaging_pb2.MessageContent) -> 'MessageContent':
        return cls(DeletedMessage.from_api(content.deletedMessage), DocumentMessage.from_api(content.documentMessage),
                   JsonMessage.from_api(content.jsonMessage), ServiceMessage.from_api(content.serviceMessage),
                   TextMessage.from_api(content.textMessage))


class Message:
    def __init__(self, mid: UUID, prev_mid: UUID, sender_peer: OutPeer, message: MessageContent, reply: list,
                 forward: list, date: int, edited_at: int) -> None:
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
        return cls(UUID.from_api(message.mid), UUID.from_api(message.prev_mid), OutPeer.from_api(message.sender_peer),
                   MessageContent.from_api(message.message), [UUID.from_api(x.mid) for x in message.reply],
                   [UUID.from_api(x.mid) for x in message.forward], message.date, message.edited_at.value)
