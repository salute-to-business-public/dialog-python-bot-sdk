import grpc

from dialog_bot_sdk.bot import DialogBot

bot = DialogBot.get_secure_bot(
    'endpoint',
    grpc.ssl_channel_credentials(),
    'token'
)
