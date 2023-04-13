from typing import List

from dialog_bot_sdk.entities.definitions import UUID
from dialog_api.search_pb2 import RequestSimpleSearch, SimpleSearchCondition, SimpleUserProfileSearchCondition, \
    RequestResolvePeer
from dialog_api.users_pb2 import RequestLoadUserData

from dialog_bot_sdk.utils import async_dec
from .entities.peers import Peer, PeerType
from .entities.sequence_and_updates import ReferencedEntities
from .entities.users import User, FullUser
from .service import ManagedService
from dialog_api import peers_pb2, users_pb2, search_pb2, sequence_and_updates_pb2


class Users(ManagedService):
    """Class for handling users
    """
    @async_dec()
    def get_user_by_nick(self, nick: str) -> User or None:
        """return User by nickname

        :param nick: user's nickname
        :return: User
        """
        request = RequestResolvePeer(
            shortname=nick
        )
        out_peer = self.internal.search.ResolvePeer(request).peer
        users = []
        if out_peer.id != 0:
            self.manager.add_out_peer(
                peers_pb2.OutPeer(id=out_peer.id, access_hash=out_peer.access_hash, type=peers_pb2.PEERTYPE_PRIVATE))
            request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
                users=[peers_pb2.UserOutPeer(uid=out_peer.id, access_hash=out_peer.access_hash)]
            )

            users = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request)).users

        for user in users:
            if user.data.nick == nick:
                return user

        request = RequestSimpleSearch(
            criteria=[
                SimpleSearchCondition(
                    userProfile=SimpleUserProfileSearchCondition(
                        query_string=nick
                    )
                )
            ]
        )

        out_peers = self.internal.search.SimpleSearch(request).user_out_peers

        for out_peer in out_peers:
            self.manager.add_out_peer(peers_pb2.OutPeer(id=out_peer.uid, access_hash=out_peer.access_hash, type=peers_pb2.PEERTYPE_PRIVATE))

        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            users=out_peers
        )

        users = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request)).users
        for user in users:
            if user.data.nick == nick:
                return user

    def get_user_by_nick_sync(self, nick: str) -> User or None:
        return self.get_user_by_nick.__wrapped__(self, nick)

    @async_dec()
    def get_user_by_id(self, user_id: int) -> User or None:
        """return User by user id. Found user in p2p chats.

        :param user_id: user's id
        :return: User or None if not found
        """
        if not isinstance(user_id, int):
            raise RuntimeError("Invalid input data. Expects {}, got {}.".format(int, type(user_id)))

        request = RequestLoadUserData(
            claims=[
                RequestLoadUserData.Claim(
                    user_peer=peers_pb2.Peer(id=user_id, type=PeerType.PEERTYPE_PRIVATE),
                    p2p=True
                ),
            ]
        )

        response = self.internal.users.LoadUserData(request).users

        if response:
            return User.from_api(response[0])

    def get_user_by_id_sync(self, user_id: int) -> User or None:
        return self.get_user_by_id.__wrapped__(self, user_id)

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

    def search_users_by_nick_substring_sync(self, query: str) -> List[User]:
        return self.search_users_by_nick_substring.__wrapped__(self, query)

    @async_dec()
    def get_full_profile_by_nick(self, nick: str) -> FullUser or None:
        """return FullUser profile by nickname

        :param nick: user's nickname
        :return: FullUser
        """
        user = self.get_user_by_nick_sync(nick)
        if user:
            return self.get_full_profile_by_id_sync(user.peer.id)

    def get_full_profile_by_nick_sync(self, nick: str) -> FullUser or None:
        return self.get_full_profile_by_nick.__wrapped__(self, nick)

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

    def get_full_profile_by_id_sync(self, id_: int) -> FullUser or None:
        return self.get_full_profile_by_id.__wrapped__(self, id_)

    @async_dec()
    def get_users_by_personnel_number(self, personnel_number: str) -> List[User]:
        request = RequestSimpleSearch(
            criteria=[
                SimpleSearchCondition(
                    userProfile=SimpleUserProfileSearchCondition(
                        query_string=personnel_number
                    )
                )
            ]
        )

        out_peers = self.internal.search.SimpleSearch(request).user_out_peers

        for out_peer in out_peers:
            self.manager.add_out_peer(peers_pb2.OutPeer(id=out_peer.uid, access_hash=out_peer.access_hash, type=peers_pb2.PEERTYPE_PRIVATE))

        request = sequence_and_updates_pb2.RequestGetReferencedEntitites(
            users=out_peers
        )

        users = ReferencedEntities.from_api(self.internal.updates.GetReferencedEntitites(request)).users
        result = []
        for user in users:
            if user.data.custom_profile.get("employee_number") == personnel_number:
                result.append(user)
        return result

    def get_users_by_personnel_number_sync(self, personnel_number: str) -> List[User]:
        return self.get_users_by_personnel_number.__wrapped__(self, personnel_number)

    @async_dec()
    def get_user(
            self, user_id: int, group_id: int = None, message_id: UUID = None, p2p: bool = None, contact: bool = None
    ) -> User or None:
        """
        return User by user_id and group_id or message_id or from p2p

        :param user_id: user's id
        :param group_id: group's id
        :param message_id: message id sending of searching user
        :param p2p: is searching in p2p?
        :param contact: is searching in contacts?
        :return: User
        """
        count_params = 0

        for param in (group_id, message_id, p2p, contact):
            if param is not None:
                count_params += 1

        if count_params == 0 or count_params > 1:
            raise ValueError(
                "must be only one parameter (group_id, message_id, p2p, contact) with user_id for search user"
            )

        request = RequestLoadUserData(
            claims=[
                RequestLoadUserData.Claim(
                    user_peer=peers_pb2.Peer(id=user_id, type=peers_pb2.PEERTYPE_PRIVATE),
                    message_sender=message_id.to_api() if message_id is not None else None,
                    group_member=peers_pb2.Peer(id=group_id, type=peers_pb2.PEERTYPE_GROUP) if group_id is not None else None,
                    p2p=p2p if p2p is not None else None,
                    contact=contact if contact is not None else None,
                ),
            ]
        )
        result = self.internal.users.LoadUserData(request).users
        for user in result:
            self.manager.add_out_peer(
                peers_pb2.OutPeer(
                    id=user.id,
                    type=peers_pb2.PEERTYPE_PRIVATE,
                    access_hash=user.access_hash
                )
            )
        if result:
            return User.from_api(result[0])

    def get_user_sync(
            self, user_id: int, group_id: int = None, message_id: UUID = None, p2p: bool = None, contact: bool = None
    ) -> User or None:
        return self.get_user.__wrapped__(self, user_id, group_id, message_id, p2p, contact)
