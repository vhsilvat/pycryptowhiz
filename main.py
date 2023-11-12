import sys

from adapter.config.BinanceKeyParser import BinanceKeyParser
from core.exception.GlobalExceptionHandler import global_exception_handler

sys.excepthook = global_exception_handler

if __name__ == '__main__':
    parser = BinanceKeyParser()
    parser.read_keys()
