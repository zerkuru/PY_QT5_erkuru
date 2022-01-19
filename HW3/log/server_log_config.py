#Создание именованного логгера;
#Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
#Журналирование должно производиться в лог-файл;
#На стороне сервера необходимо настроить ежедневную ротацию лог-файлов
#
#
import sys
import os
import logging
import utils

CONFIGURATIONS = utils.load_configuration()

sys.path.append('../')

formatter = logging.formatter('%(asctime)s%(levelname)-10s%(filename)s%(message)s')
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

HANDLER = logging.StreamHandler(sys.stderr)
HANDLER.setFormatter(formatter)
HANDLER.setLevel(logging.ERROR)
L_FILE = logging.handlers.TimeRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
L_FILE.setFormatter(formatter)

LOGGER = logging.getLogger('server')
LOGGER.addHandler(HANDLER)
LOGGER.addHandler(L_FILE)
LOGGER.setLevel(CONFIGURATIONS.get('LOGGING_LEVEL', logging.DEBUG))

if __name__ = '__main__':
    LOGGER.critical("Критическая ошибка: ")
    LOGGER.error("Ошибка: ")
    LOGGER.debug("Отладочная информация: ")
    LOGGER.info("Информация: ")


