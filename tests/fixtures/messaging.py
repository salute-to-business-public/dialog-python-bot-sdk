from dialog_api.messaging_pb2 import RequestLoadDialogs, ResponseLoadDialogs, RequestSendMessage, ResponseSendMessage, \
    RequestUpdateMessage, RequestMessageRead, RequestLoadHistory, ResponseLoadHistory
from tests.fixtures.server_entities import user_outpeer, group_outpeer, mid, history_message


class Messaging:
    def LoadDialogs(self, request: RequestLoadDialogs) -> ResponseLoadDialogs:
        response = ResponseLoadDialogs(user_peers=[user_outpeer], group_peers=[group_outpeer])
        return response

    def SendMessage(self, request: RequestSendMessage) -> ResponseSendMessage:
        response = ResponseSendMessage(message_id=mid)
        return response

    def UpdateMessage(self, request: RequestUpdateMessage) -> None:
        pass

    def MessageRead(self, request: RequestMessageRead) -> None:
        pass

    def LoadHistory(self, request: RequestLoadHistory) -> ResponseLoadHistory:
        return ResponseLoadHistory(history=[history_message])
