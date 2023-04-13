from typing import List
from dialog_api import profile_pb2, users_pb2
from google.protobuf.wrappers_pb2 import StringValue

from dialog_bot_sdk.entities.media_and_files import Avatar
from dialog_bot_sdk.entities.users import Sex, UserStatus, BotCommand
from dialog_bot_sdk.utils import async_dec
from dialog_bot_sdk.service import ManagedService


class Profile(ManagedService):
    """Class for changing bot profile.

    """
    @async_dec()
    def edit_name(self, name: str) -> None:
        """Edit bot name.

        :param name: new bot name
        :return: None
        """
        self.internal.profile.EditName(profile_pb2.RequestEditName(name=name))

    def edit_name_sync(self, name: str) -> None:
        return self.edit_name.__wrapped__(self, name)

    @async_dec()
    def edit_nickname(self, nick: str) -> None:
        """Edit bot nickname (shortname).

        :param nick: new bot nickname.
        :return: None
        """
        self.internal.profile.EditNickName(profile_pb2.RequestEditNickName(nickname=StringValue(value=nick)))

    def edit_nickname_sync(self, nick: str) -> None:
        return self.edit_nickname.__wrapped__(self, nick)

    @async_dec()
    def check_nickname(self, nick: str) -> bool:
        """Validate nickname (shortname).

        :param nick: nickname.
        :return: True or False
        """
        if not isinstance(nick, str):
            raise TypeError("nick must be str.")
        try:
            return self.internal.profile.CheckNickName(profile_pb2.RequestCheckNickName(nickname=nick)).value
        except:
            return False

    def check_nickname_sync(self, nick: str) -> bool:
        return self.check_nickname.__wrapped__(self, nick)

    @async_dec()
    def edit_about(self, about: str) -> None:
        """Edit bot about.

        :param about: new bot about.
        :return:
        """
        self.internal.profile.EditAbout(profile_pb2.RequestEditAbout(about=StringValue(value=about)))

    def edit_about_sync(self, about: str) -> None:
        return self.edit_about.__wrapped__(self, about)

    @async_dec()
    def edit_avatar(self, file: str) -> Avatar or None:
        """Edit bot avatar.

        :param file: new bot avatar (path to file).
        :return: Avatar or None.
        """
        location = self.internal.uploading.upload_file_sync(file)
        if location is None:
            return None
        return self.internal.profile.EditAvatar(profile_pb2.RequestEditAvatar(file_location=location.to_api()))

    def edit_avatar_sync(self, file: str) -> Avatar or None:
        return self.edit_avatar.__wrapped__(self, file)

    @async_dec()
    def remove_avatar(self) -> None:
        """Remove bot avatar.

        :return: None.
        """
        self.internal.profile.RemoveAvatar(profile_pb2.RequestRemoveAvatar())

    def remove_avatar_sync(self) -> None:
        return self.remove_avatar.__wrapped__(self)

    @async_dec()
    def edit_time_zone(self, tz: str) -> None:
        """Edit bot timezone.

        :param tz: new bot timezone.
        :return: None.
        """
        self.internal.profile.EditMyTimeZone(profile_pb2.RequestEditMyTimeZone(tz=tz))

    def edit_time_zone_sync(self, tz: str) -> None:
        return self.edit_time_zone.__wrapped__(self, tz)

    @async_dec()
    def edit_preferred_languages(self, preferred_languages: List[str]) -> None:
        """Edit bot preferred languages.

        :param preferred_languages: new bot preferred languages.
        :return: None.
        """
        self.internal.profile.EditMyPreferredLanguages(
            profile_pb2.RequestEditMyPreferredLanguages(preferred_languages=preferred_languages)
        )

    def edit_preferred_languages_sync(self, preferred_languages: List[str]) -> None:
        return self.edit_preferred_languages.__wrapped__(self, preferred_languages)

    @async_dec()
    def edit_sex(self, sex: Sex) -> None:
        """Edit bot sex.

        :param sex: new bot sex.
        :return: None.
        """
        self.internal.profile.EditSex(profile_pb2.RequestEditSex(sex=sex))

    def edit_sex_sync(self, sex: Sex) -> None:
        return self.edit_sex.__wrapped__(self, sex)

    @async_dec()
    def edit_custom_profile(self, custom_profile: str) -> None:
        """Edit bot custom profile.

        :param custom_profile: new bot custom profile.
        :return: None.
        """
        self.internal.profile.EditCustomProfile(profile_pb2.RequestEditCustomProfile(custom_profile=custom_profile))

    def edit_custom_profile_sync(self, custom_profile: str) -> None:
        return self.edit_custom_profile.__wrapped__(self, custom_profile)

    @async_dec()
    def edit_user_status(self, type: UserStatus, text: str) -> None:
        """Edit bot user status.

        :param type: new bot status type.
        :param text: new bot status text.
        :return: None.
        """
        self.internal.profile.ChangeUserStatus(
            profile_pb2.RequestChangeUserStatus(status=users_pb2.UserStatus(type=type, text=StringValue(value=text)))
        )

    def edit_user_status_sync(self, type: UserStatus, text: str) -> None:
        return self.edit_user_status.__wrapped__(self, type, text)

    @async_dec()
    def update_bot_commands(self, bot_commands: List[BotCommand]) -> None:
        """Edit bot user status.

        :param bot_commands: bot commands
        :return: None.
        """
        self.internal.profile.UpdateBotCommands(
            profile_pb2.RequestUpdateBotCommands(
                bot_commands=[x.to_api() for x in bot_commands]
            )
        )

    def update_bot_commands_sync(self, bot_commands: List[BotCommand]) -> None:
        return self.update_bot_commands.__wrapped__(self, bot_commands)
