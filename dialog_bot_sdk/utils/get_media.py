import google.protobuf.wrappers_pb2 as wrappers_pb2
from dialog_api import messaging_pb2, media_and_files_pb2
import mimetypes


def get_str_val(s):
    """Return obj google.protobuf.StringValue

    :param s: string
    :return: StringValue
    """
    return wrappers_pb2.StringValue(value=s)


def get_webpage(url, title=None, description=None, image_location=None):
    """Return MessageMedia with WebpageMedia for messaging.send_media

    :param url: url (str)
    :param title: title (str)
    :param description: description (str)
    :param image_location: image (ImageLocation)
    :return: MessageMedia obj
    """
    return messaging_pb2.MessageMedia(
        webpage=messaging_pb2.WebpageMedia(
            url=get_str_val(url),
            title=get_str_val(title),
            description=get_str_val(description),
            image=image_location
        )
    )


def get_image_location(bot, file, width=100, height=100):
    """Return obj ImageLocation

    :param bot: DialogBot
    :param file: image's file
    :param width: image's width
    :param height: image's height
    :return: ImageLocation
    """
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


def get_audio(bot, file, duration=0):
    """Return MessageMedia with AudioMedia for messaging.send_media

    :param bot: DialogBot
    :param file: audio's file
    :param duration: duration audio
    :return: MessageMedia obj
    """
    mime_type = mimetypes.guess_type(file)[0]
    file_location = bot.internal.uploading.upload_file(file)
    return messaging_pb2.MessageMedia(
        audio=messaging_pb2.AudioMedia(
            audio=media_and_files_pb2.AudioLocation(
                file_location=file_location, mime_type=mime_type, duration=duration))
    )
