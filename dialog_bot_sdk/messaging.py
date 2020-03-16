import math
import sched
import time
from typing import List, Tuple

from dialog_bot_sdk.entities.ListLoadMode import ListLoadMode
from dialog_bot_sdk.entities.ReferencedEntities import ReferencedEntities
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.UpdateInteractiveMediaEvent import UpdateInteractiveMediaEvent
from dialog_bot_sdk.entities.UpdateMessage import UpdateMessage
from dialog_bot_sdk.entities.message.TextMessage import MessageMedia
from dialog_bot_sdk.interactive_media import InteractiveMediaGroup
from google.protobuf import empty_pb2
import threading
import random
import grpc
import logging

from dialog_bot_sdk.entities.message.Message import Message
from dialog_bot_sdk.entities.Peer import Peer
from dialog_bot_sdk.utils import POOL
from .service import ManagedService
from dialog_api import messaging_pb2, sequence_and_updates_pb2, peers_pb2, media_and_files_pb2
from .content import content
import google.protobuf.wrappers_pb2 as wrappers_pb2
from dialog_bot_sdk.utils import get_peer, async_dec, AsyncTask, is_image, get_uuids

SCHEDULER = sched.scheduler(time.time, time.sleep)
MAX_SLEEP_TIME = 30


class Messaging(ManagedService):
    retry = 0
    timer = 0
    """Main messaging class.
    """
    @async_dec()
    def send_message(self, peer: Peer or AsyncTask, text: str,
                     interactive_media_groups: List[InteractiveMediaGroup] = None,
                     uid: int = None) -> UUID:
        """Send text message to peer.
        Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :param uid: send message only for user by id
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        if text == '' or text is None:
            raise AttributeError('Text message must contain some text.')
        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)
        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            is_only_for_user=uid
        )
        return self.__send_message(request)

    @async_dec()
    def update_message(self, message: Message or AsyncTask, text: str,
                       interactive_media_groups: List[InteractiveMediaGroup] = None) -> None:
        """Update text message or interactive media (buttons, selects etc.).

        :param message: Message or AsyncTask (in which located Message)
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: None
        """
        try:
            if isinstance(message, AsyncTask):
                message = message.wait()[0]
                if not isinstance(message, Message):
                    raise AttributeError()
        except Exception as e:
            raise AttributeError("if message is AsyncTask class, result must be list of Message")
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)

        self.__update(message, msg)

    @async_dec()
    def delete(self, message: Message or AsyncTask) -> None:
        """Delete message.

        :param message: Message or AsyncTask (in which located Message)
        :return: None
        """
        msg = messaging_pb2.MessageContent(
            deletedMessage=messaging_pb2.DeletedMessage(is_local=wrappers_pb2.BoolValue(value=False))
        )
        self.__update(message, msg)

    @async_dec()
    def get_messages_by_id(self, mids: List[UUID or AsyncTask]) -> List[Message]:
        """Find and return messages by UUIDs

        :param mids: list of UUID or AsyncTask (in which located UUID)
        :return: list of Messages
        """
        mids = get_uuids(mids)
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                mids=mids
            )
        result = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request))
        return result.messages

    @async_dec()
    def messages_read(self, peer: Peer or AsyncTask, date: int) -> None:
        """Marking a message and all previous as read

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param date: date of message
        :return: None
        """
        peer = get_peer(peer)
        peer = self.manager.get_out_peer(peer)
        request = messaging_pb2.RequestMessageRead(
            peer=peer,
            date=date
        )
        self.internal.messaging.MessageRead(request)

    @async_dec()
    def send_file(self, peer: Peer or AsyncTask, file: str) -> UUID or None:
        """Send file to peer.

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param file: path to file
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        location = self.internal.uploading.upload_file(file).wait()
        if location is None:
            return None
        location = location.to_api()

        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_document_content(file, location)
        )

        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self.__send_message(request)

    @async_dec()
    def send_media(self, peer: Peer or AsyncTask, medias: List[MessageMedia]) -> UUID:
        """Send media to peer.

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param medias: medias (list of MessageMedias)
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        medias = self.__get_medias(medias)
        out_peer = self.manager.get_out_peer(peer)
        text_message = messaging_pb2.TextMessage()
        for media in medias:
            text_message.media.append(media)
        msg = messaging_pb2.MessageContent(textMessage=text_message)
        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )
        return self.__send_message(request)

    @async_dec()
    def send_image(self, peer: Peer or AsyncTask, file: str) -> UUID or None:
        """Send image as image (not as file) to peer.

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param file: path to image file
        :return: UUID (message id)
        """
        peer = get_peer(peer)

        if isinstance(file, str) and not is_image(file):
            raise IOError('File is not an image.')

        location = self.internal.uploading.upload_file(file).wait()
        if location is None:
            return None
        location = location.to_api()
        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            content.get_image_content(file, location)
        )

        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg
        )

        return self.__send_message(request)

    @async_dec()
    def reply(self, peer: Peer or AsyncTask, mids: List[UUID or AsyncTask], text: str = None,
              interactive_media_groups: List[InteractiveMediaGroup] = None) -> UUID:
        """Reply messages to peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param mids: list of UUIDs
        :param text: message text
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        mids = get_uuids(mids)
        if text is None:
            text = ''

        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)
        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            reply=messaging_pb2.ReferencedMessages(mids=mids)
        )
        return self.__send_message(request)

    @async_dec()
    def forward(self, peer: Peer or AsyncTask, mids: List[UUID or AsyncTask], text: str = None,
                interactive_media_groups: List[InteractiveMediaGroup] = None) -> UUID:
        """Forward messages to peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param mids: list of UUIDs
        :param text: message text
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        mids = get_uuids(mids)
        if text is None:
            text = ''

        out_peer, msg = self.__get_out_peer_and_message(peer, text, interactive_media_groups)
        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            forward=messaging_pb2.ReferencedMessages(mids=mids),
        )
        return self.__send_message(request)

    @async_dec()
    def load_message_history(self, peer: Peer or AsyncTask, date: int = 0,
                             direction: ListLoadMode = ListLoadMode.LISTLOADMODE_BACKWARD,
                             limit: int = 2) -> List[Message]:
        """Load and return messages by peer.

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param date: date of message
        :param direction: ListLoadMode
        :param limit: messages count
        :return: list of Messages
        """
        peer = get_peer(peer)
        out_peer = self.manager.get_out_peer(peer)
        request = messaging_pb2.RequestLoadHistory(
                peer=out_peer,
                date=date,
                load_mode=direction,
                limit=limit
            )
        return [Message.from_api(x) for x in self.internal.messaging.LoadHistory(request).history]

    def on_message_async(self, callback, interactive_media_callback=None) -> None:
        updates_thread = threading.Thread(target=self.on_message, args=(callback, interactive_media_callback))
        updates_thread.start()

    def on_message(self, callback, interactive_media_callback=None, raw_callback=None) -> None:
        """Message receiving event handler.

        :param callback: function that will be called when message received
        :param interactive_media_callback: function that will be called when interactive media action is performed
        :param raw_callback: function to handle any other type of update
        :return: None
        """
        while True:
            try:
                SCHEDULER.enter(min(math.exp(self.retry), MAX_SLEEP_TIME), 1, self.__on_message_schedule,
                                kwargs={'callback': callback,
                                        'interactive_media_callback': interactive_media_callback,
                                        'raw_callback': raw_callback})
                SCHEDULER.run()
            except grpc.RpcError as e:
                logging.error(e)
                if e.details() == 'failed to connect to all addresses':
                    self.timer += min(math.exp(self.retry), MAX_SLEEP_TIME)
                    self.retry += 1
                    continue
                if e.details() in ['Socket closed', 'GOAWAY received']:
                    continue

    def __on_message_schedule(self, callback, interactive_media_callback=None, raw_callback=None):
        try:
            self.internal.updates.GetState(sequence_and_updates_pb2.RequestGetState())
            if self.retry:
                logging.info("Server was unavailable {} seconds.".format(int(self.timer)))
                self.timer = 0
                self.retry = 0
        except grpc.RpcError as e:
            raise e
        for update in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
            up = sequence_and_updates_pb2.UpdateSeqUpdate()
            up.ParseFromString(update.update.value)
            if up.WhichOneof('update') == 'updateMessage':
                self.internal.messaging.MessageReceived(messaging_pb2.RequestMessageReceived(
                    peer=self.manager.get_out_peer(up.updateMessage.peer),
                    date=up.updateMessage.date
                ))
                self.internal.messaging.MessageRead(messaging_pb2.RequestMessageRead(
                    peer=self.manager.get_out_peer(up.updateMessage.peer),
                    date=up.updateMessage.date
                ))
                POOL.submit(
                    callback(UpdateMessage.from_api(up.updateMessage))
                )
            elif up.WhichOneof('update') == 'updateInteractiveMediaEvent' and \
                    callable(interactive_media_callback):
                POOL.submit(
                    interactive_media_callback(UpdateInteractiveMediaEvent.from_api(up.updateInteractiveMediaEvent))
                )
            else:
                if callable(raw_callback):
                    POOL.submit(
                        raw_callback(up)
                    )

    def __get_out_peer_and_message(self, peer: peers_pb2.Peer, text: str,
                                   interactive_media_groups: List[InteractiveMediaGroup]) \
            -> Tuple[peers_pb2.OutPeer, messaging_pb2.MessageContent]:
        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            for g in interactive_media_groups:
                media = msg.textMessage.media.add()
                g.render(media)
        return out_peer, msg

    @staticmethod
    def __get_medias(medias: List[MessageMedia]) -> List[messaging_pb2.MessageMedia] or None:
        for i in range(len(medias)):
            if medias[i].audio and isinstance(medias[i].audio.audio.file_location, AsyncTask):
                medias[i].audio.audio.file_location = medias[i].audio.audio.file_location.wait()
            if medias[i].image and isinstance(medias[i].image.image.file_location, AsyncTask):
                medias[i].image.image.file_location = medias[i].image.image.file_location.wait()
            if medias[i].web_page and medias[i].web_page.image and \
                    isinstance(medias[i].web_page.image.file_location, AsyncTask):
                medias[i].web_page.image.file_location = medias[i].web_page.image.file_location.wait()
        return [x.to_api() for x in medias]

    def __send_message(self, request: messaging_pb2.RequestSendMessage) -> UUID:
        return UUID.from_api(self.internal.messaging.SendMessage(request).message_id)

    def __update(self, message: Message, new_message: messaging_pb2.MessageContent) -> None:
        if hasattr(message, "mid"):
            mid = message.mid
        else:
            raise AttributeError("message has not attribute message_id or mid")

        if message.edited_at:
            last_edited_at = message.edited_at
        else:
            last_edited_at = message.date

        request = messaging_pb2.RequestUpdateMessage(
            mid=mid.to_api(),
            updated_message=new_message,
            last_edited_at=last_edited_at
        )
        self.internal.messaging.UpdateMessage(request)
