from typing import List

from dialog_api import authentication_pb2

from dialog_bot_sdk.entities.miscellaneous import Config
from dialog_bot_sdk.entities.peers import Peer
from dialog_bot_sdk.entities.users import User


class AuthExtraInfoType:
    NONE_EXTRA_INFO = authentication_pb2.NONE_EXTRA_INFO
    NEED_CHANGE_PASSWORD = authentication_pb2.NEED_CHANGE_PASSWORD


class ForceReloadFieldType:
    FORCE_RELOAD_DIALOGS = "force_reload_dialogs"
    FORCE_RELOAD_CONTACTS = "force_reload_contacts"
    FORCE_RELOAD_HISTORY = "force_reload_history"


force_reload_field_type_mapper = {
    "forceReloadDialogs": ForceReloadFieldType.FORCE_RELOAD_DIALOGS,
    "forceReloadContacts": ForceReloadFieldType.FORCE_RELOAD_CONTACTS,
    "forceReloadHistory": ForceReloadFieldType.FORCE_RELOAD_HISTORY,
}


class ForceReloadDialogs:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_api(cls, force_reload: authentication_pb2.ForceReloadDialogs) -> 'ForceReloadDialogs':
        return cls()

    def __dict__(self):
        return {}

    def __str__(self):
        return "ForceReloadDialogs({})".format(self.__dict__())


class ForceReloadContacts:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_api(cls, force_reload: authentication_pb2.ForceReloadContacts) -> 'ForceReloadContacts':
        return cls()

    def __dict__(self):
        return {}

    def __str__(self):
        return "ForceReloadContacts({})".format(self.__dict__())


class ForceReloadHistory:
    def __init__(self, peer: Peer) -> None:
        self.peer = peer

    @classmethod
    def from_api(cls, force_reload: authentication_pb2.ForceReloadHistory) -> 'ForceReloadHistory':
        return cls(Peer.from_api(force_reload.peer))

    def __dict__(self):
        return {"peer": self.peer.__dict__()}

    def __str__(self):
        return "ForceReloadHistory({})".format(self.__dict__())


class ForceReloadField:
    def __init__(
            self,
            type: ForceReloadFieldType,
            force_reload_dialogs: ForceReloadDialogs,
            force_reload_contacts: ForceReloadContacts,
            force_reload_history: ForceReloadHistory
    ) -> None:
        self.type = type
        self.force_reload_dialogs = force_reload_dialogs
        self.force_reload_contacts = force_reload_contacts
        self.force_reload_history = force_reload_history

    @classmethod
    def from_api(cls, field: authentication_pb2.ForceReloadField) -> 'ForceReloadField':
        return cls(
            force_reload_field_type_mapper.get(field.WhichOneof('body')),
            ForceReloadDialogs.from_api(field.forceReloadDialogs),
            ForceReloadContacts.from_api(field.forceReloadContacts),
            ForceReloadHistory.from_api(field.forceReloadHistory)
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == ForceReloadFieldType.FORCE_RELOAD_DIALOGS:
            return self.force_reload_dialogs
        if self.type == ForceReloadFieldType.FORCE_RELOAD_CONTACTS:
            return self.force_reload_contacts
        if self.type == ForceReloadFieldType.FORCE_RELOAD_HISTORY:
            return self.force_reload_history

    def __str__(self):
        return "ForceReloadField({})".format(self.__dict__())


class UserInfo:
    def __init__(self, user: User, config: Config, config_hash: int, extra_info: AuthExtraInfoType) -> None:
        self.user = user
        self.config = config
        self.config_hash = config_hash
        self.extra_info = extra_info

    @classmethod
    def from_api(cls, user_info: authentication_pb2.ResponseAuth) -> 'UserInfo':
        return cls(User.from_api(user_info.user), Config.from_api(user_info.config), user_info.config_hash.value,
                   user_info.extra_info)

    def __dict__(self):
        return {"user": self.user.__dict__(), "config": self.config.__dict__(), "config_hash": self.config_hash,
                "extra_info": self.extra_info}

    def __str__(self):
        return "UserInfo({})".format(self.__dict__())


# updates
class UpdateForceReloadState:
    def __init__(self, fields: List[ForceReloadField]) -> None:
        self.fields = fields

    @classmethod
    def from_api(cls, update: authentication_pb2.UpdateForceReloadState) -> 'UpdateForceReloadState':
        return cls([ForceReloadField.from_api(x) for x in update.fields])

    def __dict__(self):
        return {"fields": [x.__dict__() for x in self.fields]}

    def __str__(self):
        return "UpdateForceReloadState({})".format(self.__dict__())
