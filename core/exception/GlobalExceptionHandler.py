import traceback
import json
import os


def handle_exception(exctype, value, tb):
    exception_name = exctype.__name__
    frames = traceback.extract_tb(tb)

    # Ignora o segundo frame (onde a exceção foi lançada)
    if len(frames) > 1:
        frame = frames[1]
        file_path = frame.filename
        function_name = frame.name
        line_number = frame.lineno

        # Use os.path.basename to get just the file name
        file_name = os.path.basename(file_path)

        print(
            f"Error in {function_name} (line {line_number}) of {exception_name} in file{file_name}: {value}")
    else:
        print(f"Error in {exception_name}: {value}")


def global_exception_handler(exctype, value, tb):
    exception_handlers = {
        FileNotFoundError: handle_exception,
        json.JSONDecodeError: handle_exception,
        # ...
    }

    handler = exception_handlers.get(exctype, None)
    if handler is not None:
        handler(exctype, value, tb)
    else:
        print(f"Exceção não tratada: {exctype} - {value}")
        traceback.print_tb(tb)
