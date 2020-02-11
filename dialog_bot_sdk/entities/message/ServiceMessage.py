from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.Avatar import Avatar


class ServiceExt:
    def __init__(self, changed_about: str, changed_avatar: Avatar, changed_short_name: str, changed_title: str,
                 changed_topic: str, user_invited: int, user_kicked: int) -> None:
        self.changed_about = changed_about
        self.changed_avatar = changed_avatar
        self.changed_short_name = changed_short_name
        self.changed_title = changed_title
        self.changed_topic = changed_topic
        self.user_invited = user_invited
        self.user_kicked = user_kicked

    @classmethod
    def from_api(cls, service_ext: messaging_pb2.ServiceEx) -> 'ServiceExt':
        return cls(service_ext.changedAbout.about.value, Avatar.from_api(service_ext.changedAvatar.avatar),
                   service_ext.changedShortname.shortname, service_ext.changedTitle.title,
                   service_ext.changedTopic.topic.value, service_ext.userInvited.invited_uid,
                   service_ext.userKicked.kicked_uid)

    def __dict__(self):
        return {"changed_about": self.changed_about, "changed_avatar": self.changed_avatar.__dict__(),
                "changed_short_name": self.changed_short_name, "changed_title": self.changed_title,
                "changed_topic": self.changed_topic, "user_invited": self.user_invited, "user_kicked": self.user_kicked}

    def __str__(self):
        return "{}".format(self.__dict__())


class ServiceMessage:
    def __init__(self, text: str, ext: ServiceExt) -> None:
        self.text = text
        self.ext = ext

    @classmethod
    def from_api(cls, service: messaging_pb2.ServiceMessage) -> 'ServiceMessage':
        return cls(service.text, ServiceExt.from_api(service.ext))

    def __dict__(self):
        return {"text": self.text, "ext": self.ext.__dict__()}

    def __str__(self):
        return "{}".format(self.__dict__())
