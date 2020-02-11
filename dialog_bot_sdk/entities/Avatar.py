from dialog_bot_sdk.entities.media.FileLocation import FileLocation
from dialog_api import media_and_files_pb2


class AvatarImage:
    def __init__(self, file_location: FileLocation, file_size: int, height: int, width: int) -> None:
        self.file_location = file_location
        self.file_size = file_size
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, avatar_image: media_and_files_pb2.AvatarImage) -> 'AvatarImage':
        return cls(FileLocation(avatar_image.file_location.file_id, avatar_image.file_location.access_hash),
                   avatar_image.file_size, avatar_image.height, avatar_image.width)

    def __dict__(self):
        return {"file_location": self.file_location.__dict__(), "file_size": self.file_size,
                "height": self.height, "width": self.width}

    def __str__(self):
        return "{}".format(self.__dict__())


class Avatar:
    def __init__(self, small_image: AvatarImage, large_image: AvatarImage, full_image: AvatarImage) -> None:
        self.small_image = small_image
        self.large_image = large_image
        self.full_image = full_image

    @classmethod
    def from_api(cls, avatar: media_and_files_pb2.Avatar) -> 'Avatar':
        return cls(AvatarImage.from_api(avatar.small_image),
                   AvatarImage.from_api(avatar.large_image),
                   AvatarImage.from_api(avatar.full_image))

    def __dict__(self):
        return {"small_image": self.small_image.__dict__(), "large_image": self.large_image.__dict__(),
                "full_image": self.full_image.__dict__()}

    def __str__(self):
        return "avatar: {}".format(self.__dict__())
