import json
from typing import List
from google.protobuf.wrappers_pb2 import StringValue
from dialog_api import messaging_pb2
from dialog_bot_sdk.entities.definitions import UUID
from dialog_bot_sdk.entities.media_and_files import Avatar, AudioLocation, ImageLocation, Color, FastThumb
from dialog_bot_sdk.entities.miscellaneous import Any
from dialog_bot_sdk.entities.peers import PeerType, Peer
from dialog_api.messaging_pb2 import INTERACTIVEMEDIASTYLE_UNKNOWN, INTERACTIVEMEDIASTYLE_DEFAULT, \
    INTERACTIVEMEDIASTYLE_PRIMARY, INTERACTIVEMEDIASTYLE_DANGER, LISTLOADMODE_UNKNOWN, LISTLOADMODE_FORWARD,\
    LISTLOADMODE_BACKWARD, LISTLOADMODE_BOTH


class ListLoadMode:
    LISTLOADMODE_UNKNOWN = LISTLOADMODE_UNKNOWN
    LISTLOADMODE_FORWARD = LISTLOADMODE_FORWARD
    LISTLOADMODE_BACKWARD = LISTLOADMODE_BACKWARD
    LISTLOADMODE_BOTH = LISTLOADMODE_BOTH


# interactive media
class InteractiveMediaStyle:
    INTERACTIVEMEDIASTYLE_UNKNOWN = INTERACTIVEMEDIASTYLE_UNKNOWN
    INTERACTIVEMEDIASTYLE_DEFAULT = INTERACTIVEMEDIASTYLE_DEFAULT
    INTERACTIVEMEDIASTYLE_PRIMARY = INTERACTIVEMEDIASTYLE_PRIMARY
    INTERACTIVEMEDIASTYLE_DANGER = INTERACTIVEMEDIASTYLE_DANGER


class DocumentCheckStatus:
    DOCUMENT_CHECK_STATUS_UNKNOWN = messaging_pb2.DOCUMENT_CHECK_STATUS_UNKNOWN
    DOCUMENT_CHECK_STATUS_CHECKING = messaging_pb2.DOCUMENT_CHECK_STATUS_CHECKING
    DOCUMENT_CHECK_STATUS_PASSED = messaging_pb2.DOCUMENT_CHECK_STATUS_PASSED
    DOCUMENT_CHECK_STATUS_BLOCKED = messaging_pb2.DOCUMENT_CHECK_STATUS_BLOCKED


class MessageState:
    MESSAGESTATE_UNKNOWN = messaging_pb2.MESSAGESTATE_UNKNOWN
    MESSAGESTATE_SENT = messaging_pb2.MESSAGESTATE_SENT
    MESSAGESTATE_RECEIVED = messaging_pb2.MESSAGESTATE_RECEIVED
    MESSAGESTATE_READ = messaging_pb2.MESSAGESTATE_READ


class InteractiveMediaWidgetType:
    INTERACTIVE_MEDIA_BUTTON = "interactive_media_button"
    INTERACTIVE_MEDIA_SELECT = "interactive_media_select"
    INTERACTIVE_MEDIA_LINK = "interactive_media_lick"


interactive_media_widget_type_mapper = {
    "interactiveMediaButton": InteractiveMediaWidgetType.INTERACTIVE_MEDIA_BUTTON,
    "interactiveMediaSelect": InteractiveMediaWidgetType.INTERACTIVE_MEDIA_SELECT,
    "interactiveMediaLink": InteractiveMediaWidgetType.INTERACTIVE_MEDIA_LINK,
}


class DocumentExType:
    DOCUMENT_EX_PHOTO = "document_ex_photo"
    DOCUMENT_EX_VIDEO = "document_ex_video"
    DOCUMENT_EX_VOICE = "document_ex_voice"


document_ex_type_mapper = {
    "photo": DocumentExType.DOCUMENT_EX_PHOTO,
    "video": DocumentExType.DOCUMENT_EX_VIDEO,
    "voice": DocumentExType.DOCUMENT_EX_VOICE,
}


class ServiceExType:
    USER_INVITED = "user_invited"
    USER_JOINED = "user_joined"
    USER_KICKED = "user_kicked"
    USER_LEFT = "user_left"
    GROUP_CREATED = "group_created"
    CHANGED_SHORTNAME = "changed_shortname"
    CHANGED_TITLE = "changed_title"
    CHANGED_TOPIC = "changed_topic"
    CHANGED_ABOUT = "changed_about"
    CHANGED_AVATAR = "changed_avatar"
    CONTACT_REGISTERED = "contact_registered"
    PHONE_MISSED = "phone_missed"
    PHONE_CALL = "phone_call"
    PHONE_REJECTED = "phone_rejected"
    CHAT_ARCHIVED = "chat_archived"
    CHAT_RESTORED = "chat_restored"


service_ex_type_mapper = {
    "userInvited": ServiceExType.USER_INVITED,
    "userJoined": ServiceExType.USER_JOINED,
    "userKicked": ServiceExType.USER_KICKED,
    "userLeft": ServiceExType.USER_LEFT,
    "groupCreated": ServiceExType.GROUP_CREATED,
    "changedShortname": ServiceExType.CHANGED_SHORTNAME,
    "changedTitle": ServiceExType.CHANGED_TITLE,
    "changedTopic": ServiceExType.CHANGED_TOPIC,
    "changedAbout": ServiceExType.CHANGED_ABOUT,
    "changedAvatar": ServiceExType.CHANGED_AVATAR,
    "contactRegistered": ServiceExType.CONTACT_REGISTERED,
    "phoneMissed": ServiceExType.PHONE_MISSED,
    "phoneCall": ServiceExType.PHONE_CALL,
    "phoneRejected": ServiceExType.PHONE_REJECTED,
    "chatArchived": ServiceExType.CHAT_ARCHIVED,
    "chatRestored": ServiceExType.CHAT_RESTORED,
}


class TextExType:
    TEXT_EX_MARKDOWN = "text_ex_markdown"
    TEXT_MODERN_MESSAGE = "text_modern_message"
    TEXT_COMMAND = "text_command"


text_ex_type_mapper = {
    "textExMarkdown": TextExType.TEXT_EX_MARKDOWN,
    "textModernMessage": TextExType.TEXT_MODERN_MESSAGE,
    "textCommand": TextExType.TEXT_COMMAND,
}


class MessageContentType:
    TEXT_MESSAGE = "text_message"
    SERVICE_MESSAGE = "service_message"
    DOCUMENT_MESSAGE = "document_message"
    JSON_MESSAGE = "json_message"
    UNSUPPORTED_MESSAGE = "unsupported_message"
    STICKER_MESSAGE = "sticker_message"
    BINARY_MESSAGE = "binary_message"
    EMPTY_MESSAGE = "empty_message"
    DELETED_MESSAGE = "deleted_message"
    PACKAGE_MESSAGE = "package_message"


message_content_type_mapper = {
    "textMessage": MessageContentType.TEXT_MESSAGE,
    "serviceMessage": MessageContentType.SERVICE_MESSAGE,
    "documentMessage": MessageContentType.DOCUMENT_MESSAGE,
    "jsonMessage": MessageContentType.JSON_MESSAGE,
    "unsupportedMessage": MessageContentType.UNSUPPORTED_MESSAGE,
    "stickerMessage": MessageContentType.STICKER_MESSAGE,
    "binaryMessage": MessageContentType.BINARY_MESSAGE,
    "emptyMessage": MessageContentType.EMPTY_MESSAGE,
    "deletedMessage": MessageContentType.DELETED_MESSAGE,
    "packageMessage": MessageContentType.PACKAGE_MESSAGE,
}


