Dialog Python Bot SDK
=================

Bot SDK for [Dialog](https://dlg.im) messenger.

**Work in progress**

Usage
-----

```python
mport dotenv from 'dotenv';
import Bot, { MessageAttachment } from '@dlghq/dialog-bot-sdk';

dotenv.config();

const token = process.env.BOT_TOKEN;
if (typeof token !== 'string') {
  throw new Error('BOT_TOKEN env variable not configured');
}

const bot = new Bot({
  token,
  endpoints: ['https://grpc-test.transmit.im:9443']
});

bot.updateSubject.subscribe({
  next(update) {
    console.log('update', update);
  }
});

bot
  .onMessage(async (message) => {
    if (message.content.type === 'text') {
      // echo message with reply
      const mid = await bot.sendText(
        message.peer,
        message.content.text,
        MessageAttachment.reply(message.id)
      );

      // reply to self sent message with document
      await bot.sendDocument(message.peer, __filename, MessageAttachment.reply(mid));
    }
  })
  .toPromise()
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

```

License
-------
[Apache 2.0](LICENSE)
