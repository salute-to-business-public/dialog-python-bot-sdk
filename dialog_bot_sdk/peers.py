from .service import ManagedService
from dialog_api import search_pb2


class Peers(ManagedService):
    """Class for handling groups

    """
    def resolve_peer(self, shortname):
        """Return OutPeer by shortname

        :param shortname: shortname (str)
        :return: OutPeer object
        """
        return self.internal.search.ResolvePeer(search_pb2.RequestResolvePeer(
                shortname=shortname
            )
        ).peer
