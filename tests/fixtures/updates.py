from dialog_api.miscellaneous_pb2 import ResponseSeq
from dialog_api.sequence_and_updates_pb2 import RequestGetReferencedEntitites, ResponseGetReferencedEntitites, \
    ResponseGetDifference, RequestGetDifference, RequestGetState

from tests.fixtures.server_entities import group, user, history_message


class Updates:
    def GetReferencedEntitites(self, request: RequestGetReferencedEntitites) -> ResponseGetReferencedEntitites:
        response = ResponseGetReferencedEntitites(groups=[group], users=[user], messages=[history_message])
        return response

    def GetDifference(self, request: RequestGetDifference) -> ResponseGetDifference:
        return ResponseGetDifference(seq=0)

    def GetState(self, request: RequestGetState) -> ResponseSeq:
        return ResponseSeq(seq=0)
