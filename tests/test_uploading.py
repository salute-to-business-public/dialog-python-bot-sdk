import unittest

from dialog_api import media_and_files_pb2
from mock import patch

from tests.bot import bot
from tests.fake_classes import FakeUrl, FakePut
from dialog_bot_sdk import uploading


class TestUploading(unittest.TestCase):
    file = "./files/test.png"

    @patch('requests.put')
    @patch('dialog_bot_sdk.uploading.Uploading._get_file_upload_part_url')
    def test_upload_file_chunk(self, get_url, put):
        get_url.return_value = FakeUrl()
        put.return_value = FakePut(400)
        self.assertIsNone(bot.internal.uploading.upload_file_chunk(0, "chunk", b'key'))
        put.return_value = FakePut(200)
        self.assertTrue(isinstance(bot.internal.uploading.upload_file_chunk(0, "chunk", b'key'), FakePut))
        self.assertTrue(isinstance(get_url.call_args.args[0], media_and_files_pb2.RequestGetFileUploadPartUrl))
        self.assertEqual(put.call_args.args[0], "url")
        self.assertEqual(put.call_args_list[0].kwargs['data'], "chunk")
        self.assertEqual(put.call_args_list[0].kwargs['headers'], {'Content-Type': 'application/octet-stream'})
        upload = uploading.Uploading(bot.internal, b'cert', b'private_key', "access_dir")
        self.assertTrue(isinstance(upload.upload_file_chunk(0, "chunk", b'key'), FakePut))

    @patch('dialog_bot_sdk.uploading.Uploading.upload_file_chunk')
    @patch('dialog_bot_sdk.uploading.Uploading._commit_file_upload')
    @patch('dialog_bot_sdk.uploading.Uploading._get_file_upload_url')
    def test_upload_file(self, get_url, commit, chunk):
        upload = uploading.Uploading(bot.internal, b'cert', b'private_key', "access_dir")
        get_url.return_value = FakePut(upload_key=b'upload_key')
        commit.return_value = FakePut(uploaded_file_location="uploaded_file_location")
        self.assertEqual(upload.upload_file(self.file), "uploaded_file_location")
        self.assertTrue(isinstance(get_url.call_args.args[0], media_and_files_pb2.RequestGetFileUploadUrl))
        self.assertTrue(isinstance(commit.call_args.args[0], media_and_files_pb2.RequestCommitFileUpload))
        self.assertEqual(chunk.call_args.args[2], b'upload_key')
        self.assertEqual(chunk.call_args.args[3], "access_dir")
        chunk.return_value = None
        self.assertIsNone(upload.upload_file(self.file))


if __name__ == '__main__':
    unittest.main()
