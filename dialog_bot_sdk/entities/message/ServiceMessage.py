from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.Avatar import Avatar


class ServiceExtChangedAbout:
    def __init__(self, about: str) -> None:
        self.about = about


class ServiceExtChangedAvatar:
    def __init__(self, avatar: Avatar) -> None:
        self.avatar = avatar


class ServiceExtChangedTitle:
    def __init__(self, title: str) -> None:
        self.title = title


class ServiceExtChangedTopic:
    def __init__(self, topic: str) -> None:
        self.topic = topic


class ServiceExtGroupCreated:
    def __init__(self) -> None:
        pass


class ServiceExtUserInvited:
    def __init__(self, user_uid: int) -> None:
        self.user_uid = user_uid


class ServiceExtUserJoined:
    def __init__(self) -> None:
        pass


class ServiceExtUserKicked:
    def __init__(self, user_uid: int) -> None:
        self.user_uid = user_uid


class ServiceExtUserLeft:
    def __init__(self) -> None:
        pass


class ServiceExt:
    def __init__(self, changed_about: ServiceExtChangedAbout, changed_avatar: ServiceExtChangedAvatar,
                 changed_title: ServiceExtChangedTitle, changed_topic: ServiceExtChangedTopic,
                 group_created: ServiceExtGroupCreated, user_invited: ServiceExtUserInvited,
                 user_joined: ServiceExtUserJoined, user_kicked: ServiceExtUserKicked,
                 user_left: ServiceExtUserLeft) -> None:
        self.changed_about = changed_about
        self.changed_avatar = changed_avatar
        self.changed_title = changed_title
        self.changed_topic = changed_topic
        self.group_created = group_created
        self.user_invited = user_invited
        self.user_joined = user_joined
        self.user_kicked = user_kicked
        self.user_left = user_left


class ServiceMessage:
    def __init__(self, text: str, ext: ServiceExt) -> None:
        self.text = text
        self.ext = ext

    @classmethod
    def from_api(cls, service: messaging_pb2.ServiceMessage) -> 'ServiceMessage':
        return cls(service.text, ServiceExt.from_api(service.ext))
