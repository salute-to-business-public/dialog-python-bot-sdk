from dialog_api.reactions_pb2 import GetReactionsRequest, GetReactionsResponse, GetMessageReactionsResponse, \
    GetMessageReactionsRequest, RequestRemoveMessageReaction, RequestSetMessageReaction

from tests.fixtures.client_entities import rnd
from tests.fixtures.server_entities import message_reactions


class Reactions:
    def GetReactions(self, request: GetReactionsRequest) -> GetReactionsResponse:
        return GetReactionsResponse(messageReactions=[message_reactions], peer_clock=rnd(), next_available=True)

    def GetMessageReactions(self, request: GetMessageReactionsRequest) -> GetMessageReactionsResponse:
        return GetMessageReactionsResponse(messageReactions=[message_reactions])

    def MessageRemoveReaction(self, request: RequestRemoveMessageReaction) -> None:
        pass

    def MessageSetReaction(self, request: RequestSetMessageReaction) -> None:
        pass
