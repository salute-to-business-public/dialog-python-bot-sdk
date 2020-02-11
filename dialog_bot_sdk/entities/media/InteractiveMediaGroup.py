from typing import List

from dialog_api import messaging_pb2
from google.protobuf.wrappers_pb2 import StringValue


class InteractiveMediaStyle:
    INTERACTIVEMEDIASTYLE_UNKNOWN = messaging_pb2.INTERACTIVEMEDIASTYLE_UNKNOWN
    INTERACTIVEMEDIASTYLE_DEFAULT = messaging_pb2.INTERACTIVEMEDIASTYLE_DEFAULT
    INTERACTIVEMEDIASTYLE_PRIMARY = messaging_pb2.INTERACTIVEMEDIASTYLE_PRIMARY
    INTERACTIVEMEDIASTYLE_DANGER = messaging_pb2.INTERACTIVEMEDIASTYLE_DANGER


class InteractiveMediaButton:
    def __init__(self, value: str, label: str) -> None:
        self.value = value
        self.label = label

    def to_api(self) -> messaging_pb2.InteractiveMediaButton:
        return messaging_pb2.InteractiveMediaButton(value=StringValue(value=self.value),
                                                    label=StringValue(value=self.label))

    @classmethod
    def from_api(cls, button: messaging_pb2.InteractiveMediaButton) -> 'InteractiveMediaButton':
        return cls(button.value.value, button.label)

    def __dict__(self):
        return {"value": self.value, "label": self.label}

    def __str__(self):
        return "{}".format(self.__dict__())


class InteractiveMediaSelectOption:
    def __init__(self, value: str, label: str) -> None:
        self.value = value
        self.label = label

    def to_api(self) -> messaging_pb2.InteractiveMediaSelectOption:
        return messaging_pb2.InteractiveMediaSelectOption(value=StringValue(value=self.value),
                                                          label=StringValue(value=self.label))

    @classmethod
    def from_api(cls, option: messaging_pb2.InteractiveMediaSelectOption) -> 'InteractiveMediaSelectOption':
        return cls(option.value.value, option.label.value)

    def __dict__(self):
        return {"value": self.value, "label": self.label}

    def __str__(self):
        return "{}".format(self.__dict__())


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
        return cls([InteractiveMediaSelectOption.from_api(x) for x in select.options], select.lable.value,
                   select.default_value.value)

    def __dict__(self):
        return {"options": [x.__dict__() for x in self.options.__dict__()], "label": self.label,
                "default_value": self.default_value}

    def __str__(self):
        return "{}".format(self.__dict__())


class InteractiveMediaWidget:
    def __init__(self, interactive_media_button: InteractiveMediaButton,
                 interactive_media_select: InteractiveMediaSelect) -> None:
        self.interactiveMediaButton = interactive_media_button
        self.interactiveMediaSelect = interactive_media_select

    def to_api(self) -> messaging_pb2.InteractiveMediaWidget:
        return messaging_pb2.InteractiveMediaWidget(interactiveMediaButton=self.interactiveMediaButton.to_api(),
                                                    interactiveMediaSelect=self.interactiveMediaSelect.to_api())

    @classmethod
    def from_api(cls, widget: messaging_pb2.InteractiveMediaWidget) -> 'InteractiveMediaWidget':
        return cls(InteractiveMediaButton.from_api(widget.interactiveMediaButton),
                   InteractiveMediaSelect.from_api(widget.interactiveMediaSelect))

    def __dict__(self):
        return {"interactive_media_button": self.interactive_media_button.__dict__(),
                "interactive_media_select": self.interactive_media_select.__dict__()}

    def __str__(self):
        return "{}".format(self.__dict__())


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
        return "{}".format(self.__dict__())


class InteractiveMedia:
    def __init__(self, id_: str, widget: InteractiveMediaWidget, style: InteractiveMediaStyle,
                 confirm: InteractiveMediaConfirm) -> None:
        self.id = id_
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
        return "{}".format(self.__dict__())


class InteractiveMediaTranslation:
    def __init__(self, id_: str, value: str):
        self.id = id_
        self.value = value

    def to_api(self) -> messaging_pb2.InteractiveMediaTranslation:
        return messaging_pb2.InteractiveMediaTranslation(id=StringValue(value=self.id),
                                                         value=StringValue(value=self.value))

    @classmethod
    def from_api(cls, translation: messaging_pb2.InteractiveMediaTranslation) -> 'InteractiveMediaTranslation':
        return cls(translation.id.value, translation.value.value)

    def __dict__(self):
        return {"id": self.id, "value": self.value}

    def __str__(self):
        return "{}".format(self.__dict__())


class InteractiveMediaTranslationGroup:
    def __init__(self, language: str, messages: List[InteractiveMediaTranslation]):
        self.language = language
        self.messages = messages

    def to_api(self) -> messaging_pb2.InteractiveMediaTranslationGroup:
        return messaging_pb2.InteractiveMediaTranslationGroup(language=StringValue(value=self.language),
                                                              messages=[x.to_api() for x in self.messages])

    @classmethod
    def from_api(cls, translation: messaging_pb2.InteractiveMediaTranslationGroup) -> 'InteractiveMediaTranslationGroup':
        return cls(translation.language.value, [InteractiveMediaTranslation.from_api(x) for x in translation.messages])

    def __dict__(self):
        return {"language": self.language, "messages": [x.__dict__() for x in self.messages]}

    def __str__(self):
        return "{}".format(self.__dict__())


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
        return "{}".format(self.__dict__())
