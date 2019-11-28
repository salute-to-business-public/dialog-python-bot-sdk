import unittest

from dialog_api import search_pb2, groups_pb2, peers_pb2, media_and_files_pb2, sequence_and_updates_pb2
from mock import patch

from tests.bot import bot
from tests.fake_classes import FakeSearch, FakeSearchResult, FakeMembers, FakeUrl


class TestGroups(unittest.TestCase):
    group_outpeer = peers_pb2.OutPeer(id=0, access_hash=0, type=peers_pb2.PEERTYPE_GROUP)
    group_peer = peers_pb2.Peer(id=0, type=peers_pb2.PEERTYPE_GROUP)
    user1 = peers_pb2.OutPeer(id=0, access_hash=0, type=peers_pb2.PEERTYPE_PRIVATE)
    user2 = peers_pb2.OutPeer(id=0, access_hash=0, type=peers_pb2.PEERTYPE_PRIVATE)
    test_file = "./files/test.png"

    @patch('dialog_bot_sdk.groups.Groups._peer_search')
    def test_find_group_by_shortname(self, search):
        search.return_value = FakeSearch("shortname")
        self.assertTrue(isinstance(bot.groups.find_group_by_shortname("shortname"), FakeSearchResult))
        self.assertTrue(isinstance(search.call_args.args[0], search_pb2.RequestPeerSearch))

    @patch('dialog_bot_sdk.groups.Groups._create_group')
    def test_create_group(self, create):
        create.return_value = "group"
        self.assertEqual(bot.groups.create_private_group("title"), "group")
        self.assertTrue(isinstance(create.call_args.args[0], groups_pb2.RequestCreateGroup))
        self.assertEqual(bot.groups.create_private_channel("title"), "group")
        self.assertTrue(isinstance(create.call_args.args[0], groups_pb2.RequestCreateGroup))
        self.assertEqual(bot.groups.create_public_group("title", "shortname"), "group")
        self.assertTrue(isinstance(create.call_args.args[0], groups_pb2.RequestCreateGroup))
        self.assertEqual(bot.groups.create_public_channel("title", "shortname"), "group")
        self.assertTrue(isinstance(create.call_args.args[0], groups_pb2.RequestCreateGroup))

    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.groups.Groups._kick_user')
    def test_kick_group(self, kick, get_outpeer):
        get_outpeer.return_value = self.group_outpeer
        kick.return_value = 1
        self.assertEqual(bot.groups.kick_users(self.group_peer, [self.user1, self.user2]), [1, 1])
        self.assertTrue(isinstance(kick.call_args.args[0], groups_pb2.RequestKickUser))

    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.groups.Groups._invite_user')
    def test_invite_group(self, invite, get_outpeer):
        get_outpeer.return_value = self.group_outpeer
        invite.return_value = 1
        self.assertEqual(bot.groups.invite_users(self.group_peer, [self.user1, self.user2]), [1, 1])
        self.assertTrue(isinstance(invite.call_args.args[0], groups_pb2.RequestInviteUser))

    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.groups.Groups._set_default_group_permissions')
    def test_set_default_group_permissions(self, permission, get_outpeer):
        get_outpeer.return_value = self.group_outpeer
        self.assertIsNone(bot.groups.set_default_group_permissions(self.group_peer))
        self.assertIsNone(bot.groups.set_default_group_permissions(self.group_peer, ['kick']))
        self.assertTrue(isinstance(permission.call_args.args[0], groups_pb2.RequestEditGroupBasePermissions))
        self.assertIsNone(bot.groups.set_default_group_permissions(self.group_peer, None,  ['invite']))
        self.assertTrue(isinstance(permission.call_args.args[0], groups_pb2.RequestEditGroupBasePermissions))

    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.groups.Groups._set_member_permissions')
    def test_set_member_permissions(self, permission, get_outpeer):
        get_outpeer.return_value = self.group_outpeer
        self.assertIsNone(bot.groups.set_member_permissions(self.group_peer, self.user1))
        self.assertIsNone(bot.groups.set_member_permissions(self.group_peer, self.user1, ['kick']))
        self.assertTrue(isinstance(permission.call_args.args[0], groups_pb2.RequestEditMemberPermissions))
        self.assertIsNone(bot.groups.set_member_permissions(self.group_peer, self.user1, None, ['invite']))
        self.assertTrue(isinstance(permission.call_args.args[0], groups_pb2.RequestEditMemberPermissions))

    @patch('dialog_bot_sdk.groups.Groups._upload')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.groups.Groups._edit_group_avatar')
    def test_edit_avatar(self, avatar, get_outpeer, upload):
        get_outpeer.return_value = self.group_outpeer
        upload.return_value = media_and_files_pb2.FileLocation(file_id=0, access_hash=0)
        self.assertTrue(bot.groups.edit_avatar(self.group_peer.id, self.test_file))
        self.assertTrue(isinstance(avatar.call_args.args[0], groups_pb2.RequestEditGroupAvatar))

    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_get_outpeer(self, get_outpeer):
        self.assertTrue(bot.groups.get_outpeer(0))

    @patch('dialog_bot_sdk.groups.Groups._get_referenced_entities')
    @patch('dialog_bot_sdk.groups.Groups._load_members')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_load_members(self, get_outpeer, load, entities):
        get_outpeer.return_value = self.group_outpeer
        load.return_value = FakeMembers()
        self.assertTrue(bot.groups.load_members(self.group_peer))
        self.assertTrue(isinstance(load.call_args.args[0], groups_pb2.RequestLoadMembers))
        self.assertTrue(isinstance(entities.call_args.args[0], sequence_and_updates_pb2.RequestGetReferencedEntitites))

    @patch('dialog_bot_sdk.groups.Groups._get_referenced_entities')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_find_group_by_id(self, get_outpeer, entities):
        get_outpeer.return_value = self.group_outpeer
        entities.return_value = FakeSearch()
        self.assertEqual(bot.groups.find_group_by_id(self.group_peer.id), "group")
        self.assertTrue(isinstance(entities.call_args.args[0], sequence_and_updates_pb2.RequestGetReferencedEntitites))

    @patch('dialog_bot_sdk.groups.Groups._edit_group_title')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_edit_group_title(self, get_outpeer, title):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.edit_group_title(self.group_peer, "title")
        self.assertTrue(isinstance(title.call_args.args[0], groups_pb2.RequestEditGroupTitle))

    @patch('dialog_bot_sdk.groups.Groups._upload')
    @patch('dialog_bot_sdk.groups.Groups._edit_group_avatar')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_edit_avatar(self, get_outpeer, avatar, upload):
        get_outpeer.return_value = self.group_outpeer
        upload.return_value = media_and_files_pb2.FileLocation()
        bot.groups.edit_avatar(self.group_peer.id, "avatar")
        self.assertEqual(upload.call_args.args[0], "avatar")
        self.assertTrue(isinstance(avatar.call_args.args[0], groups_pb2.RequestEditGroupAvatar))

    @patch('dialog_bot_sdk.groups.Groups._remove_group_avatar')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_remove_group_avatar(self, get_outpeer, avatar):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.remove_group_avatar(self.group_peer)
        self.assertTrue(isinstance(avatar.call_args.args[0], groups_pb2.RequestRemoveGroupAvatar))

    @patch('dialog_bot_sdk.groups.Groups._edit_group_about')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_edit_group_about(self, get_outpeer, about):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.edit_group_about(self.group_peer, "about")
        self.assertTrue(isinstance(about.call_args.args[0], groups_pb2.RequestEditGroupAbout))

    @patch('dialog_bot_sdk.groups.Groups._leave_group')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_leave_group(self, get_outpeer, leave):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.leave_group(self.group_peer)
        self.assertTrue(isinstance(leave.call_args.args[0], groups_pb2.RequestLeaveGroup))

    @patch('dialog_bot_sdk.groups.Groups._make_user_admin')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_make_user_admin(self, get_outpeer, make_user_admin):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.make_user_admin(self.group_peer, self.user1, ["invite"])
        self.assertTrue(isinstance(make_user_admin.call_args.args[0], groups_pb2.RequestMakeUserAdmin))

    @patch('dialog_bot_sdk.groups.Groups._make_user_admin')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_make_user_admin(self, get_outpeer, make_user_admin):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.make_user_admin(self.group_peer, self.user1, ["invite"])
        self.assertTrue(isinstance(make_user_admin.call_args.args[0], groups_pb2.RequestMakeUserAdmin))

    @patch('dialog_bot_sdk.groups.Groups._get_group_member_permissions')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_get_group_member_permissions(self, get_outpeer, get_group_member_permissions):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.get_group_member_permissions(self.group_peer, self.user1)
        self.assertTrue(isinstance(get_group_member_permissions.call_args.args[0],
                                   groups_pb2.RequestGetGroupMemberPermissions))

    @patch('dialog_bot_sdk.groups.Groups._transfer_ownership')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_transfer_ownership(self, get_outpeer, transfer_ownership):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.transfer_ownership(self.group_peer, self.user1)
        self.assertTrue(isinstance(transfer_ownership.call_args.args[0],
                                   groups_pb2.RequestTransferOwnership))

    @patch('dialog_bot_sdk.groups.Groups._get_group_invite_url')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_get_group_invite_url(self, get_outpeer, get_group_invite_url):
        get_outpeer.return_value = self.group_outpeer
        get_group_invite_url.return_value = FakeUrl()
        self.assertEqual(bot.groups.get_group_invite_url(self.group_peer), "url")
        self.assertTrue(isinstance(get_group_invite_url.call_args.args[0],
                                   groups_pb2.RequestGetGroupInviteUrl))

    @patch('dialog_bot_sdk.groups.Groups._get_group_invite_url_base')
    def test_get_group_invite_url_base(self, get_group_invite_url_base):
        get_group_invite_url_base.return_value = FakeUrl()
        self.assertEqual(bot.groups.get_group_invite_url_base(), "url")
        self.assertTrue(isinstance(get_group_invite_url_base.call_args.args[0],
                                   groups_pb2.RequestGetGroupInviteUrlBase))

    @patch('dialog_bot_sdk.groups.Groups._revoke_invite_url')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_revoke_invite_url(self, get_outpeer, revoke_invite_url):
        get_outpeer.return_value = self.group_outpeer
        revoke_invite_url.return_value = FakeUrl()
        self.assertEqual(bot.groups.revoke_invite_url(self.group_peer), "url")
        self.assertTrue(isinstance(revoke_invite_url.call_args.args[0],
                                   groups_pb2.RequestRevokeInviteUrl))

    @patch('dialog_bot_sdk.groups.Groups._join_group')
    def test_join_group(self, join_group):
        bot.groups.join_group("url")
        self.assertTrue(isinstance(join_group.call_args.args[0],
                                   groups_pb2.RequestJoinGroup))

    @patch('dialog_bot_sdk.groups.Groups._join_group_by_peer')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_join_group_by_peer(self, get_outpeer, join_group_by_peer):
        get_outpeer.return_value = self.group_outpeer
        bot.groups.join_group_by_peer(self.group_peer)
        self.assertTrue(isinstance(join_group_by_peer.call_args.args[0],
                                   groups_pb2.RequestJoinGroupByPeer))


if __name__ == '__main__':
    unittest.main()
