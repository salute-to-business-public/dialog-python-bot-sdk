from pytest import raises

from dialog_bot_sdk.entities.reactions import MessageReactions
from dialog_bot_sdk.reactions import Reactions
from tests.fixtures.client_entities import user_peer, mid
from tests.fixtures.internal import manager, internal


reactions = Reactions(manager, internal)


def test_get_reactions():
    assert isinstance(reactions.get_reactions(user_peer, 123), list)
    assert isinstance(reactions.get_reactions(user_peer, 123)[0], MessageReactions)
    with raises(AttributeError):
        assert reactions.get_reactions(123, 123)
    with raises(TypeError):
        assert reactions.get_reactions(user_peer, user_peer)


def test_get_message_reactions():
    assert isinstance(reactions.get_message_reactions(user_peer, mid), list)
    assert isinstance(reactions.get_message_reactions(user_peer, mid)[0], MessageReactions)
    with raises(AttributeError):
        assert reactions.get_message_reactions(mid, mid)
        assert reactions.get_message_reactions(user_peer, user_peer)


def test_set_message_reaction():
    assert reactions.set_message_reaction(user_peer, mid, "😀") is None
    with raises(AttributeError):
        assert reactions.set_message_reaction(mid, mid, "😀")
        assert reactions.set_message_reaction(user_peer, user_peer, "😀")
    with raises(TypeError):
        assert reactions.set_message_reaction(user_peer, mid, mid)


def test_remove_message_reaction():
    assert reactions.remove_message_reaction(user_peer, mid, "😀") is None
    with raises(AttributeError):
        assert reactions.remove_message_reaction(mid, mid, "😀")
        assert reactions.remove_message_reaction(user_peer, user_peer, "😀")
    with raises(TypeError):
        assert reactions.remove_message_reaction(user_peer, mid, mid)
