import logging
import time

from aiogram import Bot, Dispatcher, executor, types

import config

with open("messages/m1.txt", "r", encoding="utf-8") as file:
    text = file.read()
text = text.split("\n\n")
# for t in text:
#     print(t)
#     print("-"*50)
# exit()

API_TOKEN = config.telegram_token

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def i_love_you(message: types.Message):
    message = await message.answer("Магия")
    for t in text:
        await message.edit_text(t)
    time.sleep(1)
    await message.edit_text("Я тебя люблю ❤")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
