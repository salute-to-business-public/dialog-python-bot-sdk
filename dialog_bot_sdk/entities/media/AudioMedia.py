from dialog_api import media_and_files_pb2, messaging_pb2

from dialog_bot_sdk.entities.media.FileLocation import FileLocation


class AudioLocation:
    def __init__(self, file_location: FileLocation, duration: int, mime_type: str, file_size: int) -> None:
        self.file_location = file_location
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    def to_api(self) -> media_and_files_pb2.AudioLocation:
        return media_and_files_pb2.AudioLocation(file_location=self.file_location.to_api(), duration=self.duration,
                                                 mime_type=self.mime_type, file_size=self.file_size)

    @classmethod
    def from_api(cls, audio: media_and_files_pb2.AudioLocation) -> 'AudioLocation':
        return cls(FileLocation.from_api(audio.file_location), audio.duration, audio.mime_type.value, audio.file_size)


class AudioMedia:
    def __init__(self, audio: AudioLocation) -> None:
        self.audio = audio

    def to_api(self) -> messaging_pb2.AudioMedia:
        return messaging_pb2.AudioMedia(audio=self.audio)

    @classmethod
    def from_api(cls, image: messaging_pb2.AudioMedia) -> 'AudioMedia':
        return cls(AudioLocation.from_api(image))
