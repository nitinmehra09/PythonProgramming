import requests
from tkinter import Tk, Label, Entry, Button
api_key : str = '931f1ba3e0d7f247497443716f8fd4e2'

user_input = input("Enter city : ")

weather_data =requests.get( f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")


if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])


print(f"The weather in {user_input}  is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºF")