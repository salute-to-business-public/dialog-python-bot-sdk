import unittest

from dialog_api import messaging_pb2, peers_pb2, users_pb2, search_pb2, sequence_and_updates_pb2
from mock import patch
from tests.bot import bot
from tests.fake_classes import FakeDialog, FakeUsers, FakeUser, FakeFullProfile, FakeFullUser, FakeOutpeer, FakeSearch


class TestUsers(unittest.TestCase):
    outpeer = peers_pb2.OutPeer(
        type=peers_pb2.PEERTYPE_PRIVATE,
        id=0,
        access_hash=0
    )

    def test_get_user_peer_by_id(self):
        self.assertTrue(isinstance(bot.users.get_user_peer_by_id(0), peers_pb2.Peer))

    @patch('dialog_bot_sdk.users.Users._load_dialogs')
    def test_get_user_outpeer_by_id(self, load):
        self.assertIsNone(bot.users.get_user_outpeer_by_id(0), peers_pb2.Peer)
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadDialogs))
        load.return_value = FakeDialog()
        self.assertTrue(isinstance(bot.users.get_user_outpeer_by_id(0), peers_pb2.OutPeer))

    @patch('dialog_bot_sdk.users.Users._resolve_peer')
    def test_find_user_outpeer_by_nick(self, resolve):
        resolve.return_value = FakeOutpeer()
        self.assertIsNone(bot.users.find_user_outpeer_by_nick("bot"))
        resolve.return_value = FakeSearch()
        self.assertTrue(isinstance(resolve.call_args.args[0], search_pb2.RequestResolvePeer))
        self.assertEqual(bot.users.find_user_outpeer_by_nick("ne_bot"), "peer")

    @patch('dialog_bot_sdk.users.Users.find_user_outpeer_by_nick')
    @patch('dialog_bot_sdk.users.Users._get_reference_entities')
    def test_get_user_by_nick(self, entities, peer):
        entities.return_value = FakeUsers("bot")
        self.assertTrue(isinstance(bot.users.get_user_by_nick("bot"), FakeUser))
        self.assertTrue(isinstance(entities.call_args.args[0], sequence_and_updates_pb2.RequestGetReferencedEntitites))
        self.assertIsNone(bot.users.get_user_by_nick("ne_bot"))
        peer.return_value = peers_pb2.OutPeer(id=0, access_hash=0)
        self.assertIsNone(bot.users.get_user_by_nick("ne_bot"))

    @patch('dialog_bot_sdk.users.Users._load_full_users')
    @patch('dialog_bot_sdk.users.Users.find_user_outpeer_by_nick')
    def test_get_user_full_profile_by_nick(self, find, load):
        find.return_value = self.outpeer
        load.return_value = FakeFullProfile()
        self.assertIsNone(bot.users.get_user_full_profile_by_nick("bot"))
        self.assertTrue(isinstance(load.call_args.args[0], users_pb2.RequestLoadFullUsers))
        load.return_value = FakeFullProfile([FakeFullUser("custom_profile")])
        self.assertTrue(isinstance(bot.users.get_user_full_profile_by_nick("bot"), FakeFullUser))

    @patch('dialog_bot_sdk.users.Users.get_user_full_profile_by_nick')
    def test_get_user_custom_profile_by_nick(self, profile):
        profile.return_value = FakeFullUser()
        self.assertIsNone(bot.users.get_user_custom_profile_by_nick("bot"))
        profile.return_value = FakeFullUser("custom_profile")
        self.assertEqual(bot.users.get_user_custom_profile_by_nick("bot"), "custom_profile")

    @patch('dialog_bot_sdk.users.Users._load_full_users')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_get_user_custom_profile_by_peer(self, get_outpeer, load):
        get_outpeer.return_value = self.outpeer
        load.return_value = FakeFullProfile()
        self.assertIsNone(bot.users.get_user_custom_profile_by_peer("bot"))
        self.assertTrue(isinstance(load.call_args.args[0], users_pb2.RequestLoadFullUsers))
        load.return_value = FakeFullProfile([FakeFullUser()])
        self.assertIsNone(bot.users.get_user_custom_profile_by_peer("bot"))
        load.return_value = FakeFullProfile([FakeFullUser("custom_profile")])
        self.assertEqual(bot.users.get_user_custom_profile_by_peer("bot"), "custom_profile")

    @patch('dialog_bot_sdk.users.Users._get_reference_entities')
    @patch('dialog_bot_sdk.users.Users._peer_search')
    def test_search_users_by_nick_substring(self, search, entities):
        self.assertEqual(bot.users.search_users_by_nick_substring("bot"), [])
        entities.return_value = FakeUsers("bot")
        self.assertTrue(isinstance(bot.users.search_users_by_nick_substring("bot")[0], FakeUser))
        self.assertTrue(isinstance(search.call_args.args[0], search_pb2.RequestPeerSearch))


if __name__ == '__main__':
    unittest.main()
