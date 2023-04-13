import json
from typing import List

from dialog_api import users_pb2
from google.protobuf.wrappers_pb2 import StringValue
from dialog_bot_sdk.entities.media_and_files import Avatar
from dialog_bot_sdk.entities.miscellaneous import RecursiveTypedMap
from dialog_bot_sdk.entities.peers import PeerType, Peer
from dialog_api.users_pb2 import USERSTATUSTYPE_UNKNOWN, USERSTATUSTYPE_UNSET, USERSTATUSTYPE_AWAY, \
    USERSTATUSTYPE_DONOTDISTURB, USERSTATUSTYPE_INVISIBLE, USERSTATUSTYPE_BUSY
from dialog_api.users_pb2 import SEX_UNKNOWN, SEX_MALE, SEX_FEMALE

from dialog_bot_sdk.entities.users_restrictions import InteractionRestrictions


class UserStatusType:
    USERSTATUSTYPE_UNKNOWN = USERSTATUSTYPE_UNKNOWN
    USERSTATUSTYPE_UNSET = USERSTATUSTYPE_UNSET
    USERSTATUSTYPE_AWAY = USERSTATUSTYPE_AWAY
    USERSTATUSTYPE_DONOTDISTURB = USERSTATUSTYPE_DONOTDISTURB
    USERSTATUSTYPE_INVISIBLE = USERSTATUSTYPE_INVISIBLE
    USERSTATUSTYPE_BUSY = USERSTATUSTYPE_BUSY


class Sex:
    UNKNOWN = SEX_UNKNOWN
    MALE = SEX_MALE
    FEMALE = SEX_FEMALE


class Lifecycle:
    MISSED = 0
    ACTIVE = 1
    DELETED = 2
    BLOCKED = 3
    BLOCKED_AND_DELETED = 4


class Hint:
    user_hint_regular = 0
    user_hint_guest = 0


class UserStatus:
    def __init__(self, type: UserStatusType, text: str, clock: int) -> None:
        self.type = type
        self.text = text
        self.clock = clock

    @classmethod
    def from_api(cls, user_status: users_pb2.UserStatus) -> 'UserStatus':
        return cls(user_status.type, user_status.text.value, user_status.clock)

    def __dict__(self):
        return {"type": self.type, "text": self.text, "clock": self.clock}

    def __str__(self):
        return "UserStatus{}".format(self.__dict__())


class ContactType:
    CONTACTTYPE_UNKNOWN = users_pb2.CONTACTTYPE_UNKNOWN
    CONTACTTYPE_PHONE = users_pb2.CONTACTTYPE_PHONE
    CONTACTTYPE_EMAIL = users_pb2.CONTACTTYPE_EMAIL
    CONTACTTYPE_WEB = users_pb2.CONTACTTYPE_WEB
    CONTACTTYPE_SOCIAL = users_pb2.CONTACTTYPE_SOCIAL


class ContactRecord:
    def __init__(self, type: ContactType, type_spec: str, string_value: str, long_value: int, title: str, subtitle: str) -> None:
        self.type = type
        self.type_spec = type_spec
        self.string_value = string_value
        self.long_value = long_value
        self.title = title
        self.subtitle = subtitle

    @classmethod
    def from_api(cls, update: users_pb2.ContactRecord) -> 'ContactRecord':
        return cls(update.type, update.type_spec.value, update.string_value.value, update.long_value.value,
                   update.title.value, update.subtitle.value)

    def __dict__(self):
        return {"type": self.type, "type_spec": self.type_spec, "string_value": self.string_value,
                "long_value": self.long_value, "title": self.title, "subtitle": self.subtitle}

    def __str__(self):
        return "ContactRecord({})".format(self.__dict__())


