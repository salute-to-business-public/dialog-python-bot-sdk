from dialog_api import peers_pb2
from pytest import raises

from dialog_bot_sdk.entities.presence import TypingType, DeviceType
from dialog_bot_sdk.presence import Presence
from tests.fixtures.client_entities import user_peer
from tests.fixtures.internal import manager, internal


presence = Presence(manager, internal)


def test_get_user_last_presence():
    manager.add_out_peer(peers_pb2.OutPeer(id=user_peer.id, type=user_peer.type, access_hash=1))
    assert isinstance(presence.get_user_last_presence(user_peer), int)
    with raises(AttributeError):
        assert presence.get_user_last_presence("123")


def test_start_typing():
    assert presence.start_typing(user_peer, TypingType.TYPINGTYPE_TEXT) is None
    with raises(AttributeError):
        assert presence.start_typing("123", TypingType.TYPINGTYPE_TEXT)
    with raises(ValueError):
        assert presence.start_typing(user_peer, "123")


def test_stop_typing():
    assert presence.stop_typing(user_peer, TypingType.TYPINGTYPE_TEXT) is None
    with raises(AttributeError):
        assert presence.stop_typing("123", TypingType.TYPINGTYPE_TEXT)
    with raises(ValueError):
        assert presence.stop_typing(user_peer, "123")


def test_set_online():
    assert presence.set_online(True, 123, DeviceType.DEVICETYPE_CAR) is None
    with raises(TypeError):
        assert presence.set_online("123")
        assert presence.set_online(True, "123", 123)
    with raises(ValueError):
        assert presence.set_online(True, 123, "123")
