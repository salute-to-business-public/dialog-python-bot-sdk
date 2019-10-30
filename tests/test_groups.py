import unittest

from dialog_api import search_pb2, groups_pb2, peers_pb2, media_and_files_pb2, sequence_and_updates_pb2
from mock import patch

from tests.bot import bot
from tests.fake_classes import FakeSearch, FakeSearchResult, FakeMembers


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


if __name__ == '__main__':
    unittest.main()
