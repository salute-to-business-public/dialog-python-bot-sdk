import unittest

from dialog_api import groups_pb2, peers_pb2, search_pb2
from mock import patch

from tests.bot import bot
from tests.fake_classes import FakeSearch


class TestGroups(unittest.TestCase):
    @patch('dialog_bot_sdk.groups.Groups._create_group')
    def test_create_group(self, create):
        bot.groups.create_group("title", "username")
        self.assertTrue(isinstance(create.call_args.args[0], groups_pb2.RequestCreateGroup))
        bot.groups.create_group("title", "username", [peers_pb2.UserOutPeer(
            uid=0,
            access_hash=0
        )])
        self.assertTrue(isinstance(create.call_args.args[0], groups_pb2.RequestCreateGroup))

    @patch('dialog_bot_sdk.groups.Groups._peer_search')
    def test_find_group_by_shortname(self, search):
        search.return_value = FakeSearch()
        self.assertEqual(bot.groups.find_group_by_shortname("shortname"), ["group"])
        self.assertTrue(isinstance(search.call_args.args[0], search_pb2.RequestPeerSearch))


if __name__ == '__main__':
    unittest.main()
