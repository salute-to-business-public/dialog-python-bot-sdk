from .service import ManagedService
from .utils.read_file_in_chunks import read_file_in_chunks
from dialog_api import messaging_pb2, sequence_and_updates_pb2, media_and_files_pb2
from google.protobuf import empty_pb2
import time
import os
import requests


class Messaging(ManagedService):
    def send_message(self, peer, text, interactive_media_groups=None):
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)
        return self.internal.messaging.SendMessage(messaging_pb2.RequestSendMessage(
            peer=outpeer,
            rid=int(time.time()),
            message=msg
        )).mid

    def send_file(self, peer, file):
        location = self.upload_file(file)
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()
        content = messaging_pb2.DocumentMessage()
        content.file_id = location.file_id
        content.access_hash = location.access_hash
        content.name = os.path.basename(file)
        content.file_size = os.path.getsize(file)
        msg.documentMessage.CopyFrom(content)

        return self.internal.messaging.SendMessage(messaging_pb2.RequestSendMessage(
            peer=outpeer,
            rid=int(time.time()),
            message=msg
        )).mid

    def upload_file_chunk(self, part_number, chunk, upload_key):
        url = self.internal.media_and_files.GetFileUploadPartUrl(
            media_and_files_pb2.RequestGetFileUploadPartUrl(
                part_number=part_number,
                part_size=len(chunk),
                upload_key=upload_key
            )
        ).url

        put_response = requests.put(
            url,
            data=chunk,
            headers={'Content-Type': 'application/octet-stream'}
        )

        if put_response.status_code != 200:
            print('Can\'t upload file chunk')

        return put_response

    def upload_file(self, file, max_chunk_size=1024*1024):
        upload_key = self.internal.media_and_files.GetFileUploadUrl(
            media_and_files_pb2.RequestGetFileUploadUrl(
                expected_size=os.path.getsize(file)
            )
        ).upload_key

        for part_number, chunk in enumerate(
                read_file_in_chunks(
                    file, max_chunk_size
                )
        ):
            self.internal.thread_pool_executor.submit(
                self.upload_file_chunk(part_number, chunk, upload_key)
            )

        return self.internal.media_and_files.CommitFileUpload(
            media_and_files_pb2.RequestCommitFileUpload(
                upload_key=upload_key,
                file_name=os.path.basename(file)
            )
        ).uploaded_file_location

    def on_message(self, callback):
        for update in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
            up = sequence_and_updates_pb2.UpdateSeqUpdate()
            up.ParseFromString(update.update.value)
            if up.WhichOneof('update') == 'updateMessage':
                self.internal.thread_pool_executor.submit(
                    callback(up.updateMessage)
                )
