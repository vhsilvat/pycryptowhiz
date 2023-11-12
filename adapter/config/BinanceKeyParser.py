import json


class BinanceKeyParser:
    def __init__(self, file_path='binance.json'):
        self.file_path = file_path

    def read_keys(self):
        with open(self.file_path, 'r') as file:
            keys = json.load(file)

        api_key = keys.get('api_key')
        api_secret = keys.get('api_secret')

        if api_key and api_secret:
            print(f'API Key: {api_key}')
            print(f'API Secret: {api_secret}')
        else:
            print('Chaves inválidas ou ausentes no arquivo JSON.')
