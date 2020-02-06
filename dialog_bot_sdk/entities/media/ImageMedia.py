from dialog_api import media_and_files_pb2, messaging_pb2

from dialog_bot_sdk.entities.media.FileLocation import FileLocation


class ImageLocation:
    def __init__(self, file_location: FileLocation, width: int, height: int, file_size: int) -> None:
        self.file_location = file_location
        self.width = width
        self.height = height
        self.file_size = file_size

    def to_api(self) -> media_and_files_pb2.ImageLocation:
        return media_and_files_pb2.ImageLocation(file_location=self.file_location.to_api(), width=self.width,
                                                 height=self.height, file_size=self.file_size)

    @classmethod
    def from_api(cls, image: media_and_files_pb2.ImageLocation) -> 'ImageLocation':
        return cls(FileLocation.from_api(image.file_location), image.width, image.height, image.file_size)


class ImageMedia:
    def __init__(self, image: ImageLocation) -> None:
        self.image = image

    def to_api(self) -> messaging_pb2.ImageMedia:
        return messaging_pb2.ImageMedia(image=self.image)

    @classmethod
    def from_api(cls, image: messaging_pb2.ImageMedia) -> 'ImageMedia':
        return cls(ImageLocation.from_api(image))
