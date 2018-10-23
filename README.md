Dialog Python Bot SDK
=================

Bot SDK for [Dialog](https://dlg.im) messenger.

**Work in progress**

Usage
-----

```python
from dialog_bot_sdk.bot import DialogBot
import os

def on_msg(*params):
    print('on msg', params)
    d.messaging.send_message(
        params[0].peer, str(params[0].message.textMessage.text)
    )


if __name__ == '__main__':
    d = DialogBot.get_insecure_bot(
        "grpc-test.transmit.im:8080", os.environ.get('BOT_TOKEN')
    )

    def receiver():
        d.messaging.on_message(on_msg)

    receiver()

```

License
-------
[Apache 2.0](LICENSE)