class BotCommand:
    def __init__(self, slash_command: str, description: str, loc_key: str) -> None:
        self.slash_command = slash_command
        self.description = description
        self.loc_key = loc_key

    @classmethod
    def from_api(cls, bot_command: users_pb2.BotCommand) -> 'BotCommand':
        return cls(bot_command.slash_command, bot_command.description, bot_command.loc_key.value)

    def to_api(self) -> users_pb2.BotCommand:
        return users_pb2.BotCommand(slash_command=self.slash_command, description=self.description,
                                    loc_key=StringValue(value=self.loc_key))

    def __dict__(self):
        return {"slash_command": self.slash_command, "description": self.description, "loc_key": self.loc_key}

    def __str__(self):
        return "BotCommand({})".format(self.__dict__())


class UserData:
    def __init__(
            self,
            name: str,
            nick: str,
            sex: Sex,
            avatar: Avatar,
            is_bot: bool,
            status: Lifecycle,
            user_status: UserStatus,
            time_zone: str,
            obsolete_clock: int,
            locales: List[str],
            about: str,
            contact_info: List[ContactRecord],
            bot_commands: List[BotCommand],
            custom_profile: str,
            hint: Hint,
            was_authorized: bool,
            clock: int
    ) -> None:
        self.name = name
        self.nick = nick
        self.sex = sex
        self.avatar = avatar
        self.is_bot = is_bot
        self.status = status
        self.user_status = user_status
        self.time_zone = time_zone
        self.obsolete_clock = obsolete_clock
        self.locales = locales
        self.about = about
        self.contact_info = contact_info
        self.bot_commands = bot_commands
        self.custom_profile_json = custom_profile
        if self.custom_profile_json is None:
            self.custom_profile = {}
        else:
            try:
                self.custom_profile = json.loads(self.custom_profile_json)
            except json.decoder.JSONDecodeError:
                self.custom_profile = {}
        self.hint = hint
        self.was_authorized = was_authorized
        self.clock = clock

    @classmethod
    def from_api(cls, data: users_pb2.UserData) -> 'UserData':
        return cls(
            data.name,
            data.nick.value,
            data.sex,
            Avatar.from_api(data.avatar),
            data.is_bot.value,
            data.status,
            UserStatus.from_api(data.user_status),
            data.time_zone,
            data.obsoleteClock.clock,
            data.locales,
            data.about.value,
            [ContactRecord.from_api(x) for x in data.contact_info],
            [BotCommand.from_api(x) for x in data.bot_commands],
            data.custom_profile.value,
            data.hint,
            data.was_authorized,
            data.clock
        )

    def __dict__(self):
        return {
            "name": self.name,
            "nick": self.nick,
            "sex": self.sex,
            "avatar": self.avatar.__dict__(),
            "is_bot": self.is_bot,
            "status": self.status,
            "user_status": self.user_status.__dict__(),
            "time_zone": self.time_zone,
            "obsolete_clock": self.obsolete_clock,
            "locales": self.locales,
            "about": self.about,
            "contact_info": [x.__dict__() for x in self.contact_info],
            "bot_commands": [x.__dict__() for x in self.bot_commands],
            "custom_profile": self.custom_profile,
            "hint": self.hint,
            "was_authorized": self.was_authorized,
            "clock": self.clock,
        }

    def __str__(self):
        return "UserData{}".format(self.__dict__())


class User:
    def __init__(self, id: int, data: UserData = None) -> None:
        self.data = data
        self.peer = Peer(id, PeerType.PEERTYPE_PRIVATE)

    @classmethod
    def from_api(cls, user: users_pb2.User) -> 'User':
        return cls(user.id, UserData.from_api(user.data))

    def __dict__(self):
        return {"data": self.data.__dict__(), "peer": self.peer.__dict__()}

    def __str__(self):
        return "User({})".format(self.__dict__())


