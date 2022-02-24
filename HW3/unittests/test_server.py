import unittest
import server
import sys

# Модульные тесты

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
            "DEFAULT_PORT": 1000,
            "MAX_CONNECTIONS": 5,
            "MAX_PACKAGE_LENGTH": 1024,
            "ENCODING": "utf-8"
        }
        r = server.checkport()
        self.assertEqual(r,sys.exit(1))

class TestHandleAuthentification(unittest.TestCase):
    # проверка аутентификации
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def nouser(self):
        message = {}
        message["user"] = "Vassman"
        message["password"] = "12345"
        r = server.handle_authentification(message)
        self.assertEqual(r, {"RESPONSE_NUMBER": 404, "ERROR_MESSAGE": "user not found"})

    def wronglogin(self):
        message = {}
        message["user"] = "IVANOV"
        message["password"] = "12345"
        r = server.handle_authentification(message)
        self.assertEqual(r, {"RESPONSE_NUMBER": 402, "ERROR_MESSAGE": "wrong login password"})

    def correctentrance(self):
        message = {}
        message["user"] = "IVANOV"
        message["password"] = "7777"
        r = server.handle_authentification(message)
        self.assertEqual(r, {"RESPONSE_NUMBER": 202, "ERROR_MESSAGE": ""})

class TestHandleMessage(unittest.TestCase):
    # проверка аутентификации
    def setUp(self):
        # Выполнить настройку тестов (если необходимо)
        pass

    def tearDown(self):
        # Выполнить завершающие действия (если необходимо)
        pass

    def testcorrectpresense(self):
        message = {}
        message["time"] = ""
        message["user"] = "Guest"
        message["password"] = ""
        message["action"] = "presence"
        r = server.handle_message(message)
        self.assertEqual(r, {"response": 200})

    def testcorrectauth(self):
        message = {}
        message["time"] = ""
        message["user"] = "Guest"
        message["password"] = ""
        message["action"] = "authenticate"
        r = server.handle_message(message)
        self.assertEqual(r, {"response": 202, "error": ""})

    def testbadrequest(self):
        message = {}
        message["password"] = ""
        message["action"] = "authenticate"
        r = server.handle_message(message)
        self.assertEqual(r, {"response": 400, "error": "Bad Request"})


# Запустить тестирование
if __name__ == '__main__':
    unittest.main()