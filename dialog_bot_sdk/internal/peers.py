from dialog_api import peers_pb2


def private_peer(user_id):
    """Returns peer for user by user id

    :param user_id: user id
    :return: Peer object
    """
    return peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=user_id)


def group_peer(group_id):
    """Returns peer for group by group id

    :param group_id: group id
    :return: Peer object
    """
    return peers_pb2.Peer(type=peers_pb2.PEERTYPE_GROUP, id=group_id)


def peer_hasher(peer):
    """Returns a hash tuple of peer

    :param peer: Peer object
    :return: hash tuple
    """
    return peer.type, peer.id
