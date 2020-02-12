import grpc

from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk.entities.Peer import Peer, PeerType

bot = DialogBot.get_secure_bot(
    'eem.dlg.im',
    grpc.ssl_channel_credentials(),
    '0a3e368bfdde3d25972b86acca14da39a233531a'
)
