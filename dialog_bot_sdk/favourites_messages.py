from typing import List
from dialog_bot_sdk.utils import async_dec
from .entities.definitions import UUID
from .entities.messaging import Message
from .entities.peers import Peer
from .entities.sequence_and_updates import ReferencedEntities
from .service import ManagedService
from dialog_api import sequence_and_updates_pb2, favourites_messages_pb2


class FavouritesMessages(ManagedService):
    """Class for handling favourites_messages

    """
    @async_dec()
    def get_favourites_messages(self, peer: Peer) -> List[Message]:
        """Get favourites messages by peer

        :param peer: peer
        :return: list Message
        """
        request = favourites_messages_pb2.GetFavouritesMessagesRequest(
            peer=peer.to_api(),
        )
        mids = self.internal.favourites_messages.GetFavouritesMessages(request).mids
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                mids=mids
            )
        result = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request))
        return result.messages

    def get_favourites_messages_sync(self, peer: Peer) -> List[Message]:
        return self.get_favourites_messages.__wrapped__(self, peer)

    @async_dec()
    def get_all_favourites_messages(self) -> List[Message]:
        """Get all favourites messages

        :return: list Message
        """
        request = favourites_messages_pb2.GetAllFavouritesMessagesRequest()
        mids = [x.mid for x in self.internal.favourites_messages.GetAllFavouritesMessages(request).messages]
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            mids=mids
        )
        result = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request))
        return result.messages

    def get_all_favourites_messages_sync(self) -> List[Message]:
        return self.get_all_favourites_messages.__wrapped__(self)

    @async_dec()
    def mark_favourites_message(self, peer: Peer, mid: UUID) -> None:
        """Mark favourites message

        :param peer: peer
        :param mid: message id
        :return: None
        """
        request = favourites_messages_pb2.RequestMarkFavouritesMessage(
            peer=peer.to_api(),
            mid=mid.to_api()
        )
        self.internal.favourites_messages.MarkFavouritesMessage(request)

    def mark_favourites_message_sync(self, peer: Peer, mid: UUID) -> None:
        return self.mark_favourites_message.__wrapped__(self, peer, mid)

    @async_dec()
    def unmark_favourites_message(self, peer: Peer, mid: UUID) -> None:
        """Unmark favourites message

        :param peer: peer
        :param mid: message id
        :return: None
        """
        request = favourites_messages_pb2.RequestUnmarkFavouritesMessage(
            peer=peer.to_api(),
            mid=mid.to_api()
        )
        self.internal.favourites_messages.UnmarkFavouritesMessage(request)

    def unmark_favourites_message_sync(self, peer: Peer, mid: UUID) -> None:
        return self.unmark_favourites_message.__wrapped__(self, peer, mid)
