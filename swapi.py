import requests
from pprint import pprint


response = requests.get('https://swapi.dev/api/starships/9/')
print(response.json().get('name'))

# А если запросить несуществующий ключ словаря?
print(response.json().get('my_name'))
pprint(response.json())


'''response = requests.get('https://swapi.dev/api/starships/9/')

# Приведем ответ сервера к типам данных Python...
response = response.json()
# ... и напечатаем в терминале содержимое ответа сервера...
print(response)
# Напечатаем и тип данных объекта, полученного в результате преобразования:
print(type(response))'''
