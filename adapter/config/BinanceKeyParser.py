import json


class BinanceKeyParser:
    def __init__(self, file_path='../../binance.json'):
        self.file_path = file_path


file_path = '../../binance.json'

with open(file_path, 'r') as file:
    binance_keys = file.readlines()

    if len(binance_keys) == 2:
        string1 = binance_keys[0].strip()
        string2 = binance_keys[1].strip()

        print(f'Key: {string1}')
        print(f'Secret: {string2}')
