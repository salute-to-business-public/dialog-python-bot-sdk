import io
import logging
import mimetypes
import sys
import time
from typing import List
from concurrent.futures import ThreadPoolExecutor

import six
from PIL import Image
from dialog_api import peers_pb2, media_and_files_pb2, messaging_pb2

from dialog_bot_sdk.entities.Peer import Peer, PeerType
from dialog_bot_sdk.entities.UUID import UUID
from dialog_bot_sdk.exceptions.exceptions import UnknownPeerError


POOL = ThreadPoolExecutor(max_workers=10)


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
    location = bot.internal.uploading.upload_file(file)
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


def read_file_in_chunks(file, chunk_size=1024*1024):
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


class AsyncTask:
    def __init__(self, target, *args, **kwargs):
        self.target = target
        self.args = args
        self.kwargs = kwargs

        self.done = False
        POOL.submit(self._run)

    def _run(self):
        try:
            self.result = self.target(*self.args, **self.kwargs)
        except:
            self.result = sys.exc_info()
            logging.error(self.result[0], self.result[1], self.result[2])
            six.reraise(self.result[0], self.result[1], self.result[2])
        self.done = True

    def wait(self):
        while not self.done:
            time.sleep(0.01)
        if isinstance(self.result, BaseException):
            logging.error(self.result[0], self.result[1], self.result[2])
            six.reraise(self.result[0], self.result[1], self.result[2])
        else:
            logging.debug("target: {}\nargs: {}\nkwargs: {}\nresult: {}\n"
                          .format(self.target, self.args, self.kwargs, self.result))
            return self.result


def async_dec():
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return AsyncTask(fn, *args, **kwargs)

        return wrapper

    return decorator


def get_peer(peer: Peer or AsyncTask) -> peers_pb2.Peer or None:
    if isinstance(peer, AsyncTask):
        from_task = peer.wait()
        if not hasattr(from_task, 'peer'):
            raise AttributeError("{} has not attribute 'peer'".format(type(from_task)))
        peer = from_task.peer
    if not isinstance(peer, Peer):
        raise AttributeError("peer must be {}, got {}.".format(Peer, type(peer)))
    if peer.type in [PeerType.PEERTYPE_PRIVATE, PeerType.PEERTYPE_GROUP]:
        return peers_pb2.Peer(id=peer.id, type=peer.type)
    else:
        raise UnknownPeerError("Unknown PeerType.")


def get_uuids(uuids: List[UUID or AsyncTask]):
    for i in range(len(uuids)):
        uuid = uuids[i]
        if isinstance(uuid, AsyncTask):
            uuid = uuid.wait()
        if isinstance(uuid, UUID):
            uuids[i] = uuid.to_api()
        else:
            raise AttributeError("uuid must be {}, got {}.".format(UUID.__class__, type(uuid)))
    return uuids
