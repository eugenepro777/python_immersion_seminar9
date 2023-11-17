from functools import wraps
from random import randint
import os
import json

"""
Задание №6
📌 Доработайте прошлую задачу добавив декоратор wraps в
каждый из декораторов.
"""


def validate_ranges(func):
    @wraps(func)
    def wrapper(number, attempts):
        number = number if 1 < number < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else randint(1, 10)
        return func(number, attempts)

    return wrapper


def save_to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        file_name = f"{func.__name__}.json"
        data = {}

        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)

        key = len(data) + 1
        result = func(*args, **kwargs)
        data[key] = {'args': args, 'kwargs': kwargs, 'result': result}

        with open(file_name, 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, indent=2, ensure_ascii=False)

        return result

    return wrapper


def launch_counter(count):
    counters = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(count):
                counters.append(func(*args, **kwargs))
            return counters

        return wrapper

    return decorator


@launch_counter(2)
@save_to_json
@validate_ranges
def is_game(number, count):
    print(f"Угадайте число от 1 до {number} за {count} попыток")
    for i in range(count):
        answer = int(input(f'Введите число: '))
        if answer == number:
            print(f'попытка {i + 1}')
            print(f'Угадал, загадано {number}. Использовал {i + 1} попыток')
            return True
        elif answer < number:
            print(f'попытка {i + 1}')
            print('Загадано большее число. Попробуйте еще раз')
        else:
            print(f'попытка {i + 1}')
            print('Загадано меньшее число. Попробуйте еще раз')
    print(f'Попытки закончились. Загадано число {number}')
    return False


# print(is_game(10, 5))
print(is_game.__name__)