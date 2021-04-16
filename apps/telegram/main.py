import logging
from aiogram import Bot, Dispatcher, executor, types
from settings import tg_token

logging.basicConfig(level=logging.INFO)

# bot and dp init
bot = Bot(tg_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    msg = message.from_user
    await message.reply(f"Hello and welcome!\n{msg}")

if __name__ == '__main__':
    executor.start_polling(dp)
