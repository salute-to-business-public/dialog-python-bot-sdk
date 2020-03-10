import unittest

from dialog_api.sequence_and_updates_pb2 import ResponseGetDifference

from dialog_bot_sdk.utils import AsyncTask
from tests.bot import bot
from tests.test_classes.updates import Updates


class TestUpdates(unittest.TestCase):
    bot.internal.updates = Updates()

    def test_get_difference(self):
        seq = bot.updates.get_difference(0)
        self.assertTrue(isinstance(seq, AsyncTask))
        self.assertTrue(isinstance(seq.wait(), ResponseGetDifference))

    def test_get_state(self):
        seq = bot.updates.get_state()
        self.assertTrue(isinstance(seq, AsyncTask))
        self.assertEqual(seq.wait(), 0)


if __name__ == '__main__':
    unittest.main()
