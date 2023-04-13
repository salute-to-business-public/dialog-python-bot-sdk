from time import sleep
import grpc
from dialog_bot_sdk.entities.messaging import InteractiveMediaStyle, MessageHandler, MessageContentType, \
    UpdateMessage, UpdateInteractiveMediaEvent
from dialog_bot_sdk.entities.sequence_and_updates import UpdateHandler, UpdateType
from dialog_bot_sdk.interactive_media import InteractiveMediaGroup, InteractiveMedia, InteractiveMediaSelect, \
    InteractiveMediaButton
from dialog_bot_sdk.bot import DialogBot
from dialog_bot_sdk.entities.peers import PeerType


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


def on_message(message: UpdateMessage) -> None:
    text = message.message.text_message.text
    peer = message.peer
    if peer.type == PeerType.PEERTYPE_PRIVATE:
        if text == "/send_text":
            bot.messaging.send_message_sync(peer, "Hi! I'm example-bot!")
        elif text == "/send_select":
            bot.messaging.send_message_sync(peer, "Select:", SELECT)
        elif text == "/send_button":
            bot.messaging.send_message_sync(peer, "Buttons:", BUTTONS)
        elif text == "/send_image":
            bot.messaging.send_image_sync(peer, "./files/example.png")
        elif text == "/send_file":
            bot.messaging.send_file_sync(peer, "./files/example.png")
        elif text == "/reply":
            bot.messaging.reply_sync(peer, [message.mid], "Your message?")
        elif text == "/update":
            mid = bot.messaging.send_message_sync(peer, "before")
            sleep(5)
            msg = bot.messaging.get_message_by_id_sync(mid)
            bot.messaging.update_message_sync(msg, "after")
        elif text.startswith("/create_group"):
            command, text = bot.messaging.get_command(message)
            if text:
                group = bot.groups.create_private_group_sync(text)
                bot.groups.invite_user_sync(group.peer, peer)
                bot.messaging.send_message_sync(group.peer, "Welcome!")
                bot.groups.transfer_ownership_sync(group.peer, peer)
                bot.messaging.send_message_sync(group.peer, "Now you owner!\nBye!")
                bot.groups.leave_group_sync(group.peer)
            else:
                bot.messaging.forward_sync(
                    peer, [message.mid], "Example for this command:\n/create_group title"
                )
        else:
            bot.messaging.send_message_sync(peer, "Reply: %s" % text)
    else:
        print(message)


def on_event(event: UpdateInteractiveMediaEvent) -> None:
    peer = event.peer
    id = event.id
    value = event.value
    if id == "select_id":
        bot.messaging.send_message_sync(peer, "selected {}".format(value))
    elif id == "button_yes":
        bot.messaging.send_message_sync(peer, "Okey!")
    elif id == "button_no":
        bot.messaging.send_message_sync(peer, "Why not? :(")


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'endpoint',                                 # bot endpoint
        grpc.ssl_channel_credentials(),             # SSL credentials (empty by default!)
        'token'                                     # bot token
    )

    bot.messaging.message_handler([MessageHandler(on_message, MessageContentType.TEXT_MESSAGE)])
    bot.updates.update_handler([UpdateHandler(on_event, UpdateType.UPDATE_INTERACTIVE_MEDIA_EVENT)])
    bot.updates.on_updates()
