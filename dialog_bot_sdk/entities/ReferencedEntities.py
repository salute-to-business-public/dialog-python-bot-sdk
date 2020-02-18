from typing import List

from dialog_api import sequence_and_updates_pb2

from dialog_bot_sdk.entities.Group import Group
from dialog_bot_sdk.entities.User import User
from dialog_bot_sdk.entities.message.Message import Message


class ReferencedEntities:
    def __init__(self, users: List[User], groups: List[Group], messages: List[Message]) -> None:
        self.users = users
        self.groups = groups
        self.messages = messages

    @classmethod
    def from_api(cls, entities: sequence_and_updates_pb2.RequestGetReferencedEntitites) -> 'ReferencedEntities':
        return cls([User.from_api(x) for x in entities.users], [Group.from_api(x) for x in entities.groups],
                   [Message.from_api(x) for x in entities.messages])
