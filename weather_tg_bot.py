import types
import requests 
import datetime
from bot_config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint               # печать красиво отформатированного jsom 

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot=bot)

#@dp.message_handler(commands=["start"])
#async def start_comand(message: types.Message):
#    await message.reply("Привет! Напиши название города и я пришлю информацию о погоде.")


@dp.message_handler()
async def get_weather(message: types.Message):
    weather_discriptions = {
        "Clear":    "Ясно \U00002600",
        "Clouds":   "Облачно \U00002601", 
        "Rain":     "Дождь \U00002614",
        "Drizzle":  "Дождь \U00002614",
        "Snow":     "Снег \U0001F328"
    }

    try:
        r = requests.get(   # получаем ответ на GET запрос строкой ниже
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric"
            )

        data = r.json()     # кодируем ответ в формат json
        # pprint(data)        # печать красиво отформатированного jsom 

        city = data["name"]
        sunset_date = datetime.fromtimestamp(data["sys"]["sunset"]).date()
        sunset_time = datetime.fromtimestamp(data["sys"]["sunset"]).time()
        sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"]).time()

        wd = data["weather"][0]["main"]     # получаем описание погоды
        if wd in weather_discriptions:      # если оно есть в нашем словаре состояний
            wd = weather_discriptions[wd]   # присваиваем значение из словаря
        else:                                   # иначе
            wd = "Сам посмотри что за погода!"  # лепим отмазку

        temp = data["main"]["temp"]
       
        await message.reply( f"*** {city} {sunset_date}***\n"
            f"{wd}\n"
            f"Температура {temp} C°\n"
            f"Время рассвета: {sunrise_time}\n"
            f"Время заката: {sunset_time}\n"
            )

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ ==  "__main__":
    executor.start_polling(dp)