class CommandHandler:
    def __init__(self, function: callable, command: str, peer_type: PeerType = None, ignored_sleep: bool = False) -> None:
        self.function = function
        self.command = command
        self.peer_type = peer_type
        self.ignored_sleep = ignored_sleep


class EventHandler:
    def __init__(self, function: callable, id: str = None, value: str = None, ignored_sleep: bool = False) -> None:
        self.function = function
        self.id = id
        self.value = value
        self.ignored_sleep = ignored_sleep
        if value is None and id is None:
            raise AttributeError("id or value must be not None.")


class MessageHandler:
    def __init__(self, function: callable, message_type: MessageContentType,
                 ext_type: ServiceExType or DocumentExType or TextExType = None,
                 peer_type: PeerType = None, ignored_sleep: bool = False) -> None:
        self.function = function
        self.message_type = message_type
        self.ext_type = ext_type
        self.peer_type = peer_type
        self.ignored_sleep = ignored_sleep
        if isinstance(ext_type, ServiceExType) and message_type != MessageContentType.SERVICE_MESSAGE:
            raise AttributeError("ServiceExType used only for MessageContentType.SERVICE_MESSAGE.")
        if isinstance(ext_type, DocumentExType) and message_type != MessageContentType.DOCUMENT_MESSAGE:
            raise AttributeError("DocumentExType used only for MessageContentType.DOCUMENT_MESSAGE.")


class InteractiveMediaLink:
    def __init__(self, url: str, label: str) -> None:
        self.url = url
        self.label = label

    def to_api(self) -> messaging_pb2.InteractiveMediaLink:
        return messaging_pb2.InteractiveMediaLink(value=self.url,
                                                  label=StringValue(value=self.label))

    @classmethod
    def from_api(cls, link: messaging_pb2.InteractiveMediaLink) -> 'InteractiveMediaLink':
        return cls(link.url, link.label.value)

    def __dict__(self):
        return {"url": self.url, "label": self.label}

    def __str__(self):
        return "InteractiveMediaLink({})".format(self.__dict__())


class InteractiveMediaButton:
    def __init__(self, value: str, label: str) -> None:
        self.value = value
        self.label = label

    def to_api(self) -> messaging_pb2.InteractiveMediaButton:
        return messaging_pb2.InteractiveMediaButton(value=StringValue(value=self.value),
                                                    label=StringValue(value=self.label))

    @classmethod
    def from_api(cls, button: messaging_pb2.InteractiveMediaButton) -> 'InteractiveMediaButton':
        return cls(button.value, button.label.value)

    def __dict__(self):
        return {"value": self.value, "label": self.label}

    def __str__(self):
        return "InteractiveMediaButton({})".format(self.__dict__())


class InteractiveMediaSelectOption:
    def __init__(self, value: str, label: str) -> None:
        self.value = value
        self.label = label

    def to_api(self) -> messaging_pb2.InteractiveMediaSelectOption:
        return messaging_pb2.InteractiveMediaSelectOption(value=StringValue(value=self.value),
                                                          label=StringValue(value=self.label))

    @classmethod
    def from_api(cls, option: messaging_pb2.InteractiveMediaSelectOption) -> 'InteractiveMediaSelectOption':
        return cls(option.value, option.label)

    def __dict__(self):
        return {"value": self.value, "label": self.label}

    def __str__(self):
        return "InteractiveMediaSelectOption({})".format(self.__dict__())


class InteractiveMediaSelect:
    def __init__(self, options: List[InteractiveMediaSelectOption], label: str, default_value: str):
        self.options = options
        self.label = label
        self.default_value = default_value

    def to_api(self) -> messaging_pb2.InteractiveMediaSelect:
        return messaging_pb2.InteractiveMediaSelect(options=[x.to_api() for x in self.options],
                                                    default_value=StringValue(value=self.default_value),
                                                    label=StringValue(value=self.label))

    @classmethod
    def from_api(cls, select: messaging_pb2.InteractiveMediaSelect) -> 'InteractiveMediaSelect':
        return cls([InteractiveMediaSelectOption.from_api(x) for x in select.options], select.label.value,
                   select.default_value.value)

    def __dict__(self):
        return {"options": [x.__dict__() for x in self.options], "label": self.label,
                "default_value": self.default_value}

    def __str__(self):
        return "InteractiveMediaSelect({})".format(self.__dict__())


