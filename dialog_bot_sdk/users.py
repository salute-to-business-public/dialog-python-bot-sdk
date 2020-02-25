from typing import List

from dialog_bot_sdk.entities.FullUser import FullUser
from dialog_bot_sdk.entities.ReferencedEntities import ReferencedEntities
from dialog_bot_sdk.entities.User import User
from dialog_bot_sdk.entities.Peer import PeerType, Peer
from dialog_bot_sdk.utils import async_dec
from .service import ManagedService
from dialog_api import peers_pb2, users_pb2, messaging_pb2, search_pb2, sequence_and_updates_pb2


class Users(ManagedService):
    """Class for handling users
    """
    @async_dec()
    def get_user_by_nick(self, nick: str) -> User or None:
        """return User by nickname

        :param nick: user's nickname
        :return: User
        """
        if not isinstance(nick, str):
            raise RuntimeError("Invalid input data. Expects {}, got {}.".format(str, type(nick)))
        out_peer = self.__find_out_peer_by_nick(nick)
        if out_peer.id == out_peer.access_hash == 0:
            return None

        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=[
                    peers_pb2.UserOutPeer(uid=out_peer.id, access_hash=out_peer.access_hash)
                ]
            )
        result = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request))
        for user in result.users:
            if hasattr(user.data, "nick") and user.data.nick == nick:
                return user

    @async_dec()
    def get_user_by_id(self, user_id: int) -> User or None:
        """return User by user id

        :param user_id: user's id
        :return: User or None if not found
        """
        if not isinstance(user_id, int):
            raise RuntimeError("Invalid input data. Expects {}, got {}.".format(int, type(user_id)))
        req = messaging_pb2.RequestLoadDialogs(
            min_date=0,
            limit=1,
            peers_to_load=[peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=user_id)]
        )
        result = self.internal.messaging.LoadDialogs(req)
        users_list = self.internal.updates.GetReferencedEntitites(
            sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=list(result.user_peers)
            )
        )

        for user in users_list.users:
            if hasattr(user, "id") and user.id == user_id:
                return User.from_api(user)

    @async_dec()
    def search_users_by_nick_substring(self, query: str) -> List[User]:
        """Returns list of User objects by substring of nickname (not complete coincidence!)

        :param query: user's nickname
        :return: list of Users
        """
        request = search_pb2.RequestPeerSearch(
                query=[
                    search_pb2.SearchCondition(
                        searchPeerTypeCondition=search_pb2.SearchPeerTypeCondition(
                            peer_type=search_pb2.SEARCHPEERTYPE_CONTACTS)
                    ),
                    search_pb2.SearchCondition(
                        searchPieceText=search_pb2.SearchPieceText(query=query)
                    )
                ]
            )
        user_peers = self.internal.search.PeerSearch(request).user_peers
        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=list(user_peers)
            )
        users_list = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request)).users
        result = []

        for user in users_list:
            if hasattr(user.data, "nick") and query in user.data.nick:
                result.append(user)
        return result

    @async_dec()
    def get_full_profile_by_nick(self, nick: str) -> FullUser or None:
        """return FullUser profile by nickname

        :param nick: user's nickname
        :return: FullUser
        """
        out_peer = self.__find_out_peer_by_nick(nick)
        return self.get_full_profile_by_id(out_peer.id).wait()

    @async_dec()
    def get_full_profile_by_id(self, id_: int) -> FullUser or None:
        out_peer = self.manager.get_out_peer(Peer(id_, PeerType.PEERTYPE_PRIVATE))
        if not out_peer:
            return None
        request = users_pb2.RequestLoadFullUsers(
            user_peers=[
                peers_pb2.UserOutPeer(
                    uid=out_peer.id,
                    access_hash=out_peer.access_hash
                )
            ]
        )
        full_profile = self.internal.users.LoadFullUsers(request)

        if full_profile and hasattr(full_profile, 'full_users') and len(full_profile.full_users) > 0:
            return FullUser.from_api(full_profile.full_users[0])

    def __find_out_peer_by_nick(self, nick: str) -> peers_pb2.OutPeer:
        if not isinstance(nick, str):
            raise RuntimeError("Invalid input data. Expects {}, got {}.".format(str, type(nick)))
        request = search_pb2.RequestResolvePeer(
                shortname=nick
            )
        result = self.internal.search.ResolvePeer(request)
        if hasattr(result, "peer"):
            self.manager.add_out_peer(result.peer)
            return result.peer
