import unittest

import grpc
from mock import patch

from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk.internal.bot import InternalBot


class TestBot(unittest.TestCase):
    @patch('dialog_bot_sdk.internal.bot.InternalBot.get_session_token')
    @patch('dialog_bot_sdk.internal.bot.InternalBot.anonymous_authorize')
    def test_get_insecure_bot(self, anon, token):
        token.return_value = "token"
        self.assertTrue(isinstance(DialogBot.get_insecure_bot("endpoint", None), DialogBot))
        self.assertTrue(anon.called)
        self.assertTrue(token.called)

    @patch('dialog_bot_sdk.internal.bot.InternalBot.get_session_token')
    @patch('dialog_bot_sdk.internal.bot.InternalBot.authorize')
    def test_get_secure_bot(self, auth, token):
        token.return_value = "token"
        self.assertTrue(isinstance(DialogBot.get_secure_bot("endpoint", grpc.ssl_channel_credentials(), "token"),
                                   DialogBot))
        self.assertEqual(auth.call_args.args[0], "token")
        self.assertTrue(token.called)


if __name__ == '__main__':
    unittest.main()
