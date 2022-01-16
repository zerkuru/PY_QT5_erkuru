#Создание именованного логгера;
#Сообщения лога должны иметь следующий формат: "<дата-время> <уровеньважности> <имямодуля> <сообщение>";
#Журналирование должно производиться в лог-файл;
#На стороне сервера необходимо настроить ежедневную ротацию лог-файлов.

import logging

logging.basicConfig(
    filename="server.log",
    format="%(asctime)s%(levelname)-10s%(__name__)s%(message)s",
    level=logging.INFO
)

log = logging.getLogger('client')
parms = {'host': 'www.python.org',
         'port': 80
         }
log.critical("Can't get connected to %(host)s port %(port)d", parms)

log.addHandler(logging.TimedRotatingFileHandler(filename='client.log', when='D', interval=1, backupCount=10))

