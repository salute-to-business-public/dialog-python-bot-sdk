from typing import List

from dialog_api import counters_pb2

from dialog_bot_sdk.entities.peers import Peer


class UnreadDialog:
    def __init__(self, peer: Peer, counter: int) -> None:
        self.peer = peer
        self.counter = counter

    @classmethod
    def from_api(cls, update: counters_pb2.UnreadDialog) -> 'UnreadDialog':
        return cls(Peer.from_api(update.peer), update.counter)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "counter": self.counter,
        }

    def __str__(self):
        return "UnreadDialog({})".format(self.__dict__())


class AppCounters:
    def __init__(self, global_counter: int, global_dialogs_counter: int, unread_dialogs: List[UnreadDialog]) -> None:
        self.global_counter = global_counter
        self.global_dialogs_counter = global_dialogs_counter
        self.unread_dialogs = unread_dialogs

    @classmethod
    def from_api(cls, update: counters_pb2.AppCounters) -> 'AppCounters':
        return cls(update.global_counter.value, update.global_dialogs_counter.value,
                   [UnreadDialog.from_api(x) for x in update.unread_dialogs])

    def __dict__(self):
        return {
            "global_counter": self.global_counter,
            "global_dialogs_counter": self.global_dialogs_counter,
            "unread_dialogs": [x.__dict__() for x in self.unread_dialogs]
        }

    def __str__(self):
        return "AppCounters({})".format(self.__dict__())


# updates
class UpdateCountersChanged:
    def __init__(self, counters: AppCounters, ts: int) -> None:
        self.counters = counters
        self.ts = ts

    @classmethod
    def from_api(cls, update: counters_pb2.UpdateCountersChanged) -> 'UpdateCountersChanged':
        return cls(AppCounters.from_api(update.counters), update.ts.value)

    def __dict__(self):
        return {
            "counters": self.counters.__dict__(),
            "ts": self.ts,
        }

    def __str__(self):
        return "UpdateCountersChanged({})".format(self.__dict__())
