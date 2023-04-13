from pytest import raises

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.messaging import Message, ListLoadMode
from dialog_bot_sdk.exceptions.exceptions import UnknownPeerError
from dialog_bot_sdk.messaging import Messaging
from tests.fixtures.client_entities import user_peer, user_peer_invalid, valid_actions, invalid_actions, message, media, \
    mid, prev_mid, invalid_mid, text, empty_text, invalid_text, file
from tests.fixtures.internal import internal, manager


messaging = Messaging(manager, internal)


def test_send_message():
    assert isinstance(messaging.send_message(user_peer, text), UUID)
    assert isinstance(messaging.send_message(user_peer, text, valid_actions), UUID)
    assert isinstance(messaging.send_message(user_peer, text, uid=user_peer.id), UUID)
    with raises(UnknownPeerError):
        messaging.send_message(user_peer_invalid, text)
    with raises(AttributeError):
        messaging.send_message(user_peer, empty_text)
        messaging.send_message(user_peer, invalid_text)
        messaging.send_message(user_peer, text, invalid_actions)
        messaging.send_message(user_peer, text, uid="user_peer.id")


def test_update_message():
    assert messaging.update_message(message, text) is None
    assert messaging.update_message(message, text, valid_actions) is None
    with raises(AttributeError):
        assert messaging.update_message("", text)
        assert messaging.update_message(message, text, invalid_actions)
        assert messaging.update_message(message, empty_text)
        assert messaging.update_message(message, invalid_text)


def test_delete():
    assert messaging.delete(message) is None
    with raises(AttributeError):
        assert messaging.delete("")


def test_get_messages_by_id():
    assert isinstance(messaging.get_messages_by_id([mid]), list)
    assert isinstance(messaging.get_messages_by_id([mid])[0], Message)
    with raises(AttributeError):
        assert messaging.get_messages_by_id("")
        assert messaging.get_messages_by_id([message])


def test_messages_read():
    assert messaging.messages_read(user_peer, 0) is None
    assert messaging.messages_read(user_peer, -1) is None
    with raises(UnknownPeerError):
        assert messaging.messages_read(user_peer_invalid, 0)
    with raises(TypeError):
        assert messaging.messages_read(user_peer, text)


def test_send_file():
    assert messaging.send_file(user_peer, file) is None
    assert messaging.send_file(user_peer, file, user_peer.id) is None
    with raises(UnknownPeerError):
        assert messaging.send_file(user_peer_invalid, file)
    with raises(TypeError):
        assert messaging.send_file(user_peer, 1)
        assert messaging.send_file(user_peer, file, text) is None
    with raises(FileNotFoundError):
        assert messaging.send_file(user_peer, text)


def test_send_image():
    assert messaging.send_image(user_peer, file) is None
    assert messaging.send_image(user_peer, file, user_peer.id) is None
    with raises(UnknownPeerError):
        assert messaging.send_image(user_peer_invalid, file)
    with raises(TypeError):
        assert messaging.send_image(user_peer, 1)
        assert messaging.send_image(user_peer, file, text) is None
    with raises(IOError):
        assert messaging.send_image(user_peer, text)


def test_reply():
    assert isinstance(messaging.reply(user_peer, [mid, prev_mid]), UUID)
    assert isinstance(messaging.reply(user_peer, [mid, prev_mid], text), UUID)
    assert isinstance(messaging.reply(user_peer, [mid, prev_mid], text, valid_actions), UUID)
    assert isinstance(messaging.reply(user_peer, [mid, prev_mid], text, valid_actions, user_peer.id), UUID)
    with raises(UnknownPeerError):
        assert messaging.reply(user_peer_invalid, [])
    with raises(TypeError):
        assert messaging.reply(user_peer, [invalid_mid])
        assert messaging.reply(user_peer, [mid], 1)
        assert messaging.reply(user_peer, [mid], text, text)


def test_forward():
    assert isinstance(messaging.forward(user_peer, [mid, prev_mid]), UUID)
    assert isinstance(messaging.forward(user_peer, [mid, prev_mid], text), UUID)
    assert isinstance(messaging.forward(user_peer, [mid, prev_mid], text, valid_actions), UUID)
    assert isinstance(messaging.forward(user_peer, [mid, prev_mid], text, valid_actions, user_peer.id), UUID)
    with raises(UnknownPeerError):
        assert messaging.forward(user_peer_invalid, [])
    with raises(TypeError):
        assert messaging.forward(user_peer, [invalid_mid])
        assert messaging.forward(user_peer, [mid], 1)
        assert messaging.forward(user_peer, [mid], text, text)


def test_load_message_history():
    assert isinstance(messaging.load_message_history(user_peer), list)
    assert isinstance(messaging.load_message_history(user_peer, 1), list)
    assert isinstance(messaging.load_message_history(user_peer, 1, ListLoadMode.LISTLOADMODE_FORWARD), list)
    assert isinstance(messaging.load_message_history(user_peer, 1, ListLoadMode.LISTLOADMODE_FORWARD, 10), list)
    with raises(UnknownPeerError):
        assert messaging.load_message_history(user_peer_invalid)
    with raises(TypeError):
        assert messaging.load_message_history(user_peer, text)
        assert messaging.load_message_history(user_peer, 1, text)
        assert messaging.load_message_history(user_peer, 1, ListLoadMode.LISTLOADMODE_FORWARD, text)