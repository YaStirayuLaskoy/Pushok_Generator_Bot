"""Отправка рандомной картинки."""

import requests
import os

from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')


bot = Bot(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 148537149


# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')

# Отправка изображения
bot.send_photo(chat_id, random_cat_url)


'''# Рассмотрим структуру и содержимое переменной response
print(response)

# Посмотрим, какого типа переменная response
print(type(response))

# response - это список. А какой длины?
print(len(response))

# Посмотрим, какого типа первый элемент
print(type(response[0]))'''
