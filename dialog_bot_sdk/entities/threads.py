from typing import List

from dialog_api import threads_pb2

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.messaging import Message
from dialog_bot_sdk.entities.peers import Peer, PeerType


class Thread:
    def __init__(
            self,
            thread_peer: Peer,
            root_message_id: UUID,
            group_peer: Peer,
            last_message_date: int,
            last_read_date: int,
            messages_count: int,
            subscribed: bool,
            clock: int
    ) -> None:
        self.thread_peer = thread_peer
        self.root_message_id = root_message_id
        self.group_peer = group_peer
        self.last_message_date = last_message_date
        self.last_read_date = last_read_date
        self.messages_count = messages_count
        self.subscribed = subscribed
        self.clock = clock

    @classmethod
    def from_api(cls, thread: threads_pb2.Thread) -> 'Thread':
        return cls(
            Peer(thread.thread_peer.thread_id, PeerType.PEERTYPE_THREAD),
            UUID.from_api(thread.root_message_id),
            Peer(thread.group_peer.group_id, PeerType.PEERTYPE_GROUP),
            thread.last_message_date,
            thread.last_read_date,
            thread.messages_count,
            thread.subscribed,
            thread.clock
        )

    def __dict__(self):
        return {
            "thread_peer": self.thread_peer.__dict__(),
            "root_message_id": self.root_message_id.__dict__(),
            "group_peer": self.group_peer.__dict__(),
            "last_message_date": self.last_message_date,
            "last_read_date": self.last_read_date,
            "messages_count": self.messages_count,
            "subscribed": self.subscribed,
            "clock": self.clock
        }

    def __str__(self):
        return "Thread({})".format(self.__dict__())


class SubscribedThread:
    def __init__(
            self,
            thread: Thread,
            unread_count: int,
            root_history_message: Message,
            date: int,
    ) -> None:
        self.thread = thread
        self.unread_count = unread_count
        self.root_history_message = root_history_message
        self.date = date

    @classmethod
    def from_api(cls, thread: threads_pb2.SubscribedThread) -> 'SubscribedThread':
        return cls(
            Thread.from_api(thread.thread),
            thread.unread_count,
            Message.from_api(thread.root_history_message),
            thread.date,
        )

    def __dict__(self):
        return {
            "thread": self.thread.__dict__(),
            "unread_count": self.unread_count,
            "root_history_message": self.root_history_message.__dict__(),
            "date": self.date,
        }

    def __str__(self):
        return "SubscribedThread({})".format(self.__dict__())


class SubscribedThreadGroup:
    def __init__(
            self,
            group_peer: Peer,
            threads_count: int,
            threads: List[SubscribedThread],
    ) -> None:
        self.group_peer = group_peer
        self.threads_count = threads_count
        self.threads = threads

    @classmethod
    def from_api(cls, thread: threads_pb2.SubscribedThreadGroup) -> 'SubscribedThreadGroup':
        return cls(
            Peer(thread.group_peer.group_id, PeerType.PEERTYPE_GROUP),
            thread.threads_count,
            [SubscribedThread.from_api(x) for x in thread.threads],
        )

    def __dict__(self):
        return {
            "group_peer": self.group_peer.__dict__(),
            "threads_count": self.threads_count,
            "threads": [x.__dict__() for x in self.threads],
        }

    def __str__(self):
        return "SubscribedThreadGroup({})".format(self.__dict__())


class UpdateThreadCreated:
    def __init__(self, thread_peer: Peer, root_message_id: UUID, group_peer: Peer) -> None:
        self.thread_peer = thread_peer
        self.root_message_id = root_message_id
        self.group_peer = group_peer

    @classmethod
    def from_api(cls, update: threads_pb2.UpdateThreadCreated) -> 'UpdateThreadCreated':
        return cls(
            Peer(update.thread_peer.id, PeerType.PEERTYPE_THREAD),
            UUID.from_api(update.root_message_id),
            Peer(update.group_peer.id, PeerType.PEERTYPE_GROUP),
        )

    def __dict__(self):
        return {
            "thread_peer": self.thread_peer.__dict__(),
            "root_message_id": self.root_message_id.__dict__(),
            "group_peer": self.group_peer.__dict__(),
        }

    def __str__(self):
        return "UpdateThreadCreated({})".format(self.__dict__())


class UpdateSubscribedToThread:
    def __init__(self, thread_peer: Peer, group_peer: Peer) -> None:
        self.thread_peer = thread_peer
        self.group_peer = group_peer

    @classmethod
    def from_api(cls, update: threads_pb2.UpdateSubscribedToThread) -> 'UpdateSubscribedToThread':
        return cls(
            Peer(update.thread_peer.id, PeerType.PEERTYPE_THREAD),
            Peer(update.group_peer.id, PeerType.PEERTYPE_GROUP),
        )

    def __dict__(self):
        return {
            "thread_peer": self.thread_peer.__dict__(),
            "group_peer": self.group_peer.__dict__(),
        }

    def __str__(self):
        return "UpdateSubscribedToThread({})".format(self.__dict__())


class UpdateUnsubscribedFromThread:
    def __init__(self, thread_peer: Peer, group_peer: Peer) -> None:
        self.thread_peer = thread_peer
        self.group_peer = group_peer

    @classmethod
    def from_api(cls, update: threads_pb2.UpdateUnsubscribedFromThread) -> 'UpdateUnsubscribedFromThread':
        return cls(
            Peer(update.thread_peer.id, PeerType.PEERTYPE_THREAD),
            Peer(update.group_peer.id, PeerType.PEERTYPE_GROUP),
        )

    def __dict__(self):
        return {
            "thread_peer": self.thread_peer.__dict__(),
            "group_peer": self.group_peer.__dict__(),
        }

    def __str__(self):
        return "UpdateUnsubscribedFromThread({})".format(self.__dict__())
