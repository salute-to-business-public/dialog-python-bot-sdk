from dialog_api import media_and_files_pb2


class ColorType:
    RGB = "rgb"
    PREDEFINED = "predefined"


color_type_mapper = {
    "rgb": ColorType.RGB,
    "predefined": ColorType.PREDEFINED,
}


class FileLocation:
    def __init__(self, file_id: int, access_hash: int) -> None:
        self.file_id = file_id
        self.access_hash = access_hash

    def to_api(self) -> media_and_files_pb2.FileLocation:
        return media_and_files_pb2.FileLocation(file_id=self.file_id, access_hash=self.access_hash)

    @classmethod
    def from_api(cls, location: media_and_files_pb2.FileLocation) -> 'FileLocation':
        return cls(location.file_id, location.access_hash)

    def __dict__(self):
        return {"file_id": self.file_id, "access_hash": self.access_hash}

    def __str__(self):
        return "FileLocation({})".format(self.__dict__())


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
        return "AvatarImage({})".format(self.__dict__())


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
        return "Avatar({})".format(self.__dict__())


class AudioLocation:
    def __init__(self, file_location: FileLocation, duration: int = 0, mime_type: str = "",
                 file_size: int = 0) -> None:
        self.file_location = file_location
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    def to_api(self) -> media_and_files_pb2.AudioLocation:
        return media_and_files_pb2.AudioLocation(file_location=self.file_location.to_api(), duration=self.duration,
                                                 mime_type=self.mime_type, file_size=self.file_size)

    @classmethod
    def from_api(cls, audio: media_and_files_pb2.AudioLocation) -> 'AudioLocation':
        return cls(FileLocation.from_api(audio.file_location), audio.duration, audio.mime_type, audio.file_size)

    def __dict__(self):
        return {"file_location": self.file_location.__dict__(), "duration": self.duration,
                "mime_type": self.mime_type, "file_size": self.file_size}

    def __str__(self):
        return "AudioLocation({})".format(self.__dict__())


class ImageLocation:
    def __init__(self, file_location: FileLocation, width: int = 100, height: int = 100,
                 file_size: int = 0) -> None:
        self.file_location = file_location
        self.width = width
        self.height = height
        self.file_size = file_size

    def to_api(self) -> media_and_files_pb2.ImageLocation:
        # if isinstance(self.file_location, AsyncTask):
        #     self.file_location.wait()
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


class RgbColor:
    def __init__(self, rgb: int) -> None:
        self.rgb = rgb

    @classmethod
    def from_api(cls, color: media_and_files_pb2.RgbColor) -> 'RgbColor':
        return cls(color.rgb)

    def __dict__(self):
        return {"rgb": self.rgb}

    def __str__(self):
        return "RgbColor({})".format(self.__dict__())


class PredefinedColor:
    def __init__(self, color: int) -> None:
        self.color = color

    @classmethod
    def from_api(cls, color: media_and_files_pb2.PredefinedColor) -> 'PredefinedColor':
        return cls(color.color)

    def __dict__(self):
        return {"color": self.color}

    def __str__(self):
        return "PredefinedColor({})".format(self.__dict__())


class Color:
    def __init__(self, type: ColorType, rgb: RgbColor, predefined: PredefinedColor) -> None:
        self.type = type
        self.rgb = rgb
        self.predefined = predefined

    @classmethod
    def from_api(cls, color: media_and_files_pb2.Color) -> 'Color':
        return cls(
            color_type_mapper.get(color.WhichOneof('body')),
            RgbColor.from_api(color.rgb),
            PredefinedColor.from_api(color.predefined)
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == ColorType.RGB:
            return self.rgb
        if self.type == ColorType.PREDEFINED:
            return self.predefined

    def __str__(self):
        return "Color({})".format(self.__dict__())


class FastThumb:
    def __init__(self, w: int, h: int, thumb: bytes) -> None:
        self.w = w
        self.h = h
        self.thumb = thumb

    @classmethod
    def from_api(cls, thumb: media_and_files_pb2.FastThumb) -> 'FastThumb':
        return cls(thumb.w, thumb.h, thumb.thumb)

    def __dict__(self):
        return {"w": self.w, "h": self.h, "thumb": self.thumb}

    def __str__(self):
        return "FastThumb({})".format(self.__dict__())
