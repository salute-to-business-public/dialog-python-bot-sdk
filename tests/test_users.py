import unittest

import grpc
from dialog_api import messaging_pb2, peers_pb2, contacts_pb2, users_pb2, search_pb2
from mock import patch
from dialog_bot_sdk.bot import DialogBot
from tests.fake_classes import FakeDialog, FakeUsers, FakeUser, FakeFullProfile, FakeFullUser


class TestUsers(unittest.TestCase):
    bot = DialogBot.get_secure_bot(
        '',                                 # bot endpoint from environment
        grpc.ssl_channel_credentials(),     # SSL credentials (empty by default!)
        ''                                  # bot token from environment
    )

    outpeer = peers_pb2.OutPeer(
        type=peers_pb2.PEERTYPE_PRIVATE,
        id=0,
        access_hash=0
    )

    def test_get_user_peer_by_id(self):
        self.assertTrue(isinstance(self.bot.users.get_user_peer_by_id(0), peers_pb2.Peer))

    @patch('dialog_bot_sdk.users.Users._load_dialogs')
    def test_get_user_outpeer_by_id(self, load):
        self.assertIsNone(self.bot.users.get_user_outpeer_by_id(0), peers_pb2.Peer)
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadDialogs))
        load.return_value = FakeDialog()
        self.assertTrue(isinstance(self.bot.users.get_user_outpeer_by_id(0), peers_pb2.OutPeer))

    @patch('dialog_bot_sdk.users.Users._search_contacts')
    def test_find_user_outpeer_by_nick(self, search):
        search.return_value = FakeUsers("bot")
        self.assertTrue(isinstance(self.bot.users.find_user_outpeer_by_nick("bot"), peers_pb2.OutPeer))
        self.assertTrue(isinstance(search.call_args.args[0], contacts_pb2.RequestSearchContacts))
        self.assertIsNone(self.bot.users.find_user_outpeer_by_nick("ne_bot"))

    @patch('dialog_bot_sdk.users.Users._search_contacts')
    def test_get_user_by_nick(self, search):
        search.return_value = FakeUsers("bot")
        self.assertTrue(isinstance(self.bot.users.get_user_by_nick("bot"), FakeUser))
        self.assertTrue(isinstance(search.call_args.args[0], contacts_pb2.RequestSearchContacts))
        self.assertIsNone(self.bot.users.get_user_by_nick("ne_bot"))

    @patch('dialog_bot_sdk.users.Users._load_full_users')
    @patch('dialog_bot_sdk.users.Users.find_user_outpeer_by_nick')
    def test_get_user_full_profile_by_nick(self, find, load):
        find.return_value = self.outpeer
        load.return_value = FakeFullProfile()
        self.assertIsNone(self.bot.users.get_user_full_profile_by_nick("bot"))
        self.assertTrue(isinstance(load.call_args.args[0], users_pb2.RequestLoadFullUsers))
        load.return_value = FakeFullProfile([FakeFullUser("custom_profile")])
        self.assertTrue(isinstance(self.bot.users.get_user_full_profile_by_nick("bot"), FakeFullUser))

    @patch('dialog_bot_sdk.users.Users.get_user_full_profile_by_nick')
    def test_get_user_custom_profile_by_nick(self, profile):
        profile.return_value = FakeFullUser()
        self.assertIsNone(self.bot.users.get_user_custom_profile_by_nick("bot"))
        profile.return_value = FakeFullUser("custom_profile")
        self.assertEqual(self.bot.users.get_user_custom_profile_by_nick("bot"), "custom_profile")

    @patch('dialog_bot_sdk.users.Users._load_full_users')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_get_user_custom_profile_by_peer(self, get_outpeer, load):
        get_outpeer.return_value = self.outpeer
        load.return_value = FakeFullProfile()
        self.assertIsNone(self.bot.users.get_user_custom_profile_by_peer("bot"))
        self.assertTrue(isinstance(load.call_args.args[0], users_pb2.RequestLoadFullUsers))
        load.return_value = FakeFullProfile([FakeFullUser()])
        self.assertIsNone(self.bot.users.get_user_custom_profile_by_peer("bot"))
        load.return_value = FakeFullProfile([FakeFullUser("custom_profile")])
        self.assertEqual(self.bot.users.get_user_custom_profile_by_peer("bot"), "custom_profile")

    @patch('dialog_bot_sdk.users.Users._peer_search')
    def test_search_users_by_nick_substring(self, search):
        search.return_value = FakeUsers("bot")
        self.assertTrue(isinstance(self.bot.users.search_users_by_nick_substring("bot")[0], FakeUser))
        self.assertTrue(isinstance(search.call_args.args[0], search_pb2.RequestPeerSearch))

    def test_get_user_outpeer_by_outpeer(self):
        self.assertTrue(isinstance(self.bot.users.get_user_outpeer_by_outpeer(self.outpeer), peers_pb2.UserOutPeer))


if __name__ == '__main__':
    unittest.main()
