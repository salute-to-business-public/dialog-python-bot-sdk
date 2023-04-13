from typing import List, Dict

from dialog_api import messaging_pb2

from dialog_bot_sdk.entities.messaging import InteractiveMediaStyle


class InteractiveMediaLink(object):
    """Link control class.

    """
    def __init__(self, url: str, label: str = None) -> None:
        self.url = url
        self.label = label

    def render(self, target) -> None:
        """Render method for link

        :param target: target link
        """
        if self.label is not None:
            target.label.value = self.label
        target.url = self.url


class InteractiveMediaButton(object):
    """Button control class.

    """
    def __init__(self, value: str, label: str = None) -> None:
        self.value = value
        self.label = label

    def render(self, target) -> None:
        """Render method for button

        :param target: target button
        """
        if self.label is not None:
            target.label.value = self.label
        target.value = self.value


class InteractiveMediaSelect(object):
    """Select control class.

    """
    def __init__(self, options: dict, label: str = None, default_value: str = None) -> None:
        if options is None:
            raise AttributeError('Attribute \'options\' can\'t be None.')

        self.options = options
        self.label = label
        self.default_value = default_value

    def render(self, target) -> None:
        """Render method for select

        :param target: target select
        """
        if self.label is not None:
            target.label.value = self.label
        if self.default_value is not None:
            target.default_value.value = self.default_value
        for value, label in self.options.items():
            opt = target.options.add()
            opt.value = value
            opt.label = label


class InteractiveMediaConfirm(object):
    """Confirm control class.

    """
    def __init__(self, text: str = None, title: str = None, ok: str = None, dismiss: str = None) -> None:
        self.text = text
        self.title = title
        self.ok = ok
        self.dismiss = dismiss

    def render(self) -> messaging_pb2.InteractiveMediaConfirm:
        """Render method for confirm

        :return: confirm
        """
        confirm = messaging_pb2.InteractiveMediaConfirm()
        if self.text is not None:
            confirm.text.value = self.text
        if self.title is not None:
            confirm.title.value = self.title
        if self.ok is not None:
            confirm.ok.value = self.ok
        if self.dismiss is not None:
            confirm.dismiss.value = self.dismiss
        return confirm


class InteractiveMedia(object):
    """Wrapper class for interactive object styling.

    """
    # widget = InteractiveMediaButton | InteractiveMediaSelect

    def __init__(self, media_id: str,
                 widget: InteractiveMediaButton or InteractiveMediaSelect,
                 style: InteractiveMediaStyle = InteractiveMediaStyle.INTERACTIVEMEDIASTYLE_UNKNOWN,
                 confirm: InteractiveMediaConfirm = None) -> None:
        self.media_id = media_id
        self.widget = widget
        self.style = style
        self.confirm = confirm

    def render(self, target):
        """Render method for wrapped interactive object.

        :param target: target interactive object
        :return: wrapped interactive object
        """
        target.id = self.media_id
        target.style = self.style
        if self.widget is not None:
            if isinstance(self.widget, InteractiveMediaButton):
                self.widget.render(target.widget.interactiveMediaButton)
            elif isinstance(self.widget, InteractiveMediaSelect):
                self.widget.render(target.widget.interactiveMediaSelect)
            elif isinstance(self.widget, InteractiveMediaLink):
                self.widget.render(target.widget.interactiveMediaLink)
        if self.confirm is not None:
            result_confirm = self.confirm.render()
            target.confirm.text.value = result_confirm.text.value
            target.confirm.title.value = result_confirm.title.value
            target.confirm.ok.value = result_confirm.ok.value
            target.confirm.dismiss.value = result_confirm.dismiss.value

        return target


class InteractiveMediaGroup(object):
    """Wrapper class for interactive object grouping.

    """
    def __init__(self, actions: List[InteractiveMedia], title: str = None, description: str = None,
                 translations: Dict[str, dict] = None) -> None:
        if not isinstance(actions, list):
            raise AttributeError('Actions must be an iterable.')

        self.actions = actions
        self.title = title
        self.description = description
        self.translations = translations

    def render(self, target) -> None:
        """Render method for group of interactive objects.

        :param target: group of interactive objects
        """
        media = target.actions.add()
        for action in self.actions:
            act = media.actions.add()
            action.render(act)
        if self.title is not None:
            media.title.value = self.title
        if self.description is not None:
            media.description.value = self.description
        if self.translations:
            for lang, trans in self.translations.items():
                group = messaging_pb2.InteractiveMediaTranslationGroup(language=lang)
                for idx, value in trans.items():
                    group.messages.append(messaging_pb2.InteractiveMediaTranslation(id=idx, value=value))
                media.translations.append(group)
