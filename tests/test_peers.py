import unittest

from dialog_api import search_pb2
from mock import patch

from dialog_bot_sdk import peers
from tests.bot import bot
from tests.fake_classes import FakeSearch


class TestPeers(unittest.TestCase):
    @patch('dialog_bot_sdk.peers.Peers._resolve_peer')
    def test_resolve_peer(self, resolve):
        resolve.return_value = FakeSearch()
        self.assertEqual(bot.peers.resolve_peer("shortname"), "peer")
        self.assertTrue(isinstance(resolve.call_args.args[0], search_pb2.RequestResolvePeer))


if __name__ == '__main__':
    unittest.main()
