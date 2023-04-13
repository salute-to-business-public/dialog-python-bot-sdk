import math
import re
import sched
import time
import traceback
from threading import Thread
from typing import List, Tuple

from dialog_api.messaging_pb2 import ReferencedMessages
from dialog_api.threads_pb2 import RequestCreateThread

from dialog_bot_sdk.interactive_media import InteractiveMediaGroup, InteractiveMediaLink
from google.protobuf import empty_pb2
import random
import grpc
from .entities.definitions import UUID
from .entities.messaging import Message, ListLoadMode, UpdateMessage, MessageHandler, \
    EventHandler, CommandHandler
from .entities.peers import Peer, PeerType, GroupOutPeer
from .entities.sequence_and_updates import ReferencedEntities, UpdateSeqUpdate, UpdateType
from .service import ManagedService
from dialog_api import messaging_pb2, sequence_and_updates_pb2, peers_pb2, stickers_pb2
import google.protobuf.wrappers_pb2 as wrappers_pb2
from dialog_bot_sdk.utils import get_peer, async_dec, AsyncTask, is_image, get_uuids, get_document_content, \
    get_image_content, deprecated, return_event, get_command, get_logger, build_error_string

SCHEDULER = sched.scheduler(time.time, time.sleep)
MAX_SLEEP_TIME = 30
EXCEPTION_CODES = [1, 13]


