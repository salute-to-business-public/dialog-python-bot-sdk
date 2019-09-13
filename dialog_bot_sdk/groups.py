from .service import ManagedService
from dialog_api import search_pb2, groups_pb2


class Groups(ManagedService):
    """Class for handling groups

    """

    def create_group(self, title, users):
        """Create group

        :param title: title of group
        :param users: list of users
        """
        self.internal.groups.CreateGroup(groups_pb2.RequestCreateGroup(
            title=title,
            users=users,
            group_type=groups_pb2.GROUPTYPE_GROUP
        ))

    def search_group_by_shortname(self, query):
        """Find a group by shortname (substring name)

        :param query: shortname of group
        :return: group
        """
        return self.internal.search.PeerSearch(
            search_pb2.RequestPeerSearch(
                query=[
                    search_pb2.SearchCondition(
                        searchPeerTypeCondition=search_pb2.SearchPeerTypeCondition(peer_type=search_pb2.SEARCHPEERTYPE_GROUPS)
                    ),
                    search_pb2.SearchCondition(
                        searchPieceText=search_pb2.SearchPieceText(query=query)
                    )
                ]
            )
        ).groups
