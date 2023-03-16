import logging
import asyncio
from telegram import Bot



class Telegram(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)
        self.bot = Bot(token=self.token)

    async def send_message(self, message):
        await self.bot.sendMessage(chat_id=self.chat_id, text=message)

    def emit(self, record):
        try:
            message = self.format(record)
            asyncio.run(self.send_message(message))
            stream = self.stream
            # issue 35046: merged two stream.writes into one.
            self.flush()
        except RecursionError:  # See issue 36272
            raise
        except Exception:
            self.handleError(record)

