import functools
import io
import logging
import mimetypes
import os
import re
import sys
import time
import traceback
import warnings
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor
import six
from PIL import Image
from dialog_bot_sdk.entities.messaging import UpdateMessage, Message
from dialog_api import peers_pb2, media_and_files_pb2, messaging_pb2
from dialog_api.media_and_files_pb2 import FileLocation
from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.peers import PeerType, Peer
from dialog_bot_sdk.exceptions.exceptions import UnknownPeerError


POOL = ThreadPoolExecutor(max_workers=10)
LOG_LEVEL = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL
}
default_logger_config = {
    "level": "error",
    "stream_handler_level": "error",
    "stream_log_format":
        "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
}


def get_stream_handler(stream_handler_level: str, stream_log_format: str) -> logging.StreamHandler:
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(LOG_LEVEL[stream_handler_level])
    stream_handler.setFormatter(logging.Formatter(stream_log_format))
    return stream_handler


def get_logger(name: str, config: dict):
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL[config["level"]])
    logger.addHandler(get_stream_handler(config["stream_handler_level"], config["stream_log_format"]))
    logger.propagate = False
    return logger


log = get_logger(__name__, default_logger_config)


def build_error_string(e, **kwargs) -> str:
    result = str(e) + "\n"
    return result + build_log_string(**kwargs)


def build_log_string(**kwargs) -> str:
    kwargs_list = []
    for k, v in kwargs.items():
        kwargs_list.append("%s: %s" % (k, v))
    return "\n".join(kwargs_list)


def get_image_w_h(file):
    """Returns image's width and height

    :param file: path to image
    :return: (width, height) tuple
    """

    im = Image.open(file)
    return im.size


def get_image_thumb_bytes(file):
    """Returns image's thumbnail in form of byte array

    :param file: path to image
    :return: size and byte array
    """

    size = 90, 90

    im = Image.open(file)
    im = im.convert('RGB')
    im.thumbnail(size)
    stream = io.BytesIO()
    im.save(stream, "JPEG")

    return size[0], size[1], stream.getvalue()


def get_image_location(bot, file, width=100, height=100):
    """Return obj ImageLocation

    :param bot: DialogBot
    :param file: image's file
    :param width: image's width
    :param height: image's height
    :return: ImageLocation
    """
    if not is_image(file):
        raise IOError('File is not an image.')
    location = bot.internal.uploading.upload_file_sync(file)
    return media_and_files_pb2.ImageLocation(file_location=location, width=width, height=height)


def get_image(bot, file, width=100, height=100):
    """Return MessageMedia with ImageMedia for messaging.send_media

    :param bot: DialogBot
    :param file: image's file
    :param width: subj
    :param height: subj
    :return: MessageMedia obj
    """
    image_location = get_image_location(bot, file, width, height)
    return messaging_pb2.MessageMedia(image=messaging_pb2.ImageMedia(image=image_location))


def is_image(file):
    mime = mimetypes.guess_type(file)[0]
    return mime in ['image/jpeg', 'image/png', 'image/gif', 'image/bmp']


def is_video(file):
    mime = mimetypes.guess_type(file)[0]
    return mime.split("/")[0] == "video"


def read_file_in_chunks(file: str, chunk_size: int = 1024*1024):
    """File chunks generator

    :param file: path to file
    :param chunk_size: size of a chunk
    :return: generator object that iterates over file chunks
    """
    file_object = open(file, 'rb')
    while True:
        data = file_object.read(chunk_size)
        if not data:
            file_object.close()
            break
        yield data


def read_file_content_in_chunks(file: bytes, chunk_size: int = 1024*1024):
    """File chunks generator

    :param file: path to file
    :param chunk_size: size of a chunk
    :return: generator object that iterates over file chunks
    """
    index = 0
    while index < len(file):
        data = file[index: index + chunk_size]
        index += chunk_size
        if not data:
            break
        yield data


def get_document_content(file: str or bytes, location: FileLocation, name=None) -> messaging_pb2.DocumentMessage:
    """Prepares DocumentMessage object that contains metadata for file sending request.

    :param file: path to file
    :param location: FileLocation object
    :param name: file name
    :return: DocumentMessage object
    """

    content = messaging_pb2.DocumentMessage()

    content.file_id = location.file_id
    content.access_hash = location.access_hash
    if name is not None:
        content.name = name
    else:
        content.name = os.path.basename(file)
    content.file_size = os.path.getsize(file) if isinstance(file, str) else len(file)

    return content


