from .service import ManagedService
from dialog_api import contacts_pb2, peers_pb2


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
