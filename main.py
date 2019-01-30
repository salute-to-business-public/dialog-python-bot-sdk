# coding: utf-8
from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk.interactive_media import InteractiveMedia, InteractiveMediaButton, InteractiveMediaGroup
import os


def on_msg(*params):
    print('on msg', params)
    actions = list()
    actions.append(InteractiveMedia(1, InteractiveMediaButton("button_1", "button_1")))
    actions.append(InteractiveMedia(2, InteractiveMediaButton("button_2", "button_2")))
    bot.messaging.send_message(
        params[0].peer, " ", [InteractiveMediaGroup(actions)]
    )


def on_click(*params):
    print('on click', params)


if __name__ == '__main__':
    bot = DialogBot.get_insecure_bot(
        os.environ.get('BOT_ENDPOINT'),
        os.environ.get('BOT_TOKEN')
    )

    bot.messaging.on_message(on_msg, on_click)
