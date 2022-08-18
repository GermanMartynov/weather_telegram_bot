import requests                         # простая и элегантная HTML библиотека для людей
from pprint import pprint               # печать красиво отформатированного jsom 
from config import open_weather_token   # импорт токена от API openweather из файла congig.py
from datetime import datetime           

def get_weather(city, token):

    weather_discriptions = {
        "Clear":    "Ясно \U00002600",
        "Clouds":   "Облачно \U00002601", 
        "Rain":     "Дождь \U00002614",
        "Drizzle":  "Дождь \U00002614",
        "Snow":     "Снег \U0001F328"
    }

    try:
        r = requests.get(   # получаем ответ на GET запрос строкой ниже
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"
            #   или можно так так:
            #   r = request.get(
            #       "https://api.openweathermap.org/data/2.5/weather", 
            #       params={"q":city, "appid":token, "units":"metric"}
            #   )
            
        )
        data = r.json()     # кодируем ответ в формат json
        pprint(data)        # печать красиво отформатированного jsom 

        sunset_date = datetime.fromtimestamp(data["sys"]["sunset"]).date()
        sunset_time = datetime.fromtimestamp(data["sys"]["sunset"]).time()
        sunrise_time = datetime.fromtimestamp(data["sys"]["sunrise"]).time()

        wd = data["weather"][0]["main"]     # получаем описание погоды
        if wd in weather_discriptions:      # если оно есть в нашем словаре состояний
            wd = weather_discriptions[wd]   # присваиваем значение из словаря
        else:                                   # иначе
            wd = "Сам посмотри что за погода!"  # лепим отмазку

        temp = data["main"]["temp"]
       
        print( f"*** {city} {sunset_date}***\n"
            f"{wd}\n"
            f"Температура {temp} C°\n"
            f"Время рассвета: {sunrise_time}\n"
            f"Время заката: {sunset_time}\n"
            )

    except Exception as ex:
            print(ex)
            print("")

def main():
    city = input("Ведите город: ")
    get_weather(city, open_weather_token)
    

if __name__ == "__main__":      # если файл запускается в качестве приложения выполняем:
    print(f"start {__name__}")
    main()

