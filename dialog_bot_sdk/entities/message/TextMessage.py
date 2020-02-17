from typing import List

from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.media.AudioMedia import AudioMedia
from dialog_bot_sdk.entities.media.ImageMedia import ImageMedia
from dialog_bot_sdk.entities.media.InteractiveMediaGroup import InteractiveMediaGroup
from dialog_bot_sdk.entities.media.WebpageMedia import WebPageMedia


class MessageMedia:
    def __init__(self, web_page: WebPageMedia = None, image: ImageMedia = None, audio: AudioMedia = None,
                 actions: List[InteractiveMediaGroup] = None) -> None:
        self.web_page = web_page
        self.image = image
        self.audio = audio
        self.actions = actions

    def to_api(self) -> messaging_pb2.MessageMedia:
        web, image, audio, actions = None, None, None, []
        if self.web_page is not None:
            web = self.web_page.to_api()
        if self.image is not None:
            image = self.image.to_api()
        if self.audio is not None:
            audio = self.audio.to_api()
        if self.actions is not None:
            actions = [x.to_api() for x in self.actions]
        return messaging_pb2.MessageMedia(webpage=web, image=image, audio=audio, actions=actions)

    @classmethod
    def from_api(cls, message_media: messaging_pb2.MessageMedia) -> 'MessageMedia':
        return cls(WebPageMedia.from_api(message_media.webpage), ImageMedia.from_api(message_media.image),
                   AudioMedia.from_api(message_media.audio),
                   [InteractiveMediaGroup.from_api(x) for x in message_media.actions])

    def __dict__(self):
        return {"web_page": self.web_page.__dict__(), "image": self.image.__dict__(),
                "audio": self.audio.__dict__(), "actions": [x.__dict__() for x in self.actions]}

    def __str__(self):
        return "MessageMedia({})".format(self.__dict__())


class TextMessage:
    def __init__(self, text: str, media: List[MessageMedia],
                 mentions: List[int]) -> None:
        self.text = text
        self.media = media
        self.mentions = mentions

    @classmethod
    def from_api(cls, text_message: messaging_pb2.TextMessage) -> 'TextMessage':
        return cls(text_message.text,
                   [MessageMedia.from_api(x) for x in text_message.media], [x for x in text_message.mentions])

    def __dict__(self):
        return {"text": self.text, "media": [x.__dict__() for x in self.media], "mentions": self.mentions}

    def __str__(self):
        return "TextMessage({})".format(self.__dict__())
