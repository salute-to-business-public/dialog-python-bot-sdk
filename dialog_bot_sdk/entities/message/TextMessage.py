from typing import List

from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.media.AudioMedia import AudioMedia
from dialog_bot_sdk.entities.media.ImageMedia import ImageMedia
from dialog_bot_sdk.entities.media.InteractiveMediaGroup import InteractiveMediaGroup
from dialog_bot_sdk.entities.media.WebpageMedia import WebpageMedia


class TextCommand:
    def __init__(self, args: str, command: str) -> None:
        self.args = args
        self.command = command

    @classmethod
    def from_api(cls, command: messaging_pb2.TextCommand) -> 'TextCommand':
        return cls(command.args.value, command.command.value)


class TextExMarkdown:
    def __init__(self, markdown: str) -> None:
        self.markdown = markdown

    @classmethod
    def from_api(cls, markdown: messaging_pb2.TextExMarkdown) -> 'TextExMarkdown':
        return cls(markdown.markdown.value)


# class TextModernMessage:
#     def __init__(self, attaches: List[], sender_name_override: str, sender_photo_override: Avatar, text: str) -> None:
#         self.attaches = attaches
#         self.sender_name_override = sender_name_override
#         self.sender_photo_override = sender_photo_override
#         self.text = text
#
#     @classmethod
#     def from_api(cls, modern: messaging_pb2.TextModernMessage) -> 'TextModernMessage':
#         return cls([], modern.sender_name_override.value, Avatar.from_api(modern.sender_name_override),
#                    modern.text.value)


class TextMessageEx:
    def __init__(self, text_command: TextCommand, text_ex_markdown: TextExMarkdown) -> None:
        self.textCommand = text_command
        self.textExMarkdown = text_ex_markdown
        # self.textModernMessage = text_modern_message

    @classmethod
    def from_api(cls, ext: messaging_pb2.TextMessageEx) -> 'TextMessageEx':
        return cls(TextCommand.from_api(ext.textCommand), TextExMarkdown.from_api(ext.textExMarkdown),
                   # TextModernMessage.from_api(ext.textModernMessage)
                   )


class MessageMedia:
    def __init__(self, webpage: WebpageMedia, image: ImageMedia, audio: AudioMedia,
                 actions: List[InteractiveMediaGroup]) -> None:
        self.webpage = webpage
        self.image = image
        self.audio = audio
        self.actions = actions

    def to_api(self) -> messaging_pb2.MessageMedia:
        return messaging_pb2.MessageMedia(webpage=self.webpage.to_api(), image=self.image.to_api(),
                                          audio=self.audio.to_api(), actions=[x.to_api() for x in self.actions])

    @classmethod
    def from_api(cls, message_media: messaging_pb2.MessageMedia) -> 'MessageMedia':
        return cls(WebpageMedia.from_api(message_media.webpage), ImageMedia.from_api(message_media.image),
                   AudioMedia.from_api(message_media.audio),
                   [InteractiveMediaGroup.from_api(x) for x in message_media.actions])


# extensions: List[]
class TextMessage:
    def __init__(self, text: str, ext: TextMessageEx, media: List[MessageMedia],
                 mentions: List[int]) -> None:
        self.text = text
        self.ext = ext
        self.media = media
        self.mentions = mentions

    @classmethod
    def from_api(cls, text_message: messaging_pb2.TextMessage) -> 'TextMessage':
        return cls(text_message.text, TextMessageEx.from_api(text_message.ext),
                   [MessageMedia.from_api(x) for x in text_message.media], [x for x in text_message.mentions])