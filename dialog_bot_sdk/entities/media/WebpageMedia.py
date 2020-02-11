from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.media.ImageMedia import ImageMedia


class WebPageMedia:
    def __init__(self, url: str, title: str, description: str, image: ImageMedia):
        self.url = url
        self.title = title
        self.description = description
        self.image = image

    def to_api(self) -> messaging_pb2.WebpageMedia:
        return messaging_pb2.WebpageMedia(url=self.url, title=self.title, description=self.description,
                                          image=self.image.to_api())

    @classmethod
    def from_api(cls, web_page: messaging_pb2.WebpageMedia) -> 'WebPageMedia':
        return cls(web_page.url, web_page.title, web_page.description, ImageMedia.from_api(web_page.image))

    def __dict__(self):
        return {"url": self.url, "title": self.title, "description": self.description, "image": self.image.__dict__()}

    def __str__(self):
        return "{}".format(self.__dict__())
