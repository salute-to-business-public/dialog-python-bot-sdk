Dialog Python Bot SDK
=================

Python Bot SDK for [Dialog](https://dlg.im) messenger.

Full documentation is available [here](https://dialogs.github.io/bots-docs/).

Usage
-----

```python
from dialog_bot_sdk.bot import DialogBot
import grpc


def on_msg(*params):
    bot.messaging.send_message(
        params[0].peer, 'Reply to : ' + str(params[0].message.textMessage.text)
    )


if __name__ == '__main__':
    bot = DialogBot.get_secure_bot(
        'grpc-test.transmit.im:9443',  # bot endpoint
        grpc.ssl_channel_credentials(), # SSL credentials (empty by default!)
        'cbb4994cabfa8d2a5bce0b5f7a44c23da943f767'  # bot token
    )

    bot.messaging.on_message(on_msg)
```

License
-------
[Apache 2.0](LICENSE)