class Messaging(ManagedService):
    retry = 0
    commands = {}
    _seq = 0
    _load_difference = False
    _load_difference_active = False
    _load_difference_more = False
    _update_down = False
    _logger = None

    """Main messaging class.
    """
    @async_dec()
    def send_message(
            self, peer: Peer or AsyncTask, text: str,
            interactive_media_groups: List[InteractiveMediaGroup] = None, uid: int = None,
            is_forward_banned: bool = False
    ) -> UUID:
        """Send text message to peer.
        Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :param uid: send message only for user by id
        :param is_forward_banned: if True users can't forward this message
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        if text == '' or text is None:
            raise AttributeError('Text message must contain some text.')
        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            self.__add_interactive_media(interactive_media_groups, msg)
        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            is_only_for_user=uid,
            is_forward_banned=is_forward_banned
        )
        return self.__send_message(request)

    def send_message_sync(
            self, peer: Peer or AsyncTask, text: str,
            interactive_media_groups: List[InteractiveMediaGroup] = None, uid: int = None,
            is_forward_banned: bool = False
    ) -> UUID:
        return self.send_message.__wrapped__(self, peer, text, interactive_media_groups, uid, is_forward_banned)

    @async_dec()
    def update_message(self, message: Message or AsyncTask, text: str,
                       interactive_media_groups: List[InteractiveMediaGroup] = None) -> None:
        """Update text message or interactive media (buttons, selects etc.).

        :param message: Message or AsyncTask (in which located Message)
        :param text: message text (not null)
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :return: None
        """
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            self.__add_interactive_media(interactive_media_groups, msg)

        self.__update(self.__get_message(message), msg)

    def update_message_sync(self, message: Message or AsyncTask, text: str,
                            interactive_media_groups: List[InteractiveMediaGroup] = None) -> None:
        return self.update_message.__wrapped__(self, message, text, interactive_media_groups)

    @async_dec()
    def delete(self, message: Message or AsyncTask) -> None:
        """Delete message.

        :param message: Message or AsyncTask (in which located Message)
        :return: None
        """
        msg = messaging_pb2.MessageContent(
            deletedMessage=messaging_pb2.DeletedMessage(is_local=wrappers_pb2.BoolValue(value=False))
        )

        self.__update(self.__get_message(message), msg)

    def delete_sync(self, message: Message or AsyncTask) -> None:
        return self.delete.__wrapped__(self, message)

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
        result = self.internal.updates.GetReferencedEntitites(request)
        for message in result.messages:
            self.manager.add_out_peer(message.host_peer)
            self.manager.add_out_peer(message.sender_peer)
        return ReferencedEntities.from_api(result).messages

    def get_messages_by_id_sync(self, mids: List[UUID or AsyncTask]) -> List[Message]:
        return self.get_messages_by_id.__wrapped__(self, mids)

    @async_dec()
    def get_message_by_id(self, mid: UUID or AsyncTask) -> Message or None:
        """Find and return message by UUID

        :param mid: UUID or AsyncTask (in which located UUID)
        :return: Message
        """
        message = self.get_messages_by_id_sync([mid])
        if message:
            return message[0]

    def get_message_by_id_sync(self, mid: UUID or AsyncTask) -> Message or None:
        return self.get_message_by_id.__wrapped__(self, mid)

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

    def messages_read_sync(self, peer: Peer or AsyncTask, date: int) -> List[Message]:
        return self.messages_read.__wrapped__(self, peer, date)

    @async_dec()
    def send_file(
            self, peer: Peer or AsyncTask, file: str or bytes, uid: int = None, text: str = None, name: str = None,
            verify: bool = None, is_forward_banned: bool = False, reply: List[UUID] = None, forward: List[UUID] = None,
    ) -> UUID or None:
        """Send file to peer.

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param file: path to file (string) or file content (in bytes)
        :param uid: send message only for user by id
        :param text: text
        :param name: file name
        :param verify: verify post request
        :param is_forward_banned: if True users can't forward this message
        :param reply: list of mids for reply
        :param forward: list of mids for forward
        :return: UUID (message id)
        """
        if isinstance(file, bytes) and name is None:
            raise ValueError("name must be str if file is bytes")
        if not (isinstance(file, str) or isinstance(file, bytes)):
            raise TypeError("File must be str or bytes")
        peer = get_peer(peer)
        self.__validate_uid(uid)
        location = self.internal.uploading.upload_file_sync(file, verify=verify)
        if location is None:
            return None
        location = location.to_api()

        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            get_document_content(file, location, name)
        )

        if text is not None:
            msg.documentMessage.caption.value = text

        reply = reply if reply is not None else []
        forward = forward if forward is not None else []

        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            is_only_for_user=uid,
            is_forward_banned=is_forward_banned,
            reply=ReferencedMessages(mids=[x.to_api() for x in reply]),
            forward=ReferencedMessages(mids=[x.to_api() for x in forward])
        )
        return self.__send_message(request)

    def send_file_sync(
            self, peer: Peer or AsyncTask, file: str or bytes, uid: int = None, text: str = None, name: str = None,
            verify: bool = None, is_forward_banned: bool = False, reply: List[UUID] = None, forward: List[UUID] = None,
    ) -> UUID or None:
        return self.send_file.__wrapped__(self, peer, file, uid, text, name, verify, is_forward_banned, reply, forward)

    @async_dec()
    def send_image(
            self, peer: Peer or AsyncTask, file: str, uid: int = None, text: str = None, name: str = None,
            verify: bool = None, is_forward_banned: bool = False, reply: List[UUID] = None, forward: List[UUID] = None
    ) -> UUID or None:
        """Send image as image (not as file) to peer.

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param file: path to image file
        :param uid: send message only for user by id
        :param text: text
        :param name: file name
        :param verify: verify post request
        :param is_forward_banned: if True users can't forward this message
        :param reply: list of mids for reply
        :param forward: list of mids for forward
        :return: UUID (message id)
        """
        peer = get_peer(peer)
        self.__validate_uid(uid)

        if isinstance(file, str) and not is_image(file):
            raise IOError('File is not an image.')

        location = self.internal.uploading.upload_file_sync(file, verify=verify)

        if location is None:
            return None

        location = location.to_api()
        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()

        msg.documentMessage.CopyFrom(
            get_image_content(file, location, name)
        )

        if text is not None:
            msg.documentMessage.caption.value = text

        reply = reply if reply is not None else []
        forward = forward if forward is not None else []

        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            is_only_for_user=uid,
            is_forward_banned=is_forward_banned,
            reply=ReferencedMessages(mids=[x.to_api() for x in reply]),
            forward=ReferencedMessages(mids=[x.to_api() for x in forward])
        )

        return self.__send_message(request)

    def send_image_sync(
            self, peer: Peer or AsyncTask, file: str, uid: int = None, text: str = None, name: str = None,
            verify: bool = None, is_forward_banned: bool = False, reply: List[UUID] = None, forward: List[UUID] = None
    ) -> UUID or None:
        return self.send_image.__wrapped__(self, peer, file, uid, text, name, verify, is_forward_banned, reply, forward)

    @async_dec()
    def reply(
            self, peer: Peer or AsyncTask, mids: List[UUID or AsyncTask], text: str = None,
            interactive_media_groups: List[InteractiveMediaGroup] = None, uid: int = None,
            is_forward_banned: bool = False
    ) -> UUID:
        """Reply messages to peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param mids: list of UUIDs
        :param text: message text
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :param uid: send message only for user by id
        :param is_forward_banned: if True users can't forward this message
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
            self.__add_interactive_media(interactive_media_groups, msg)
        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
            reply=messaging_pb2.ReferencedMessages(mids=mids),
            is_only_for_user=uid,
            is_forward_banned=is_forward_banned
        )
        return self.__send_message(request)

    def reply_sync(
            self, peer: Peer or AsyncTask, mids: List[UUID or AsyncTask], text: str = None,
            interactive_media_groups: List[InteractiveMediaGroup] = None, uid: int = None,
            is_forward_banned: bool = False
    ) -> UUID:
        return self.reply.__wrapped__(self, peer, mids, text, interactive_media_groups, uid, is_forward_banned)

    @async_dec()
    def forward(
            self, peer: Peer or AsyncTask, mids: List[UUID or AsyncTask], text: str = None,
            interactive_media_groups: List[InteractiveMediaGroup] = None, uid: int = None,
            is_forward_banned: bool = False
    ) -> UUID:
        """Forward messages to peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param mids: list of UUIDs
        :param text: message text
        :param interactive_media_groups: groups of interactive media components (buttons etc.)
        :param uid: send message only for user by id
        :param is_forward_banned: if True users can't forward this message
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
            is_only_for_user=uid,
            is_forward_banned=is_forward_banned
        )
        return self.__send_message(request)

    def forward_sync(
            self, peer: Peer or AsyncTask, mids: List[UUID or AsyncTask], text: str = None,
            interactive_media_groups: List[InteractiveMediaGroup] = None, uid: int = None,
            is_forward_banned: bool = False
    ) -> UUID:
        return self.forward.__wrapped__(self, peer, mids, text, interactive_media_groups, uid, is_forward_banned)

    @async_dec()
    def send_sticker(self, peer: Peer, collection_id: int, sticker_id: int) -> UUID:
        """Forward messages to peer. Message can contain interactive media groups (buttons, selects etc.).

        :param peer: Peer or AsyncTask (in which located User or Group)
        :param collection_id: sticker collection's id
        :param sticker_id: sticker's id
        :return: UUID (message id)
        """
        out_peer = self.manager.get_out_peer(peer)
        collection = self.internal.stickers.LoadStickerCollection(
            stickers_pb2.RequestLoadStickerCollection(
                id=collection_id
            )
        ).collection

        sticker = None
        for s in collection.stickers:
            if s.id == sticker_id:
                sticker = s
                break

        if sticker is None:
            raise ValueError("Sticker with id %s not found" % sticker_id)

        msg = messaging_pb2.MessageContent()
        msg.stickerMessage.CopyFrom(
            messaging_pb2.StickerMessage(
                sticker_id=wrappers_pb2.Int32Value(value=sticker_id),
                image_512=sticker.image_512,
                image_256=sticker.image_256,
                sticker_collection_id=wrappers_pb2.Int32Value(value=collection_id),
                emoji=sticker.emoji,
            )
        )

        request = messaging_pb2.RequestSendMessage(
            peer=out_peer,
            deduplication_id=random.randint(0, 100000000),
            message=msg,
        )
        return self.__send_message(request)

    def send_sticker_sync(self, peer: Peer, collections_id: int, sticker_id: int) -> UUID:
        return self.send_sticker.__wrapped__(self, peer, collections_id, sticker_id)

    @async_dec()
    def load_message_history(
            self, peer: Peer or AsyncTask, date: int = 0, direction: ListLoadMode = ListLoadMode.LISTLOADMODE_BACKWARD,
            limit: int = 2
    ) -> List[Message]:
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

    def load_message_history_sync(
            self, peer: Peer or AsyncTask, date: int = 0, direction: ListLoadMode = ListLoadMode.LISTLOADMODE_BACKWARD,
            limit: int = 2
    ) -> List[Message]:
        return self.load_message_history.__wrapped__(self, peer, date, direction, limit)

    @async_dec()
    def hide_message_for_other_user(self, peer: Peer, message_id: UUID, uid: int) -> None:
        request = messaging_pb2.RequestHideMessageForOtherUser(
            peer=peer.to_api(),
            message_id=message_id.to_api(),
            user_id=uid
        )
        return self.internal.messaging.HideMessageForOtherUser(request)

    def hide_message_for_other_user_sync(self, peer: Peer, message_id: UUID, uid: int) -> None:
        return self.hide_message_for_other_user.__wrapped__(self, peer, message_id, uid)

    @async_dec()
    def update_for_user_ids_message(self, peer: Peer, message_id: UUID, uid: int) -> None:
        request = messaging_pb2.RequestUpdateForUserIdsMessage(
            peer=peer.to_api(),
            message_id=message_id.to_api(),
            user_id=uid
        )
        return self.internal.messaging.UpdateForUserIdsMessage(request)

    def update_for_user_ids_message_sync(self, peer: Peer, message_id: UUID, uid: int) -> None:
        return self.update_for_user_ids_message.__wrapped__(self, peer, message_id, uid)

    def command_handler(self, commands: List[Tuple[str, callable, PeerType or None]] or List[CommandHandler]) -> None:
        for command in commands:
            if isinstance(command, tuple):
                if len(command) == 2:
                    self.manager.commands[(command[0], None)] = CommandHandler(command[1], command[0])
                else:
                    self.manager.commands[(command[0], command[2])] = CommandHandler(command[1], command[0], command[2])
            if isinstance(command, CommandHandler):
                self.manager.commands[(command.command, command.peer_type)] = command

    def event_handler(self, events: List[EventHandler]) -> None:
        for event in events:
            self.manager.events[(event.id, event.value)] = event

    def message_handler(self, messages: List[MessageHandler]) -> None:
        for message in messages:
            self.manager.messages[(message.message_type, message.ext_type, message.peer_type)] = message

    def message_changed_handler(self, messages: List[MessageHandler]) -> None:
        for message in messages:
            self.manager.messages_changed[(message.message_type, message.ext_type, message.peer_type)] = message

    def get_command(self, message: UpdateMessage or Message) -> Tuple[str, str] or None:
        return get_command(message, self.manager.user_info.user.data.nick)

    @deprecated
    def on_message_async(self, callback, interactive_media_callback=None, raw_callback=None) -> None:
        self.on_message(callback, interactive_media_callback, raw_callback, True)

    def on_message(self, callback, interactive_media_callback=None, raw_callback=None, is_async=False) -> None:
        """Message receiving event handler.

        :param callback: function that will be called when message received
        :param interactive_media_callback: function that will be called when interactive media action is performed
        :param raw_callback: function to handle any other type of update
        :param is_async: is async method
        :return: None
        """
        if self.manager.run is True:
            raise RuntimeError("Updates listener already running")
        else:
            self.manager.run = True

        if self._logger is None:
            self._logger = get_logger(__name__, self.manager.logger_config)

        self._seq = self.internal.updates.GetState(sequence_and_updates_pb2.RequestGetState()).seq
        while True:
            try:
                delay = min(math.exp(self.retry), MAX_SLEEP_TIME)
                SCHEDULER.enter(delay, 1, self.__on_message_schedule,
                                kwargs={'callback': callback,
                                        'interactive_media_callback': interactive_media_callback,
                                        'raw_callback': raw_callback,
                                        'is_async': is_async})
                if self._load_difference_active is False and self._load_difference is True:
                    self._load_difference_active = True
                    thread = Thread(target=self.__on_seq_difference,
                                    args=(callback, interactive_media_callback, raw_callback, is_async))
                    thread.start()
                else:
                    self._load_difference_more = True
                SCHEDULER.run()
            except grpc.RpcError as e:
                if e.details() in ("Received RST_STREAM with error code 2", "Received http2 header with status: 503"):
                    self.retry = 0
                elif e.details() == 'failed to connect to all addresses' or e._state.code.value[0] in EXCEPTION_CODES:
                    self._logger.error(build_error_string(e))
                    self.retry += 1
            except AttributeError as e:
                self.retry = 0
            except Exception as e:
                self.retry += 1
            self._load_difference = True
            self._update_down = True

    def __on_message_schedule(self, callback, interactive_media_callback=None, raw_callback=None, is_async=False):
        self._update_down = False
        for update in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
            self.retry = 0
            while self._load_difference is True:
                time.sleep(0.1)
            update = UpdateSeqUpdate.from_api(update)
            if update.seq <= self._seq:
                continue
            self._seq = update.seq
            self.__update_processing(update, callback, interactive_media_callback, raw_callback, is_async)

    def __on_seq_difference(
            self, callback: callable, interactive_media_callback: callable, raw_callback: callable, is_async: bool
    ):
        if self._load_difference is False:
            return

        self._load_difference_more = True
        while self._load_difference_more is True:
            while self._update_down is True:
                time.sleep(1)
            self._load_difference_more = False
            difference = self.__get_diff(self._seq)
            for diff in difference:
                self._seq = diff.seq
                try:
                    diff = UpdateSeqUpdate.from_api(diff)
                    self.__update_processing(diff, callback, interactive_media_callback, raw_callback, is_async)
                except AttributeError as e:
                    self._logger.error(traceback.format_exc())
                    continue
                except:
                    continue
            time.sleep(1)
        self._load_difference = False
        self._load_difference_active = False

    def __get_diff(self, seq: int) -> List[UpdateSeqUpdate]:
        while True:
            try:
                difference = self.internal.updates.GetDifference(sequence_and_updates_pb2.RequestGetDifference(seq=seq)).updates
                break
            except grpc.RpcError as e:
                time.sleep(1)
        return difference

    def __update_processing(
            self, update: UpdateSeqUpdate, callback: callable, interactive_media_callback: callable,
            raw_callback: callable, is_async: bool
    ) -> None:
        update_callback = None
        if update.type == UpdateType.UPDATE_MESSAGE:
            message = update.update_message
            command_func = self.__prepare_update_message(message)
            if command_func is not None:
                update_callback = return_event(self, command_func, message)
            else:
                update_callback = return_event(self, callback, message)
        elif update.type == UpdateType.UPDATE_INTERACTIVE_MEDIA_EVENT and interactive_media_callback is not None:
            self.manager.set_update_interactive_media_event_out_peers(update.update_interactive_media_event)
            update_callback = return_event(self, interactive_media_callback, update.update_interactive_media_event)
        else:
            if update.type == UpdateType.UPDATE_THREAD_CREATED:
                out_peer = self.manager.get_out_peer(update.update_thread_created.group_peer)
                if out_peer is not None:
                    request = RequestCreateThread(
                        group_peer=GroupOutPeer(group_id=out_peer.id, access_hash=out_peer.access_hash),
                        root_message_id=update.update_thread_created.root_message_id.to_api()
                    )
                    thread_peer = self.internal.threads.CreateThread(request).peer
                    self.manager.add_thread_out_peer(thread_peer)
            if raw_callback is not None:
                update_callback = return_event(self, raw_callback, update.oneof_type())
        if not is_async and update_callback is not None:
            update_callback.wait()

    def __prepare_update_message(self, update_message: UpdateMessage) -> None or callable:
        self.manager.set_update_message_out_peers(update_message)
        out_peer = self.manager.get_out_peer(update_message.peer)
        self.internal.messaging.MessageReceived(messaging_pb2.RequestMessageReceived(
            peer=out_peer,
            date=update_message.date
        ))
        self.internal.messaging.MessageRead(messaging_pb2.RequestMessageRead(
            peer=out_peer,
            date=update_message.date
        ))
        command = get_command(update_message, self.manager.user_info.user.data.nick)
        if command is not None and (command[0], update_message.peer.type) in self.manager.commands:
            return self.manager.commands[(command[0], update_message.peer.type)]
        if command is not None and (command[0], None) in self.manager.commands:
            return self.manager.commands[(command[0], None)]

    @staticmethod
    def __is_command(text: str) -> str or None:
        try:
            regs = re.search(r'/[\w]+', text).regs[0]
            if regs[0] == 0:
                return text[regs[0]:regs[1]][1:]
        except:
            return None

    def __get_out_peer_and_message(self, peer: peers_pb2.Peer, text: str,
                                   interactive_media_groups: List[InteractiveMediaGroup]) \
            -> Tuple[peers_pb2.OutPeer, messaging_pb2.MessageContent]:
        out_peer = self.manager.get_out_peer(peer)
        msg = messaging_pb2.MessageContent()
        msg.textMessage.text = text
        if interactive_media_groups is not None:
            self.__add_interactive_media(interactive_media_groups, msg)
        return out_peer, msg

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

    @staticmethod
    def __get_message(message: Message or AsyncTask) -> Message:
        if isinstance(message, Message):
            return message
        if isinstance(message, AsyncTask):
            message = message.wait()
            if isinstance(message, Message):
                return message
            if isinstance(message, list) and isinstance(message[0], Message):
                return message[0]
        raise AttributeError("message must be Message or AsyncTask with Message or list of Messages")

    @staticmethod
    def __validate_uid(uid):
        if uid is not None and not isinstance(uid, int):
            raise TypeError('uid must be int')

    @staticmethod
    def __add_interactive_media(
            interactive_media_groups: List[InteractiveMediaGroup], msg: messaging_pb2.MessageContent
    ) -> None:
        for g in interactive_media_groups:
            for interactive_media in g.actions:
                if isinstance(interactive_media.widget, InteractiveMediaLink):
                    media = msg.textMessage.media.add(webpage=messaging_pb2.WebpageMedia())
                    break
            else:
                media = msg.textMessage.media.add()
            g.render(media)
