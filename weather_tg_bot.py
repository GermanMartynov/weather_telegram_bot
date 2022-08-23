import types
import requests 
import datetime
from bot_config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start"])
async def start_comand(message: types.Message):
    await message.reply("Привет!")

if __name__ ==  "__main__":
    executor.start_polling(dp)
    
