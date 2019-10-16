import time

from google.protobuf import empty_pb2
import threading
import random
import grpc

from .service import ManagedService
from dialog_api import messaging_pb2, sequence_and_updates_pb2
from .content import content
from .utils.get_image_metadata import is_image
from .utils.get_video_metadata import is_video
from .utils.get_audio_metadata import is_audio


class Messaging(ManagedService):
    """Main messaging class.

    """
    def send_message(self, peer, text, interactive_media_groups=None, uid=None):
        """Send text message to current peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: receiver's peer
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :param uid: send message only for user by id
        :return: value of SendMessage response object
        """

        if text == '' or text is None:
            raise AttributeError('Text message must contain some text.')

        if not peer:
            print('Peer can\'t be None!')
            return None

        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)
        request = messaging_pb2.RequestSendMessage(
            peer=outpeer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            is_only_for_user=uid
        )
        return self._send_message(request)

    def update_message(self, message, text, interactive_media_groups=None):
        """Update text message or interactive media (buttons, selects etc.).
        :param message object received from any send method (send_message, send_file etc.)
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: value of UpdateMessage response object
        """
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)

        # TODO: uncomment after 0.3.3 version
        # if message.edited_at.value:
        #     last_edited_at = message.edited_at.value
        # else:
        #     last_edited_at = int(time.time() * 1000)
        last_edited_at = int(time.time() * 1000)
        request = messaging_pb2.RequestUpdateMessage(
            mid=message.mid,
            updated_message=msg,
            last_edited_at=last_edited_at
        )
        return self._update_message(request)

    def delete(self, mids):
        """Delete text messages or interactive media (buttons, selects etc.).

        :param mids array objects received from any send method (send_message, send_file etc.)
        """
        request = messaging_pb2.RequestDeleteMessageObsolete(
            mids=mids
        )
        self._delete(request)

    def messages_read(self, peer, date):
        """Marking a message and all previous as read

        :param peer - chat peer
        :param date - date of message
        """
        request = messaging_pb2.RequestMessageRead(
            peer=peer,
            date=date
        )
        self._read(request)

    def send_file(self, peer, file):
        """Send file to current peer.

        :param peer: receiver's peer
        :param file: path to file
        :return: value of SendMessage response object
        """
        if not peer:
            print('Peer can\'t be None!')
            return None

        location = self.internal.uploading.upload_file(file)
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_document_content(file, location)
        )

        request = messaging_pb2.RequestSendMessage(
            peer=outpeer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self._send_message(request)

    def send_media(self, peer, medias):
        """Send media to current peer.

        :param peer: receiver's peer
        :param medias: medias (list)
        :return: value of SendMessage response object
        """
        if not peer:
            print('Peer can\'t be None!')
            return None
        outpeer = self.manager.get_outpeer(peer)
        text_message = messaging_pb2.TextMessage()
        for media in medias:
            text_message.media.append(media)
        msg = messaging_pb2.MessageContent(textMessage=text_message)

        request = messaging_pb2.RequestSendMessage(
            peer=outpeer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self._send_message(request)

    def send_image(self, peer, file):
        """Send image as image (not as file) to current peer.

        :param peer: receiver's peer
        :param file: path to image file
        :return: value of SendMessage response object
        """
        if not peer:
            print('Peer can\'t be None!')
            return None

        if not is_image(file):
            raise IOError('File is not an image.')
        location = self.internal.uploading.upload_file(file)
        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_image_content(file, location)
        )

        request = messaging_pb2.RequestSendMessage(
            peer=outpeer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self._send_message(request)

    def send_audio(self, peer, file):
        """Send audio as audio (not as file) to current peer.

            :param peer: receiver's peer
            :param file: path to audio file
            :return: value of SendMessage response object
        """
        if not peer:
            print('Peer can\'t be None!')
            return None

        if not is_audio(file):
            raise IOError('File is not an image.')

        location = self.internal.uploading.upload_file(file)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_audio_content(file, location)
        )

        request = messaging_pb2.RequestSendMessage(
            peer=peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self._send_message(request)

    def send_video(self, peer, file):
        """Send video as video (not as file) to current peer.

            :param peer: receiver's peer
            :param file: path to video file
            :return: value of SendMessage response object
        """
        if not peer:
            print('Peer can\'t be None!')
            return None

        if not is_video(file):
            raise IOError('File is not a video.')

        location = self.internal.uploading.upload_file(file)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_video_content(file, location)
        )

        request = messaging_pb2.RequestSendMessage(
            peer=peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self._send_message(request)

    def reply(self, peer, mids, text=None, interactive_media_groups=None):
        """Reply message to current peer. Message can contain interactive media groups (buttons, selects etc.).

        :param mids: mids (array) of messages
        :param peer: receiver's peer
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: value of SendMessage response object
        """

        if text is None:
            text = ''

        if not peer:
            print('Peer can\'t be None!')
            return None

        outpeer = self.manager.get_outpeer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)
        request = messaging_pb2.RequestSendMessage(
            peer=outpeer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            reply=messaging_pb2.ReferencedMessages(mids=mids)
        )
        return self._send_message(request)

    def load_message_history(self, outpeer, date=0, direction=messaging_pb2.LISTLOADMODE_FORWARD, limit=2):
        if not outpeer:
            print('Outpeer can\'t be None!')
            return None

        request = messaging_pb2.RequestLoadHistory(
            peer=outpeer,
            date=date,
            load_mode=direction,
            limit=limit
        )
        return self._load_history(request)

    def on_message_async(self, callback, interactive_media_callback=None):
        updates_thread = threading.Thread(target=self.on_message, args=(callback, interactive_media_callback))
        updates_thread.start()

    def on_message(self, callback, interactive_media_callback=None, raw_callback=None):
        """Message receiving event handler.

        :param callback: function that will be called when message received
        :param interactive_media_callback: function that will be called when interactive media action is performed
        :param raw_callback: function to handle any other type of update
        :return: None
        """

        while True:
            try:
                for update in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
                    up = sequence_and_updates_pb2.UpdateSeqUpdate()
                    up.ParseFromString(update.update.value)
                    if up.WhichOneof('update') == 'updateMessage':
                        self.internal.messaging.MessageReceived(messaging_pb2.RequestMessageReceived(
                            peer=self.manager.get_outpeer(up.updateMessage.peer),
                            date=up.updateMessage.date
                        ))
                        self.internal.messaging.MessageRead(messaging_pb2.RequestMessageRead(
                            peer=self.manager.get_outpeer(up.updateMessage.peer),
                            date=up.updateMessage.date
                        ))
                        self.internal.thread_pool_executor.submit(
                            callback(up.updateMessage)
                        )
                    elif up.WhichOneof('update') == 'updateInteractiveMediaEvent' and \
                            callable(interactive_media_callback):
                        self.internal.thread_pool_executor.submit(
                            interactive_media_callback(up.updateInteractiveMediaEvent)
                        )
                    else:
                        if callable(raw_callback):
                            self.internal.thread_pool_executor.submit(
                                raw_callback(up)
                            )
            except grpc.RpcError as e:
                if e.details() in ['Socket closed', 'GOAWAY received']:
                    continue

    def _send_message(self, request):
        return self.internal.messaging.SendMessage(request)

    def _update_message(self, request):
        return self.internal.messaging.UpdateMessage(request)

    def _send_message(self, request):
        return self.internal.messaging.SendMessage(request)

    def _load_history(self, request):
        return self.internal.messaging.LoadHistory(request)

    def _delete(self, request):
        return self.internal.messaging.DeleteMessageObsolete(request)

    def _read(self, request):
        return self.internal.messaging.MessageRead(request)
