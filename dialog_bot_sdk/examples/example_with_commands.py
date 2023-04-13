from time import sleep
import grpc
from dialog_bot_sdk.entities.messaging import InteractiveMediaStyle, MessageHandler, MessageContentType, CommandHandler, \
    UpdateMessage, UpdateInteractiveMediaEvent
from dialog_bot_sdk.entities.sequence_and_updates import UpdateHandler, UpdateType
from dialog_bot_sdk.entities.users import BotCommand
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


def send_text(message: UpdateMessage) -> None:
    bot.messaging.send_message_sync(message.peer, "Hi! I'm example-bot!")


def send_select(message: UpdateMessage) -> None:
    bot.messaging.send_message_sync(message.peer, "Select:", SELECT)


def send_button(message: UpdateMessage) -> None:
    bot.messaging.send_message_sync(message.peer, "Buttons:", BUTTONS)


def send_image(message: UpdateMessage) -> None:
    bot.messaging.send_image_sync(message.peer, "./files/example.png")


def send_file(message: UpdateMessage) -> None:
    bot.messaging.send_file_sync(message.peer, "./files/example.png")


def reply(message: UpdateMessage) -> None:
    bot.messaging.reply_sync(message.peer, [message.mid], "Your message?")


def update(message: UpdateMessage) -> None:
    mid = bot.messaging.send_message(message.peer, "before")
    sleep(5)
    msg = bot.messaging.get_message_by_id(mid)
    bot.messaging.update_message(msg, "after")


def create_group(message: UpdateMessage) -> None:
    command, text = bot.messaging.get_command(message)
    if text:
        group = bot.groups.create_private_group_sync(text)
        bot.groups.invite_user_sync(group.peer, message.peer)
        bot.messaging.send_message_sync(group.peer, "Welcome!")
        bot.groups.transfer_ownership_sync(group.peer, message.peer)
        bot.messaging.send_message_sync(group.peer, "Now you owner!\nBye!")
        bot.groups.leave_group_sync(group.peer)
    else:
        bot.messaging.forward_sync(
            message.peer, [message.mid], "Example for this command:\n/create_group title"
        )


def on_message(message: UpdateMessage) -> None:
    text = message.message.text_message.text
    peer = message.peer
    if peer.type == PeerType.PEERTYPE_PRIVATE:
        bot.messaging.send_message(peer, "Reply: %s" % text)
    else:
        print(message)


def on_event(event: UpdateInteractiveMediaEvent):
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

    commands = [
        BotCommand("send_text", 'Used method send_message with text "Hi! I\'m example-bot!"', "send_text"),
        BotCommand("send_select", 'Used method send_message with InteractiveMediaSelect', "send_select"),
        BotCommand("send_button", 'Used method send_message with InteractiveMediaButton', "send_button"),
        BotCommand("send_image", 'Used method send_image', "send_image"),
        BotCommand("send_file", 'Used method send_file', "send_file"),
        BotCommand("reply", 'Used method reply', "reply"),
        BotCommand("update", 'Used method send_message and before 5 sec - update_message', "update"),
        BotCommand("create_group", 'Used method create_private_group with param title', "create_group"),
    ]

    bot.messaging.command_handler([
        CommandHandler(send_text, "send_text", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(send_select, "send_select", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(send_button, "send_button", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(send_image, "send_image", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(send_file, "send_file", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(reply, "reply", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(update, "update", PeerType.PEERTYPE_PRIVATE),
        CommandHandler(create_group, "create_group", PeerType.PEERTYPE_PRIVATE),
    ])
    bot.messaging.message_handler([MessageHandler(on_message, MessageContentType.TEXT_MESSAGE)])
    bot.updates.update_handler([UpdateHandler(on_event, UpdateType.UPDATE_INTERACTIVE_MEDIA_EVENT)])
    bot.updates.on_updates()
