from dialog_api.groups_pb2 import GROUPADMINPERMISSION_EDITSHORTNAME
from pytest import raises
from dialog_bot_sdk.entities.groups import Group
from dialog_bot_sdk.exceptions.exceptions import UnknownPeerError
from dialog_bot_sdk.groups import Groups
from tests.fixtures.client_entities import text, invalid_text, group_peer, user_peer, group_peer_invalid, \
    user_peer_invalid, file
from tests.fixtures.internal import manager, internal
from tests.fixtures.server_entities import group

groups = Groups(manager, internal)


def test_create_group():
    assert isinstance(groups.create_public_group(text, text), Group)
    assert isinstance(groups.create_private_group(text), Group)
    assert isinstance(groups.create_public_channel(text, text), Group)
    assert isinstance(groups.create_private_channel(text), Group)
    with raises(TypeError):
        assert groups.create_public_group(invalid_text, text)
        assert groups.create_public_group(text, invalid_text)
        assert groups.create_private_group(invalid_text)
        assert groups.create_public_channel(invalid_text, text)
        assert groups.create_public_channel(text, invalid_text)
        assert groups.create_private_channel(invalid_text)


def test_find_group_by_short_name():
    assert isinstance(groups.find_group_by_short_name(text), Group)
    assert groups.find_group_by_short_name("123") is None
    with raises(TypeError):
        assert groups.create_public_group(invalid_text, "")


def test_find_group_by_id():
    assert isinstance(groups.find_group_by_id(group.id), Group)
    assert groups.find_group_by_id(123).peer.id != 123
    with raises(TypeError):
        assert groups.find_group_by_id(text)


def test_load_members():
    pass


def test_kick_user():
    assert groups.kick_user(group_peer, user_peer) is None
    with raises(UnknownPeerError):
        assert groups.kick_user(group_peer_invalid, user_peer)
        assert groups.kick_user(group_peer, user_peer_invalid)


def test_invite_user():
    assert groups.invite_user(group_peer, user_peer) is None
    with raises(UnknownPeerError):
        assert groups.invite_user(group_peer_invalid, user_peer)
        assert groups.invite_user(group_peer, user_peer_invalid)


