import unittest

from dialog_api import media_and_files_pb2, messaging_pb2
from google.protobuf import wrappers_pb2
from mock import patch
from dialog_bot_sdk.utils import get_media

from tests.bot import bot


class TestGetMedia(unittest.TestCase):
    def test_get_str_val(self):
        self.assertTrue(isinstance(get_media.get_str_val("string"), wrappers_pb2.StringValue))

    def test_get_webpage(self):
        self.assertTrue(isinstance(get_media.get_webpage("https"), messaging_pb2.MessageMedia))
        self.assertTrue(isinstance(get_media.get_webpage("https", "title"), messaging_pb2.MessageMedia))
        self.assertTrue(isinstance(get_media.get_webpage("https", "title", "description"), messaging_pb2.MessageMedia))
        image_location = media_and_files_pb2.ImageLocation(file_location=
                                                           media_and_files_pb2.FileLocation(file_id=0, access_hash=0),
                                                           width=100, height=100)
        self.assertTrue(isinstance(get_media.get_webpage("https", "title", "description", image_location),
                                   messaging_pb2.MessageMedia))

    @patch('dialog_bot_sdk.uploading.Uploading.upload_file')
    def test_get_image_location(self, upload):
        with self.assertRaises(IOError):
            get_media.get_image_location(bot, "./files/test.mp3")
        upload.return_value = media_and_files_pb2.FileLocation(file_id=0, access_hash=0)
        self.assertTrue(isinstance(get_media.get_image_location(bot, "./files/test.png"),
                                   media_and_files_pb2.ImageLocation))
        self.assertEqual(upload.call_args.args[0], "./files/test.png")
        self.assertTrue(isinstance(get_media.get_image_location(bot, "./files/test.png", 100),
                                   media_and_files_pb2.ImageLocation))
        self.assertTrue(isinstance(get_media.get_image_location(bot, "./files/test.png", 100, 100),
                                   media_and_files_pb2.ImageLocation))

    @patch('dialog_bot_sdk.utils.get_media.get_image_location')
    def test_get_image(self, get):
        get.return_value = media_and_files_pb2.ImageLocation(file_location=
                                                             media_and_files_pb2.FileLocation(file_id=0, access_hash=0),
                                                             width=100, height=100)
        self.assertTrue(isinstance(get_media.get_image(bot, "./files/test.png"),
                                   messaging_pb2.MessageMedia))
        self.assertTrue(isinstance(get_media.get_image(bot, "./files/test.png", 100),
                                   messaging_pb2.MessageMedia))
        self.assertTrue(isinstance(get_media.get_image(bot, "./files/test.png", 100, 100),
                                   messaging_pb2.MessageMedia))
        self.assertEqual(get.call_args.args, (bot, "./files/test.png", 100, 100))

    @patch('dialog_bot_sdk.uploading.Uploading.upload_file')
    def test_get_audio(self, upload):
        with self.assertRaises(IOError):
            get_media.get_audio(bot, "./files/test.png")
            upload.return_value = media_and_files_pb2.FileLocation(file_id=0, access_hash=0)
            self.assertTrue(isinstance(get_media.get_audio(bot, "./files/test.mp3"),
                                       messaging_pb2.MessageMedia))
            self.assertTrue(isinstance(get_media.get_audio(bot, "./files/test.mp3", 2),
                                       messaging_pb2.MessageMedia))
            self.assertEqual(upload.call_args.args, (bot, "./files/test.mp3", 2))


if __name__ == '__main__':
    unittest.main()
