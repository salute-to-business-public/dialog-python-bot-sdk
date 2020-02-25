import unittest

from dialog_api import peers_pb2

from dialog_bot_sdk.entities.FullUser import FullUser
from dialog_bot_sdk.entities.User import User
from dialog_bot_sdk.utils import AsyncTask
from tests.bot import bot
from tests.test_classes.messaging import Messaging
from tests.test_classes.search import Search
from tests.test_classes.updates import Updates
from tests.test_classes.users import Users


class TestUsers(unittest.TestCase):
    out_peer = peers_pb2.OutPeer(
        type=peers_pb2.PEERTYPE_PRIVATE,
        id=0,
        access_hash=0
    )
    bot.internal.search = Search()
    bot.internal.updates = Updates()
    bot.internal.messaging = Messaging()
    bot.internal.users = Users()

    def test_get_user_by_nick(self):
        user = bot.users.get_user_by_nick("name")
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertIsNone(user.wait())
        user = bot.users.get_user_by_nick("nick")
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertTrue(isinstance(user.wait(), User))

    def test_get_user_by_id(self):
        user = bot.users.get_user_by_id(0)
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertIsNone(user.wait())
        user = bot.users.get_user_by_id(1)
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertTrue(isinstance(user.wait(), User))

    def test_search_users_by_nick_substring(self):
        user = bot.users.search_users_by_nick_substring("name")
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertEqual(user.wait(), [])
        user = bot.users.search_users_by_nick_substring("nick")
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertTrue(isinstance(user.wait()[0], User))

    def test_get_full_profile_by_nick(self):
        user = bot.users.get_full_profile_by_nick("nick")
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertTrue(isinstance(user.wait(), FullUser))

    def test_get_full_profile_by_id(self):
        user = bot.users.get_full_profile_by_id(0)
        self.assertTrue(isinstance(user, AsyncTask))
        self.assertIsNone(user.wait())


if __name__ == '__main__':
    unittest.main()
