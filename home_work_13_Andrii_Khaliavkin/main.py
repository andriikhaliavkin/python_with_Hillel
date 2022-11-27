# Підключіться до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ), отримайте курс валют і запишіть його в текстовий файл такому форматі (список):
#  "[дата створення запиту]"
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]


import requests
import datetime


def get_data():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.get(url)
    return response.json()


def write_data(data):
    with open("currency.txt", "w", encoding="utf-8") as file:
        file.write(f"{datetime.datetime.now()} \n")
        for i, currency in enumerate(data, 1):
            file.write(f"{i}. {currency['txt']} to UAH: {currency['rate']} \n")


if __name__ == "__main__":
    write_data(get_data())
