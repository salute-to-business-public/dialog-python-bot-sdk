from .service import ManagedService
from dialog_api import contacts_pb2, peers_pb2, users_pb2, messaging_pb2


class Users(ManagedService):
    """Class for handling users

    """

    def get_user_outpeer_by_id(self, uid):
        req = messaging_pb2.RequestLoadDialogs(
            min_date=0,
            limit=1,
            peers_to_load=[peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=uid)]
        )
        result = self.internal.messaging.LoadDialogs(req)

        for outpeer in result.user_peers:
            if outpeer.uid == uid:
                return peers_pb2.OutPeer(
                    type=peers_pb2.PEERTYPE_PRIVATE,
                    id=outpeer.uid,
                    access_hash=outpeer.access_hash
                )

    def find_user_outpeer_by_nick(self, nick):
        """Returns user's Outpeer object by nickname for direct messaging

        :param nick: user's nickname
        :return: Outpeer object of user
        """
        users = self.internal.contacts.SearchContacts(
            contacts_pb2.RequestSearchContacts(
                request=nick
            )
        ).users

        for user in users:
            if user.data.nick.value == nick:
                outpeer = peers_pb2.OutPeer(
                    type=peers_pb2.PEERTYPE_PRIVATE,
                    id=int(user.id),
                    access_hash=int(user.access_hash)
                )
                return outpeer
        return None

    def get_user_by_nick(self, nick):
        """Returns User object by nickname

        :param nick: user's nickname
        :return: User object
        """
        users = self.internal.contacts.SearchContacts(
            contacts_pb2.RequestSearchContacts(
                request=nick
            )
        ).users

        for user in users:
            if user.data.nick.value == nick:
                return user

    def get_user_full_profile_by_nick(self, nick):
        """Returns FullUser object by nickname

        :param nick: user's nickname
        :return: FullUser object
        """
        user = self.find_user_outpeer_by_nick(nick)
        full_profile = self.internal.users.LoadFullUsers(
            users_pb2.RequestLoadFullUsers(
                user_peers=[
                    peers_pb2.UserOutPeer(
                        uid=user.id,
                        access_hash=user.access_hash
                    )
                ]
            )
        )

        if full_profile:
            if hasattr(full_profile, 'full_users'):
                if len(full_profile.full_users) > 0:
                    return full_profile.full_users[0]

    def get_user_custom_profile_by_nick(self, nick):
        """Returns custom_profile field of FullUser object by nickname

        :param nick: user's nickname
        :return: user's custom profile string
        """
        full_profile = self.get_user_full_profile_by_nick(nick)

        if hasattr(full_profile, 'custom_profile'):
            return str(full_profile.custom_profile)

    def get_user_custom_profile_by_peer(self, peer):
        """Returns custom_profile field of FullUser object by Peer object

        :param peer: user's Peer object
        :return: user's custom profile string
        """
        outpeer = self.manager.get_outpeer(peer)

        full_profile = self.internal.users.LoadFullUsers(
            users_pb2.RequestLoadFullUsers(
                user_peers=[
                    peers_pb2.UserOutPeer(
                        uid=outpeer.id,
                        access_hash=outpeer.access_hash
                    )
                ]
            )
        )

        if full_profile:
            if hasattr(full_profile, 'full_users'):
                if len(full_profile.full_users) > 0:
                    if hasattr(full_profile.full_users[0], 'custom_profile'):
                        return str(full_profile.full_users[0].custom_profile)
