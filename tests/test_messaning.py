import unittest
from dialog_api import peers_pb2, messaging_pb2, definitions_pb2
from dialog_api.peers_pb2 import PEERTYPE_PRIVATE
from mock import patch

from dialog_bot_sdk.entities.ListLoadMode import ListLoadMode
from dialog_bot_sdk.entities.Peer import Peer
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.media.ImageMedia import ImageMedia, ImageLocation
from dialog_bot_sdk.entities.message.Message import Message, MessageContent
from dialog_bot_sdk.entities.message.TextMessage import MessageMedia
from dialog_bot_sdk.interactive_media import InteractiveMediaGroup, InteractiveMedia, InteractiveMediaButton
from dialog_bot_sdk.utils import AsyncTask
from tests.bot import bot
from tests.test_classes.media_and_files import MediaAndFiles, Put

from tests.test_classes.messaging import Messaging
from tests.test_classes.updates import Updates


class TestMessaging(unittest.TestCase):
    bot.internal.messaging = Messaging()
    bot.internal.updates = Updates()
    bot.internal.media_and_files = MediaAndFiles()

    test_file = "../dialog_bot_sdk/examples/files/example.png"

    peer = Peer(1, PEERTYPE_PRIVATE)
    message = Message(UUID(1, 1), UUID(0, 0), peer, None, [], [], 0, 0)
    outpeer = peers_pb2.OutPeer(type=PEERTYPE_PRIVATE, id=0, access_hash=0)
    mid = definitions_pb2.UUIDValue(msb=0, lsb=0)
    msg_content = messaging_pb2.MessageContent()
    msg_content.textMessage.text = "Hello"
    interactive_media = [InteractiveMediaGroup(
        [
            InteractiveMedia(
                "1",
                InteractiveMediaButton("Yes", "Да")
            ),
            InteractiveMedia(
                "2",
                InteractiveMediaButton("No", "Нет")
            ),
        ]
    )]
    # msg_content_with_group = copy.deepcopy(msg_content)
    # group[0].render(msg_content_with_group.textMessage.media.add())
    # doc_msg = messaging_pb2.DocumentMessage(
    #     file_id=0,
    #     access_hash=0,
    #     file_size=60,
    #     name=""
    # )

    def test_send_message(self):
        send = bot.messaging.send_message(self.peer, "text", self.interactive_media)
        self.assertTrue(isinstance(send, AsyncTask))
        self.assertTrue(isinstance(send.wait(), UUID))

    def test_update_message(self):
        update = bot.messaging.update_message(self.message, "text", self.interactive_media)
        self.assertTrue(isinstance(update, AsyncTask))
        self.assertIsNone(update.wait())

    def test_delete_message(self):
        delete = bot.messaging.delete(self.message)
        self.assertTrue(isinstance(delete, AsyncTask))
        self.assertIsNone(delete.wait())

    def test_get_messages_by_id(self):
        msg = bot.messaging.get_messages_by_id([UUID(1, 1)])
        self.assertTrue(isinstance(msg, AsyncTask))
        self.assertTrue(isinstance(msg.wait()[0], Message))

    def test_messages_read(self):
        read = bot.messaging.messages_read(self.peer, 0)
        self.assertTrue(isinstance(read, AsyncTask))
        self.assertIsNone(read.wait())

    @patch('requests.put')
    def test_send_file(self, put):
        put.return_value = Put(200)
        send = bot.messaging.send_file(self.peer, self.test_file)
        self.assertTrue(isinstance(send, AsyncTask))
        self.assertTrue(isinstance(send.wait(), UUID))
        put.return_value = Put(400)
        send = bot.messaging.send_file(self.peer, self.test_file)
        self.assertTrue(isinstance(send, AsyncTask))
        self.assertIsNone(send.wait())

    @patch('requests.put')
    def test_send_media(self, put):
        put.return_value = Put(200)
        image = bot.internal.uploading.upload_file(self.test_file).wait()
        media = MessageMedia(image=ImageMedia(ImageLocation(image)))
        send = bot.messaging.send_media(self.peer, [media])
        self.assertTrue(isinstance(send, AsyncTask))
        self.assertTrue(isinstance(send.wait(), UUID))

    @patch('requests.put')
    def test_send_image(self, put):
        put.return_value = Put(200)
        send = bot.messaging.send_image(self.peer, self.test_file)
        self.assertTrue(isinstance(send, AsyncTask))
        self.assertTrue(isinstance(send.wait(), UUID))
        put.return_value = Put(400)
        send = bot.messaging.send_image(self.peer, self.test_file)
        self.assertTrue(isinstance(send, AsyncTask))
        self.assertIsNone(send.wait())

    def test_reply(self):
        reply = bot.messaging.reply(self.peer, [UUID(1, 1)], None, self.interactive_media)
        self.assertTrue(isinstance(reply, AsyncTask))
        self.assertTrue(isinstance(reply.wait(), UUID))

    def test_forward(self):
        forward = bot.messaging.forward(self.peer, [UUID(1, 1)], None, self.interactive_media)
        self.assertTrue(isinstance(forward, AsyncTask))
        self.assertTrue(isinstance(forward.wait(), UUID))

    def test_load_message_history(self):
        history = bot.messaging.load_message_history(self.peer, 0, ListLoadMode.LISTLOADMODE_BACKWARD, 1)
        self.assertTrue(isinstance(history, AsyncTask))
        self.assertTrue(isinstance(history.wait()[0], Message))


if __name__ == '__main__':
    unittest.main()
