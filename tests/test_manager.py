import unittest

from dialog_api import contacts_pb2, peers_pb2, messaging_pb2
from dialog_api.peers_pb2 import PEERTYPE_PRIVATE, PEERTYPE_GROUP
from mock import patch

from tests.bot import bot
from tests.fake_classes import FakeDialog, FakeOutpeer
from dialog_bot_sdk import entity_manager


class TestManager(unittest.TestCase):

    user_out_peer = peers_pb2.UserOutPeer(uid=0, access_hash=0)
    group_out_peer = peers_pb2.GroupOutPeer(group_id=1, access_hash=-1)
    out_peer = peers_pb2.OutPeer(id=0, access_hash=0)
    peer = peers_pb2.Peer(type=PEERTYPE_PRIVATE, id=0)
    group_peer = peers_pb2.Peer(type=PEERTYPE_GROUP, id=1)

    @patch('dialog_bot_sdk.entity_manager.EntityManager.adopt_peer')
    @patch('dialog_bot_sdk.entity_manager.EntityManager._get_contacts')
    def test_bootstrap(self, contacts, peer):
        contacts.return_value = FakeDialog()
        entity_manager.EntityManager(bot.internal)
        self.assertTrue(isinstance(contacts.call_args.args[0], contacts_pb2.RequestGetContacts))
        self.assertTrue(isinstance(peer.call_args.args[0], FakeOutpeer))

    def test_adopt_peer(self):
        manager = entity_manager.EntityManager(bot.internal)
        manager.adopt_peer(self.user_out_peer)
        manager.adopt_peer(self.group_out_peer)
        self.assertTrue(isinstance(manager.peers_to_outpeers[(1, 0)], peers_pb2.OutPeer))
        self.assertEqual(manager.peers_to_outpeers[(1, 0)].type, 1)
        self.assertTrue(isinstance(manager.peers_to_outpeers[(2, 1)], peers_pb2.OutPeer))
        self.assertEqual(manager.peers_to_outpeers[(2, 1)].type, 2)
        with self.assertRaises(RuntimeError):
            manager.adopt_peer("no_peer")

    @patch('dialog_bot_sdk.entity_manager.EntityManager._load_dialogs')
    def test_get_outpeer(self, load):
        manager = entity_manager.EntityManager(bot.internal)

        self.assertEqual(self.out_peer, manager.get_outpeer(self.out_peer))

        load.return_value = FakeDialog(user_peers=[self.user_out_peer], group_peers=[self.group_out_peer])

        self.assertTrue(isinstance(manager.get_outpeer(self.peer), peers_pb2.OutPeer))
        self.assertTrue(isinstance(manager.get_outpeer(self.group_peer), peers_pb2.OutPeer))
        self.assertTrue(isinstance(load.call_args.args[0], messaging_pb2.RequestLoadDialogs))




if __name__ == '__main__':
    unittest.main()
