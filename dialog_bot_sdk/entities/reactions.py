from typing import List

from dialog_api import reactions_pb2

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.peers import Peer


class Reaction:
    def __init__(self, code: str, users: List[int], users_amount: int) -> None:
        self.code = code
        self.users = users
        self.users_amount = users_amount

    @classmethod
    def from_api(cls, reaction: reactions_pb2.Reaction) -> 'Reaction':
        return cls(reaction.code, [x for x in reaction.users], reaction.users_amount)

    def __dict__(self):
        return {"code": self.code, "users": self.users, "users_amount": self.users_amount}

    def __str__(self):
        return "Reaction({})".format(self.__dict__())


class MessageReactions:
    def __init__(self, mid: UUID, reactions: List[Reaction]) -> None:
        self.mid = mid
        self.reactions = reactions

    @classmethod
    def from_api(cls, message_reaction: reactions_pb2.MessageReactions) -> 'MessageReactions':
        return cls(UUID.from_api(message_reaction.mid), [Reaction.from_api(x) for x in message_reaction.reactions])

    def __dict__(self):
        return {"mid": self.mid.__dict__(), "reactions": [x.__dict__() for x in self.reactions]}

    def __str__(self):
        return "MessageReactions({})".format(self.__dict__())


# updates
class MessageReactionsUpdate:
    def __init__(self, peer: Peer, reaction: MessageReactions, peer_clock: int, prev_peer_clock: int) -> None:
        self.peer = peer
        self.reaction = reaction
        self.peer_clock = peer_clock
        self.prev_peer_clock = prev_peer_clock

    @classmethod
    def from_api(cls, update: reactions_pb2.MessageReactionsUpdate) -> 'MessageReactionsUpdate':
        return cls(Peer.from_api(update.peer), MessageReactions.from_api(update.messageReaction), update.peer_clock,
                   update.prev_peer_clock)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "reaction": self.reaction.__dict__(), "peer_clock": self.peer_clock,
                "prev_peer_clock": self.prev_peer_clock}

    def __str__(self):
        return "MessageReactionsUpdate({})".format(self.__dict__())
