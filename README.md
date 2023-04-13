Python Bot SDK
=================
Бот сдк на python для Dialog Messanger.

Usage
-----

```python
from dialog_bot_sdk.bot import DialogBot
import grpc
import os
from dialog_bot_sdk.entities.messaging import UpdateMessage, MessageHandler, MessageContentType


def on_message(message: UpdateMessage) -> None:
    bot.messaging.send_message(
        message.peer, 'Reply to : ' + str(message.message.text_message.text)
    )


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        os.environ.get("ENDPOINT"),      # bot endpoint
        grpc.ssl_channel_credentials(),  # SSL credentials (empty by default!)
        os.environ.get("TOKEN"),         # bot token
        **os.environ.get('BOT_OPTIONS') if os.environ.get('BOT_OPTIONS') is not None else {}
    )

    bot.messaging.message_handler(MessageHandler(on_message, MessageContentType.TEXT_MESSAGE))
    bot.updates.on_updates()

```

Больше примеров в папке dialog_bot_sdk/examples