class InteractiveMediaWidget:
    def __init__(self,
                 type: InteractiveMediaWidgetType,
                 interactive_media_button: InteractiveMediaButton,
                 interactive_media_select: InteractiveMediaSelect,
                 interactive_media_link: InteractiveMediaLink,

                 ) -> None:
        self.type = type
        self.interactive_media_button = interactive_media_button
        self.interactive_media_select = interactive_media_select
        self.interactive_media_link = interactive_media_link

    def to_api(self) -> messaging_pb2.InteractiveMediaWidget:
        return messaging_pb2.InteractiveMediaWidget(
            interactiveMediaButton=self.interactive_media_button.to_api(),
            interactiveMediaSelect=self.interactive_media_select.to_api(),
            interactiveMediaLink=self.interactive_media_link.to_api()
        )

    @classmethod
    def from_api(cls, widget: messaging_pb2.InteractiveMediaWidget) -> 'InteractiveMediaWidget':
        return cls(
            interactive_media_widget_type_mapper.get(widget.WhichOneof('body')),
            InteractiveMediaButton.from_api(widget.interactiveMediaButton),
            InteractiveMediaSelect.from_api(widget.interactiveMediaSelect),
            InteractiveMediaLink.from_api(widget.interactiveMediaLink)
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == InteractiveMediaWidgetType.INTERACTIVE_MEDIA_BUTTON:
            return self.interactive_media_button
        if self.type == InteractiveMediaWidgetType.INTERACTIVE_MEDIA_SELECT:
            return self.interactive_media_select
        if self.type == InteractiveMediaWidgetType.INTERACTIVE_MEDIA_LINK:
            return self.interactive_media_link

    def __str__(self):
        return "InteractiveMediaWidget({})".format(self.__dict__())


class InteractiveMediaConfirm:
    def __init__(self, text: str, title: str, ok: str, dismiss: str):
        self.text = text
        self.title = title
        self.ok = ok
        self.dismiss = dismiss

    def to_api(self) -> messaging_pb2.InteractiveMediaConfirm:
        return messaging_pb2.InteractiveMediaConfirm(text=StringValue(value=self.text),
                                                     title=StringValue(value=self.title),
                                                     ok=StringValue(value=self.ok),
                                                     dismiss=StringValue(value=self.dismiss))

    @classmethod
    def from_api(cls, confirm: messaging_pb2.InteractiveMediaConfirm) -> 'InteractiveMediaConfirm':
        return cls(confirm.text.value, confirm.title.value, confirm.ok.value, confirm.dismiss.value)

    def __dict__(self):
        return {"text": self.text, "title": self.title, "ok": self.ok, "dismiss": self.dismiss}

    def __str__(self):
        return "InteractiveMediaConfirm({})".format(self.__dict__())


class InteractiveMedia:
    def __init__(self, id: str, widget: InteractiveMediaWidget, style: InteractiveMediaStyle,
                 confirm: InteractiveMediaConfirm) -> None:
        self.id = id
        self.widget = widget
        self.style = style
        self.confirm = confirm

    def to_api(self) -> messaging_pb2.InteractiveMedia:
        return messaging_pb2.InteractiveMedia(id=self.id, widget=self.widget,
                                              style=self.style,
                                              confirm=self.confirm.to_api())

    @classmethod
    def from_api(cls, media: messaging_pb2.InteractiveMedia) -> 'InteractiveMedia':
        return cls(media.id, InteractiveMediaWidget.from_api(media.widget),
                   media.style, InteractiveMediaConfirm.from_api(media.confirm))

    def __dict__(self):
        return {"id": self.id, "widget": self.widget.__dict__(), "style": self.style, "confirm": self.confirm.__dict__()}

    def __str__(self):
        return "InteractiveMedia({})".format(self.__dict__())


class InteractiveMediaTranslation:
    def __init__(self, id: str, value: str):
        self.id = id
        self.value = value

    def to_api(self) -> messaging_pb2.InteractiveMediaTranslation:
        return messaging_pb2.InteractiveMediaTranslation(id=self.id, value=self.value)

    @classmethod
    def from_api(cls, translation: messaging_pb2.InteractiveMediaTranslation) -> 'InteractiveMediaTranslation':
        return cls(translation.id, translation.value)

    def __dict__(self):
        return {"id": self.id, "value": self.value}

    def __str__(self):
        return "InteractiveMediaTranslation({})".format(self.__dict__())


class InteractiveMediaTranslationGroup:
    def __init__(self, language: str, messages: List[InteractiveMediaTranslation]):
        self.language = language
        self.messages = messages

    def to_api(self) -> messaging_pb2.InteractiveMediaTranslationGroup:
        return messaging_pb2.InteractiveMediaTranslationGroup(language=self.language,
                                                              messages=[x.to_api() for x in self.messages])

    @classmethod
    def from_api(cls, translation: messaging_pb2.InteractiveMediaTranslationGroup) -> 'InteractiveMediaTranslationGroup':
        return cls(translation.language, [InteractiveMediaTranslation.from_api(x) for x in translation.messages])

    def __dict__(self):
        return {"language": self.language, "messages": [x.__dict__() for x in self.messages]}

    def __str__(self):
        return "InteractiveMediaTranslationGroup({})".format(self.__dict__())


class InteractiveMediaGroup:
    def __init__(self, actions: List[InteractiveMedia], title: str, description: str,
                 translations: List[InteractiveMediaTranslationGroup]) -> None:
        self.actions = actions
        self.title = title
        self.description = description
        self.translations = translations

    def to_api(self) -> messaging_pb2.InteractiveMediaGroup:
        return messaging_pb2.InteractiveMediaGroup(actions=[x.to_api() for x in self.actions], title=self.title,
                                                   description=self.description,
                                                   translations=[x.to_api() for x in self.translations])

    @classmethod
    def from_api(cls, media_group: messaging_pb2.InteractiveMediaGroup) -> 'InteractiveMediaGroup':
        return cls([InteractiveMedia.from_api(x) for x in media_group.actions], media_group.title,
                   media_group.description,
                   [InteractiveMediaTranslationGroup.from_api(x) for x in media_group.translations])

    def __dict__(self):
        return {"actions": [x.__dict__() for x in self.actions], "title": self.title, "description": self.description,
                "translations": [x.__dict__() for x in self.translations]}

    def __str__(self):
        return "InteractiveMediaGroup({})".format(self.__dict__())


# simple classes
class Mention:
    def __init__(self, all: bool, peer: Peer) -> None:
        self.all = all
        self.peer = peer

    @classmethod
    def from_api(cls, mention: messaging_pb2.Mention) -> 'Mention':
        return cls(mention.all, Peer.from_api(mention.peer))

    def __dict__(self):
        return {"all": self.all, "peer": self.peer.__dict__()}

    def __str__(self):
        return "Mention({})".format(self.__dict__())


class AudioMedia:
    def __init__(self, audio: AudioLocation) -> None:
        self.audio = audio

    def to_api(self) -> messaging_pb2.AudioMedia:
        return messaging_pb2.AudioMedia(audio=self.audio.to_api())

    @classmethod
    def from_api(cls, audio: messaging_pb2.AudioMedia) -> 'AudioMedia':
        return cls(AudioLocation.from_api(audio.audio))

    def __dict__(self):
        return {"audio": self.audio.__dict__()}

    def __str__(self):
        return "AudioMedia({})".format(self.__dict__())


class ImageMedia:
    def __init__(self, image: ImageLocation) -> None:
        self.image = image

    def to_api(self) -> messaging_pb2.ImageMedia:
        return messaging_pb2.ImageMedia(image=self.image.to_api())

    @classmethod
    def from_api(cls, image: messaging_pb2.ImageMedia) -> 'ImageMedia':
        return cls(ImageLocation.from_api(image.image))

    def __dict__(self):
        return {"image": self.image.__dict__()}

    def __str__(self):
        return "ImageMedia({})".format(self.__dict__())


class WebPageMedia:
    def __init__(self, url: str, title: str = "", description: str = "", image: ImageLocation = None):
        self.url = url
        self.title = title
        self.description = description
        self.image = image

    def to_api(self) -> messaging_pb2.WebpageMedia:
        if self.image is not None:
            image = self.image.to_api()
        else:
            image = None
        return messaging_pb2.WebpageMedia(url=StringValue(value=self.url), title=StringValue(value=self.title),
                                          description=StringValue(value=self.description), image=image)

    @classmethod
    def from_api(cls, web_page: messaging_pb2.WebpageMedia) -> 'WebPageMedia':
        return cls(web_page.url, web_page.title, web_page.description, ImageLocation.from_api(web_page.image))

    def __dict__(self):
        return {"url": self.url, "title": self.title, "description": self.description, "image": self.image.__dict__()}

    def __str__(self):
        return "WebPageMedia({})".format(self.__dict__())


# ex classes
class DocumentExPhoto:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, photo: messaging_pb2.DocumentExPhoto) -> 'DocumentExPhoto':
        return cls(photo.h, photo.w)

    def __dict__(self):
        return {"height": self.height, "width": self.width}

    def __str__(self):
        return "DocumentExPhoto({})".format(self.__dict__())


class DocumentExVideo:
    def __init__(self, duration: int, height: int, width: int) -> None:
        self.duration = duration
        self.height = height
        self.width = width

    @classmethod
    def from_api(cls, video: messaging_pb2.DocumentExVideo) -> 'DocumentExVideo':
        return cls(video.duration, video.h, video.w)

    def __dict__(self):
        return {"duration": self.duration, "height": self.height, "width": self.width}

    def __str__(self):
        return "DocumentExVideo({})".format(self.__dict__())


class DocumentExVoice:
    def __init__(self, duration: int) -> None:
        self.duration = duration

    @classmethod
    def from_api(cls, voice: messaging_pb2.DocumentExVoice) -> 'DocumentExVoice':
        return cls(voice.duration)

    def __dict__(self):
        return {"duration": self.duration}

    def __str__(self):
        return "DocumentExVoice({})".format(self.__dict__())


