from dialog_api.presence_pb2 import RequestGetUserLastPresence, RequestStartTyping, RequestStopTyping, \
    ResponseUserLastPresence, RequestSetOnline
from google.protobuf.timestamp_pb2 import Timestamp

from tests.fixtures.client_entities import rnd


class Presence:
    def GetUserLastPresence(self, request: RequestGetUserLastPresence) -> ResponseUserLastPresence:
        return ResponseUserLastPresence(last_online_at=Timestamp(seconds=rnd(), nanos=rnd()))

    def StartTyping(self, request: RequestStartTyping) -> None:
        pass

    def StopTyping(self, request: RequestStopTyping) -> None:
        pass

    def SetOnline(self, request: RequestSetOnline) -> None:
        pass
