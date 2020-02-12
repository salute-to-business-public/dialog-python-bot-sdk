import math
import sched
import time
from typing import List, Tuple

from dialog_bot_sdk.entities.ListLoadMode import ListLoadMode
from dialog_bot_sdk.entities.ReferencedEntities import ReferencedEntities
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.entities.UpdateInteractiveMediaEvent import UpdateInteractiveMediaEvent
from dialog_bot_sdk.entities.UpdateMessage import UpdateMessage
from dialog_bot_sdk.entities.media.AudioMedia import AudioMedia
from dialog_bot_sdk.entities.media.FileLocation import FileLocation
from dialog_bot_sdk.entities.media.ImageMedia import ImageMedia
from dialog_bot_sdk.entities.media.WebpageMedia import WebPageMedia
from dialog_bot_sdk.interactive_media import InteractiveMediaGroup
from google.protobuf import empty_pb2
import threading
import random
import grpc
import logging

from dialog_bot_sdk.entities.message.Message import Message
from dialog_bot_sdk.entities.Peer import Peer
from .service import ManagedService
from dialog_api import messaging_pb2, sequence_and_updates_pb2, peers_pb2, media_and_files_pb2
from .content import content
import google.protobuf.wrappers_pb2 as wrappers_pb2
from dialog_bot_sdk.utils import get_peer, async_dec, AsyncTask, is_image

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
        """Send text message to peer. Message can contain interactive media groups (buttons, selects etc.).
        :param peer: receiver's peer
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :param uid: send message only for user by id
        :return: value of SendMessage response object
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
        :param message: object received from any send method (send_message, send_file etc.)
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

        self.__update(message, msg)

    @async_dec()
    def delete(self, message: Message or AsyncTask) -> None:
        """Delete text messages or interactive media (buttons, selects etc.).
        :param message: message object received from any send method (send_message, send_file etc.)
        """
        msg = messaging_pb2.MessageContent(
            deletedMessage=messaging_pb2.DeletedMessage(is_local=wrappers_pb2.BoolValue(value=False))
        )
        self.__update(message, msg)

    @async_dec()
    def get_messages_by_id(self, mids: List[UUID]) -> Message:
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                mids=mids
            )
        result = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request))
        return result.messages

    @async_dec()
    def messages_read(self, peer: Peer or AsyncTask, date: int) -> None:
        """Marking a message and all previous as read
        :param peer - chat peer
        :param date - date of message
        """
        peer = get_peer(peer)
        request = messaging_pb2.RequestMessageRead(
            peer=peer,
            date=date
        )
        self.internal.messaging.MessageRead(request)

    @async_dec()
    def send_file(self, peer: Peer or AsyncTask, file: str or FileLocation) -> UUID:
        """Send file to peer.
        :param peer: receiver's peer
        :param file: path to file
        :return: value of SendMessage response object
        """
        peer = get_peer(peer)
        location = self.__get_file_location(file)
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
    def send_media(self, peer: Peer or AsyncTask, medias: List[AudioMedia or ImageMedia or WebPageMedia]) -> UUID:
        """Send media to peer.
        :param peer: receiver's peer
        :param medias: medias (list)
        :return: value of SendMessage response object
        """
        peer = get_peer(peer)
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
    def send_image(self, peer: Peer or AsyncTask, file: str or FileLocation) -> UUID:
        """Send image as image (not as file) to peer.
        :param peer: receiver's peer
        :param file: path to image file
        :return: value of SendMessage response object
        """
        peer = get_peer(peer)

        if isinstance(file, str) and not is_image(file):
            raise IOError('File is not an image.')

        location = self.__get_file_location(file)
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
    def reply(self, peer: Peer or AsyncTask, mids: List[UUID], text: str = None,
              interactive_media_groups: List[InteractiveMediaGroup] = None) -> UUID:
        """Reply messages to peer. Message can contain interactive media groups (buttons, selects etc.).
        :param mids: mids (array) of messages
        :param peer: receiver's peer
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: value of SendMessage response object
        """
        peer = get_peer(peer)
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
    def forward(self, peer: Peer or AsyncTask, mids: List[UUID], text: str = None,
                interactive_media_groups: List[InteractiveMediaGroup] = None) -> UUID:
        """Forward messages to peer. Message can contain interactive media groups (buttons, selects etc.).
        :param peer: receiver's peer
        :param mids: mids (array) of messages
        :param text: message text (may be None)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: value of SendMessage response object
        """
        peer = get_peer(peer)
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
        peer = get_peer(peer)
        out_peer = self.manager.get_out_peer(peer)
        request = messaging_pb2.RequestLoadHistory(
                peer=out_peer,
                date=date,
                load_mode=direction,
                limit=limit
            )
        return [Message.from_api(x) for x in self.internal.messaging.LoadHistory(request)]

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
                self.internal.thread_pool_executor.submit(
                    callback(UpdateMessage.from_api(up.updateMessage))
                )
            elif up.WhichOneof('update') == 'updateInteractiveMediaEvent' and \
                    callable(interactive_media_callback):
                self.internal.thread_pool_executor.submit(
                    interactive_media_callback(UpdateInteractiveMediaEvent.from_api(up.updateInteractiveMediaEvent))
                )
            else:
                if callable(raw_callback):
                    self.internal.thread_pool_executor.submit(
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

    def __get_file_location(self, file: str or FileLocation) -> media_and_files_pb2.FileLocation:
        if isinstance(file, str):
            location = self.internal.uploading.upload_file(file)
        elif isinstance(file, FileLocation):
            location = file.to_api()
        else:
            raise AttributeError("extends file type {} or {}, got {}.".format(str.__class__,
                                                                              FileLocation.__class__, type(file)))
        return location

    def __send_message(self, request: messaging_pb2.RequestSendMessage) -> UUID:
        return UUID.from_api(self.internal.messaging.SendMessage(request).message_id)

    def __update(self, message: Message, new_message: messaging_pb2.MessageContent) -> None:
        if hasattr(message, "mid"):
            mid = message.mid
        else:
            raise AttributeError("message has not attribute message_id or mid")

        if message.edited_at.value:
            last_edited_at = message.edited_at.value
        else:
            last_edited_at = message.date

        request = messaging_pb2.RequestUpdateMessage(
            mid=mid,
            updated_message=new_message,
            last_edited_at=last_edited_at
        )
        self.internal.messaging.UpdateMessage(request)