class DocumentEx:
    def __init__(self, type: DocumentExType, photo: DocumentExPhoto, video: DocumentExVideo, voice: DocumentExVoice) \
            -> None:
        self.type = type
        self.photo = photo
        self.video = video
        self.voice = voice

    @classmethod
    def from_api(cls, ext: messaging_pb2.DocumentEx) -> 'DocumentEx':
        return cls(
            document_ex_type_mapper.get(ext.WhichOneof('body')),
            DocumentExPhoto.from_api(ext.photo),
            DocumentExVideo.from_api(ext.video),
            DocumentExVoice.from_api(ext.voice)
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == DocumentExType.DOCUMENT_EX_PHOTO:
            return self.photo
        if self.type == DocumentExType.DOCUMENT_EX_VIDEO:
            return self.video
        if self.type == DocumentExType.DOCUMENT_EX_VOICE:
            return self.voice

    def __str__(self):
        return "DocumentEx({})".format(self.__dict__())


class ServiceEx:
    def __init__(
            self,
            type: ServiceExType,
            user_invited: int,
            user_joined: int,
            user_kicked: int,
            user_left: int,
            group_created,
            changed_shortname: str,
            changed_title: str,
            changed_topic: str,
            changed_about: str,
            changed_avatar: Avatar,
            contact_registered,
            phone_missed,
            phone_call: int,
            phone_rejected,
            chat_archived,
            chat_restored,
    ) -> None:
        self.type = type
        self.user_invited = user_invited
        self.user_joined = user_joined
        self.user_kicked = user_kicked
        self.user_left = user_left
        self.group_created = group_created
        self.changed_shortname = changed_shortname
        self.changed_title = changed_title
        self.changed_topic = changed_topic
        self.changed_about = changed_about
        self.changed_avatar = changed_avatar
        self.contact_registered = contact_registered
        self.phone_missed = phone_missed
        self.phone_call = phone_call
        self.phone_rejected = phone_rejected
        self.chat_archived = chat_archived
        self.chat_restored = chat_restored

    @classmethod
    def from_api(cls, service_ex: messaging_pb2.ServiceEx) -> 'ServiceEx':
        return cls(
            service_ex_type_mapper.get(service_ex.WhichOneof('body')),
            service_ex.userInvited.invited_uid,
            service_ex.userJoined.joined_user_id,
            service_ex.userKicked.kicked_uid,
            service_ex.userLeft.left_user_id,
            service_ex.groupCreated,
            service_ex.changedShortname.shortname,
            service_ex.changedTitle.title,
            service_ex.changedTopic.topic.value,
            service_ex.changedAbout.about.value,
            Avatar.from_api(service_ex.changedAvatar.avatar),
            service_ex.contactRegistered.uid,
            service_ex.phoneMissed,
            service_ex.phoneCall.duration,
            service_ex.phoneRejected,
            service_ex.chatArchived,
            service_ex.chatRestored
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == ServiceExType.USER_INVITED:
            return self.user_invited
        if self.type == ServiceExType.USER_JOINED:
            return self.user_joined
        if self.type == ServiceExType.USER_KICKED:
            return self.user_kicked
        if self.type == ServiceExType.USER_LEFT:
            return self.user_left
        if self.type == ServiceExType.GROUP_CREATED:
            return self.group_created
        if self.type == ServiceExType.CHANGED_SHORTNAME:
            return self.changed_shortname
        if self.type == ServiceExType.CHANGED_TITLE:
            return self.changed_title
        if self.type == ServiceExType.CHANGED_TOPIC:
            return self.changed_topic
        if self.type == ServiceExType.CHANGED_ABOUT:
            return self.changed_about
        if self.type == ServiceExType.CHANGED_AVATAR:
            return self.changed_avatar
        if self.type == ServiceExType.CONTACT_REGISTERED:
            return self.contact_registered
        if self.type == ServiceExType.PHONE_MISSED:
            return self.phone_missed
        if self.type == ServiceExType.PHONE_CALL:
            return self.phone_call
        if self.type == ServiceExType.PHONE_REJECTED:
            return self.phone_rejected
        if self.type == ServiceExType.CHAT_ARCHIVED:
            return self.chat_archived
        if self.type == ServiceExType.CHAT_RESTORED:
            return self.chat_restored

    def __str__(self):
        return "ServiceEx({})".format(self.__dict__())


# Messages type
class MessageMedia:
    def __init__(self, web_page: WebPageMedia, image: ImageMedia, audio: AudioMedia,
                 actions: List[InteractiveMediaGroup]) -> None:
        self.web_page = web_page
        self.image = image
        self.audio = audio
        self.actions = actions

    def to_api(self) -> messaging_pb2.MessageMedia:
        web, image, audio, actions = None, None, None, []
        if self.web_page is not None:
            web = self.web_page.to_api()
        if self.image is not None:
            image = self.image.to_api()
        if self.audio is not None:
            audio = self.audio.to_api()
        if self.actions is not None:
            actions = [x.to_api() for x in self.actions]
        return messaging_pb2.MessageMedia(webpage=web, image=image, audio=audio, actions=actions)

    @classmethod
    def from_api(cls, message_media: messaging_pb2.MessageMedia) -> 'MessageMedia':
        return cls(
            WebPageMedia.from_api(message_media.webpage),
            ImageMedia.from_api(message_media.image),
            AudioMedia.from_api(message_media.audio),
            [InteractiveMediaGroup.from_api(x) for x in message_media.actions]
        )

    def __dict__(self):
        return {
            "web_page": self.web_page.__dict__(),
            "image": self.image.__dict__(),
            "audio": self.audio.__dict__(),
            "actions": [x.__dict__() for x in self.actions]
        }

    def __str__(self):
        return "MessageMedia({})".format(self.__dict__())


class ParagraphStyle:
    def __init__(self, show_paragraph: bool, paragraph_color: Color, bg_color: Color) -> None:
        self.show_paragraph = show_paragraph
        self.paragraph_color = paragraph_color
        self.bg_color = bg_color

    @classmethod
    def from_api(cls, style: messaging_pb2.ParagraphStyle) -> 'ParagraphStyle':
        return cls(style.show_paragraph.value, Color.from_api(style.paragraph_color), Color.from_api(style.bg_color))

    def __dict__(self):
        return {"show_paragraph": self.show_paragraph, "paragraph_color": self.paragraph_color.__dict__(),
                "bg_color": self.bg_color}

    def __str__(self):
        return "ParagraphStyle({})".format(self.__dict__())


class TextModernField:
    def __init__(self, title: str, value: str, is_short: bool) -> None:
        self.title = title
        self.value = value
        self.is_short = is_short

    @classmethod
    def from_api(cls, field: messaging_pb2.TextModernField) -> 'TextModernField':
        return cls(field.title, field.value, field.is_short.value)

    def __dict__(self):
        return {"title": self.title, "value": self.value, "is_short": self.is_short}

    def __str__(self):
        return "TextModernField({})".format(self.__dict__())


class TextModernAttach:
    def __init__(self, title: str, title_url: str, title_icon: ImageLocation, text: str, style: ParagraphStyle,
                 fields: List[TextModernField]) -> None:
        self.title = title
        self.title_url = title_url
        self.title_icon = title_icon
        self.text = text
        self.style = style
        self.fields = fields

    @classmethod
    def from_api(cls, attach: messaging_pb2.TextModernAttach) -> 'TextModernAttach':
        return cls(attach.title.value, attach.title_url.value, ImageLocation.from_api(attach.title_icon),
                   attach.text.value, ParagraphStyle.from_api(attach.style),
                   [TextModernField.from_api(x) for x in attach.fields])

    def __dict__(self):
        return {"title": self.title, "title_url": self.title_url, "title_icon": self.title_icon.__dict__(),
                "text": self.text, "style": self.style.__dict__(), "fields": [x.__dict__() for x in self.fields]}

    def __str__(self):
        return "TextModernAttach({})".format(self.__dict__())


class TextModernMessage:
    def __init__(self, text: str, sender_name_override: str, sender_photo_override: Avatar, style: ParagraphStyle,
                 attaches: List[TextModernAttach]) -> None:
        self.text = text
        self.sender_name_override = sender_name_override
        self.sender_photo_override = sender_photo_override
        self.style = style
        self.attaches = attaches

    @classmethod
    def from_api(cls, text: messaging_pb2.TextModernMessage) -> 'TextModernMessage':
        return cls(text.text.value, text.sender_name_override.value, Avatar.from_api(text.sender_photo_override),
                   ParagraphStyle.from_api(text.style), [TextModernAttach.from_api(x) for x in text.attaches])

    def __dict__(self):
        return {"text": self.text, "sender_name_override": self.sender_name_override,
                "sender_photo_override": self.sender_photo_override.__dict__(), "style": self.style.__dict__(),
                "attaches": [x.__dict__() for x in self.attaches]}

    def __str__(self):
        return "TextModernMessage({})".format(self.__dict__())


class TextExMarkdown:
    def __init__(self, markdown: str) -> None:
        self.markdown = markdown

    @classmethod
    def from_api(cls, ex: messaging_pb2.TextExMarkdown) -> 'TextExMarkdown':
        return cls(ex.markdown)

    def __dict__(self):
        return {"markdown": self.markdown}

    def __str__(self):
        return "TextExMarkdown({})".format(self.__dict__())


class TextCommand:
    def __init__(self, command: str, args: str) -> None:
        self.command = command
        self.args = args

    @classmethod
    def from_api(cls, command: messaging_pb2.TextCommand) -> 'TextCommand':
        return cls(command.command, command.args)

    def __dict__(self):
        return {"command": self.command, "args": self.args}

    def __str__(self):
        return "TextCommand({})".format(self.__dict__())


class TextMessageEx:
    def __init__(
            self,
            type: TextExType,
            text_ex_markdown: TextExMarkdown,
            text_modern_message: TextModernMessage,
            text_command: TextCommand
    ) -> None:
        self.type = type
        self.text_ex_markdown = text_ex_markdown
        self.text_modern_message = text_modern_message
        self.text_command = text_command

    @classmethod
    def from_api(cls, ex: messaging_pb2.TextMessageEx) -> 'TextMessageEx':
        return cls(
            text_ex_type_mapper.get(ex.WhichOneof('body')),
            TextExMarkdown.from_api(ex.textExMarkdown),
            TextModernMessage.from_api(ex.textModernMessage),
            TextCommand.from_api(ex.textCommand)
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == TextExType.TEXT_EX_MARKDOWN:
            return self.text_ex_markdown
        if self.type == TextExType.TEXT_MODERN_MESSAGE:
            return self.text_modern_message
        if self.type == TextExType.TEXT_COMMAND:
            return self.text_command

    def __str__(self):
        return "TextMessageEx({})".format(self.__dict__())


class TextMessage:
    def __init__(
            self,
            text: str,
            obsolete_mentions: List[int],
            ext: TextMessageEx,
            media: List[MessageMedia],
            extensions: List[Any],
            mentions: List[Mention]
    ) -> None:
        self.text = text
        self.obsolete_mentions = obsolete_mentions
        self.ext = ext
        self.media = media
        self.extensions = extensions
        self.mentions = mentions

    @classmethod
    def from_api(cls, text_message: messaging_pb2.TextMessage) -> 'TextMessage':
        return cls(
            text_message.text.strip(),
            [x for x in text_message.obsolete_mentions],
            TextMessageEx.from_api(text_message.ext),
            [MessageMedia.from_api(x) for x in text_message.media],
            [Any.from_api(x) for x in text_message.extensions],
            [Mention.from_api(x) for x in text_message.mentions]
        )

    def __dict__(self):
        return {
            "text": self.text,
            "obsolete_mentions": self.obsolete_mentions,
            "ext": self.ext.__dict__(),
            "media": [x.__dict__() for x in self.media],
            "extensions": [x.__dict__() for x in self.extensions],
            "mentions": [x.__dict__() for x in self.mentions]
        }

    def __str__(self):
        return "TextMessage({})".format(self.__dict__())


class ServiceMessage:
    def __init__(self, text: str, ext: ServiceEx) -> None:
        self.text = text
        self.ext = ext

    @classmethod
    def from_api(cls, service: messaging_pb2.ServiceMessage) -> 'ServiceMessage':
        return cls(service.text, ServiceEx.from_api(service.ext))

    def __dict__(self):
        return {"text": self.text, "ext": self.ext.__dict__()}

    def __str__(self):
        return "ServiceMessage({})".format(self.__dict__())


class DocumentMessage:
    def __init__(self, file_id: int, access_hash: int, file_size: int, mime_type: str, name: str, ext: DocumentEx,
                 thumb: FastThumb, caption: str, mentions: List[Mention], document_check_status: DocumentCheckStatus) -> None:
        self.file_id = file_id
        self.access_hash = access_hash
        self.file_size = file_size
        self.mime_type = mime_type
        self.name = name
        self.ext = ext
        self.thumb = thumb
        self.caption = caption
        self.mentions = mentions
        self.document_check_status = document_check_status

    @classmethod
    def from_api(cls, document: messaging_pb2.DocumentMessage) -> 'DocumentMessage':
        return cls(document.file_id, document.access_hash, document.file_size, document.mime_type, document.name,
                   DocumentEx.from_api(document.ext), FastThumb.from_api(document.thumb), document.caption.value,
                   [Mention.from_api(x) for x in document.mentions], document.document_check_status)

    def __dict__(self):
        return {"file_id": self.file_id, "access_hash": self.access_hash, "file_size": self.file_size,
                "mime_type": self.mime_type, "name": self.name, "ex": self.ext.__dict__(), "caption": self.caption,
                "mentions": [x.__dict__() for x in self.mentions], "document_check_status": self.document_check_status}

    def __str__(self):
        return "DocumentMessage({})".format(self.__dict__())


class JsonMessage:
    def __init__(self, raw_json: str) -> None:
        self.raw_json = raw_json

    @classmethod
    def from_api(cls, json_: messaging_pb2.JsonMessage) -> 'JsonMessage':
        return cls(json_.raw_json)

    def __dict__(self):
        return {"raw_json": self.raw_json}

    def __str__(self):
        return "JsonMessage({})".format(self.__dict__())


class UnsupportedMessage:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_api(cls, unsupported: messaging_pb2.UnsupportedMessage) -> 'UnsupportedMessage':
        return cls()

    def __dict__(self):
        return {}

    def __str__(self):
        return "UnsupportedMessage({})".format(self.__dict__())


class StickerMessage:
    def __init__(
            self, 
            sticker_id: int, 
            fast_preview: bytes, 
            image_512: ImageLocation, 
            image_256: ImageLocation, 
            sticker_collection_id: int, 
            emoji: str, 
            animated_sticker_json: dict
    ) -> None:
        self.sticker_id = sticker_id
        self.fast_preview = fast_preview
        self.image_512 = image_512
        self.image_256 = image_256
        self.sticker_collection_id = sticker_collection_id
        self.emoji = emoji
        self.animated_sticker_json = animated_sticker_json

    @classmethod
    def from_api(cls, sticker: messaging_pb2.StickerMessage) -> 'StickerMessage':
        return cls(
            sticker.sticker_id.value, 
            sticker.fast_preview.value, 
            ImageLocation.from_api(sticker.image_512),
            ImageLocation.from_api(sticker.image_256),
            sticker.sticker_collection_id.value,
            sticker.emoji.value,
            json.loads(sticker.animatedStickerJson.value) if sticker.animatedStickerJson.value else {}
        )

    def __dict__(self):
        return {
            "sticker_id": self.sticker_id,
            "fast_preview": self.fast_preview,
            "image_512": self.image_512.__dict__(),
            "image_256": self.image_256.__dict__(),
            "sticker_collection_id": self.sticker_collection_id,
            "emoji": self.emoji,
            "animated_sticker_json": self.animated_sticker_json,
        }

    def __str__(self):
        return "StickerMessage({})".format(self.__dict__())


class BinaryMessage:
    def __init__(self, content_tag: str, msg: bytes) -> None:
        self.content_tag = content_tag
        self.msg = msg

    @classmethod
    def from_api(cls, binary: messaging_pb2.BinaryMessage) -> 'BinaryMessage':
        return cls(binary.content_tag, binary.msg)

    def __dict__(self):
        return {"content_tag": self.content_tag, "msg": self.msg}

    def __str__(self):
        return "BinaryMessage({})".format(self.__dict__())


class EmptyMessage:
    def __init__(self) -> None:
        pass

    @classmethod
    def from_api(cls, empty: messaging_pb2.EmptyMessage) -> 'EmptyMessage':
        return cls()

    def __dict__(self):
        return {}

    def __str__(self):
        return "EmptyMessage({})".format(self.__dict__())


class DeletedMessage:
    def __init__(self, is_local: bool) -> None:
        self.is_local = is_local

    @classmethod
    def from_api(cls, deleted: messaging_pb2.DeletedMessage) -> 'DeletedMessage':
        return cls(deleted.is_local.value)

    def __dict__(self):
        return {"is_local": self.is_local}

    def __str__(self):
        return "DeleteMessage({})".format(self.__dict__())


class PackageMessage:
    def __init__(self, message_ids: List[UUID], caption: str) -> None:
        self.message_ids = message_ids
        self.caption = caption

    @classmethod
    def from_api(cls, package: messaging_pb2.PackageMessage) -> 'PackageMessage':
        return cls([UUID.from_api(x) for x in package.message_ids], package.caption.value)

    def __dict__(self):
        return {"message_ids": [x.__dict__() for x in self.message_ids], "caption": self.caption}

    def __str__(self):
        return "PackageMessage({})".format(self.__dict__())


class MessageContent:
    def __init__(
            self,
            type: MessageContentType,
            text: TextMessage,
            service: ServiceMessage,
            document: DocumentMessage,
            json_: JsonMessage,
            unsupported: UnsupportedMessage,
            sticker: StickerMessage,
            binary: BinaryMessage,
            empty: EmptyMessage,
            deleted: DeletedMessage,
            package: PackageMessage
    ) -> None:
        self.type = type
        self.text_message = text
        self.service_message = service
        self.document_message = document
        self.json_message = json_
        self.unsupported_message = unsupported
        self.sticker_message = sticker
        self.binary_message = binary
        self.empty_message = empty
        self.deleted_message = deleted
        self.package_message = package

    @classmethod
    def from_api(cls, content: messaging_pb2.MessageContent) -> 'MessageContent':
        return cls(
            message_content_type_mapper.get(content.WhichOneof('body')),
            TextMessage.from_api(content.textMessage),
            ServiceMessage.from_api(content.serviceMessage),
            DocumentMessage.from_api(content.documentMessage),
            JsonMessage.from_api(content.jsonMessage),
            UnsupportedMessage.from_api(content.unsupportedMessage),
            StickerMessage.from_api(content.stickerMessage),
            BinaryMessage.from_api(content.binaryMessage),
            EmptyMessage.from_api(content.emptyMessage),
            DeletedMessage.from_api(content.deletedMessage),
            PackageMessage.from_api(content.packageMessage),
        )

    def __dict__(self):
        oneof = self.oneof_type()
        return {
            self.type: oneof.__dict__() if oneof is not None else oneof,
        }

    def oneof_type(self):
        if self.type == MessageContentType.TEXT_MESSAGE:
            return self.text_message
        if self.type == MessageContentType.SERVICE_MESSAGE:
            return self.service_message
        if self.type == MessageContentType.DOCUMENT_MESSAGE:
            return self.document_message
        if self.type == MessageContentType.JSON_MESSAGE:
            return self.json_message
        if self.type == MessageContentType.UNSUPPORTED_MESSAGE:
            return self.unsupported_message
        if self.type == MessageContentType.STICKER_MESSAGE:
            return self.sticker_message
        if self.type == MessageContentType.BINARY_MESSAGE:
            return self.binary_message
        if self.type == MessageContentType.EMPTY_MESSAGE:
            return self.empty_message
        if self.type == MessageContentType.DELETED_MESSAGE:
            return self.deleted_message
        if self.type == MessageContentType.PACKAGE_MESSAGE:
            return self.package_message

    def __str__(self):
        return "MessageContent({})".format(self.__dict__())


class MessageAttributes:
    def __init__(self, is_mentioned: bool, is_highlighted: bool, is_notified: bool, is_only_for_you: bool) -> None:
        self.is_mentioned = is_mentioned
        self.is_highlighted = is_highlighted
        self.is_notified = is_notified
        self.is_only_for_you = is_only_for_you

    @classmethod
    def from_api(cls, attributes: messaging_pb2.MessageAttributes) -> 'MessageAttributes':
        return cls(attributes.is_mentioned.value, attributes.is_highlighted.value, attributes.is_notified.value,
                   attributes.is_only_for_you.value)

    def __dict__(self):
        return {"is_mentioned": self.is_mentioned, "is_highlighted": self.is_highlighted,
                "is_notified": self.is_notified,
                "is_only_for_you": self.is_only_for_you}

    def __str__(self):
        return "MessageAttributes({})".format(self.__dict__())


class MessageReaction:
    def __init__(self, users: List[Peer], code: str) -> None:
        self.users = users
        self.code = code

    @classmethod
    def from_api(cls, reaction: messaging_pb2.MessageReaction) -> 'MessageReaction':
        return cls([Peer(x, PeerType.PEERTYPE_PRIVATE) for x in reaction.users], reaction.code)

    def __dict__(self):
        return {"users": [x.__dict__() for x in self.users], "code": self.code}

    def __str__(self):
        return "MessageReaction({})".format(self.__dict__())


class Message:
    def __init__(
            self,
            sender_peer: Peer,
            peer: Peer,
            mid: UUID,
            prev_mid: UUID,
            date: int,
            message: MessageContent,
            state: MessageState,
            reactions: List[MessageReaction],
            attribute: MessageAttributes,
            forward: List[UUID],
            reply: List[UUID],
            edited_at: int,
            random_id: int,
            is_part_of_package: bool,
            thread: Peer
    ) -> None:
        self.sender_peer = sender_peer
        self.peer = peer
        self.mid = mid
        self.prev_mid = prev_mid
        self.date = date
        self.message = message
        self.state = state
        self.reactions = reactions
        self.attribute = attribute
        self.forward = forward
        self.reply = reply
        self.edited_at = edited_at
        self.random_id = random_id
        self.is_part_of_package = is_part_of_package
        self.thread = thread

    @classmethod
    def from_api(cls, message: messaging_pb2.HistoryMessage) -> 'Message':
        return cls(
            Peer(message.sender_uid, PeerType.PEERTYPE_PRIVATE),
            Peer(message.host_peer.id, message.host_peer.type),
            UUID.from_api(message.mid),
            UUID.from_api(message.prev_mid),
            message.date,
            MessageContent.from_api(message.message),
            message.state,
            [MessageReaction.from_api(x) for x in message.reactions],
            MessageAttributes.from_api(message.attribute),
            [UUID.from_api(x) for x in message.forward.mids],
            [UUID.from_api(x) for x in message.reply.mids],
            message.edited_at.value,
            message.random_id,
            message.is_part_of_package,
            Peer(message.thread.thread_id, PeerType.PEERTYPE_THREAD)
        )

    def __dict__(self):
        return {
            "sender_peer": self.sender_peer.__dict__(),
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "prev_mid": self.prev_mid.__dict__(),
            "date": self.date,
            "message": self.message.__dict__(),
            "state": self.state,
            "reactions": [x.__dict__() for x in self.reactions],
            "attribute": self.attribute.__dict__(),
            "forward": [x.__dict__() for x in self.forward],
            "reply": [x.__dict__() for x in self.reply],
            "edited_at": self.edited_at,
            "random_id": self.random_id,
            "is_part_of_package": self.is_part_of_package,
            "thread": self.thread.__dict__()
        }

    def __str__(self):
        return "Message({})".format(self.__dict__())


class DialogShort:
    def __init__(
            self,
            peer: Peer,
            counter: int,
            date: int,
    ) -> None:
        self.peer = peer
        self.counter = counter
        self.date = date

    @classmethod
    def from_api(cls, dialog_short: messaging_pb2.DialogShort) -> 'DialogShort':
        return cls(Peer.from_api(dialog_short.peer), dialog_short.counter, dialog_short.date)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "counter": self.counter,
            "dialogs": self.date,
        }

    def __str__(self):
        return "DialogShort({})".format(self.__dict__())


class DialogGroup:
    def __init__(
            self,
            title: str,
            key: str,
            dialogs: List[DialogShort],
    ) -> None:
        self.title = title
        self.key = key
        self.dialogs = dialogs

    @classmethod
    def from_api(cls, dialog_group: messaging_pb2.DialogGroup) -> 'DialogGroup':
        return cls(dialog_group.title, dialog_group.key, [DialogShort.from_api(x) for x in dialog_group.dialogs])

    def __dict__(self):
        return {
            "title": self.title,
            "key": self.key,
            "dialogs": [x.__dict__() for x in self.dialogs],
        }

    def __str__(self):
        return "DialogGroup({})".format(self.__dict__())


# from UpdateSeqUpdate
class UpdateMessage:
    def __init__(
            self, 
            peer: Peer, 
            sender_peer: Peer, 
            date: int, 
            mid: UUID, 
            message: MessageContent, 
            attributes: MessageAttributes,
            forward: List[UUID],
            reply: List[UUID], 
            previous_mid: UUID,
            prev_message_date: int,
            unread_counter_clock: int,
            counter: int,
            my_read_date: int,
            random_id: int,
            modified_at: int,
            prev_edit_in_peer_at: int,
            is_part_of_package: bool
    ) -> None:
        self.peer = peer
        self.sender_peer = sender_peer
        self.date = date
        self.mid = mid
        self.message = message
        self.attributes = attributes
        self.forward = forward
        self.reply = reply
        self.previous_mid = previous_mid
        self.prev_message_date = prev_message_date
        self.unread_counter_clock = unread_counter_clock
        self.counter = counter
        self.my_read_date = my_read_date
        self.random_id = random_id
        self.modified_at = modified_at
        self.prev_edit_in_peer_at = prev_edit_in_peer_at
        self.is_part_of_package = is_part_of_package

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessage) -> 'UpdateMessage':
        return cls(
            Peer.from_api(update.peer), 
            Peer(update.sender_uid, PeerType.PEERTYPE_PRIVATE),
            update.date,
            UUID.from_api(update.mid), 
            MessageContent.from_api(update.message),
            MessageAttributes.from_api(update.attributes),
            [UUID.from_api(x) for x in update.forward.mids], 
            [UUID.from_api(x) for x in update.reply.mids],
            UUID.from_api(update.previous_mid),
            update.prev_message_date.value,
            update.unread_counter_clock,
            update.counter.value,
            update.my_read_date.value,
            update.random_id,
            update.modified_at,
            update.prev_edit_in_peer_at.value,
            update.is_part_of_package
        )
    
    def __dict__(self):
        return {
            "peer": self.peer.__dict__(), 
            "sender_peer": self.sender_peer.__dict__(),
            "mid": self.mid.__dict__(), 
            "message": self.message.__dict__(),
            "attributes": self.attributes.__dict__(),
            "forward": [x.__dict__() for x in self.forward], 
            "reply": [x.__dict__() for x in self.reply],
            "previous_mid": self.previous_mid.__dict__(), 
            "date": self.date,
            "prev_message_date": self.prev_message_date,
            "unread_counter_clock": self.unread_counter_clock,
            "counter": self.counter,
            "my_read_date": self.my_read_date,
            "random_id": self.random_id,
            "modified_at": self.modified_at,
            "prev_edit_in_peer_at": self.prev_edit_in_peer_at,
            "is_part_of_package": self.is_part_of_package
        }

    def __str__(self):
        return "UpdateMessage({})".format(self.__dict__())


class UpdateMessageContentChanged:
    def __init__(
            self,
            peer: Peer,
            mid: UUID,
            message: MessageContent,
            edited_at: int,
            prev_edit_in_peer_at: int,
            is_silent: bool
    ) -> None:
        self.peer = peer
        self.mid = mid
        self.message = message
        self.edited_at = edited_at
        self.prev_edit_in_peer_at = prev_edit_in_peer_at
        self.is_silent = is_silent

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageContentChanged) -> 'UpdateMessageContentChanged':
        return cls(
            Peer.from_api(update.peer),
            UUID.from_api(update.mid),
            MessageContent.from_api(update.message),
            update.edited_at,
            update.prev_edit_in_peer_at,
            update.is_silent.value
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "message": self.message.__dict__(),
            "edited_at": self.edited_at,
            "prev_edit_in_peer_at": self.prev_edit_in_peer_at,
            "is_silent": self.is_silent
        }

    def __str__(self):
        return "UpdateMessageContentChanged({})".format(self.__dict__())


