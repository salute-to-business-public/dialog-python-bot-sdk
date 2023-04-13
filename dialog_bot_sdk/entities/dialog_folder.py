from typing import List

from dialog_api import dialog_folder_pb2

from dialog_bot_sdk.entities.peers import Peer


class DialogFolderType:
    DIALOG_FOLDER_TYPE_UNKNOWN = dialog_folder_pb2.DIALOG_FOLDER_TYPE_UNKNOWN
    DIALOG_FOLDER_TYPE_CUSTOM = dialog_folder_pb2.DIALOG_FOLDER_TYPE_CUSTOM
    DIALOG_FOLDER_TYPE_UNREAD = dialog_folder_pb2.DIALOG_FOLDER_TYPE_UNREAD
    DIALOG_FOLDER_TYPE_GROUPS = dialog_folder_pb2.DIALOG_FOLDER_TYPE_GROUPS
    DIALOG_FOLDER_TYPE_CHANNELS = dialog_folder_pb2.DIALOG_FOLDER_TYPE_CHANNELS


class DialogFolder:
    def __init__(self, type_: DialogFolderType, id_: int, name: str, peers: List[Peer]) -> None:
        self.type = type_
        self.id = id_
        self.name = name
        self.peers = peers

    @classmethod
    def from_api(cls, update: dialog_folder_pb2.DialogFolder) -> 'DialogFolder':
        return cls(update.type, update.id, update.name, [Peer.from_api(x) for x in update.peers])

    def __dict__(self):
        return {"type": self.type, "id": self.id, "name": self.name, "peers": [x.__dict__() for x in self.peers]}

    def __str__(self):
        return "DialogFolder({})".format(self.__dict__())


# updates
class UpdateDialogFolderChanged:
    def __init__(self, folder: DialogFolder) -> None:
        self.folder = folder

    @classmethod
    def from_api(cls, update: dialog_folder_pb2.UpdateDialogFolderChanged) -> 'UpdateDialogFolderChanged':
        return cls(DialogFolder.from_api(update.folder))

    def __dict__(self):
        return {"folder": self.folder}

    def __str__(self):
        return "UpdateDialogFolderChanged({})".format(self.__dict__())


class UpdateDialogFolderDeleted:
    def __init__(self, id_: int) -> None:
        self.id = id_

    @classmethod
    def from_api(cls, update: dialog_folder_pb2.UpdateDialogFolderDeleted) -> 'UpdateDialogFolderDeleted':
        return cls(update.id)

    def __dict__(self):
        return {"id": self.id}

    def __str__(self):
        return "UpdateDialogFolderDeleted({})".format(self.__dict__())


class UpdateDialogFoldersOrderChanged:
    def __init__(self, order: List[int]) -> None:
        self.order = order

    @classmethod
    def from_api(cls, update: dialog_folder_pb2.UpdateDialogFoldersOrderChanged) -> 'UpdateDialogFoldersOrderChanged':
        return cls(update.order)

    def __dict__(self):
        return {"order": self.order}

    def __str__(self):
        return "UpdateDialogFoldersOrderChanged({})".format(self.__dict__())
