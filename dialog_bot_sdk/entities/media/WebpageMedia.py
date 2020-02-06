from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.media.ImageMedia import ImageMedia


class WebpageMedia:
    def __init__(self, url: str, title: str, description: str, image: ImageMedia):
        self.url = url
        self.title = title
        self.description = description
        self.image = image

    def to_api(self) -> messaging_pb2.WebpageMedia:
        return messaging_pb2.WebpageMedia(url=self.url, title=self.title, description=self.description,
                                          image=self.image.to_api())

    @classmethod
    def from_api(cls, webpage: messaging_pb2.WebpageMedia) -> 'WebpageMedia':
        return cls(webpage.url, webpage.title, webpage.description, ImageMedia.from_api(webpage.image))
