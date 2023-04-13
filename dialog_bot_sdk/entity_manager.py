import sched
import time
from concurrent.futures.thread import ThreadPoolExecutor
from dialog_bot_sdk.entities.messaging import Message
from dialog_bot_sdk.entities.authentication import UserInfo
from dialog_api.messaging_pb2 import UpdateInteractiveMediaEvent, UpdateMessage
from dialog_api.peers_pb2 import PEERTYPE_GROUP, PEERTYPE_PRIVATE, GroupOutPeer, PEERTYPE_THREAD
from dialog_api.sequence_and_updates_pb2 import RequestGetReferencedEntitites
from dialog_api.users_pb2 import RequestLoadUserData
from dialog_bot_sdk.entities.peers import Peer
from dialog_bot_sdk.exceptions.exceptions import UnknownPeerError
from dialog_bot_sdk.internal.bot import InternalBot
from dialog_api import peers_pb2, sequence_and_updates_pb2


class EntityManager(object):
    """Entity manager class.

    Add OutPeer's to dict when bot receive a message, to avoid going to the server once again.
    """
    def __init__(
        self, internal: InternalBot, update_pool: ThreadPoolExecutor, methods_pool: ThreadPoolExecutor,
        user_info: UserInfo, logger_config: dict
    ) -> None:
        self.internal = internal
        self.update_pool = update_pool
        self.methods_pool = methods_pool
        self.user_info = user_info
        self.peer_to_out_peer = {}
        self.commands = {}
        self.events = {}
        self.messages = {}
        self.messages_changed = {}
        self.updates = {}
        self.sleep = False
        self.run = False
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.stop_updates_uids = []
        self.logger_config = logger_config

    def get_out_peer(self, peer: Peer or peers_pb2.Peer) -> peers_pb2.OutPeer or None:
        """Returns OutPeer for given Peer.

        :param peer: Peer
        :return: OutPeer
        """
        if isinstance(peer, Peer):
            peer = peer.to_api()

        if not isinstance(peer, peers_pb2.Peer):
            raise RuntimeError("Invalid input data. Expects {}, got {}.".format(Peer.__class__, type(peer)))

        result = self.peer_to_out_peer.get((peer.type, peer.id))

        if result is None:
            if peer.type == PEERTYPE_GROUP:
                return self.__get_group_out_peer(peer)
            elif peer.type == PEERTYPE_PRIVATE:
                return self.__get_user_out_peer(peer)
            elif peer.type == PEERTYPE_THREAD:
                return self.peer_to_out_peer.get((peer.type, peer.id))
            else:
                raise UnknownPeerError("Unknown PeerType.")
        return result

    def add_out_peer(self, out_peer: peers_pb2.OutPeer) -> None:
        """Adding OutPeers to peer_to_out_peer

        :param out_peer: OutPeer
        :return: None
        """
        self.peer_to_out_peer[(out_peer.type, out_peer.id)] = out_peer

    def add_thread_out_peer(self, out_peer: peers_pb2.ThreadOutPeer) -> None:
        """Adding OutPeers to peer_to_out_peer

        :param out_peer: OutPeer
        :return: None
        """
        self.add_out_peer(peers_pb2.OutPeer(id=out_peer.thread_id, type=PEERTYPE_THREAD, access_hash=out_peer.access_hash))

    def set_update_message_out_peers(self, message: UpdateMessage or Message) -> None:
        peer = message.sender_peer.to_api()
        mid = message.mid.to_api()
        if message.peer.type == PEERTYPE_GROUP:
            self.__get_group_out_peer(message.peer)

            request_user_data = RequestLoadUserData(
                claims=[
                    RequestLoadUserData.Claim(
                        user_peer=peer,
                        message_sender=mid
                    ),
                ]
            )

            result = self.internal.users.LoadUserData(request_user_data).users

            if result:
                self.__result_add_out_peer(result, PEERTYPE_PRIVATE)
        elif message.peer.type == PEERTYPE_THREAD:
            if self.get_out_peer(message.peer):
                return
            request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                mids=[mid]
            )
            result = self.internal.updates.GetReferencedEntitites(request)
            for msg in result.messages:
                self.add_out_peer(msg.host_peer)
                self.add_out_peer(msg.sender_peer)
        else:
            return self.get_out_peer(peer)

    def set_update_interactive_media_event_out_peers(self, media: UpdateInteractiveMediaEvent) -> None:
        request = RequestGetReferencedEntitites(
            mids=[media.mid.to_api()]
        )
        messages = self.internal.updates.GetReferencedEntitites(request).messages

        for message in messages:
            self.add_out_peer(message.sender_peer)
            self.add_out_peer(message.host_peer)

    def __get_group_out_peer(self, peer: peers_pb2.Peer) -> peers_pb2.OutPeer or None:
        request = RequestGetReferencedEntitites(
            groups=[GroupOutPeer(group_id=peer.id, access_hash=0)]
        )

        result = self.internal.updates.GetReferencedEntitites(request).groups

        if result:
            self.__result_add_out_peer(result, PEERTYPE_GROUP)
            return self.peer_to_out_peer.get((peer.type, peer.id))

    def __get_user_out_peer(self, peer: peers_pb2.Peer) -> peers_pb2.OutPeer or None:
        request = RequestLoadUserData(
            claims=[
                RequestLoadUserData.Claim(
                    user_peer=peer,
                    p2p=True
                ),
            ]
        )

        result = self.internal.users.LoadUserData(request).users

        if result:
            self.__result_add_out_peer(result, PEERTYPE_PRIVATE)
            return self.peer_to_out_peer.get((peer.type, peer.id))

    def __result_add_out_peer(self, result: list, type: PEERTYPE_PRIVATE or PEERTYPE_GROUP) -> peers_pb2.OutPeer:
        for peer in result:
            self.add_out_peer(peers_pb2.OutPeer(id=peer.id, type=type, access_hash=peer.access_hash))
