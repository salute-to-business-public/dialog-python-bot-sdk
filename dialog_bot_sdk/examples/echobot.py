from dialog_bot_sdk.bot import DialogBot
import grpc
import os


def on_msg(*params):
    message = bot.messaging.send_message(
        params[0].peer, 'Reply to : ' + str(params[0].message.textMessage.text)
    )


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'eem.dlg.im:443',  # bot endpoint
        grpc.ssl_channel_credentials(),  # SSL credentials (empty by default!)
        'e60137c00345e62ea8a21506cfe31b2be10852ec'  # bot token
    )

    bot.messaging.on_message(on_msg)
