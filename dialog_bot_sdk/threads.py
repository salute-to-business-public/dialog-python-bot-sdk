from typing import List
from dialog_api import peers_pb2
from dialog_api.peers_pb2 import ThreadOutPeer
from dialog_api.threads_pb2 import RequestCreateThread, RequestGetThreads, RequestGetConversationThreads, \
    RequestSubscribeToThread, RequestUnsubscribeFromThread, RequestSubscribedThreads, RequestUnsubscribeFromAllThreads
from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.peers import Peer, PeerType
from dialog_bot_sdk.entities.threads import Thread, SubscribedThreadGroup
from dialog_bot_sdk.service import ManagedService
from dialog_bot_sdk.utils import async_dec


class Threads(ManagedService):
    """Class for handling users
    """
    @async_dec()
    def create_thread(self, group_peer: Peer, root_message_id: UUID) -> Peer or None:
        """return thread peer

        :param group_peer: group peer for thread
        :param root_message_id: message id for thread
        :return: thread peer
        """
        out_peer = self.manager.get_out_peer(group_peer)
        if out_peer is None:
            return
        if group_peer.type == PeerType.PEERTYPE_GROUP:
            out_peer = peers_pb2.GroupOutPeer(group_id=out_peer.id, access_hash=out_peer.access_hash)

        request = RequestCreateThread(
            group_peer=out_peer,
            root_message_id=root_message_id.to_api()
        )
        thread_peer = self.internal.threads.CreateThread(request).peer
        if thread_peer.thread_id == 0:
            return
        self.manager.add_thread_out_peer(thread_peer)
        return Peer(thread_peer.thread_id, PeerType.PEERTYPE_THREAD)

    def create_thread_sync(self, group_peer: Peer, root_message_id: UUID) -> Peer or None:
        return self.create_thread.__wrapped__(self, group_peer, root_message_id)

    @async_dec()
    def get_threads(self, thread_peers: List[Peer]) -> List[Thread]:
        """return list of thread peers

        :param thread_peers: thread peers
        :return: thread peers
        """

        out_peers = [self.manager.get_out_peer(x) for x in thread_peers]
        out_peers_for_request = []

        for out_peer in out_peers:
            if out_peer is not None:
                out_peers_for_request.append(ThreadOutPeer(thread_id=out_peer.id, access_hash=out_peer.access_hash))

        request = RequestGetThreads(
            thread_out_peers=out_peers_for_request,
        )
        threads = self.internal.threads.GetThreads(request).threads
        [self.manager.add_thread_out_peer(x.thread_peer) for x in threads]
        threads = {x.thread_peer.thread_id: Thread.from_api(x) for x in self.internal.threads.GetThreads(request).threads}
        result = []
        for peer in thread_peers:
            if peer.id in threads:
                result.append(threads.get(peer.id))

        return result

    def get_threads_sync(self, thread_peers: List[Peer]) -> List[Thread]:
        return self.get_threads.__wrapped__(self, thread_peers)

    @async_dec()
    def get_conversation_threads(self, group_peer: Peer, from_clock: int, limit: int) -> List[Thread]:
        """return list of thread peers

        :param group_peer: group peer
        :param from_clock: from clock
        :param limit: limit
        :return: thread peers
        """
        out_peer = self.manager.get_out_peer(group_peer)
        if out_peer is None:
            return []

        request = RequestGetConversationThreads(
            group_peer=peers_pb2.GroupOutPeer(group_id=out_peer.id, access_hash=out_peer.access_hash),
            from_clock=from_clock,
            limit=limit
        )
        result = self.internal.threads.GetConversationThreads(request).threads
        [self.manager.add_thread_out_peer(x.thread_peer) for x in result]
        return [Thread.from_api(x) for x in result]

    def get_conversation_threads_sync(self, group_peer: Peer, from_clock: int = 0, limit: int = 2) -> List[Thread]:
        return self.get_conversation_threads.__wrapped__(self, group_peer, from_clock, limit)

    @async_dec()
    def subscribe_to_thread(self, thread_peer: Peer) -> None:
        """return None

        :param thread_peer: thread peer
        :return: None
        """
        out_peer = self.manager.get_out_peer(thread_peer)
        if out_peer is None:
            out_peer = ThreadOutPeer(thread_id=thread_peer.id, access_hash=0)
        else:
            out_peer = ThreadOutPeer(thread_id=out_peer.id, access_hash=out_peer.access_hash)
        request = RequestSubscribeToThread(
            thread_peer=out_peer,
        )
        return self.internal.threads.Subscribe(request)

    def subscribe_to_thread_sync(self, thread_peer: Peer) -> None:
        return self.subscribe_to_thread.__wrapped__(self, thread_peer)

    @async_dec()
    def unsubscribe_from_thread(self, thread_peer: Peer) -> None:
        """return None

        :param thread_peer: thread peer
        :return: None
        """
        out_peer = self.manager.get_out_peer(thread_peer)
        if out_peer is None:
            out_peer = ThreadOutPeer(thread_id=thread_peer.id, access_hash=0)
        else:
            out_peer = ThreadOutPeer(thread_id=out_peer.id, access_hash=out_peer.access_hash)
        request = RequestUnsubscribeFromThread(
            thread_peer=out_peer,
        )
        return self.internal.threads.Unsubscribe(request)

    def unsubscribe_from_thread_sync(self, thread_peer: Peer) -> None:
        return self.unsubscribe_from_thread.__wrapped__(self, thread_peer)

    @async_dec()
    def subscribed_threads(self, min_date: int = 0, limit: int = 0) -> List[SubscribedThreadGroup]:
        """return list of threads

        :param min_date: min date
        :param limit: limit
        :return: threads
        """
        request = RequestSubscribedThreads(
            min_date=min_date,
            limit=limit
        )
        result = self.internal.threads.GetSubscribedThreads(request).thread_groups
        for subscribed_thread in result:
            for thread in subscribed_thread.threads:
                self.manager.add_thread_out_peer(thread.thread.thread_peer)

        return [SubscribedThreadGroup.from_api(x) for x in result]

    def subscribed_threads_sync(self, min_date: int = 0, limit: int = 0) -> List[SubscribedThreadGroup]:
        return self.subscribed_threads.__wrapped__(self, min_date, limit)

    @async_dec()
    def unsubscribe_from_all_threads(self) -> None:
        """return None
        :return: None
        """
        return self.internal.threads.UnsubscribeFromAllThreads(RequestUnsubscribeFromAllThreads())

    def unsubscribe_from_all_threads_sync(self) -> None:
        return self.unsubscribe_from_all_threads.__wrapped__(self)
