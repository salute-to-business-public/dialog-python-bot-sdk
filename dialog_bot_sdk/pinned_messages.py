from typing import List
from dialog_bot_sdk.utils import async_dec
from .entities.definitions import UUID
from .entities.messaging import Message
from .entities.peers import Peer
from .entities.sequence_and_updates import ReferencedEntities
from .service import ManagedService
from dialog_api import sequence_and_updates_pb2, pinned_messages_pb2


class PinnedMessages(ManagedService):
    """Class for handling pinned messages

    """
    @async_dec()
    def get_pinned_messages(self, peer: Peer) -> List[Message]:
        """Get pinned messages by peer

        :param peer: peer
        :return: list Message
        """
        request = pinned_messages_pb2.GetPinnedMessagesRequest(
            peer=peer.to_api(),
        )
        mids = self.internal.pinned_messages.GetPinnedMessages(request).mids
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            mids=mids
        )
        result = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request))
        return result.messages

    def get_pinned_messages_sync(self, peer: Peer) -> List[Message]:
        return self.get_pinned_messages.__wrapped__(self, peer)

    @async_dec()
    def pin_message(self, peer: Peer, mid: UUID) -> None:
        """pin message

        :param peer: peer
        :param mid: message id
        :return: None
        """
        request = pinned_messages_pb2.RequestPinMessage(
            peer=peer.to_api(),
            mid=mid.to_api()
        )
        self.internal.pinned_messages.PinMessage(request)

    def pin_message_sync(self, peer: Peer, mid: UUID) -> None:
        return self.pin_message.__wrapped__(self, peer, mid)

    @async_dec()
    def unpin_message(self, peer: Peer, mid: UUID) -> None:
        """unpin message

        :param peer: peer
        :param mid: message id
        :return: None
        """
        request = pinned_messages_pb2.RequestUnpinMessage(
            peer=peer.to_api(),
            mid=mid.to_api()
        )
        self.internal.pinned_messages.UnpinMessage(request)

    def unpin_message_sync(self, peer: Peer, mid: UUID) -> None:
        return self.unpin_message.__wrapped__(self, peer, mid)
