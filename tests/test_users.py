from pytest import raises

from dialog_bot_sdk.entities.peers import PeerType
from dialog_bot_sdk.entities.users import User, FullUser
from dialog_bot_sdk.users import Users
from tests.fixtures.client_entities import text, invalid_text
from tests.fixtures.internal import manager, internal
from tests.fixtures.server_entities import user, uop

users = Users(manager, internal)


def test_get_user_by_nick():
    assert isinstance(users.get_user_by_nick("nick"), User)
    assert users.get_user_by_nick("123") is None
    with raises(RuntimeError):
        assert users.get_user_by_nick(invalid_text)


def test_get_user_by_id():
    assert isinstance(users.get_user_by_id(user.id), User)
    assert users.get_user_by_id(123).peer.id != 123
    with raises(RuntimeError):
        assert users.get_user_by_id(text)


def test_search_users_by_nick_substring():
    assert isinstance(users.search_users_by_nick_substring("nick"), list)
    with raises(TypeError):
        assert users.search_users_by_nick_substring(invalid_text)


def test_get_full_profile_by_nick():
    with raises(RuntimeError):
        assert users.get_full_profile_by_nick(invalid_text)


def test_get_full_profile_by_id():
    assert users.get_full_profile_by_id(user.id).id != user.id
    users.manager.peer_to_out_peer[(uop.id, PeerType.PEERTYPE_PRIVATE)] = uop
    assert isinstance(users.get_full_profile_by_id(uop.id), FullUser)
    with raises(TypeError):
        assert users.get_full_profile_by_id(text)
