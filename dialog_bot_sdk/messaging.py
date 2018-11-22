from .service import ManagedService
from dialog_api import messaging_pb2, sequence_and_updates_pb2
from dialog_bot_sdk.content import content
from google.protobuf import empty_pb2
import time


class Messaging(ManagedService):
    """Main messaging class.

    """
    def send_message(self, peer, text, interactive_media_groups=None):
        """Send text message to current peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: receiver's peer
        :param text: message text
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: mid value of SendMessage response object
        """
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
        """Send file to current peer.

        :param peer: receiver's peer
        :param file: path to file
        :return: mid value of SendMessage response object
        """
        location = self.internal.uploading.upload_file(file)
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_document_content(file, location)
        )

        return self.internal.messaging.SendMessage(messaging_pb2.RequestSendMessage(
            peer=outpeer,
            rid=int(time.time()),
            message=msg
        )).mid

    def send_image(self, peer, file):
        """Send image as image (not as file) to current peer.

        :param peer: receiver's peer
        :param file: path to image file
        :return: mid value of SendMessage response object
        """

        location = self.internal.uploading.upload_file(file)
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_image_content(file, location)
        )

        return self.internal.messaging.SendMessage(messaging_pb2.RequestSendMessage(
            peer=outpeer,
            rid=int(time.time()),
            message=msg
        )).mid

    def on_message(self, callback):
        """Message receiving event handler.

        :param callback: function that will be called when message received
        :return: None
        """

        for update in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
            up = sequence_and_updates_pb2.UpdateSeqUpdate()
            up.ParseFromString(update.update.value)
            if up.WhichOneof('update') == 'updateMessage':
                self.internal.thread_pool_executor.submit(
                    callback(up.updateMessage)
                )
