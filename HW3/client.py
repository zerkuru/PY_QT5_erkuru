import json
import sys
import socket
import time
import logging
import log.client_log_config

from utils import load_configuration, get_message, send_message, load_authentification

CONFIGURATIONS = dict()
CLIENT_LOG = log.client_log_config.LOGGER


def create_presence_message(account_name):
    message = {
        CONFIGURATIONS.get('ACTION'): CONFIGURATIONS.get('PRESENCE'),
        CONFIGURATIONS.get('TIME'): time.time(),
        CONFIGURATIONS.get('USER'): {
            CONFIGURATIONS.get('ACCOUNT_NAME'): account_name
        }
    }
    return message


def handle_response(message):
    if CONFIGURATIONS.get('RESPONSE') in message:
        if message[CONFIGURATIONS.get('RESPONSE')] == 200:
            return '200 : OK'
        return f'400 : {message[CONFIGURATIONS.get("ERROR")]}'
    CLIENT_LOG.error("Неверный ответ сервера")
    raise ValueError

def checkport():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        CLIENT_LOG.error("Неверный адрес сервера")
        server_address = CONFIGURATIONS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGURATIONS.get('DEFAULT_PORT')
    except ValueError:
        CLIENT_LOG.error("Неверный порт сервера")
        print('Порт должен быть в пределах от 1024 до 65535')
        sys.exit(1)

def messageexchange():
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    presence_message = create_presence_message('Guest')
    send_message(transport, presence_message, CONFIGURATIONS)
    try:
        response = get_message(transport, CONFIGURATIONS)
        hanlded_response = handle_response(response)
        print(f'Ответ от сервера: {response}')
        print(hanlded_response)
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOG.error("Ошибка декодирования")
        print('Ошибка декодирования сообщения')

def main():
    global CONFIGURATIONS
    CONFIGURATIONS = load_configuration(on_server=False)
    checkport()
    messageexchange()


if __name__ == '__main__':
    main()
