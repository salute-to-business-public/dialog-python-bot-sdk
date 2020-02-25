from typing import List

from dialog_api.definitions_pb2 import UUIDValue
from dialog_api.messaging_pb2 import RequestLoadDialogs, ResponseLoadDialogs, RequestSendMessage, ResponseSendMessage, \
    RequestUpdateMessage, RequestMessageRead, RequestLoadHistory, HistoryMessage
from dialog_api.peers_pb2 import UserOutPeer
from dialog_api.users_pb2 import User, UserData
from google.protobuf.wrappers_pb2 import StringValue, Int64Value


class Messaging:
    def LoadDialogs(self, request: RequestLoadDialogs) -> ResponseLoadDialogs:
        return ResponseLoadDialogs(user_peers=[UserOutPeer(uid=1, access_hash=1)])

    def SendMessage(self, request: RequestSendMessage) -> ResponseSendMessage:
        return ResponseSendMessage(message_id=UUIDValue(msb=1, lsb=1))

    def UpdateMessage(self, request: RequestUpdateMessage) -> None:
        pass

    def MessageRead(self, request: RequestMessageRead) -> None:
        pass

    def LoadHistory(self, request: RequestLoadHistory) -> List[HistoryMessage]:
        return [HistoryMessage(mid=None, prev_mid=None, sender_peer=None, message=None, date=0, forward=None,
                               reply=None, edited_at=Int64Value(value=0))]
