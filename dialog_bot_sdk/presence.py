from dialog_api.peers_pb2 import UserOutPeer
from dialog_api.presence_pb2 import RequestGetUserLastPresence, RequestStartTyping, RequestStopTyping, RequestSetOnline
from dialog_bot_sdk.utils import async_dec, get_peer, AsyncTask
from .entities.peers import Peer
from .entities.presence import TypingType, DeviceType
from .service import ManagedService


class Presence(ManagedService):
    """Class for handling grpc's server presence.

    """
    @async_dec()
    def get_user_last_presence(self, peer: Peer or AsyncTask) -> int:
        """Get last online timestamp by peer

        :param peer: user Peer or AsyncTask with User.
        :return: int last_online_at (in seconds)
        """
        peer = get_peer(peer)
        request = RequestGetUserLastPresence(
            user_out_peer=UserOutPeer(uid=peer.id, access_hash=self.manager.get_out_peer(peer).access_hash)
        )

        return self.internal.presence.GetUserLastPresence(request).last_online_at.seconds

    def get_user_last_presence_sync(self, peer: Peer or AsyncTask) -> int:
        return self.get_user_last_presence.__wrapped__(self, peer)

    @async_dec()
    def start_typing(self, peer: Peer, type: TypingType) -> None:
        """start typing

        :param peer: user or group Peer or AsyncTask with User or Group.
        :param type: TypingType enum
        :return:
        """
        peer = get_peer(peer)
        request = RequestStartTyping(
            peer=self.manager.get_out_peer(peer),
            typing_type=type
        )

        self.internal.presence.StartTyping(request)

    def start_typing_sync(self, peer: Peer, type: TypingType) -> None:
        return self.start_typing.__wrapped__(self, peer, type)

    @async_dec()
    def stop_typing(self, peer: Peer, type: TypingType) -> None:
        """stop typing

        :param peer: user or group Peer or AsyncTask with User or Group.
        :param type: TypingType enum
        :return:
        """
        peer = get_peer(peer)
        request = RequestStopTyping(
            peer=self.manager.get_out_peer(peer),
            typing_type=type
        )

        self.internal.presence.StopTyping(request)

    def stop_typing_sync(self, peer: Peer, type: TypingType) -> None:
        return self.stop_typing.__wrapped__(self, peer, type)

    @async_dec()
    def set_online(self, is_online: bool, timeout: int, device_type: DeviceType) -> None:
        """Set your online

        :param is_online: bool
        :param timeout: time in seconds
        :param device_type: DeviceType enum
        :return: int last_online_at (in seconds)
        """
        request = RequestSetOnline(
            is_online=is_online,
            timeout=timeout,
            device_type=device_type
        )

        self.internal.presence.SetOnline(request)

    def set_online_sync(self, is_online: bool, timeout: int, device_type: DeviceType) -> None:
        return self.set_online.__wrapped__(self, is_online, timeout, device_type)
