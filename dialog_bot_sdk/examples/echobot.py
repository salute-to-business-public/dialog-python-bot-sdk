from dialog_bot_sdk.bot import DialogBot
import grpc
import os


def on_msg(*params):
    print('on msg', params)
    bot.messaging.send_message(
        params[0].peer, 'Reply to : ' + str(params[0].message.textMessage.text)
    )


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'grpc-test.transmit.im:9443',  # bot endpoint
        grpc.ssl_channel_credentials(),  # SSL credentials (empty by default!)
        os.environ.get('BOT_TOKEN')  # bot token
    )

    bot.messaging.on_message(on_msg)
