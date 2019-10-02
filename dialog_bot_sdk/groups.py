from google.protobuf import wrappers_pb2

from .service import ManagedService
from dialog_api import search_pb2, groups_pb2


class Groups(ManagedService):
    """Class for handling groups

    """

    def create_group(self, title, username, users=None):
        """Create group

        :param title: title of group
        :param username: group name
        :param users: list of UserOutPeer's objects
        """
        if users is None:
            users = []
        request = groups_pb2.RequestCreateGroup(
            title=title,
            username=wrappers_pb2.StringValue(value=username),
            users=users,
            group_type=groups_pb2.GROUPTYPE_GROUP
        )
        self._create_group(request)

    def find_group_by_shortname(self, query):
        """Find a groups by shortname (substring name)

        :param query: shortname of group
        :return: groups list
        """
        request = search_pb2.RequestPeerSearch(
            query=[
                search_pb2.SearchCondition(
                    searchPeerTypeCondition=search_pb2.SearchPeerTypeCondition(peer_type=search_pb2.SEARCHPEERTYPE_GROUPS)
                ),
                search_pb2.SearchCondition(
                    searchPieceText=search_pb2.SearchPieceText(query=query)
                )
            ]
        )
        return self._peer_search(request).groups

    def _create_group(self, request):
        self.internal.groups.CreateGroup(request)

    def _peer_search(self, request):
        return self.internal.search.PeerSearch(request)
