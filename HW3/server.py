import json
import sys
import socket

from utils.utils import load_configuration, get_message, send_message

CONFIGURATIONS = dict()
AUTHENTIFICATIONS = dict()


def handle_authentification(message):
    response = {
        "RESPONSE_NUMBER": 404,
        "ERROR_MESSAGE": "user not found"
    }
    if message[CONFIGURATIONS.get('USER')][CONFIGURATIONS.get('ACCOUNT_NAME')] in AUTHENTIFICATIONS:
        if AUTHENTIFICATIONS[[CONFIGURATIONS.get('USER')][CONFIGURATIONS.get('ACCOUNT_NAME')]] == \
            message[CONFIGURATIONS.get('USER')][CONFIGURATIONS.get('PASSWORD')]:
            response["RESPONSE_NUMBER"] = 202
            response["ERROR_MESSAGE"] = ""
        else:
            response["RESPONSE_NUMBER"] = 402
            response["ERROR_MESSAGE"] = "wrong login password"
    else:
        response["RESPONSE_NUMBER"] = 404
        response["ERROR_MESSAGE"] = "user not found"
    return response


def handle_message(message):
    if CONFIGURATIONS.get('ACTION') in message \
            and message[CONFIGURATIONS.get('ACTION')] == CONFIGURATIONS.get('PRESENCE') \
            and CONFIGURATIONS.get('TIME') in message \
            and CONFIGURATIONS.get('USER') in message \
            and message[CONFIGURATIONS.get('USER')][CONFIGURATIONS.get('ACCOUNT_NAME')] == 'Guest':
        return {CONFIGURATIONS.get('RESPONSE'): 200}
    elif CONFIGURATIONS.get('ACTION') in message \
             and message[CONFIGURATIONS.get('ACTION')] == CONFIGURATIONS.get('AUTHENTIFICATION') \
             and CONFIGURATIONS.get('TIME') in message \
             and CONFIGURATIONS.get('USER') in message:
        response = handle_authentification(message)
        return {
            CONFIGURATIONS.get('RESPONSE'): response.get('RESPONSE_NUMBER'),
            CONFIGURATIONS.get('ERROR'): response.get('ERROR_MESSAGE')
        }
    else:
        return {
            CONFIGURATIONS.get('RESPONSE'): 400,
            CONFIGURATIONS.get('ERROR'): 'Bad Request'
        }

def checkport():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = CONFIGURATIONS.get('DEFAULT_PORT')
        if not 65535 >= listen_port >= 1024:
            raise ValueError
    except IndexError:
        print('После -\'p\' необходимо указать порт')
        sys.exit(1)
    except ValueError:
        print(
            'Значение порта должно быть в пределах от 1024 до 65535')
        sys.exit(1)

def checkaddress():
    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''

    except IndexError:
        print(
            'После \'a\'- необходимо указать адрес для ')
        sys.exit(1)

def messageexchange():
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(CONFIGURATIONS.get('MAX_CONNECTIONS'))

    while True:
        client, client_address = transport.accept()
        try:
            message = get_message(client, CONFIGURATIONS)
            response_message = handle_message(message)
            send_message(client, response_message, CONFIGURATIONS)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента')
            client.close()



def main():
    global CONFIGURATIONS
    CONFIGURATIONS = load_configuration()
    checkport()
    checkaddress()
    messageexchange()

if __name__ == '__main__':
    main()


