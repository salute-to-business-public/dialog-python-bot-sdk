from dialog_api import users_restrictions_pb2


class RestrictionReason:
    RESTRICTION_REASON_UNKNOWN = 0
    RESTRICTION_REASON_IS_DELETED = 1
    RESTRICTION_REASON_IS_VIP = 2
    RESTRICTION_REASON_IS_BOT = 3


class RestrictShareContact:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictShareContact':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictShareContact({})".format(self.__dict__())


class RestrictAddContact:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictAddContact':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictAddContact({})".format(self.__dict__())


class RestrictMsgUser:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictMsgUser':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictMsgUser({})".format(self.__dict__())


class RestrictCallExtUser:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictCallExtUser':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictCallExtUser({})".format(self.__dict__())


class RestrictAudioCallUser:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictAudioCallUser':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictAudioCallUser({})".format(self.__dict__())


class RestrictVideoCallUser:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictVideoCallUser':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictVideoCallUser({})".format(self.__dict__())


class RestrictSendInviteMailUser:
    def __init__(self, reason: RestrictionReason) -> None:
        self.reason = reason

    @classmethod
    def from_api(cls, restrict) -> 'RestrictSendInviteMailUser':
        return cls(restrict.reason)

    def __dict__(self):
        return {"reason": self.reason}

    def __str__(self):
        return "RestrictSendInviteMailUser({})".format(self.__dict__())


class InteractionRestrictions:
    def __init__(
            self,
            restrict_share_contact: RestrictShareContact,
            restrict_add_contact: RestrictAddContact,
            restrict_msg_user: RestrictMsgUser,
            restrict_call_ext_user: RestrictCallExtUser,
            restrict_audio_call_user: RestrictAudioCallUser,
            restrict_video_call_user: RestrictVideoCallUser,
            restrict_send_invite_mail_user: RestrictSendInviteMailUser
    ) -> None:
        self.restrict_share_contact = restrict_share_contact
        self.restrict_add_contact = restrict_add_contact
        self.restrict_msg_user = restrict_msg_user
        self.restrict_call_ext_user = restrict_call_ext_user
        self.restrict_audio_call_user = restrict_audio_call_user
        self.restrict_video_call_user = restrict_video_call_user
        self.restrict_send_invite_mail_user = restrict_send_invite_mail_user

    @classmethod
    def from_api(cls, restrict: users_restrictions_pb2.InteractionRestrictions) -> 'InteractionRestrictions':
        return cls(
            RestrictShareContact.from_api(restrict.restrictShareContact),
            RestrictAddContact.from_api(restrict.restrictAddContact),
            RestrictMsgUser.from_api(restrict.restrictMsgUser),
            RestrictCallExtUser.from_api(restrict.restrictCallExtUser),
            RestrictAudioCallUser.from_api(restrict.restrictAudioCallUser),
            RestrictVideoCallUser.from_api(restrict.restrictVideoCallUser),
            RestrictSendInviteMailUser.from_api(restrict.restrictSendInviteMailUser)
        )

    def __dict__(self):
        return {
            "restrict_share_contact": self.restrict_share_contact.__dict__(),
            "restrict_add_contact": self.restrict_add_contact.__dict__(),
            "restrict_msg_user": self.restrict_msg_user.__dict__(),
            "restrict_call_ext_user": self.restrict_call_ext_user.__dict__(),
            "restrict_audio_call_user": self.restrict_audio_call_user.__dict__(),
            "restrict_video_call_user": self.restrict_video_call_user.__dict__(),
            "restrict_send_invite_mail_user": self.restrict_send_invite_mail_user.__dict__(),

        }

    def __str__(self):
        return "InteractionRestrictions({})".format(self.__dict__())
