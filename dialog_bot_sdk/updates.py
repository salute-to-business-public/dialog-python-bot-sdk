import math
import time
import traceback
from threading import Thread
from typing import List
import grpc
from google.protobuf import empty_pb2
from dialog_api.peers_pb2 import GroupOutPeer
from dialog_api.threads_pb2 import RequestCreateThread
from dialog_bot_sdk.utils import async_dec, get_command, return_event, get_logger, build_error_string
from .entities.messaging import UpdateMessage, MessageContentType, MessageContent, UpdateMessageContentChanged, \
    CommandHandler, MessageHandler, EventHandler
from .entities.peers import PeerType
from .entities.sequence_and_updates import UpdateHandler, GetDifference, UpdateSeqUpdate, UpdateType
from .messaging import MAX_SLEEP_TIME, EXCEPTION_CODES
from .service import ManagedService
from dialog_api import sequence_and_updates_pb2, messaging_pb2, sequence_and_updates_pb2_grpc


class Updates(ManagedService):
    """Class for handling grpc's server updates.

    """
    retry = 0
    _default_params = {
        "any_updates": None,
        "ignored_sleep": False,
        "is_async": True,
        "in_thread": False,
        "do_received_message": False,
        "do_read_message": False,
    }
    _seq = 0
    _load_difference = False
    _load_difference_active = False
    _load_difference_more = False
    _update_down = False
    _logger = None

    @async_dec()
    def get_difference(self, seq: int) -> GetDifference:
        """Raw implementation of API schema GetDifference method, which returns updates between attribute 'seq' and
        current seq at server side.

        :param seq: seq value
        :return: GetDifference
        """
        return GetDifference.from_api(
            self.internal.updates.GetDifference(sequence_and_updates_pb2.RequestGetDifference(seq=seq))
        )

    def get_difference_sync(self, seq: int) -> GetDifference:
        return self.get_difference.__wrapped__(self, seq)

    @async_dec()
    def get_state(self) -> int:
        """Current application seq number

        :return: seq
        """
        return self.internal.updates.GetState(sequence_and_updates_pb2.RequestGetState()).seq

    def get_state_sync(self) -> int:
        return self.get_state.__wrapped__(self)

    def sleep(self) -> None:
        self.manager.sleep = True

    def wake(self) -> None:
        self.manager.sleep = False

    def is_sleep(self) -> bool:
        return self.manager.sleep

    def stop(self) -> None:
        self.manager.run = False

    def update_handler(self, updates: List[UpdateHandler]) -> None:
        for update in updates:
            self.manager.updates[update.update_type] = update

    def on_updates(self, **kwargs) -> None:
        """UpdateSeqUpdate handler.

        Kwargs:
            :any_updates: function that will be called when skipped all handlers
            :ignored_sleep: ignored sleep for any updates (default False)
            :is_async: is async method (default True)
            :in_thread: run on_updates in Thread (default False)
            :do_received_message: used ReceivedMessage for updates (default False)
            :do_read_message: used ReadMessage for updates (default False)
        Returns: None
        """
        if self.manager.run is True:
            raise RuntimeError("Updates listener already running")
        else:
            self.manager.run = True

        if self._logger is None:
            self._logger = get_logger(__name__, self.manager.logger_config)

        self.__update_default_params(**kwargs)
        self._seq = self.get_state_sync()
        if self._default_params["in_thread"] is True:
            thread = Thread(target=self.__on_updates)
            thread.start()
        else:
            self.__on_updates()

    def on_get_difference_updates(self, timeout: int = 5, **kwargs) -> None:
        """UpdateSeqUpdate handler.

        Args:
            timeout: timeout between GetDifference calls
        Kwargs:
            :any_updates: function that will be called when skipped all handlers
            :ignored_sleep: ignored sleep for any updates (default False)
            :is_async: is async method (default True)
            :in_thread: run on_updates in Thread (default False)
            :do_received_message: used ReceivedMessage for updates (default False)
            :do_read_message: used ReadMessage for updates (default False)
        Returns: None
        """
        if self.manager.run is True:
            raise RuntimeError("Updates listener already running")
        else:
            self.manager.run = True

        if self._logger is None:
            self._logger = get_logger(__name__, self.manager.logger_config)

        self.__update_default_params(**kwargs)
        self._seq = self.get_state_sync()
        if self._default_params["in_thread"] is True:
            thread = Thread(target=self.__on_get_difference_updates, args=(timeout,))
            thread.start()
        else:
            self.__on_get_difference_updates(timeout)

    def __on_updates(self) -> None:
        while True:
            try:
                delay = min(math.exp(self.retry), MAX_SLEEP_TIME)
                self.manager.scheduler.enter(delay, 1, self.__on_seq_update)
                if self._load_difference_active is False and self._load_difference is True:
                    self._load_difference_active = True
                    thread = Thread(target=self.__on_seq_difference)
                    thread.start()
                else:
                    self._load_difference_more = True
                self.manager.scheduler.run(delay)
            except grpc.RpcError as e:
                if e.details() in ("Received RST_STREAM with error code 2", "Received http2 header with status: 503"):
                    self.retry = 0
                elif e.details() == 'failed to connect to all addresses' or e._state.code.value[0] in EXCEPTION_CODES:
                    self.retry += 1
                    self._logger.error(build_error_string(e))
            except:
                self._logger.error(traceback.format_exc())
                self.retry = 0
            self._load_difference = True
            self._update_down = True
            if self.manager.run is False:
                return

    def __on_seq_difference(self) -> None:
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
                    self.__update_processing(UpdateSeqUpdate.from_api(diff))
                except:
                    self._logger.error(traceback.format_exc())
                    continue
            time.sleep(1)
        self._load_difference = False
        self._load_difference_active = False

    def __on_get_difference_updates(self, timeout: int) -> None:
        while True:
            if self.manager.run is False:
                return
            difference = self.__get_diff(self._seq)
            for diff in difference:
                self._seq = diff.seq
                try:
                    self.__update_processing(UpdateSeqUpdate.from_api(diff))
                except:
                    self._logger.error(traceback.format_exc())
                    continue
            time.sleep(timeout)

    def __get_diff(self, seq: int) -> List[sequence_and_updates_pb2.UpdateSeqUpdate]:
        while True:
            try:
                request = sequence_and_updates_pb2.RequestGetDifference(seq=seq)
                difference = sequence_and_updates_pb2_grpc.SequenceAndUpdatesStub(self.internal.channel)\
                    .GetDifference(
                    request,
                    metadata=(('x-auth-ticket', self.internal.token),)
                ).updates
                break
            except grpc.RpcError as e:
                time.sleep(1)
        return difference

    def __on_seq_update(self):
        self._update_down = False
        for up in self.internal.updates.SeqUpdates(empty_pb2.Empty()):
            if self.manager.run is False:
                return
            self.retry = 0
            while self._load_difference is True:
                time.sleep(0.1)
            update = UpdateSeqUpdate.from_api(up)
            if update.seq <= self._seq:
                continue
            self._seq = update.seq
            self.__update_processing(update)

    def __update_processing(self, update: UpdateSeqUpdate) -> None:
        _callback = None
        if update.type == UpdateType.UPDATE_MESSAGE:
            _callback = self.__update_message_handle(update.update_message)
        elif update.type == UpdateType.UPDATE_MESSAGE_CONTENT_CHANGED:
            _callback = self.__update_message_changed_handle(update.update_message_content_changed)
        elif update.type == UpdateType.UPDATE_INTERACTIVE_MEDIA_EVENT:
            _callback = self.__update_event_handle(update)

        if _callback is None:
            if update.type == UpdateType.UPDATE_THREAD_CREATED:
                out_peer = self.manager.get_out_peer(update.update_thread_created.group_peer)
                if out_peer is not None:
                    request = RequestCreateThread(
                        group_peer=GroupOutPeer(group_id=out_peer.id, access_hash=out_peer.access_hash),
                        root_message_id=update.update_thread_created.root_message_id.to_api()
                    )
                    thread_peer = self.internal.threads.CreateThread(request).peer
                    self.manager.add_thread_out_peer(thread_peer)
            if update.type in self.manager.updates:
                _callback = self.manager.updates[update.type]
            elif "any_updates" in self._default_params:
                _callback = UpdateHandler(
                    self._default_params["any_updates"], update.type,
                    ignored_sleep=self._default_params["ignored_sleep"]
                )

        if _callback is None or not hasattr(_callback, "function") or _callback.function is None:
            return
        if _callback.ignored_sleep is False and self.is_sleep() is True:
            return

        _callback = return_event(self, _callback.function, update.oneof_type())
        if self._default_params["is_async"] is False:
            _callback.wait()
        if self.manager.run is False:
            return

    def __update_message_handle(self, message: UpdateMessage) -> CommandHandler or MessageHandler or None:
        self.manager.set_update_message_out_peers(message)
        out_peer = self.manager.get_out_peer(message.peer)
        if self._default_params["do_received_message"] is True:
            self.internal.messaging.MessageReceived(
                messaging_pb2.RequestMessageReceived(
                    peer=out_peer,
                    date=message.date
                )
            )

        if self._default_params["do_read_message"] is True and message.peer.type == PeerType.PEERTYPE_PRIVATE or \
                message.message.service_message.ext.user_invited == self.manager.user_info.user.peer.id:
            self.internal.messaging.MessageRead(
                messaging_pb2.RequestMessageRead(
                    peer=out_peer,
                    date=message.date
                )
            )
        command = get_command(message, self.manager.user_info.user.data.nick)
        if command is not None and (command[0], message.peer.type) in self.manager.commands:
            return self.manager.commands[(command[0], message.peer.type)]
        if command is not None and (command[0], None) in self.manager.commands:
            return self.manager.commands[(command[0], None)]

        return self.__message_content_handle(message.message, self.manager.messages, message.peer.type)

    def __update_message_changed_handle(self, message: UpdateMessageContentChanged) -> callable or None:
        return self.__message_content_handle(message.message, self.manager.messages_changed, message.peer.type)

    @staticmethod
    def __message_content_handle(message_content: MessageContent, handler: dict, peer_type: PeerType) \
            -> MessageHandler or None:
        message_type = message_content.type
        if message_type == MessageContentType.SERVICE_MESSAGE:
            if (MessageContentType.SERVICE_MESSAGE, message_content.service_message.ext.type, peer_type) in handler:
                return handler[(MessageContentType.SERVICE_MESSAGE, message_content.service_message.ext.type, peer_type)]
            if (MessageContentType.SERVICE_MESSAGE, message_content.service_message.ext.type, None) in handler:
                return handler[(MessageContentType.SERVICE_MESSAGE, message_content.service_message.ext.type, None)]
        if message_type == MessageContentType.DOCUMENT_MESSAGE:
            if (MessageContentType.DOCUMENT_MESSAGE, message_content.document_message.ext.type, peer_type) in handler:
                return handler[(MessageContentType.DOCUMENT_MESSAGE, message_content.document_message.ext.type, peer_type)]
            if (MessageContentType.DOCUMENT_MESSAGE, message_content.document_message.ext.type, None) in handler:
                return handler[(MessageContentType.DOCUMENT_MESSAGE, message_content.document_message.ext.type, None)]
        if message_type == MessageContentType.TEXT_MESSAGE:
            if (MessageContentType.TEXT_MESSAGE, message_content.text_message.ext.type, peer_type) in handler:
                return handler[(MessageContentType.TEXT_MESSAGE, message_content.text_message.ext.type, peer_type)]
            if (MessageContentType.TEXT_MESSAGE, message_content.text_message.ext.type, None) in handler:
                return handler[(MessageContentType.TEXT_MESSAGE, message_content.text_message.ext.type, None)]
        if (message_type, None, peer_type) in handler:
            return handler[(message_type, None, peer_type)]
        if (message_type, None, None) in handler:
            return handler[(message_type, None, None)]

    def __update_event_handle(self, update: UpdateSeqUpdate) -> EventHandler or None:
        self.manager.set_update_interactive_media_event_out_peers(update.update_interactive_media_event)
        event = update.update_interactive_media_event
        id, value = event.id, event.value
        if (id, value) in self.manager.events:
            return self.manager.events[(id, value)]
        if (id, None) in self.manager.events:
            return self.manager.events[(id, None)]
        if (None, value) in self.manager.events:
            return self.manager.events[(None, value)]

    def __update_default_params(self, **kwargs) -> None:
        for k, v in kwargs.items():
            self._default_params[k] = v
