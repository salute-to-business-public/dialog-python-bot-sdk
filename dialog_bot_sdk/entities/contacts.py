from typing import List

from dialog_api import contacts_pb2

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.peers import Peer, PeerType


# updates
class UpdateContactRegistered:
    def __init__(self, peer: Peer, is_silent: bool, date: int, mid: UUID) -> None:
        self.peer = peer
        self.is_silent = is_silent
        self.date = date
        self.mid = mid

    @classmethod
    def from_api(cls, update: contacts_pb2.UpdateContactRegistered) -> 'UpdateContactRegistered':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.is_silent, update.date, UUID.from_api(update.mid))

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "is_silent": self.is_silent, "date": self.date, "mid": self.mid.__dict__()}

    def __str__(self):
        return "UpdateContactRegistered({})".format(self.__dict__())


class UserPhoneHashContact:
    def __init__(self, peer: Peer, phone_hash: str, name: str) -> None:
        self.peer = peer
        self.phone_hash = phone_hash
        self.name = name

    @classmethod
    def from_api(cls, update: contacts_pb2.UserPhoneHashContact) -> 'UserPhoneHashContact':
        return cls(Peer(update.user_id, PeerType.PEERTYPE_PRIVATE), update.phone_hash, update.name)

    def __dict__(self):
        return {"peer":  self.peer.__dict__(), "phone_hash": self.phone_hash, "name": self.name}

    def __str__(self):
        return "UserPhoneHashContact({})".format(self.__dict__())


class UpdateContactsAdded:
    def __init__(self, peers: List[Peer], task_id: str, phone_contacts: List[UserPhoneHashContact]) -> None:
        self.peers = peers
        self.task_id = task_id
        self.phone_contacts = phone_contacts

    @classmethod
    def from_api(cls, update: contacts_pb2.UpdateContactsAdded) -> 'UpdateContactsAdded':
        return cls([Peer(x, PeerType.PEERTYPE_PRIVATE) for x in update.uids], update.task_id.value,
                   [UserPhoneHashContact.from_api(x) for x in update.phone_contacts])

    def __dict__(self):
        return {"peers": [x.__dict__() for x in self.peers], "task_id": self.task_id,
                "phone_contacts": [x.__dict__() for x in self.phone_contacts]}

    def __str__(self):
        return "UpdateContactsAdded({})".format(self.__dict__())


class UpdateContactsAddTaskSuspended:
    def __init__(self, task_id: str) -> None:
        self.task_id = task_id

    @classmethod
    def from_api(cls, update: contacts_pb2.UpdateContactsAddTaskSuspended) -> 'UpdateContactsAddTaskSuspended':
        return cls(update.task_id)

    def __dict__(self):
        return {"task_id": self.task_id}

    def __str__(self):
        return "UpdateContactsAddTaskSuspended({})".format(self.__dict__())


class UpdateContactsRemoved:
    def __init__(self, peers: List[Peer]) -> None:
        self.peers = peers

    @classmethod
    def from_api(cls, update: contacts_pb2.UpdateContactsRemoved) -> 'UpdateContactsRemoved':
        return cls([Peer(x, PeerType.PEERTYPE_PRIVATE) for x in update.uids])

    def __dict__(self):
        return {"peers": [x.__dict__() for x in self.peers]}

    def __str__(self):
        return "UpdateContactsRemoved({})".format(self.__dict__())