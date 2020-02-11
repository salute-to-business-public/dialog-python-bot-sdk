from dialog_api import messaging_pb2


class DocumentExtPhoto:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, photo: messaging_pb2.DocumentExPhoto) -> 'DocumentExtPhoto':
        return cls(photo.h, photo.w)

    def __dict__(self):
        return {"height": self.height, "width": self.width}

    def __str__(self):
        return "{}".format(self.__dict__())


class DocumentExtVideo:
    def __init__(self, duration: int, height: int, width: int) -> None:
        self.duration = duration
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, video: messaging_pb2.DocumentExVideo) -> 'DocumentExtVideo':
        return cls(video.duration, video.h, video.w)

    def __dict__(self):
        return {"duration": self.duration, "height": self.height, "width": self.width}

    def __str__(self):
        return "{}".format(self.__dict__())


class DocumentExtVoice:
    def __init__(self, duration: int) -> None:
        self.duration = duration

    @classmethod
    def from_api(cls, voice: messaging_pb2.DocumentExVoice) -> 'DocumentExtVoice':
        return cls(voice.duration)

    def __dict__(self):
        return {"duration": self.duration}

    def __str__(self):
        return "{}".format(self.__dict__())


class DocumentExt:
    def __init__(self, photo: DocumentExtPhoto, video: DocumentExtVideo, voice: DocumentExtVoice) -> None:
        self.photo = photo
        self.video = video
        self.voice = voice

    @classmethod
    def from_api(cls, ext: messaging_pb2.DocumentEx) -> 'DocumentExt':
        return cls(DocumentExtPhoto.from_api(ext.photo), DocumentExtVideo.from_api(ext.video),
                   DocumentExtVoice.from_api(ext.voice))

    def __dict__(self):
        return {"photo": self.photo.__dict__(), "video": self.video.__dict__(), "voice": self.voice.__dict__(), }

    def __str__(self):
        return "{}".format(self.__dict__())


class DocumentMessage:
    def __init__(self, file_id: int, access_hash: int, file_size: int, mime_type: str, name: str, ext: DocumentExt) -> None:
        self.file_id = file_id
        self.access_hash = access_hash
        self.file_size = file_size
        self.mime_type = mime_type
        self.name = name
        self.ext = ext

    @classmethod
    def from_api(cls, document: messaging_pb2.DocumentMessage) -> 'DocumentMessage':
        return cls(document.file_id, document.access_hash, document.file_size, document.mime_type, document.name,
                   DocumentExt.from_api(document.ext))

    def __dict__(self):
        return {"file_id": self.file_id, "access_hash": self.access_hash, "file_size": self.file_size,
                "mime_type": self.mime_type, "name": self.name, "ext": self.ext.__dict__()}

    def __str__(self):
        return "{}".format(self.__dict__())
