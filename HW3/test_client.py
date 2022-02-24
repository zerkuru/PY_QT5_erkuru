import time
import unittest
import client
import sys
import time
import logging
import log.client_log_config


CLIENT_LOGGER = log.client_log_config.LOGGER

class TestCheckPort(unittest.TestCase):
    # проверка порта
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass
    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass
    def wrongport(self):
        global CONFIGURATIONS
        CONFIGURATIONS = {
            "DEFAULT_IP_ADDRESS": "127.0.0.1",
            "DEFAULT_PORT": 78666,
            "MAX_CONNECTIONS": 5,
            "MAX_PACKAGE_LENGTH": 1024,
            "ENCODING": "utf-8"
        }
        r = client.checkport()
        self.assertEqual(r,sys.exit(1))

class TestCreatePresenceMessage():
    # проверка создания сообщения
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def testpresense(self):
        username = "IVANOV"
        r = client.create_presence_message(username)
        timeval = time.time()
        returnmessage = {"action": "presence", "time": timeval, "user": {"account_name" : username}}
        self.assertEqual(r, returnmessage)


class TestHandleResponse():
    # проверка обработки ответа
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def testresponse(self):
        message = {}
        message["time"] = ""
        message["response"] = 200
        r = client.handle_response(message)
        self.assertEqual(r, '200 : OK')

    def wrongresponse(self):
        message = {}
        message["time"] = ""
        message["response"] = 404
        r = client.handle_response(message)
        self.assertEqual(r, '400 : error')

# Запустить тестирование
if __name__ == '__main__':
    unittest.main()