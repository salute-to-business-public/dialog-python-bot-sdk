from dialog_api import media_and_files_pb2, messaging_pb2

from dialog_bot_sdk.entities.media.FileLocation import FileLocation
from dialog_bot_sdk.utils import AsyncTask


class ImageLocation:
    def __init__(self, file_location: FileLocation or AsyncTask, width: int = 100, height: int = 100,
                 file_size: int = 0) -> None:
        self.file_location = file_location
        self.width = width
        self.height = height
        self.file_size = file_size

    def to_api(self) -> media_and_files_pb2.ImageLocation:
        if isinstance(self.file_location, AsyncTask):
            self.file_location.wait()
        return media_and_files_pb2.ImageLocation(file_location=self.file_location.to_api(), width=self.width,
                                                 height=self.height, file_size=self.file_size)

    @classmethod
    def from_api(cls, image: media_and_files_pb2.ImageLocation) -> 'ImageLocation':
        return cls(FileLocation.from_api(image.file_location), image.width, image.height, image.file_size)

    def __dict__(self):
        return {"file_location": self.file_location.__dict__(), "width": self.width, "height": self.height,
                "file_size": self.file_size}

    def __str__(self):
        return "ImageLocation({})".format(self.__dict__())


class ImageMedia:
    def __init__(self, image: ImageLocation) -> None:
        self.image = image

    def to_api(self) -> messaging_pb2.ImageMedia:
        return messaging_pb2.ImageMedia(image=self.image.to_api())

    @classmethod
    def from_api(cls, image: messaging_pb2.ImageMedia) -> 'ImageMedia':
        return cls(ImageLocation.from_api(image.image))

    def __dict__(self):
        return {"image": self.image.__dict__()}

    def __str__(self):
        return "ImageMedia({})".format(self.__dict__())
