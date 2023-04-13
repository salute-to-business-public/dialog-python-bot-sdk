from typing import List

from dialog_api.reactions_pb2 import GetReactionsRequest, GetMessageReactionsRequest, RequestRemoveMessageReaction,\
    RequestSetMessageReaction

from dialog_bot_sdk.utils import async_dec, get_peer, get_uuid, AsyncTask
from .entities.definitions import UUID
from .entities.peers import Peer
from .entities.reactions import MessageReactions
from .service import ManagedService


class Reactions(ManagedService):
    """Class for handling grpc's server reactions.

    """
    @async_dec()
    def get_reactions(self, peer: Peer or AsyncTask, from_clock: int) -> List[MessageReactions]:
        """Get messages reaction from defined time

        :param peer: user or Group Peer or AsyncTask with User or Group
        :param from_clock: from timestamp
        :return: int last_online_at (in seconds)
        """
        peer = get_peer(peer)
        request = GetReactionsRequest(
            peer=peer,
            from_clock=from_clock
        )

        return [MessageReactions.from_api(x) for x in self.internal.reactions.GetReactions(request).messageReactions]

    def get_reactions_sync(self, peer: Peer or AsyncTask, from_clock: int) -> List[MessageReactions]:
        return self.get_reactions.__wrapped__(self, peer, from_clock)

    @async_dec()
    def get_message_reactions(self, peer: Peer or AsyncTask, mid: UUID or AsyncTask) -> List[MessageReactions]:
        """Get reactions from message

        :param peer: user or Group Peer or AsyncTask with User or Group
        :param mid: message id or AsyncTask with UUID
        :return:
        """
        peer = get_peer(peer)
        mid = get_uuid(mid)
        request = GetMessageReactionsRequest(
            peer=peer,
            message_ids=[mid]
        )

        return [MessageReactions.from_api(x) for x in self.internal.reactions.GetMessageReactions(request).messageReactions]

    def get_message_reactions_sync(self, peer: Peer or AsyncTask, mid: UUID or AsyncTask) -> List[MessageReactions]:
        return self.get_message_reactions.__wrapped__(self, peer, mid)

    @async_dec()
    def remove_message_reaction(self, peer: Peer or AsyncTask, mid: UUID or AsyncTask, code: str) -> None:
        """Remove self reaction from message

        :param peer: user or Group Peer or AsyncTask with User or Group
        :param mid: message id or AsyncTask with UUID
        :param code: str reaction
        :return:
        """
        peer = get_peer(peer)
        mid = get_uuid(mid)
        request = RequestRemoveMessageReaction(
            peer=peer,
            mid=mid,
            code=code
        )

        self.internal.reactions.MessageRemoveReaction(request)

    def remove_message_reaction_sync(self, peer: Peer or AsyncTask, mid: UUID or AsyncTask, code: str) -> None:
        return self.remove_message_reaction.__wrapped__(self, peer, mid, code)

    @async_dec()
    def set_message_reaction(self, peer: Peer or AsyncTask, mid: UUID or AsyncTask, code: str) -> None:
        """Set self reaction to message

        :param peer: user or Group Peer or AsyncTask with User or Group
        :param mid: message id or AsyncTask with UUID
        :param code: str reaction
        :return:
        """
        peer = get_peer(peer)
        mid = get_uuid(mid)
        request = RequestSetMessageReaction(
            peer=peer,
            mid=mid,
            code=code
        )

        self.internal.reactions.MessageSetReaction(request)

    def set_message_reaction_sync(self, peer: Peer or AsyncTask, mid: UUID or AsyncTask, code: str) -> None:
        return self.set_message_reaction.__wrapped__(self, peer, mid, code)
