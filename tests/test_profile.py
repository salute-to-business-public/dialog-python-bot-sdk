from pytest import raises

from dialog_bot_sdk.entities.users import UserStatus, Sex
from dialog_bot_sdk.profile import Profile
from tests.fixtures.client_entities import text, invalid_text, file
from tests.fixtures.internal import manager, internal

profile = Profile(manager, internal)


def test_edit_name():
    assert profile.edit_name(text) is None
    with raises(TypeError):
        assert profile.edit_name(invalid_text)


def test_edit_nickname():
    assert profile.edit_nickname(text) is None
    with raises(TypeError):
        assert profile.edit_nickname(invalid_text)


def test_check_nickname():
    assert profile.check_nickname("nick")
    assert profile.check_nickname(text) is False
    with raises(TypeError):
        assert profile.check_nickname(invalid_text)


def test_edit_about():
    assert profile.edit_about(text) is None
    with raises(TypeError):
        assert profile.edit_about(invalid_text)


def test_edit_avatar():
    assert profile.edit_avatar(file) is None
    with raises(OSError):
        assert profile.edit_avatar(invalid_text)


def test_remove_avatar():
    assert profile.remove_avatar() is None


def test_edit_time_zone():
    assert profile.edit_time_zone(text) is None
    with raises(TypeError):
        assert profile.edit_time_zone(invalid_text)


def test_edit_preferred_languages():
    assert profile.edit_preferred_languages([text]) is None
    with raises(TypeError):
        assert profile.edit_preferred_languages([invalid_text])
        assert profile.edit_preferred_languages(text)


def test_edit_sex():
    assert profile.edit_sex(Sex.MALE) is None
    with raises(ValueError):
        assert profile.edit_sex("MALE")


def test_edit_custom_profile():
    assert profile.edit_custom_profile(text) is None
    with raises(TypeError):
        assert profile.edit_custom_profile(invalid_text)


def test_edit_user_status():
    assert profile.edit_user_status(UserStatus.USERSTATUSTYPE_UNSET, text) is None
    with raises(ValueError):
        assert profile.edit_user_status(text, text)
    with raises(TypeError):
        assert profile.edit_user_status(UserStatus.USERSTATUSTYPE_UNSET, invalid_text)