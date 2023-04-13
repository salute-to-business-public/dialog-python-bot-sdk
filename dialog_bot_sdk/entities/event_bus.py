from dialog_api import event_bus_pb2

from dialog_bot_sdk.entities.peers import Peer, PeerType


# updates
class UpdateEventBusDeviceConnected:
    def __init__(self, id: str, user_peer: Peer, device_id: int, peer: Peer) -> None:
        self.id = id
        self.user_peer = user_peer
        self.device_id = device_id
        self.peer = peer

    @classmethod
    def from_api(cls, update: event_bus_pb2.UpdateEventBusDeviceConnected) -> 'UpdateEventBusDeviceConnected':
        return cls(update.id, Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.device_id,
                   Peer.from_api(update.peer))

    def __dict__(self):
        return {
            "id": self.id,
            "user_peer": self.user_peer.__dict__(),
            "device_id": self.device_id,
            "peer": self.peer.__dict__()
        }

    def __str__(self):
        return "UpdateEventBusDeviceConnected({})".format(self.__dict__())


class UpdateEventBusDeviceDisconnected:
    def __init__(self, id: str, user_peer: Peer, device_id: int, peer: Peer) -> None:
        self.id = id
        self.user_peer = user_peer
        self.device_id = device_id
        self.peer = peer

    @classmethod
    def from_api(cls, update: event_bus_pb2.UpdateEventBusDeviceDisconnected) -> 'UpdateEventBusDeviceDisconnected':
        return cls(update.id, Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.device_id,
                   Peer.from_api(update.peer))

    def __dict__(self):
        return {
            "id": self.id,
            "user_peer": self.user_peer.__dict__(),
            "device_id": self.device_id,
            "peer": self.peer.__dict__()
        }

    def __str__(self):
        return "UpdateEventBusDeviceDisconnected({})".format(self.__dict__())


class UpdateEventBusMessage:
    def __init__(self, id: str, sender_peer: Peer, sender_device_id: int, message: bytes) -> None:
        self.id = id
        self.sender_peer = sender_peer
        self.sender_device_id = sender_device_id
        self.message = message

    @classmethod
    def from_api(cls, update: event_bus_pb2.UpdateEventBusMessage) -> 'UpdateEventBusMessage':
        return cls(update.id, Peer(update.sender_id, PeerType.PEERTYPE_PRIVATE), update.sender_device_id, update.message)

    def __dict__(self):
        return {
            "id": self.id,
            "sender_peer": self.sender_peer.__dict__(),
            "sender_device_id": self.sender_device_id,
            "message": self.message
        }

    def __str__(self):
        return "UpdateEventBusMessage({})".format(self.__dict__())


class UpdateEventBusDisposed:
    def __init__(self, id: str) -> None:
        self.id = id

    @classmethod
    def from_api(cls, update: event_bus_pb2.UpdateEventBusDisposed) -> 'UpdateEventBusDisposed':
        return cls(update.id)

    def __dict__(self):
        return {"id": self.id}

    def __str__(self):
        return "UpdateEventBusDisposed({})".format(self.__dict__())
