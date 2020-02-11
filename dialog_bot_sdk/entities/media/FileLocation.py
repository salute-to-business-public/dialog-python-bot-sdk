from dialog_api import media_and_files_pb2


class FileLocation:
    def __init__(self, file_id: int, access_hash: int) -> None:
        self.file_id = file_id
        self.access_hash = access_hash

    def to_api(self) -> media_and_files_pb2.FileLocation:
        return FileLocation(file_id=self.file_id, access_hash=self.access_hash)

    @classmethod
    def from_api(cls, location: media_and_files_pb2.FileLocation) -> 'FileLocation':
        return cls(location.file_id, location.access_hash)

    def __dict__(self):
        return {"file_id": self.file_id, "access_hash": self.access_hash}

    def __str__(self):
        return "{}".format(self.__dict__())
