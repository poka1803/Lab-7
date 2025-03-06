#1задание
import  requests

API_KEY ="8782d0149f22765a2c7496369ff085d4"
CITY = "Saint Petersburg"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]

    print(f"Погода в Санкт-Петербурге:")
    print(f"Описание: {weather_description}")
    print(f"Температура: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Скорость ветра: {wind_speed} м/с")
else:
    print(f"Ошибка: {response.status_code}")
#2задание
import requests

url = "https://rickandmortyapi.com/api/character"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    characters = data["results"]

    for character in characters[:7]:
        print(f"Имя: {character['name']}")
        print(f"Статус: {character['status']}")
        print(f"Последнее известное местоположение: {character['location']['name']}")
        print(f"Впервые замечен: {character['origin']['name']}")
        print(f"Фото: {character['image']}")
        print("-" * 30)
else:
    print(f"Ошибка: {response.status_code}")