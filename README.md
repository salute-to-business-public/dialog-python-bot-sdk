Dialog Python Bot SDK
=================
![PyPI](https://img.shields.io/pypi/v/dialog-bot-sdk.svg)

Python Bot SDK for [Dialog](https://dlg.im) messenger.

Full documentation is available [here](https://dialogs.github.io/bots-docs/).

Usage
-----

```python
from dialog_bot_sdk.bot import DialogBot
import grpc
import os


def on_msg(*params):
    bot.messaging.send_message(
        params[0].peer, 'Reply to : ' + str(params[0].message.textMessage.text)
    )


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        os.environ.get('BOT_ENDPOINT'),  # bot endpoint from environment
        grpc.ssl_channel_credentials(), # SSL credentials (empty by default!)
        os.environ.get('BOT_TOKEN')  # bot token from environment
    )

    bot.messaging.on_message(on_msg)
```

License
-------
[Apache 2.0](LICENSE)
