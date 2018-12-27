from dialog_bot_sdk.bot import DialogBot
import grpc
import os


def on_msg(*params):
    print('on msg', params)
    d.messaging.send_message(
        params[0].peer, str(params[0].message.textMessage.text)
    )


if __name__ == '__main__':
    d = DialogBot.get_secure_bot(
        'grpc-test.transmit.im:8080',  # bot endpoint
        grpc.ssl_channel_credentials(),  # SSL credentials
        os.environ.get('BOT_TOKEN')  # bot token
    )

    d.messaging.on_message(on_msg)
