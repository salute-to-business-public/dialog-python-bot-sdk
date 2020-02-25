from dialog_api.peers_pb2 import Peer, PEERTYPE_GROUP, PEERTYPE_PRIVATE, OutPeer
from dialog_api.search_pb2 import RequestPeerSearch, ResponsePeerSearch, PeerSearchResult, RequestResolvePeer, \
    ResponseResolvePeer
from dialog_api.users_pb2 import User, UserData
from google.protobuf.wrappers_pb2 import StringValue


class Search:
    def PeerSearch(self, request: RequestPeerSearch) -> ResponsePeerSearch:
        return ResponsePeerSearch(users=[],
                                  groups=[],
                                  search_results=[PeerSearchResult(peer=Peer(id=1, type=PEERTYPE_GROUP),
                                                  shortname=StringValue(value="short_name"))],
                                  user_peers=[],
                                  group_peers=[])

    def ResolvePeer(self, request: RequestResolvePeer) -> ResponseResolvePeer:
        if request.shortname == "nick":
            return ResponseResolvePeer(peer=OutPeer(id=1, access_hash=1, type=PEERTYPE_PRIVATE))
        else:
            return ResponseResolvePeer(peer=OutPeer(id=0, access_hash=0, type=PEERTYPE_PRIVATE))
