from dialog_api import web_rtc_pb2

from dialog_bot_sdk.entities.peers import Peer, OutPeer


class CallDisposedReason:
    CALLDISPOSEDREASON_UNKNOWN = web_rtc_pb2.CALLDISPOSEDREASON_UNKNOWN
    CALLDISPOSEDREASON_REJECTED = web_rtc_pb2.CALLDISPOSEDREASON_REJECTED
    CALLDISPOSEDREASON_BUSY = web_rtc_pb2.CALLDISPOSEDREASON_BUSY
    CALLDISPOSEDREASON_ENDED = web_rtc_pb2.CALLDISPOSEDREASON_ENDED
    CALLDISPOSEDREASON_ANSWER_TIMEOUT = web_rtc_pb2.CALLDISPOSEDREASON_ANSWER_TIMEOUT


# updates
class UpdateIncomingCallDeprecated:
    def __init__(self, call_id: int, attempt_index: int) -> None:
        self.call_id = call_id
        self.attempt_index = attempt_index

    @classmethod
    def from_api(cls, update: web_rtc_pb2.UpdateIncomingCallDeprecated) -> 'UpdateIncomingCallDeprecated':
        return cls(update.call_id, update.attempt_index.value)

    def __dict__(self):
        return {
            "call_id": self.call_id,
            "attempt_index": self.attempt_index,
        }

    def __str__(self):
        return "UpdateIncomingCallDeprecated({})".format(self.__dict__())


class UpdateIncomingCall:
    def __init__(self, call_id: int, event_bus_id: str, peer: Peer, display_name: str, attempt_index: int,
                 out_peer: OutPeer, video: bool) -> None:
        self.call_id = call_id
        self.event_bus_id = event_bus_id
        self.peer = peer
        self.display_name = display_name
        self.attempt_index = attempt_index
        self.out_peer = out_peer
        self.video = video

    @classmethod
    def from_api(cls, update: web_rtc_pb2.UpdateIncomingCall) -> 'UpdateIncomingCall':
        return cls(
            update.call_id,
            update.event_bus_id,
            Peer.from_api(update.peer),
            update.display_name.value,
            update.attempt_index.value,
            OutPeer.from_api(update.out_peer),
            update.video,
        )

    def __dict__(self):
        return {
            "call_id": self.call_id,
            "event_bus_id": self.event_bus_id,
            "peer": self.peer.__dict__(),
            "display_name": self.display_name,
            "attempt_index": self.attempt_index,
            "out_peer": self.out_peer.__dict__(),
            "video": self.video,
        }

    def __str__(self):
        return "UpdateIncomingCall({})".format(self.__dict__())


class UpdateCallHandled:
    def __init__(self, call_id: int, attempt_index: int) -> None:
        self.call_id = call_id
        self.attempt_index = attempt_index

    @classmethod
    def from_api(cls, update: web_rtc_pb2.UpdateCallHandled) -> 'UpdateCallHandled':
        return cls(update.call_id, update.attempt_index.value)

    def __dict__(self):
        return {
            "call_id": self.call_id,
            "attempt_index": self.attempt_index,
        }

    def __str__(self):
        return "UpdateCallHandled({})".format(self.__dict__())


class UpdateCallDisposed:
    def __init__(self, call_id: int, attempt_index: int, reason: CallDisposedReason) -> None:
        self.call_id = call_id
        self.attempt_index = attempt_index
        self.reason = reason

    @classmethod
    def from_api(cls, update: web_rtc_pb2.UpdateCallDisposed) -> 'UpdateCallDisposed':
        return cls(update.call_id, update.attempt_index.value, update.reason)

    def __dict__(self):
        return {
            "call_id": self.call_id,
            "attempt_index": self.attempt_index,
            "reason": self.reason
        }

    def __str__(self):
        return "UpdateCallDisposed({})".format(self.__dict__())
