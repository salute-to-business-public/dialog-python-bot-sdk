from time import sleep

from dialog_bot_sdk.entities.media.InteractiveMediaGroup import InteractiveMediaStyle
from dialog_bot_sdk.interactive_media import InteractiveMediaGroup, InteractiveMedia, InteractiveMediaSelect, \
    InteractiveMediaConfirm, InteractiveMediaButton

from dialog_bot_sdk.bot import DialogBot
import grpc

from dialog_bot_sdk.entities.Peer import PeerType
from dialog_bot_sdk.entities.media.ImageMedia import ImageLocation
from dialog_bot_sdk.entities.media.WebpageMedia import WebPageMedia
from dialog_bot_sdk.entities.message.TextMessage import MessageMedia


SELECT = [
    InteractiveMediaGroup(
        [
            InteractiveMedia(
                "select_id",
                InteractiveMediaSelect({"Yes": "yes", "No": "no"}, "default", "choose"),
                InteractiveMediaStyle.INTERACTIVEMEDIASTYLE_DANGER,
            )
        ]
    )
]
BUTTONS = [
    InteractiveMediaGroup(
        [
            InteractiveMedia(
                "button_yes",
                InteractiveMediaButton("yes", "Yes"),
                InteractiveMediaStyle.INTERACTIVEMEDIASTYLE_PRIMARY,
            ),
            InteractiveMedia(
                "button_no",
                InteractiveMediaButton("no", "No"),
                InteractiveMediaStyle.INTERACTIVEMEDIASTYLE_PRIMARY,
            )
        ]
    )
]


def on_msg(params):
    text = params.message.text_message.text
    peer = params.peer
    if peer.type == PeerType.PEERTYPE_PRIVATE:
        if text == "send text":
            bot.messaging.send_message(peer, "Hi! I'm example-bot!")
        elif text == "send select":
            bot.messaging.send_message(peer, "Select:", SELECT)
        elif text == "send button":
            bot.messaging.send_message(peer, "Buttons:", BUTTONS)
        elif text == "send image":
            bot.messaging.send_image(peer, "./files/example.png")
        elif text == "send file":
            bot.messaging.send_file(peer, "./files/example.png")
        elif text == "send media":
            image_location = ImageLocation(bot.internal.uploading.upload_file("./files/example.png"),
                                           200, 50, 1337)
            media = MessageMedia()
            media.web_page = WebPageMedia("url", "title", "description", image_location)
            bot.messaging.send_media(peer, [media])
        elif text == "reply":
            bot.messaging.reply(peer, [params.mid], "Your message?")
        elif text == "update":
            mid = bot.messaging.send_message(peer, "before")
            msg = bot.messaging.get_messages_by_id([mid])
            sleep(5)
            bot.messaging.update_message(msg, "after")
        elif text.startswith("create group"):
            gr = text.split(' ')
            if len(gr) == 4:
                group = bot.groups.create_public_group(gr[2], gr[3])
                bot.groups.invite_user(group, peer).wait()
                bot.messaging.send_message(group, "Welcome!")
                bot.groups.transfer_ownership(group, peer).wait()
                bot.messaging.send_message(group, "Now you owner!\nBye!")
                bot.groups.leave_group(group)
            else:
                bot.messaging.forward(peer, [params.mid], "Example for this command:\ncreate group title short_name")
        else:
            bot.messaging.send_message(peer, "Reply: {}".format(text))
    else:
        print(params)


def on_event(params):
    peer = params.peer
    id = params.id
    value = params.value
    if id == "select_id":
        bot.messaging.send_message(peer, "selected {}".format(value))
    elif id == "button_yes":
        bot.messaging.send_message(peer, "Okey!")
    elif id == "button_no":
        bot.messaging.send_message(peer, "Why not? :(")


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'eem.dlg.im:443',                           # bot endpoint
        grpc.ssl_channel_credentials(),             # SSL credentials (empty by default!)
        '072e0743ce68189fdde6aa6944c0fcde86c4b73a'  # bot token
    )

    bot.messaging.on_message_async(on_msg, on_event)
