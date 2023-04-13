from dialog_api.peers_pb2 import PEERTYPE_PRIVATE, OutPeer
from dialog_api.search_pb2 import RequestPeerSearch, ResponsePeerSearch, RequestResolvePeer, ResponseResolvePeer
from tests.fixtures.server_entities import user, group, search_result, user_outpeer, group_outpeer, uop


class Search:
    def PeerSearch(self, request: RequestPeerSearch) -> ResponsePeerSearch:
        return ResponsePeerSearch(users=[user],
                                  groups=[group],
                                  search_results=search_result,
                                  user_peers=[user_outpeer],
                                  group_peers=[group_outpeer])

    def ResolvePeer(self, request: RequestResolvePeer) -> ResponseResolvePeer:
        if request.shortname == "nick":
            return ResponseResolvePeer(peer=uop)
        else:
            return ResponseResolvePeer(peer=OutPeer(id=0, access_hash=0, type=PEERTYPE_PRIVATE))
