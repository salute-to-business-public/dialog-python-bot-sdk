from .service import ManagedService
from dialog_api import contacts_pb2, peers_pb2, users_pb2


class Users(ManagedService):
    def find_user_outpeer_by_nick(self, nick):
        users = self.internal.contacts.SearchContacts(
            contacts_pb2.RequestSearchContacts(
                request=nick
            )
        ).users

        for user in users:
            if user.nick.value == nick:
                outpeer = peers_pb2.OutPeer(
                    type=peers_pb2.PEERTYPE_PRIVATE,
                    id=int(user.id),
                    access_hash=int(user.access_hash)
                )
                return outpeer
        return None

    def get_user_by_nick(self, nick):
        users = self.internal.contacts.SearchContacts(
            contacts_pb2.RequestSearchContacts(
                request=nick
            )
        ).users

        for user in users:
            if user.nick.value == nick:
                return user

    def get_user_full_profile(self, nick):
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

    def get_user_custom_profile(self, nick):
        full_profile = self.get_user_full_profile(nick)

        if hasattr(full_profile, 'custom_profile'):
            return str(full_profile.custom_profile)