class UpdateInteractiveMediaEvent:
    def __init__(self, mid: UUID, id_: str, value: str, peer: Peer) -> None:
        self.mid = mid
        self.id = id_
        self.value = value
        self.peer = peer

    @classmethod
    def from_api(cls, event: messaging_pb2.UpdateInteractiveMediaEvent) -> 'UpdateInteractiveMediaEvent':
        return cls(UUID.from_api(event.mid), event.id, event.value, Peer(event.uid, PeerType.PEERTYPE_PRIVATE))

    def __dict__(self):
        return {"mid": self.mid.__dict__(), "id": self.id, "value": self.value, "peer": self.peer.__dict__()}

    def __str__(self):
        return "UpdateInteractiveMediaEvent({})".format(self.__dict__())


class UpdateMessageSent:
    def __init__(
            self,
            peer: Peer,
            rid: int,
            date: int,
            mid: UUID,
            prev_mid: UUID,
            unread_counter_clock: int,
            unread_counter: int,
            my_read_date: int,
            forward: List[UUID],
            reply: List[UUID],
    ) -> None:
        self.peer = peer
        self.rid = rid
        self.date = date
        self.mid = mid
        self.prev_mid = prev_mid
        self.unread_counter_clock = unread_counter_clock
        self.unread_counter = unread_counter
        self.my_read_date = my_read_date
        self.forward = forward
        self.reply = reply

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageSent) -> 'UpdateMessageSent':
        return cls(
            Peer.from_api(update.peer),
            update.rid,
            update.date,
            UUID.from_api(update.mid),
            UUID.from_api(update.prev_mid),
            update.unread_counter_clock,
            update.unread_counter.value,
            update.myReadDate.value,
            [UUID.from_api(x) for x in update.forward.mids],
            [UUID.from_api(x) for x in update.reply.mids],
        )

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "rid": self.rid,
            "date": self.date,
            "mid": self.mid.__dict__(),
            "prev_mid": self.prev_mid.__dict__(),
            "unread_counter_clock": self.unread_counter_clock,
            "unread_counter": self.unread_counter,
            "my_read_date": self.my_read_date,
            "forward": [x.__dict__() for x in self.forward],
            "reply": [x.__dict__() for x in self.reply],
        }

    def __str__(self):
        return "UpdateMessageSent({})".format(self.__dict__())


