import requests
import datetime
from config import open_weather_token
from pprint import pprint

def get_weather(city, open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }



    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
#        pprint(data)

        city = data["name"]
        weather_decription = data["weather"][0]["main"]
        if weather_decription in code_to_smile:
            wd = code_to_smile[weather_decription]
        else:
            wd = "Посмотри в окно, не пойму что там за погода"
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = sunrise_timestamp - sunset_timestamp

        
        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city} \nТемпература: {cur_weather}° {wd}\nВлажность: {humidity} \nДавление: {pressure} \nОщущается как: {feels_like}° \nВетер: {wind}м/с"
              f"\nВосход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}"
              f"\nХорошего дня!"
        )


    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, open_weather_token)

if __name__  == '__main__':
    main()