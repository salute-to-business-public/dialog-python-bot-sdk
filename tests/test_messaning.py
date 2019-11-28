import copy
import unittest
from dialog_api import peers_pb2, messaging_pb2, definitions_pb2, sequence_and_updates_pb2
from dialog_bot_sdk import interactive_media
from dialog_api.peers_pb2 import PEERTYPE_PRIVATE
from mock import patch

from tests.bot import bot
from dialog_bot_sdk.utils.get_media import get_webpage
from tests.fake_classes import FakeMessage, FakeEntities, FakeMessageFromSend


class TestMessaging(unittest.TestCase):

    test_file = "./files/test.png"
    test_image = test_file
    test_video = "./files/test.mov"
    test_audio = "./files/test.mp3"

    outpeer = peers_pb2.OutPeer(type=PEERTYPE_PRIVATE, id=0, access_hash=0)
    mid = definitions_pb2.UUIDValue(msb=0, lsb=0)
    msg_content = messaging_pb2.MessageContent()
    msg_content.textMessage.text = "Hello"
    group = [interactive_media.InteractiveMediaGroup(
        [
            interactive_media.InteractiveMedia(
                1,
                interactive_media.InteractiveMediaButton("Yes", "Да")
            ),
            interactive_media.InteractiveMedia(
                2,
                interactive_media.InteractiveMediaButton("No", "Нет")
            ),
        ]
    )]
    msg_content_with_group = copy.deepcopy(msg_content)
    group[0].render(msg_content_with_group.textMessage.media.add())
    doc_msg = messaging_pb2.DocumentMessage(
        file_id=0,
        access_hash=0,
        file_size=60,
        name=""
    )

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_send_message(self, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.send_message(None, "hello"))

        with self.assertRaises(AttributeError):
            self.assertRaises(bot.messaging.send_message(None, ""))

        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        bot.messaging.send_message(self.outpeer, "Hello")

        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

        bot.messaging.send_message(self.outpeer, "Hello", self.group)

        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('dialog_bot_sdk.messaging.Messaging._update_message')
    def test_update_message(self, update):
        message = FakeMessage(self.mid)

        bot.messaging.update_message(message, "Hello")

        self.assertTrue(isinstance(update.call_args.args[0], messaging_pb2.RequestUpdateMessage))

        bot.messaging.update_message(message, "Hello", self.group)

        args = update.call_args.args[0]
        self.assertTrue(isinstance(args, messaging_pb2.RequestUpdateMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.uploading.Uploading.upload_file')
    def test_send_file(self, upload, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.send_file(None, ""))
        upload.return_value = self.doc_msg
        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        bot.messaging.send_file(self.outpeer, self.test_file)
        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_send_media(self, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.send_media(None, ""))

        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        media = [get_webpage("dlg.im")]

        bot.messaging.send_media(self.outpeer, media)
        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.uploading.Uploading.upload_file')
    def test_send_image(self, upload, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.send_image(None, ""))
        with self.assertRaises(IOError):
            self.assertRaises(bot.messaging.send_image("peer", ""))

        upload.return_value = self.doc_msg
        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        with self.assertRaises(IOError):
            bot.messaging.send_image(self.outpeer, self.test_audio)

        bot.messaging.send_image(self.outpeer, self.test_image)
        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.uploading.Uploading.upload_file')
    def test_send_audio(self, upload, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.send_audio(None, ""))
        with self.assertRaises(IOError):
            self.assertRaises(bot.messaging.send_audio("peer", ""))

        upload.return_value = self.doc_msg
        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        with self.assertRaises(IOError):
            bot.messaging.send_audio(self.outpeer, self.test_image)

        bot.messaging.send_audio(self.outpeer, self.test_audio)
        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    @patch('dialog_bot_sdk.uploading.Uploading.upload_file')
    def test_send_video(self, upload, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.send_video(None, ""))
        with self.assertRaises(IOError):
            self.assertRaises(bot.messaging.send_video("peer", ""))
        upload.return_value = self.doc_msg
        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        with self.assertRaises(IOError):
            bot.messaging.send_video(self.outpeer, self.test_image)

        bot.messaging.send_video(self.outpeer, self.test_video)
        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_reply(self, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.reply(None, ""))

        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        bot.messaging.reply(self.outpeer, [self.mid])

        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

        bot.messaging.reply(self.outpeer, [self.mid], "hello", self.group)

        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

    @patch('dialog_bot_sdk.messaging.Messaging._load_history')
    def test_load_message_history(self, load):
        self.assertIsNone(bot.messaging.load_message_history(None))
        bot.messaging.load_message_history(self.outpeer)
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadHistory))
        bot.messaging.load_message_history(self.outpeer, 1)
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadHistory))
        bot.messaging.load_message_history(self.outpeer, 1, messaging_pb2.LISTLOADMODE_BACKWARD)
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadHistory))
        bot.messaging.load_message_history(self.outpeer, 1, messaging_pb2.LISTLOADMODE_BACKWARD, 1)
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadHistory))

    @patch('dialog_bot_sdk.messaging.Messaging._update')
    def test_delete(self, update):
        bot.messaging.delete([self.mid])
        self.assertTrue(isinstance(update.call_args.args[1], messaging_pb2.MessageContent))

    @patch('dialog_bot_sdk.messaging.Messaging._read')
    def test_read(self, read):
        bot.messaging.messages_read(self.outpeer, 0)
        self.assertTrue(isinstance(read.call_args.args[0], messaging_pb2.RequestMessageRead))

    @patch('dialog_bot_sdk.messaging.Messaging._get_referenced_entities')
    def test_get_message_by_id(self, entities):
        entities.return_value = FakeEntities()
        self.assertEqual(bot.messaging.get_messages_by_id([self.mid]), ["your message"])
        self.assertTrue(isinstance(entities.call_args.args[0], sequence_and_updates_pb2.RequestGetReferencedEntitites))

    @patch('dialog_bot_sdk.messaging.Messaging._update_message')
    def test_update(self, update):
        msg = messaging_pb2.MessageContent()
        with self.assertRaises(AttributeError):
            bot.messaging._update("1", msg)
        self.assertTrue(bot.messaging._update(FakeMessage(self.mid), msg))
        self.assertTrue(bot.messaging._update(FakeMessageFromSend(self.mid), msg))
        self.assertTrue(isinstance(update.call_args.args[0], messaging_pb2.RequestUpdateMessage))

    @patch('random.randint')
    @patch('dialog_bot_sdk.messaging.Messaging._send_message')
    @patch('dialog_bot_sdk.entity_manager.EntityManager.get_outpeer')
    def test_forward(self, get_outpeer, send, rnd):
        self.assertIsNone(bot.messaging.forward(None, ""))

        get_outpeer.return_value = self.outpeer
        rnd.return_value = 1

        bot.messaging.forward(self.outpeer, [self.mid])

        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))

        bot.messaging.forward(self.outpeer, [self.mid], "hello", self.group)

        self.assertTrue(isinstance(send.call_args.args[0], messaging_pb2.RequestSendMessage))


if __name__ == '__main__':
    unittest.main()