import grpc

from dialog_bot_sdk.bot import DialogBot

bot = DialogBot.get_secure_bot(
    'eem.dlg.im',
    grpc.ssl_channel_credentials(),
    '0a3e368bfdde3d25972b86acca14da39a233531a'
)