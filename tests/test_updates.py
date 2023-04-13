from dialog_api.sequence_and_updates_pb2 import ResponseGetDifference
from pytest import raises

from dialog_bot_sdk.updates import Updates
from tests.fixtures.internal import manager, internal


updates = Updates(manager, internal)


def test_get_difference():
    assert isinstance(updates.get_difference(0), ResponseGetDifference)
    with raises(TypeError):
        assert updates.get_difference("0")


def test_get_state():
    assert isinstance(updates.get_state(), int)
