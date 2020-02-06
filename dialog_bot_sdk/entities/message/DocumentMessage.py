from dialog_api import messaging_pb2


class DocumentExtPhoto:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, photo: messaging_pb2.DocumentExPhoto) -> 'DocumentExtPhoto':
        return cls(photo.height, photo.width)


class DocumentExtVideo:
    def __init__(self, duration: int, height: int, width: int) -> None:
        self.duration = duration
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, video: messaging_pb2.DocumentExVideo) -> 'DocumentExtVideo':
        return cls(video.duration, video.height, video.width)


class DocumentExtVoice:
    def __init__(self, duration: int) -> None:
        self.duration = duration

    @classmethod
    def from_api(cls, voice: messaging_pb2.DocumentExVoice) -> 'DocumentExtVoice':
        return cls(voice.duration)


class DocumentExt:
    def __init__(self, photo: DocumentExtPhoto, video: DocumentExtVideo, voice: DocumentExtVoice) -> None:
        self.photo = photo
        self.video = video
        self.voice = voice

    @classmethod
    def from_api(cls, ext: messaging_pb2.DocumentEx) -> 'DocumentExt':
        return cls(DocumentExtPhoto.from_api(ext.photo), DocumentExtVideo.from_api(ext.video),
                   DocumentExtVoice.from_api(ext.voice))


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
