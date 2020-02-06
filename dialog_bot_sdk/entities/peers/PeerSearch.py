from typing import List

from dialog_api import search_pb2

from dialog_bot_sdk.entities.peers.OutPeer import OutPeer
from dialog_bot_sdk.entities.peers.Peer import Peer, PeerType


class PeerSearchResult:
    def __init__(self, peer: Peer, title: str, shortname: str, description: str, members_count: int,
                 creator: int) -> None:
        self.peer = peer
        self.title = title
        self.shortname = shortname
        self.description = description
        self.members_count = members_count
        self.creator = creator

    @classmethod
    def from_api(cls, result: search_pb2.PeerSearchResult) -> 'PeerSearchResult':
        return cls(Peer.from_api(result.peer), result.title, result.shortname.value, result.description.value,
                   result.members_count.value, result.creator.value)


class PeerSearch:
    def __init__(self, search_results: List[PeerSearchResult], user_peers: List[OutPeer],
                 group_peers: List[OutPeer]) -> None:
        self.search_results = search_results
        self.user_peers = user_peers
        self.group_peers = group_peers

    @classmethod
    def from_api(cls, search: search_pb2.ResponsePeerSearch) -> 'PeerSearch':
        return cls([PeerSearchResult.from_api(x) for x in search.search_results],
                   [OutPeer(x.uid, x.access_hash, PeerType.PEERTYPE_PRIVATE) for x in search.user_peers],
                   [OutPeer(x.group_id, x.access_hash, PeerType.PEERTYPE_GROUP) for x in search.group_peers])
