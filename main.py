import sys

from adapter.config.BinanceKeyParser import BinanceKeyParser
from core.exception.GlobalExceptionHandler import global_exception_handler

sys.excepthook = global_exception_handler

if __name__ == '__main__':
    parser = BinanceKeyParser()
    api_key, api_secret = parser.read_keys()

    print(f'API Key: {api_key}')
    print(f'API Secret: {api_secret}')
