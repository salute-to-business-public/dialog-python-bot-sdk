from dialog_bot_sdk.internal.bot import InternalBot
from dialog_bot_sdk.entity_manager import EntityManager


class ManagedService(object):
    """Base class for managed services.

    """
    def __init__(self, manager: EntityManager, internal: InternalBot) -> None:
        self.manager = manager
        self.internal = internal