class FullUser:
    def __init__(
            self,
            id: int,
            contact_info: List[ContactRecord],
            about: str,
            preferred_languages: List[str],
            time_zone: str,
            bot_commands: List[BotCommand],
            is_blocked: bool,
            custom_profile: str,
            integration_token: str,
            status: UserStatus
    ) -> None:
        self.id = id
        self.contact_info = contact_info
        self.about = about
        self.preferred_languages = preferred_languages
        self.time_zone = time_zone
        self.bot_commands = bot_commands
        self.is_blocked = is_blocked
        self.custom_profile = custom_profile
        self.integration_token = integration_token
        self.status = status

    @classmethod
    def from_api(cls, full_user: users_pb2.FullUser) -> 'FullUser':
        return cls(
            full_user.id,
            [ContactRecord.from_api(x) for x in full_user.contact_info],
            full_user.about.value,
            [x for x in full_user.preferred_languages],
            full_user.time_zone.value,
            [BotCommand.from_api(x) for x in full_user.bot_commands],
            full_user.is_blocked.value,
            full_user.custom_profile,
            full_user.integration_token.value,
            UserStatus.from_api(full_user.status)
        )

    def __dict__(self):
        return {
            "id": self.id,
            "contact_info": [x.__dict__() for x in self.contact_info],
            "about": self.about,
            "preferred_languages": self.preferred_languages,
            "time_zone": self.time_zone,
            "bot_commands": [x.__dict__() for x in self.bot_commands],
            "is_blocked": self.is_blocked,
            "custom_profile": self.custom_profile,
            "integration_token": self.integration_token,
            "status": self.status.__dict__()
        }

    def __str__(self):
        return "FullUser({})".format(self.__dict__())


class UpdateUserAvatarChanged:
    def __init__(self, peer: Peer, avatar: Avatar) -> None:
        self.peer = peer
        self.avatar = avatar

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserAvatarChanged) -> 'UpdateUserAvatarChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), Avatar.from_api(update.avatar))

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "avatar": self.avatar.__dict__()}

    def __str__(self):
        return "UpdateUserAvatarChanged({})".format(self.__dict__())


class UpdateUserNameChanged:
    def __init__(self, peer: Peer, name: str) -> None:
        self.peer = peer
        self.name = name

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserNameChanged) -> 'UpdateUserNameChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.name)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "name": self.name}

    def __str__(self):
        return "UpdateUserNameChanged({})".format(self.__dict__())


class UpdateUserLocalNameChanged:
    def __init__(self, peer: Peer, local_name: str) -> None:
        self.peer = peer
        self.local_name = local_name

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserLocalNameChanged) -> 'UpdateUserLocalNameChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.local_name.value)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "name": self.local_name}

    def __str__(self):
        return "UpdateUserNameChanged({})".format(self.__dict__())


class UpdateUserContactsChanged:
    def __init__(self, peer: Peer, contact_records: List[ContactRecord]) -> None:
        self.peer = peer
        self.contact_records = contact_records

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserContactsChanged) -> 'UpdateUserContactsChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), [ContactRecord.from_api(x) for x in update.contact_records])

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "name": [str(x) for x in self.contact_records]}

    def __str__(self):
        return "UpdateUserContactsChanged({})".format(self.__dict__())


class UpdateUserNickChanged:
    def __init__(self, peer: Peer, nickname: str) -> None:
        self.peer = peer
        self.nickname = nickname

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserNickChanged) -> 'UpdateUserNickChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.nickname.value)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "nickname": self.nickname}

    def __str__(self):
        return "UpdateUserNickChanged({})".format(self.__dict__())


class UpdateUserAboutChanged:
    def __init__(self, peer: Peer, about: str) -> None:
        self.peer = peer
        self.about = about

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserAboutChanged) -> 'UpdateUserAboutChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.about.value)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "about": self.about}

    def __str__(self):
        return "UpdateUserAboutChanged({})".format(self.__dict__())


