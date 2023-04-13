from dialog_api import spaces_pb2

from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.media_and_files import Avatar
from dialog_bot_sdk.entities.peers import Peer, PeerType


class SpaceType:
    GENERAL = "general"
    PUBLIC = "public"
    PRIVATE = "private"


space_type_mapper = {
    "general": SpaceType.GENERAL,
    "public": SpaceType.PUBLIC,
    "private": SpaceType.PRIVATE,
}


class General:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_api(cls, update: spaces_pb2.Space.General) -> 'General':
        return cls()

    def __dict__(self):
        return {}

    def __str__(self):
        return "General({})".format(self.__dict__())


class Public:
    def __init__(self, owner_user_id: int, shortname: str) -> None:
        self.owner_user_id = owner_user_id
        self.shortname = shortname

    @classmethod
    def from_api(cls, update: spaces_pb2.Space.Public) -> 'Public':
        return cls(update.owner_user_id, update.shortname)

    def __dict__(self):
        return {"owner_user_id": self.owner_user_id, "shortname": self.shortname}

    def __str__(self):
        return "Public({})".format(self.__dict__())


class Private:
    def __init__(self, owner_user_id: int) -> None:
        self.owner_user_id = owner_user_id

    @classmethod
    def from_api(cls, update: spaces_pb2.Space.Private) -> 'Private':
        return cls(update.owner_user_id)

    def __dict__(self):
        return {"owner_user_id": self.owner_user_id}

    def __str__(self):
        return "Private({})".format(self.__dict__())


class SpaceMember:
    def __init__(
            self,
            space_id: UUID,
            peer: Peer,
            invited_at: int,
            joined_at: int,
            deleted_at: int,
            clock: int,
    ) -> None:
        self.space_id = space_id
        self.peer = peer
        self.invited_at = invited_at
        self.joined_at = joined_at
        self.deleted_at = deleted_at
        self.clock = clock

    @classmethod
    def from_api(cls, update: spaces_pb2.SpaceMember) -> 'SpaceMember':
        return cls(
            UUID.from_api(update.space_id),
            Peer(update.user_id, PeerType.PEERTYPE_PRIVATE),
            update.invited_at.seconds,
            update.joined_at.seconds,
            update.deleted_at.seconds,
            update.clock.clock,
        )

    def __dict__(self):
        return {
            "space_id": self.space_id.__dict__(),
            "peer": self.peer.__dict__(),
            "invited_at": self.invited_at,
            "joined_at": self.joined_at,
            "deleted_at": self.deleted_at,
            "clock": self.clock
        }

    def __str__(self):
        return "SpaceMember({})".format(self.__dict__())


class Space:
    def __init__(
            self,
            id: UUID,
            created_at: int,
            space_type: SpaceType,
            general: General,
            public: Public,
            private: Private,
            title: str,
            about: str,
            avatar: Avatar,
            deleted_at: int,
            clock: int
    ) -> None:
        self.id = id
        self.created_at = created_at
        self.space_type = space_type
        self.general = general
        self.public = public
        self.private = private
        self.title = title
        self.about = about
        self.avatar = avatar
        self.deleted_at = deleted_at
        self.clock = clock

    @classmethod
    def from_api(cls, update: spaces_pb2.Space) -> 'Space':
        return cls(
            UUID.from_api(update.id),
            update.created_at.seconds,
            space_type_mapper.get(update.WhichOneof('space_type')),
            General.from_api(update.general),
            Public.from_api(update.public),
            Private.from_api(update.private),
            update.title,
            update.about.value,
            Avatar.from_api(update.avatar),
            update.deleted_at.seconds,
            update.clock.clock,
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            "id": self.id,
            "created_at": self.created_at,
            self.space_type: oneof.__dict__() if oneof is not None else oneof,
            "title": self.title,
            "about": self.about,
            "avatar": self.avatar.__dict__(),
            "deleted_at": self.deleted_at,
            "clock": self.clock
        }

    def oneof_type(self):
        if self.space_type == SpaceType.GENERAL:
            return self.general
        if self.space_type == SpaceType.PUBLIC:
            return self.public
        if self.space_type == SpaceType.PRIVATE:
            return self.private

    def __str__(self):
        return "Space({})".format(self.__dict__())


# updates
class UpdateSpaceModified:
    def __init__(self, space: Space) -> None:
        self.space = space

    @classmethod
    def from_api(cls, update: spaces_pb2.UpdateSpaceModified) -> 'UpdateSpaceModified':
        return cls(Space.from_api(update.space))

    def __dict__(self):
        return {"space": self.space.__dict__()}

    def __str__(self):
        return "UpdateSpaceModified({})".format(self.__dict__())


class UpdateSpaceMemberModified:
    def __init__(self, member: SpaceMember) -> None:
        self.member = member

    @classmethod
    def from_api(cls, update: spaces_pb2.UpdateSpaceMemberModified) -> 'UpdateSpaceMemberModified':
        return cls(SpaceMember.from_api(update.member))

    def __dict__(self):
        return {"member": self.member.__dict__()}

    def __str__(self):
        return "UpdateSpaceMemberModified({})".format(self.__dict__())
