from typing import List

from dialog_api import favourites_messages_pb2

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.peers import Peer


class UpdateFavouritesMessagesChanged:
    def __init__(self, peer: Peer, mids: List[UUID], clock: int, prev_clock: int) -> None:
        self.peer = peer
        self.mids = mids
        self.clock = clock
        self.prev_clock = prev_clock

    @classmethod
    def from_api(cls, update: favourites_messages_pb2.UpdateFavouritesMessagesChanged) -> 'UpdateFavouritesMessagesChanged':
        return cls(Peer.from_api(update.peer), [UUID.from_api(x) for x in update.mids], update.clock, update.prev_clock)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "mids": [x.__dict__() for x in self.mids], "clock": self.clock,
                "prev_clock": self.prev_clock}

    def __str__(self):
        return "UpdateFavouritesMessagesChanged({})".format(self.__dict__())
