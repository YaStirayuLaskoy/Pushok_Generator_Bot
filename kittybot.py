"""Бот для отправки котиков и собачек."""


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
import requests
import os
import logging

from dotenv import load_dotenv


load_dotenv()

secret_token = os.getenv('TOKEN')

updater = Updater(token=secret_token)
URL = 'https://api.thecatapi.com/v1/images/search'
URL_DOG = 'https://api.thedogapi.com/v1/images/search'
URL_FOX = 'https://randomfox.ca/floof/'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def get_new_image_cat():
    """Вынимает картинку кота из API."""
    try:
        response = requests.get(URL)
    except Exception as error:
        # print(error)
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = 'https://api.thedogapi.com/v1/images/search'
        response = requests.get(new_url)

    response = response.json()
    random_cat = response[0].get('url')
    return random_cat


def get_new_image_dog():
    """Вынимает картинку собаки из API."""
    try:
        response = requests.get(URL_DOG)
    except Exception as error:
        # print(error)
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = URL
        response = requests.get(new_url)

    response = response.json()
    random_dog = response[0].get('url')
    return random_dog


def get_new_image_fox():
    """Вынимает картинку лисы из API."""
    try:
        response = requests.get(URL_FOX)
    except Exception as error:
        # print(error)
        logging.error(f'Ошибка при запросе к основному API: {error}')
        new_url = URL
        response = requests.get(new_url)

    response = response.json()
    random_fox = response.get('image')
    return random_fox


def new_cat(update, context):
    """Отправляет картинку кота."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_cat())


def new_dog(update, context):
    """Отправляет картинку собаки."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_dog())


def new_fox(update, context):
    """Отправляет картинку лисы."""
    chat = update.effective_chat
    context.bot.send_photo(chat.id, get_new_image_fox())


def wake_up(update, context):
    """/Start бота."""
    # Получаем инфу о чате, из которого пришло сообщение,
    # и сохраним в переменную chat
    chat = update.effective_chat
    name = update.message.chat.first_name

    # За счёт парметра resize_keyboard=True сделаем кнопки поменьше
    button = ReplyKeyboardMarkup([
        ['/newcat', '/newdog'],
        ['/fox'],
        # ['/hello']
    ], resize_keyboard=True)

    # В ответ на команду /start будет отправлено сообщение
    context.bot.send_message(chat_id=chat.id,
                             text='Здарова, {}! Держи пушистого'.format(name),
                             reply_markup=button)

    context.bot.send_photo(chat.id, get_new_image_cat())


def say_hi(update, context):
    """Отправляет сообщение."""
    # Получаем инфу о чате, из которого пришло сообщение,
    # и сохраним в переменную chat
    chat = update.effective_chat

    # В ответ на любое сообщение
    # будет отправлено 'Привет, я KittyBot!'
    context.bot.send_message(chat_id=chat.id,
                             text='Привет, я KittyBot!')


def main():
    """Основная логика работы бота."""
    # Регистрируется обработчик CommandHandler;
    # Он будет выбирать только сообщения с содержимым '/start'
    # и передавать их в функцию wake_up()
    updater.dispatcher.add_handler(CommandHandler('start', wake_up))

    updater.dispatcher.add_handler(CommandHandler('newcat', new_cat))

    updater.dispatcher.add_handler(CommandHandler('newdog', new_dog))

    updater.dispatcher.add_handler(CommandHandler('fox', new_fox))

    updater.dispatcher.add_handler(CommandHandler('hello', say_hi))

    # Регистрируется обработчик MessageHandler;
    # из всех полученных сообщений он будет выбирать только текстовые сообщения
    # и передавать их в функцию say_hi()
    updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

    # Метод start_polling(), запускает процесс polling,
    # приложение начнёт отправлять регулярные запросы для получения обновлений.
    updater.start_polling(poll_interval=10.0)
    # Бот будет работать до тех пор, пока не нажмёшь Ctrl+C
    updater.idle()


if __name__ == '__main__':
    main()


'''# Здесь укажите токен,
# который вы получили от @Botfather при создании бот-аккаунта
bot = Bot(token='TOKEN')
# Укажите id своего аккаунта в Telegram
chat_id = 148537149
text = 'Вам телеграмма!'
# Отправка сообщения
bot.send_message(chat_id, text)'''


'''# Кнопки
button = ReplyKeyboardMarkup([
    ['Покажи мне кота!'],
    ['Который час?', 'Определи мой ip'],
    ['/random_digit']
    ])'''
