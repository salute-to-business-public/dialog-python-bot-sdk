import unittest

from dialog_api import peers_pb2
from mock import patch

from dialog_bot_sdk.entities.Avatar import Avatar
from dialog_bot_sdk.entities.Group import Group
from dialog_bot_sdk.entities.Peer import Peer, PeerType
from dialog_bot_sdk.entities.User import User
from dialog_bot_sdk.utils import AsyncTask
from tests.bot import bot
from tests.test_classes.groups import Groups
from tests.test_classes.media_and_files import MediaAndFiles, Put
from tests.test_classes.search import Search
from tests.test_classes.updates import Updates


class TestGroups(unittest.TestCase):
    group_peer = Peer(id=0, type=PeerType.PEERTYPE_GROUP)
    user1 = Peer(id=0, type=PeerType.PEERTYPE_PRIVATE)
    test_file = "../dialog_bot_sdk/examples/files/example.png"

    bot.internal.groups = Groups()
    bot.internal.search = Search()
    bot.internal.media_and_files = MediaAndFiles()
    bot.internal.updates = Updates()

    def test_create_group(self):
        group = bot.groups.create_public_group("title", "short_name")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))
        group = bot.groups.create_private_group("title")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))
        group = bot.groups.create_public_channel("title", "short_name")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))
        group = bot.groups.create_private_channel("title")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))

    def test_find_group_by_short_name(self):
        group = bot.groups.find_group_by_short_name("title")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertIsNone(group.wait())
        bot.manager.add_out_peer(peers_pb2.OutPeer(id=1, access_hash=1, type=PeerType.PEERTYPE_GROUP))
        group = bot.groups.find_group_by_short_name("short_name")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))

    def test_find_group_by_id(self):
        group = bot.groups.find_group_by_id(1)
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertIsNone(group.wait())
        bot.manager.add_out_peer(peers_pb2.OutPeer(id=1, access_hash=1, type=PeerType.PEERTYPE_GROUP))
        group = bot.groups.find_group_by_id(1)
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))

    def test_load_members(self):
        members = bot.groups.load_members(self.group_peer, 2)
        self.assertTrue(isinstance(members, AsyncTask))
        self.assertTrue(isinstance(members.wait()[0], User))

    def test_kick_user(self):
        kick = bot.groups.kick_user(self.group_peer, self.user1)
        self.assertTrue(isinstance(kick, AsyncTask))
        self.assertIsNone(kick.wait())

    def test_invite_user(self):
        invite = bot.groups.invite_user(self.group_peer, self.user1)
        self.assertTrue(isinstance(invite, AsyncTask))
        self.assertIsNone(invite.wait())

    def test_set_default_group_permissions(self):
        permissions = bot.groups.set_default_group_permissions(self.group_peer)
        self.assertTrue(isinstance(permissions, AsyncTask))
        self.assertIsNone(permissions.wait())

    def test_set_member_permissions(self):
        permissions = bot.groups.set_member_permissions(self.group_peer, self.user1)
        self.assertTrue(isinstance(permissions, AsyncTask))
        self.assertIsNone(permissions.wait())

    def test_get_group_member_permissions(self):
        permissions = bot.groups.get_group_member_permissions(self.group_peer, [self.user1])
        self.assertTrue(isinstance(permissions, AsyncTask))
        self.assertEqual(permissions.wait(), [])

    def test_edit_group_title(self):
        title = bot.groups.edit_group_title(self.group_peer, "title")
        self.assertTrue(isinstance(title, AsyncTask))
        self.assertIsNone(title.wait())

    @patch('requests.put')
    def test_edit_avatar(self, put):
        put.return_value = Put(200)
        avatar = bot.groups.edit_avatar(self.group_peer, self.test_file)
        self.assertTrue(isinstance(avatar, AsyncTask))
        self.assertTrue(isinstance(avatar.wait(), Avatar))
        put.return_value = Put(400)
        avatar = bot.groups.edit_avatar(self.group_peer, self.test_file)
        self.assertTrue(isinstance(avatar, AsyncTask))
        self.assertIsNone(avatar.wait())

    def test_remove_group_avatar(self):
        remove = bot.groups.remove_group_avatar(self.group_peer)
        self.assertTrue(isinstance(remove, AsyncTask))
        self.assertIsNone(remove.wait())

    def test_edit_group_about(self):
        about = bot.groups.edit_group_about(self.group_peer, "about")
        self.assertTrue(isinstance(about, AsyncTask))
        self.assertIsNone(about.wait())

    def test_leave_group(self):
        leave = bot.groups.leave_group(self.group_peer)
        self.assertTrue(isinstance(leave, AsyncTask))
        self.assertIsNone(leave.wait())

    def test_make_user_admin(self):
        admin = bot.groups.make_user_admin(self.group_peer, self.user1, None)
        self.assertTrue(isinstance(admin, AsyncTask))
        self.assertIsNone(admin.wait())

    def test_transfer_ownership(self):
        owner = bot.groups.transfer_ownership(self.group_peer, self.user1)
        self.assertTrue(isinstance(owner, AsyncTask))
        self.assertIsNone(owner.wait())

    def test_get_group_invite_url(self):
        url = bot.groups.get_group_invite_url(self.group_peer)
        self.assertTrue(isinstance(url, AsyncTask))
        self.assertEqual(url.wait(), "url")

    def test_get_group_invite_url_base(self):
        url = bot.groups.get_group_invite_url_base()
        self.assertTrue(isinstance(url, AsyncTask))
        self.assertEqual(url.wait(), "url")

    def test_revoke_invite_url(self):
        url = bot.groups.revoke_invite_url(self.group_peer)
        self.assertTrue(isinstance(url, AsyncTask))
        self.assertEqual(url.wait(), "url")

    def test_join_group(self):
        group = bot.groups.join_group("url")
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertTrue(isinstance(group.wait(), Group))

    def test_join_group_by_peer(self):
        group = bot.groups.join_group_by_peer(self.group_peer)
        self.assertTrue(isinstance(group, AsyncTask))
        self.assertIsNone(group.wait())


if __name__ == '__main__':
    unittest.main()
