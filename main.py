

import json
import requests
import datetime as dt
from dotenv import load_dotenv,find_dotenv
import os
from sys import platform
import time


api_response = ""
city = ""
load_dotenv(find_dotenv())

def clear_screen() -> None:
    if platform == 'win32':
        os.system("cls")
    os.system("clear")

def kelvin_to_celsius(kelvin:float) -> float:
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin:float) -> float:
    return kelvin * (9/5) + 3

# retrieve token from enviroment
def get_key() -> str:
    return f"{os.getenv('TOKEN')}"

# retrieve api data
def get_weather_data(token:str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"
    return requests.get(url)

def load_author_info() -> None:
    print("="*40)
    print("Author: John Jayson B. De Leon\nGithub: savjaylade84\nEmail: savjaylade84@gmail.com")
    print("="*40)

def get_timezone(timezone):
    temp = dt.timezone(dt.timedelta(seconds=int(timezone)))
    return dt.datetime.now(tz = temp).strftime("%I:%M %p - %m/%d/%Y") 
print("="*40)
print("Weather Terminal App")
exit = "n"

while exit == 'n':
    print("="*40)
    city = input('Enter A City Name: ').capitalize()
    print("="*40)
    api_response = get_weather_data(token = get_key())
    clear_screen()

    
    if api_response.status_code == 200:
        data = api_response.json()


        print("="*40)
        country = data["sys"]["country"]
        print(f"Country Code: {country.upper()}")
        print(f"City Name: {data['name'].upper()}")
        print("="*40)
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        print(f"Latitude: {lat}")
        print(f"Longtitude: {lon}")
        print("="*40)
        time = data["timezone"]
        sunrise = dt.datetime.fromtimestamp(data["sys"]["sunrise"] + time, dt.UTC).strftime("%I:%M %p")
        sunset = dt.datetime.fromtimestamp(data["sys"]["sunset"] + time, dt.UTC).strftime("%I:%M %p")
        timezone = get_timezone(time)
        print(f"Timezone: {timezone}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
        print("="*40)
        weather = data["weather"][0]["description"]
        print(f"Weather Status: {weather.upper()}")
        kelvin = data["main"]["temp"]
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} km/h")
        print(f"Temperature: {celsius:.0f}*C / {fahrenheit:.0f}*F")
        print("="*40)
        print("")

        print("="*40)
        exit = input('Exit Yes[y] or  No[n]: ')
        exit = exit.lower()
        print("="*40)

clear_screen()
load_author_info()
