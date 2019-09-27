import grpc

from dialog_bot_sdk.bot import DialogBot

bot = DialogBot.get_secure_bot(
    '',
    grpc.ssl_channel_credentials(),
    ''
)