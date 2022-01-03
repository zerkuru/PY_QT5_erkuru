import json
import os
import sys

def load_authentification(on_server=True):
    if not os.path.exists('auth.json'):
        print('Не найден файл аутентификации')
        sys.exit(True)
    with open('auth.json') as auth_file:
        AUTHENTIFICATIONS = json.load(auth_file)
    return AUTHENTIFICATIONS

def load_configuration(on_server=True):
    configuration_keys = [
        'DEFAULT_PORT',
        'MAX_CONNECTIONS',
        'MAX_PACKAGE_LENGTH',
        'ENCODING',
        'ACTION',
        'TIME',
        'USER',
        'ACCOUNT_NAME',
        'PRESENCE',
        'RESPONSE',
        'ERROR'
    ]
    if not on_server:
        configuration_keys.append('DEFAULT_IP_ADDRESS')
    if not os.path.exists('config.json'):
        print('Не найден файл конфигурации')
        sys.exit(True)
    with open('config.json') as configuration_file:
        CONFIGURATIONS = json.load(configuration_file)
    loaded_configuration_keys = list(CONFIGURATIONS.keys())
    for key in configuration_keys:
        if key not in loaded_configuration_keys:
            print(f'Ключ: {key} отсутствует в файле')
            sys.exit(1)
    return CONFIGURATIONS


def send_message(opened_socket, message, CONFIGURATIONS):
    json_message = json.dumps(message)
    response = json_message.encode(CONFIGURATIONS.get('ENCODING'))
    opened_socket.send(response)


def get_message(opened_socket, CONFIGURATIONS):
    response = opened_socket.recv(CONFIGURATIONS.get('MAX_PACKAGE_LENGTH'))
    if isinstance(response, bytes):
        json_response = response.decode(CONFIGURATIONS.get('ENCODING'))
        response_dict = json.loads(json_response)
        if isinstance(response_dict, dict):
            return response_dict
        raise ValueError
    raise ValueError