class UpdateMessageReceived:
    def __init__(
            self,
            peer: Peer,
            start_date: int,
            received_date: int,
    ) -> None:
        self.peer = peer
        self.start_date = start_date
        self.received_date = received_date

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageReceived) -> 'UpdateMessageReceived':
        return cls(Peer.from_api(update.peer), update.start_date, update.received_date)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "start_date": self.start_date,
            "received_date": self.received_date,
        }

    def __str__(self):
        return "UpdateMessageReceived({})".format(self.__dict__())


class UpdateMessageRead:
    def __init__(
            self,
            peer: Peer,
            start_date: int,
            read_date: int,
    ) -> None:
        self.peer = peer
        self.start_date = start_date
        self.read_date = read_date

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageRead) -> 'UpdateMessageRead':
        return cls(Peer.from_api(update.peer), update.start_date, update.read_date)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "start_date": self.start_date,
            "read_date": self.read_date,
        }

    def __str__(self):
        return "UpdateMessageRead({})".format(self.__dict__())


class UpdateMessageReadByMe:
    def __init__(
            self,
            peer: Peer,
            start_date: int,
            unread_counter_clock: int,
            unread_counter: int
    ) -> None:
        self.peer = peer
        self.start_date = start_date
        self.unread_counter_clock = unread_counter_clock
        self.unread_counter = unread_counter

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageReadByMe) -> 'UpdateMessageReadByMe':
        return cls(Peer.from_api(update.peer), update.start_date, update.unread_counter_clock, update.unread_counter.value)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "start_date": self.start_date,
            "unread_counter_clock": self.unread_counter_clock,
            "unread_counter": self.unread_counter
        }

    def __str__(self):
        return "UpdateMessageReadByMe({})".format(self.__dict__())


