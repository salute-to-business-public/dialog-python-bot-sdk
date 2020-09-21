from typing import List

from dialog_api import profile_pb2, users_pb2
from google.protobuf.wrappers_pb2 import StringValue

from dialog_bot_sdk.entities.Sex import Sex
from dialog_bot_sdk.entities.UserStatus import UserStatus

from dialog_bot_sdk.entities.Avatar import Avatar

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

    @async_dec()
    def edit_nickname(self, nick: str) -> None:
        """Edit bot nickname (shortname).

        :param nick: new bot nickname.
        :return: None
        """
        self.internal.profile.EditNickName(profile_pb2.RequestEditNickName(nickname=StringValue(value=nick)))

    @async_dec()
    def check_nickname(self, nick: str) -> bool:
        """Validate nickname (shortname).

        :param nick: nickname.
        :return: True or False
        """
        try:
            return self.internal.profile.CheckNickName(profile_pb2.RequestCheckNickName(nickname=nick)).value
        except:
            return False

    @async_dec()
    def edit_about(self, about: str) -> None:
        """Edit bot about.

        :param about: new bot about.
        :return:
        """
        self.internal.profile.EditAbout(profile_pb2.RequestEditAbout(about=StringValue(value=about)))

    @async_dec()
    def edit_avatar(self, file: str) -> Avatar or None:
        """Edit bot avatar.

        :param file: new bot avatar (path to file).
        :return: Avatar or None.
        """
        location = self.internal.uploading.upload_file(file).wait()
        if location is None:
            return None
        return self.internal.profile.EditAvatar(profile_pb2.RequestEditAvatar(file_location=location.to_api()))

    @async_dec()
    def remove_avatar(self) -> None:
        """Remove bot avatar.

        :return: None.
        """
        self.internal.profile.RemoveAvatar(profile_pb2.RequestRemoveAvatar())

    @async_dec()
    def edit_time_zone(self, tz: str) -> None:
        """Edit bot timezone.

        :param tz: new bot timezone.
        :return: None.
        """
        self.internal.profile.EditMyTimeZone(profile_pb2.RequestEditMyTimeZone(tz=tz))

    @async_dec()
    def edit_preferred_languages(self, preferred_languages: List[str]) -> None:
        """Edit bot preferred languages.

        :param preferred_languages: new bot preferred languages.
        :return: None.
        """
        self.internal.profile.EditMyPreferredLanguages(
            profile_pb2.RequestEditMyPreferredLanguages(preferred_languages=preferred_languages)
        )

    @async_dec()
    def edit_sex(self, sex: Sex) -> None:
        """Edit bot sex.

        :param sex: new bot sex.
        :return: None.
        """
        self.internal.profile.EditSex(profile_pb2.RequestEditSex(sex=sex))

    @async_dec()
    def edit_custom_profile(self, custom_profile: str) -> None:
        """Edit bot sex.

        :param custom_profile: new bot custom profile.
        :return: None.
        """
        self.internal.profile.EditCustomProfile(profile_pb2.RequestEditCustomProfile(custom_profile=custom_profile))

    @async_dec()
    def edit_user_status(self, type: UserStatus, text: str) -> None:
        """Edit bot sex.

        :param type: new bot status type.
        :param text: new bot status text.
        :return: None.
        """
        self.internal.profile.ChangeUserStatus(
            profile_pb2.RequestChangeUserStatus(status=users_pb2.UserStatus(type=type, text=StringValue(value=text)))
        )
