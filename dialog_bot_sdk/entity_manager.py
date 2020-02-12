from dialog_bot_sdk.entities.Peer import Peer, PeerType
from dialog_bot_sdk.exceptions.exceptions import UnknownPeerError
from dialog_bot_sdk.internal.bot import InternalBot

from dialog_api import peers_pb2, messaging_pb2


class EntityManager(object):
    """Entity manager class.

    Add OutPeer's to dict when bot receive a message, to avoid going to the server once again.
    """
    def __init__(self, internal: InternalBot) -> None:
        self.internal = internal
        self.peer_to_out_peer = {}

    def get_out_peer(self, peer: Peer or peers_pb2.Peer) -> peers_pb2.OutPeer or None:
        """Returns OutPeer for given Peer.

        :param peer: Peer object
        :return: OutPeer object
        """
        if isinstance(peer, Peer):
            peer = peer.to_api()
        if not isinstance(peer, peers_pb2.Peer):
            raise RuntimeError("Invalid input data. Expects {}, got {}.".format(Peer.__class__, type(peer)))
        result = self.peer_to_out_peer.get((peer.type, peer.id))
        if result is None:
            req = messaging_pb2.RequestLoadDialogs(
                min_date=0,
                limit=1,
                peers_to_load=[peer],
            )
            result = self.internal.messaging.LoadDialogs(req)
            for user in result.user_peers:
                self.__adopt_peer(user)
            for group in result.group_peers:
                self.__adopt_peer(group)
            return self.peer_to_out_peer.get((peer.type, peer.id))
        return result

    def __adopt_peer(self, peer: peers_pb2.UserOutPeer or peers_pb2.GroupOutPeer) -> None:
        """Find outpeer for given peer and store it in internal peers_to_outpeers dict.

        :param peer: Peer object (UserOutPeer or GroupOutPeer)
        """
        if isinstance(peer, peers_pb2.UserOutPeer):
            out_peer = peers_pb2.OutPeer(id=peer.uid, access_hash=peer.access_hash, type=PeerType.PEERTYPE_PRIVATE)
        elif isinstance(peer, peers_pb2.GroupOutPeer):
            out_peer = peers_pb2.OutPeer(id=peer.group_id, access_hash=peer.access_hash, type=PeerType.PEERTYPE_GROUP)
        else:
            raise UnknownPeerError("Unknown PeerType.")
        self.peer_to_out_peer[(out_peer.type, out_peer.id)] = out_peer

    def add_out_peer(self, out_peer: peers_pb2.OutPeer) -> None:
        self.peer_to_out_peer.get((out_peer.type, out_peer.id))
