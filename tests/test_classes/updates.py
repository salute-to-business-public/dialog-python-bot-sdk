from dialog_api.groups_pb2 import Group
from dialog_api.messaging_pb2 import HistoryMessage
from dialog_api.sequence_and_updates_pb2 import RequestGetReferencedEntitites, ResponseGetReferencedEntitites, \
    ResponseGetDifference, RequestGetDifference, RequestGetState
from dialog_api.users_pb2 import UserData, User
from google.protobuf.wrappers_pb2 import StringValue, Int64Value


class ResponseGetState(object):
    def __init__(self, seq: int) -> None:
        self.seq = seq


class Updates:
    def GetReferencedEntitites(self, request: RequestGetReferencedEntitites) -> ResponseGetReferencedEntitites:
        return ResponseGetReferencedEntitites(groups=[Group(id=1, access_hash=1, data=None)],
                                              users=[User(id=1, access_hash=1, data=UserData(nick=StringValue(value="nick")))],
                                              messages=[HistoryMessage(mid=None, prev_mid=None, sender_peer=None,
                                                                       message=None, date=0, forward=None, reply=None,
                                                                       edited_at=Int64Value(value=0))])

    def GetDifference(self, request: RequestGetDifference) -> ResponseGetDifference:
        return ResponseGetDifference(seq=0)

    def GetState(self, request: RequestGetState) -> ResponseGetState:
        return ResponseGetState(0)
