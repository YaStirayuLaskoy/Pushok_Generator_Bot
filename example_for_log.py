"""Тренировка в логировании."""

import logging

from logging.handlers import RotatingFileHandler


# Здесь задана глобальная конфигурация для всех логгеров
logging.basicConfig(
    level=logging.DEBUG,
    filename='program.log',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)


# В переменной __name__ хранится имя пакета;
# это же имя будет присвоено логгеру.
# Это имя будет передаваться в логи, в аргумент %(name)
logger = logging.getLogger(__name__)
# Устанавливаем уровень, с которого логи будут сохраняться в файл
logger.setLevel(logging.INFO)
# Указываем обработчик логов
handler = RotatingFileHandler('my_logger.log',
                              maxBytes=50000000,
                              backupCount=5)
logger.addHandler(handler)


logging.debug('123')  # Когда нужна отладочная информация
logging.info('Сообщение отправлено')  # Когда нужна дополнительная информация
logging.warning('Большая нагрузка!')  # Когда что-то идёт не так, но работает
logging.error('Бот не смог отправить сообщение')  # Когда что-то сломалось
logging.critical('Всё упало! Зовите админа!1!111')  # Когда всё совсем плохо


# Значения параметра filemode:
# w — содержимое файла перезаписывается при каждом запуске программы;

# x — создать файл и записывать логи в него;
# если файл с таким именем уже существует — возникнет ошибка;

# a — дописывать новые логи в конец указанного файла.