class UpdateMessageDelete:
    def __init__(
            self,
            peer: Peer,
            mid: UUID,
            previous_mid: UUID,
            counter: int,
            deleted_at: int,
            prev_edit_in_peer_at: int
    ) -> None:
        self.peer = peer
        self.mid = mid
        self.previous_mid = previous_mid
        self.counter = counter
        self.deleted_at = deleted_at
        self.prev_edit_in_peer_at = prev_edit_in_peer_at

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageDelete) -> 'UpdateMessageDelete':
        return cls(Peer.from_api(update.peer), UUID.from_api(update.mid), UUID.from_api(update.previous_mid),
                   update.counter.value, update.deleted_at, update.prev_edit_in_peer_at)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "previous_mid": self.previous_mid.__dict__(),
            "counter": self.counter,
            "deleted_at": self.deleted_at,
            "prev_edit_in_peer_at": self.prev_edit_in_peer_at
        }

    def __str__(self):
        return "UpdateMessageDelete({})".format(self.__dict__())


class UpdateChatClear:
    def __init__(
            self,
            peer: Peer,
            action_date: int
    ) -> None:
        self.peer = peer
        self.action_date = action_date

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateChatClear) -> 'UpdateChatClear':
        return cls(Peer.from_api(update.peer), update.action_date)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "action_date": self.action_date
        }

    def __str__(self):
        return "UpdateChatClear({})".format(self.__dict__())


