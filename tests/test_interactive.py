import unittest

from dialog_api import messaging_pb2, peers_pb2
from dialog_api.peers_pb2 import PEERTYPE_PRIVATE
from mock import patch

from dialog_bot_sdk import interactive_media
from tests.bot import bot


class TestInteractive(unittest.TestCase):
    def test_confirm(self):
        confirm = interactive_media.InteractiveMediaConfirm("text", "title", "ok", "dismiss")
        self.assertTrue(isinstance(confirm.render(), messaging_pb2.InteractiveMediaConfirm))
        confirm = interactive_media.InteractiveMediaConfirm("text", "title", "ok")
        self.assertTrue(isinstance(confirm.render(), messaging_pb2.InteractiveMediaConfirm))
        confirm = interactive_media.InteractiveMediaConfirm("text", "title")
        self.assertTrue(isinstance(confirm.render(), messaging_pb2.InteractiveMediaConfirm))
        confirm = interactive_media.InteractiveMediaConfirm("text")
        self.assertTrue(isinstance(confirm.render(), messaging_pb2.InteractiveMediaConfirm))
        confirm = interactive_media.InteractiveMediaConfirm()
        self.assertTrue(isinstance(confirm.render(), messaging_pb2.InteractiveMediaConfirm))

    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_button_and_media(self, get, send):
        get.return_value = peers_pb2.OutPeer(type=PEERTYPE_PRIVATE, id=0, access_hash=0)
        confirm = interactive_media.InteractiveMediaConfirm()
        button = interactive_media.InteractiveMediaButton("value", "label")
        interactive = interactive_media.InteractiveMedia(1, button, 'default', confirm)
        group = interactive_media.InteractiveMediaGroup([interactive])
        bot.messaging.send_message("peer", "text", [group])
        media = send.call_args.args[0].message.textMessage.media[0]
        self.assertTrue(isinstance(media, messaging_pb2.MessageMedia))
        actions_group = media.actions[0]
        self.assertTrue(isinstance(actions_group, messaging_pb2.InteractiveMediaGroup))
        actions = actions_group.actions[0]
        self.assertTrue(isinstance(actions, messaging_pb2.InteractiveMedia))
        self.assertTrue(isinstance(actions.widget.interactiveMediaButton, messaging_pb2.InteractiveMediaButton))
        self.assertEqual(actions.id, '1')
        self.assertEqual(actions.style, 1)
        self.assertTrue(isinstance(actions.confirm, messaging_pb2.InteractiveMediaConfirm))
        self.assertEqual(actions.widget.interactiveMediaButton.value, 'value')
        self.assertEqual(actions.widget.interactiveMediaButton.label.value, 'label')

    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_select_and_media(self, get, send):
        get.return_value = peers_pb2.OutPeer(type=PEERTYPE_PRIVATE, id=0, access_hash=0)
        with self.assertRaises(AttributeError):
            interactive_media.InteractiveMediaSelect(None)
        select = interactive_media.InteractiveMediaSelect({"yes": "true", "no": "false"}, "yes", "true")
        interactive = interactive_media.InteractiveMedia(1, select)
        group = interactive_media.InteractiveMediaGroup([interactive])
        bot.messaging.send_message("peer", "text", [group])
        i_select = send.call_args.args[0].message.textMessage.media[0].actions[0].actions[0].\
            widget.interactiveMediaSelect
        self.assertTrue(isinstance(i_select, messaging_pb2.InteractiveMediaSelect))
        self.assertTrue(isinstance(i_select.options[0], messaging_pb2.InteractiveMediaSelectOption))
        self.assertEqual(i_select.label.value, 'yes')
        self.assertEqual(i_select.default_value.value, 'true')

    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_group(self, get, send):
        get.return_value = peers_pb2.OutPeer(type=PEERTYPE_PRIVATE, id=0, access_hash=0)
        with self.assertRaises(AttributeError):
            interactive_media.InteractiveMediaGroup("not_list")
        button = interactive_media.InteractiveMediaButton("value", "label")
        interactive = interactive_media.InteractiveMedia(1, button)
        group = interactive_media.InteractiveMediaGroup([interactive], "title", "description",
                                                        {"lang": {"id": "value"}})
        bot.messaging.send_message("peer", "text", [group])
        group_args = send.call_args.args[0].message.textMessage.media[0].actions[0]
        self.assertEqual(group_args.description.value, 'description')
        self.assertEqual(group_args.title.value, 'title')
        self.assertTrue(isinstance(group_args.translations[0], messaging_pb2.InteractiveMediaTranslationGroup))
        self.assertEqual(group_args.translations[0].language, "lang")
        self.assertEqual(group_args.translations[0].messages[0].id, 'id')
        self.assertEqual(group_args.translations[0].messages[0].value, 'value')


if __name__ == '__main__':
    unittest.main()
