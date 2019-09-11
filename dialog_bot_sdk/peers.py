from .service import ManagedService
from dialog_api import search_pb2, peers_pb2, users_pb2, messaging_pb2, groups_pb2
import random
import google.protobuf


class Peers(ManagedService):
    """Class for handling groups

    """
    def resolve_peer(self, shortname):
        """peer by shortname

        :param shortname: shortname (str)
        :return: peer
        """
        return self.internal.search.ResolvePeer(search_pb2.RequestResolvePeer(
                shortname=shortname
            )
        ).peer