class UpdateChatDelete:
    def __init__(
            self,
            peer: Peer,
            action_date: int
    ) -> None:
        self.peer = peer
        self.action_date = action_date

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateChatDelete) -> 'UpdateChatDelete':
        return cls(Peer.from_api(update.peer), update.action_date)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "action_date": self.action_date
        }

    def __str__(self):
        return "UpdateChatDelete({})".format(self.__dict__())


class UpdateChatArchive:
    def __init__(
            self,
            peer: Peer,
    ) -> None:
        self.peer = peer

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateChatArchive) -> 'UpdateChatArchive':
        return cls(Peer.from_api(update.peer))

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
        }

    def __str__(self):
        return "UpdateChatArchive({})".format(self.__dict__())


class UpdateChatGroupsChanged:
    def __init__(
            self,
            dialogs: List[DialogGroup],
    ) -> None:
        self.dialogs = dialogs

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateChatGroupsChanged) -> 'UpdateChatGroupsChanged':
        return cls([DialogGroup.from_api(x) for x in update.dialogs])

    def __dict__(self):
        return {
            "dialogs": [x.__dict__() for x in self.dialogs],
        }

    def __str__(self):
        return "UpdateChatGroupsChanged({})".format(self.__dict__())


class UpdateReactionsUpdate:
    def __init__(
            self,
            peer: Peer,
            mid: UUID,
            reactions: List[MessageReaction],
    ) -> None:
        self.peer = peer
        self.mid = mid
        self.reactions = reactions

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateReactionsUpdate) -> 'UpdateReactionsUpdate':
        return cls(Peer.from_api(update.peer), UUID.from_api(update.mid), [MessageReaction.from_api(x) for x in update.reactions])

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "reactions": [x.__dict__() for x in self.reactions],
        }

    def __str__(self):
        return "UpdateReactionsUpdate({})".format(self.__dict__())


class UpdateDialogFavouriteChanged:
    def __init__(
            self,
            peer: Peer,
            is_favourite: bool,
    ) -> None:
        self.peer = peer
        self.is_favourite = is_favourite

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateDialogFavouriteChanged) -> 'UpdateDialogFavouriteChanged':
        return cls(Peer.from_api(update.peer), update.is_favourite.value)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "is_favourite": self.is_favourite
        }

    def __str__(self):
        return "UpdateDialogFavouriteChanged({})".format(self.__dict__())


class UpdateMessageRejectedByHook:
    def __init__(
            self,
            peer: Peer,
            rid: int,
            date: int,
            hook_id: str,
            reason: str,

    ) -> None:
        self.peer = peer
        self.rid = rid
        self.date = date
        self.hook_id = hook_id
        self.reason = reason

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageRejectedByHook) -> 'UpdateMessageRejectedByHook':
        return cls(Peer.from_api(update.peer), update.rid, update.date, update.hookId, update.reason.value)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "rid": self.rid,
            "date": self.date,
            "hook_id": self.hook_id,
            "reason": self.reason,
        }

    def __str__(self):
        return "UpdateMessageRejectedByHook({})".format(self.__dict__())


class UpdateMessageEditRejectedByHook:
    def __init__(
            self,
            peer: Peer,
            mid: UUID,
            date: int,
            hook_id: str,
            reason: str,

    ) -> None:
        self.peer = peer
        self.mid = mid
        self.date = date
        self.hook_id = hook_id
        self.reason = reason

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateMessageEditRejectedByHook) -> 'UpdateMessageEditRejectedByHook':
        return cls(Peer.from_api(update.peer), UUID.from_api(update.mid), update.date, update.hookId, update.reason.value)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "mid": self.mid.__dict__(),
            "date": self.date,
            "hook_id": self.hook_id,
            "reason": self.reason,
        }

    def __str__(self):
        return "UpdateMessageEditRejectedByHook({})".format(self.__dict__())


class UpdateDialogReadLaterChanged:
    def __init__(
            self,
            peer: Peer,
            read_later: bool
    ) -> None:
        self.peer = peer
        self.read_later = read_later

    @classmethod
    def from_api(cls, update: messaging_pb2.UpdateDialogReadLaterChanged) -> 'UpdateDialogReadLaterChanged':
        return cls(Peer.from_api(update.peer), update.read_later)

    def __dict__(self):
        return {
            "peer": self.peer.__dict__(),
            "read_later": self.read_later,
        }

    def __str__(self):
        return "UpdateDialogReadLaterChanged({})".format(self.__dict__())
