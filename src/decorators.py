import os
import time
from functools import wraps
from typing import Any, Callable


def log(file_name: str | None = None) -> Callable:
    """
    Декоратор, который логирует время выполнения функции при успешной отработке, а также логирует ошибки
    """

    def my_dec(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = time.time()

            try:
                result = func(*args, **kwargs)
                stop = time.time()
                func_time = stop - start

                if file_name is not None:
                    os.makedirs(os.path.dirname(file_name), exist_ok=True)
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(f"Функция: {func.__name__}, результат: {result} - всё ОК\n")
                        file.write(f"Время работы функции: {func_time}")

                else:
                    print(f"Функция: {func.__name__}, результат: {result} - всё ОК\n")
                    print(f"Время работы функции: {func_time} сек")

            except Exception as er:
                stop = time.time()
                func_time = stop - start
                if file_name is not None:
                    os.makedirs(os.path.dirname(file_name), exist_ok=True)
                    with open(file_name, "a", encoding="utf-8") as file:
                        file.write(f"Функция: {func.__name__} - ERROR: {er} with inputs: {args}, {kwargs}")
                        file.write(f"Время работы функции: {func_time}")

                else:
                    print(f"Функция: {func.__name__} - ERROR: {er} with inputs: {args}, {kwargs}")

                result = "Произошла ошибка"

            return result

        return wrapper

    return my_dec
