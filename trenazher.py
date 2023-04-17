"""Задание для тренажёра."""
import os

from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

secret_token = os.getenv('TOKEN')


# Добавьте токен в код (не делайте так в реальных проектах!)
TELEGRAM_TOKEN = secret_token
CHAT_ID = '148537149'  # Укажите chat_id

bot = Bot(token=TELEGRAM_TOKEN)


def send_message(message):
    """Просто отправка сообщения пользователю."""
    bot.send_message(CHAT_ID, message)


# Вызовите функцию здесь
send_message('Я тренажёр')