def test_set_default_group_permissions():
    assert groups.set_default_group_permissions(group_peer) is None
    assert groups.set_default_group_permissions(group_peer, [GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    assert groups.set_default_group_permissions(group_peer, del_permissions=[GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    assert groups.set_default_group_permissions(group_peer, [GROUPADMINPERMISSION_EDITSHORTNAME],
                                                            [GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    with raises(UnknownPeerError):
        assert groups.set_default_group_permissions(group_peer_invalid)
    with raises(ValueError):
        assert groups.set_default_group_permissions(group_peer, add_permissions=["EDITSHORTNAME"])
        assert groups.set_default_group_permissions(group_peer, del_permissions=["EDITSHORTNAME"])
    with raises(TypeError):
        assert groups.set_default_group_permissions(group_peer, add_permissions=1)
        assert groups.set_default_group_permissions(group_peer, del_permissions=1)


def test_set_member_permissions():
    assert groups.set_member_permissions(group_peer, user_peer) is None
    assert groups.set_member_permissions(group_peer, user_peer,
                                                     [GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    assert groups.set_member_permissions(group_peer, user_peer, del_permissions=[
                                                                GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    assert groups.set_member_permissions(group_peer, user_peer,
                                                     [GROUPADMINPERMISSION_EDITSHORTNAME],
                                                     [GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    with raises(UnknownPeerError):
        assert groups.set_member_permissions(group_peer_invalid, user_peer)
        assert groups.set_member_permissions(group_peer, user_peer_invalid)
    with raises(ValueError):
        assert groups.set_member_permissions(group_peer, user_peer, add_permissions=["EDITSHORTNAME"])
        assert groups.set_member_permissions(group_peer, user_peer, del_permissions=["EDITSHORTNAME"])
    with raises(TypeError):
        assert groups.set_member_permissions(group_peer, user_peer, add_permissions=1)
        assert groups.set_member_permissions(group_peer, user_peer, del_permissions=1)


def test_get_group_member_permissions():
    assert isinstance(groups.get_group_member_permissions(group_peer, [user_peer]), list)
    with raises(UnknownPeerError):
        assert groups.get_group_member_permissions(group_peer_invalid, [user_peer])
        assert groups.get_group_member_permissions(group_peer, [user_peer_invalid])
    with raises(TypeError):
        assert groups.get_group_member_permissions(group_peer, user_peer)


def test_edit_group_title():
    assert groups.edit_group_title(group_peer, text) is None
    with raises(UnknownPeerError):
        assert groups.edit_group_title(group_peer_invalid, text)
    with raises(TypeError):
        assert groups.edit_group_title(group_peer, invalid_text)


def test_edit_avatar():
    assert groups.edit_avatar(group_peer, file) is None
    with raises(UnknownPeerError):
        assert groups.edit_avatar(group_peer_invalid, file)
    with raises(OSError):
        assert groups.edit_avatar(group_peer, invalid_text)
    with raises(FileNotFoundError):
        assert groups.edit_avatar(group_peer, text)


def test_remove_group_avatar():
    assert groups.remove_group_avatar(group_peer) is None
    with raises(UnknownPeerError):
        assert groups.remove_group_avatar(group_peer_invalid)


def test_edit_group_about():
    assert groups.edit_group_about(group_peer, text) is None
    with raises(UnknownPeerError):
        assert groups.edit_group_about(group_peer_invalid, text)
    with raises(TypeError):
        assert groups.edit_group_about(group_peer, invalid_text)


def test_leave_group():
    assert groups.leave_group(group_peer) is None
    with raises(UnknownPeerError):
        assert groups.leave_group(group_peer_invalid)


def test_make_user_admin():
    assert groups.make_user_admin(group_peer, user_peer, [GROUPADMINPERMISSION_EDITSHORTNAME]) is None
    with raises(UnknownPeerError):
        assert groups.make_user_admin(group_peer, user_peer_invalid, [GROUPADMINPERMISSION_EDITSHORTNAME])
        assert groups.make_user_admin(group_peer_invalid, user_peer, [GROUPADMINPERMISSION_EDITSHORTNAME])
    with raises(ValueError):
        assert groups.make_user_admin(group_peer, user_peer, ["EDITSHORTNAME"])
    with raises(TypeError):
        assert groups.make_user_admin(group_peer, user_peer, 1)


def test_transfer_ownership():
    assert groups.transfer_ownership(group_peer, user_peer) is None
    with raises(UnknownPeerError):
        assert groups.transfer_ownership(group_peer, user_peer_invalid)
        assert groups.transfer_ownership(group_peer_invalid, user_peer)


def test_get_group_invite_url():
    assert isinstance(groups.get_group_invite_url(group_peer), str)
    with raises(UnknownPeerError):
        assert groups.get_group_invite_url(group_peer_invalid)


def test_get_group_invite_url_base():
    assert isinstance(groups.get_group_invite_url_base(), str)


def test_revoke_invite_url():
    assert isinstance(groups.revoke_invite_url(group_peer), str)
    with raises(UnknownPeerError):
        assert groups.revoke_invite_url(group_peer_invalid)


def test_join_group():
    assert isinstance(groups.join_group(text), Group)
    with raises(TypeError):
        assert groups.join_group(invalid_text)


def test_join_group_by_peer():
    assert groups.join_group_by_peer(group_peer) is None
    with raises(UnknownPeerError):
        assert groups.join_group_by_peer(group_peer_invalid)


def test_delete_group():
    assert groups.delete_group(group_peer.id) is None
    assert groups.delete_group(group_peer) is None
    with raises(UnknownPeerError):
        assert groups.delete_group(group_peer_invalid)
