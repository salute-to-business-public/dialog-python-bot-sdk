from dialog_api import peers_pb2

def private_peer(user_id):
    return peers_pb2.Peer(type=peers_pb2.PEERTYPE_PRIVATE, id=user_id)

def group_peer(group_id):
    return peers_pb2.Peer(type=peers_pb2.PEERTYPE_GROUP, id=group_id)

def peer_hasher(peer):
    return (peer.type, peer.id)
