from dialog_api.definitions_pb2 import UUIDValue
from dialog_api.messaging_pb2 import RequestLoadDialogs, ResponseLoadDialogs, RequestSendMessage, ResponseSendMessage, \
    RequestUpdateMessage, RequestMessageRead, RequestLoadHistory, HistoryMessage, ResponseLoadHistory
from dialog_api.peers_pb2 import UserOutPeer
from google.protobuf.wrappers_pb2 import Int64Value


class Messaging:
    def LoadDialogs(self, request: RequestLoadDialogs) -> ResponseLoadDialogs:
        return ResponseLoadDialogs(user_peers=[UserOutPeer(uid=1, access_hash=1)])

    def SendMessage(self, request: RequestSendMessage) -> ResponseSendMessage:
        return ResponseSendMessage(message_id=UUIDValue(msb=1, lsb=1))

    def UpdateMessage(self, request: RequestUpdateMessage) -> None:
        pass

    def MessageRead(self, request: RequestMessageRead) -> None:
        pass

    def LoadHistory(self, request: RequestLoadHistory) -> ResponseLoadHistory:
        return ResponseLoadHistory(history=[HistoryMessage(mid=None, prev_mid=None, sender_peer=None, message=None,
                                                           date=0, forward=None,
                                                           reply=None, edited_at=Int64Value(value=0))],
                                   )
