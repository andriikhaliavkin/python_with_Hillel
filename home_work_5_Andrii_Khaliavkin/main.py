import requests
import pandas as pd

print(
    '''---------------------------------TASK 1----------------------------------------''')
# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті (дані не фейкові, оновлюються в режимі реального часу)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()['people']
pd_people = pd.DataFrame(people)
print(pd_people)

print(
    '''---------------------------------TASK 2----------------------------------------''')
# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv, london)
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране

api_key = '47503e85fabbabc93cff28c52398ae97'
city_name = input('Enter city name: ')
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
r = requests.get(url)
weather = r.json()
print(f'Temperature in {city_name.capitalize()} is {weather["main"]["temp"]} C')
print(f'Wind speed in {city_name.capitalize()} is {weather["wind"]["speed"]} m/s')