def get_image_content(file: str, location: FileLocation, name=None) -> messaging_pb2.DocumentMessage:
    """Same as get_document_content for image sending.

    :param file: path to image
    :param location: FileLocation object
    :param name: image name
    :return: DocumentMessage object
    """

    content = get_document_content(file, location, name)

    content.mime_type = mimetypes.guess_type(file)[0]
    content.thumb.w, content.thumb.h, content.thumb.thumb = get_image_thumb_bytes(file)

    ext = messaging_pb2.DocumentEx()

    photo = messaging_pb2.DocumentExPhoto()
    photo.w, photo.h = get_image_w_h(file)
    ext.photo.CopyFrom(photo)
    content.ext.CopyFrom(ext)

    return content


class AsyncTask:
    def __init__(self, target: callable, poll_type: str, *args, **kwargs):
        self.target = target
        self.args = args
        self.poll = args[0].manager.methods_pool if poll_type == "methods_pool" else args[0].manager.update_pool
        self.kwargs = kwargs
        self.done = False
        self.poll.submit(self._run)

    def _run(self):
        try:
            self.result = self.target(*self.args, **self.kwargs)
        except:
            log.error(traceback.format_exc())
            self.result = sys.exc_info()
            six.reraise(self.result[0], self.result[1], self.result[2])
        self.done = True

    def wait(self):
        while not self.done:
            time.sleep(0.01)
        if isinstance(self.result, BaseException):
            log.error(traceback.format_exc())
            six.reraise(self.result[0], self.result[1], self.result[2])
        else:
            log.debug("target: {}\nargs: {}\nkwargs: {}\nresult: {}\n"
                      .format(self.target, self.args, self.kwargs, self.result))
            return self.result


def async_dec(poll_type: str = "methods_pool"):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            return AsyncTask(fn, poll_type, *args, **kwargs)
        return wrapper
    return decorator


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return new_func


def get_peer(peer: Peer or AsyncTask) -> peers_pb2.Peer or None:
    if isinstance(peer, AsyncTask):
        from_task = peer.wait()
        if not hasattr(from_task, 'peer'):
            raise AttributeError("{} has not attribute 'peer'".format(type(from_task)))
        peer = from_task.peer
    if not isinstance(peer, Peer):
        raise AttributeError("peer must be {}, got {}.".format(Peer, type(peer)))
    if peer.type in [PeerType.PEERTYPE_PRIVATE, PeerType.PEERTYPE_GROUP, PeerType.PEERTYPE_THREAD]:
        return peers_pb2.Peer(id=peer.id, type=peer.type)
    else:
        raise UnknownPeerError("Unknown PeerType.")


def get_uuids(uuids: List[UUID or AsyncTask]) -> List[UUID]:
    result = []
    for uuid in uuids:
        result.append(get_uuid(uuid))
    return result


def get_uuid(uuid: UUID or AsyncTask) -> UUID:
    if isinstance(uuid, AsyncTask):
        uuid = uuid.wait()
    if isinstance(uuid, UUID):
        uuid = uuid.to_api()
    else:
        raise AttributeError("uuid must be {}, got {}.".format(UUID.__class__, type(uuid)))
    return uuid


@async_dec("update_pool")
def return_event(self, callback, params):
    callback(params)


def get_command(message: UpdateMessage or Message, nick: str) -> Tuple[str, str] or None:
    text = message.message.text_message.text
    if message.peer.type == PeerType.PEERTYPE_PRIVATE:
        split_text = text.split(" ", 1)
        command = is_command(split_text[0])
        if command:
            return command, split_text[1] if len(split_text) == 2 else ""
    elif message.peer.type in (PeerType.PEERTYPE_GROUP, PeerType.PEERTYPE_THREAD):
        split_text = text.split(" ", 2)
        if split_text[0] != "@" + nick or len(split_text) < 2:
            return
        command = is_command(split_text[1])
        if command:
            return command, split_text[2] if len(split_text) == 3 else ""


def is_command(text: str) -> str or None:
    try:
        regs = re.search(r'/[\w]+', text).regs[0]
        return text[regs[0]:regs[1]][1:]
    except:
        return None