class UpdateUserPreferredLanguagesChanged:
    def __init__(self, peer: Peer, preferred_languages: List[str]) -> None:
        self.peer = peer
        self.preferred_languages = preferred_languages

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserPreferredLanguagesChanged) -> 'UpdateUserPreferredLanguagesChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), [x for x in update.preferred_languages])

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "preferred_languages": self.preferred_languages}

    def __str__(self):
        return "UpdateUserPreferredLanguagesChanged({})".format(self.__dict__())


class UpdateUserTimeZoneChanged:
    def __init__(self, peer: Peer, time_zone: str) -> None:
        self.peer = peer
        self.time_zone = time_zone

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserTimeZoneChanged) -> 'UpdateUserTimeZoneChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.time_zone.value)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "time_zone": self.time_zone}

    def __str__(self):
        return "UpdateUserPreferredLanguagesChanged({})".format(self.__dict__())


class UpdateUserBotCommandsChanged:
    def __init__(self, peer: Peer, commands: List[BotCommand]) -> None:
        self.peer = peer
        self.commands = commands

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserBotCommandsChanged) -> 'UpdateUserBotCommandsChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), [BotCommand.from_api(x) for x in update.commands])

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "commands": [x.__dict__() for x in self.commands]}

    def __str__(self):
        return "UpdateUserBotCommandsChanged({})".format(self.__dict__())


class UpdateUserSexChanged:
    def __init__(self, peer: Peer, sex: Sex) -> None:
        self.peer = peer
        self.sex = sex

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserSexChanged) -> 'UpdateUserSexChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), update.sex)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "sex": self.sex}

    def __str__(self):
        return "UpdateUserSexChanged({})".format(self.__dict__())


class UpdateUserCustomProfileChanged:
    def __init__(self, peer: Peer, custom_profile: dict) -> None:
        self.peer = peer
        self.custom_profile = custom_profile

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserCustomProfileChanged) -> 'UpdateUserCustomProfileChanged':
        return cls(
            Peer(update.uid, PeerType.PEERTYPE_PRIVATE),
            json.loads(update.custom_profile) if update.custom_profile else {}
        )

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "custom_profile": self.custom_profile}

    def __str__(self):
        return "UpdateUserCustomProfileChanged({})".format(self.__dict__())


class UpdateUserStatusChanged:
    def __init__(self, peer: Peer, status: UserStatus) -> None:
        self.peer = peer
        self.status = status

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserStatusChanged) -> 'UpdateUserStatusChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), UserStatus.from_api(update.status))

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "status": self.status.__dict__()}

    def __str__(self):
        return "UpdateUserStatusChanged({})".format(self.__dict__())


class UpdateUser:
    def __init__(self, peer: Peer, data: UserData) -> None:
        self.peer = peer
        self.data = data

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUser) -> 'UpdateUser':
        user = User.from_api(update)
        return cls(user.peer, user.data)

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "data": self.data.__dict__()}

    def __str__(self):
        return "UpdateUser({})".format(self.__dict__())


class UpdateUserRestrictionsChanged:
    def __init__(self, peer: Peer, restrictions: InteractionRestrictions) -> None:
        self.peer = peer
        self.restrictions = restrictions

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserRestrictionsChanged) -> 'UpdateUserRestrictionsChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), InteractionRestrictions.from_api(update.restrictions))

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "restrictions": self.restrictions.__dict__()}

    def __str__(self):
        return "UpdateUserRestrictionsChanged({})".format(self.__dict__())


class UpdateUserExtChanged:
    def __init__(self, peer: Peer, ext: RecursiveTypedMap) -> None:
        self.peer = peer
        self.ext = ext

    @classmethod
    def from_api(cls, update: users_pb2.UpdateUserExtChanged) -> 'UpdateUserExtChanged':
        return cls(Peer(update.uid, PeerType.PEERTYPE_PRIVATE), RecursiveTypedMap.from_api(update.ext))

    def __dict__(self):
        return {"peer": self.peer.__dict__(), "ext": self.ext.__dict__()}

    def __str__(self):
        return "UpdateUserExtChanged({})".format(self.__dict__())
