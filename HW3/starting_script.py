#a) Реализовать скрипт, запускающий два клиентских приложения: на чтение чата и на запись в него.
# Уместно использовать модуль subprocess).
#b) Реализовать скрипт, запускающий указанное количество клиентских приложений.

import subprocess

def call_client():

    p = subprocess.run(['python', '-V'], stdout=subprocess.PIPE)
    print(p.stdout)