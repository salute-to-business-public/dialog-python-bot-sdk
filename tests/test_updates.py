import unittest

from dialog_api import sequence_and_updates_pb2
from mock import patch

from tests.bot import bot
from tests.fake_classes import FakeState


class TestUpdates(unittest.TestCase):
    @patch('dialog_bot_sdk.updates.Updates._get_difference')
    def test_get_difference(self, diff):
        bot.updates.get_difference(1337)
        self.assertTrue(isinstance(diff.call_args.args[0], sequence_and_updates_pb2.RequestGetDifference))

    @patch('dialog_bot_sdk.updates.Updates._get_state')
    def test_get_state(self, state):
        state.return_value = FakeState()
        self.assertEqual(bot.updates.get_state(), 1)
        self.assertTrue(isinstance(state.call_args.args[0], sequence_and_updates_pb2.RequestGetState))


if __name__ == '__main__':
    unittest.main()
