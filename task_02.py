from random import randint

"""
Задание №2
📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декоратор.
📌 Он должен проверять входят ли переданные в функцию-
угадайку числа в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами
из диапазонов.
"""


def validate_ranges(func):

    def wrapper(number, attempt):
        if number not in range(1, 101) and attempt not in range(1, 11):
            number = randint(1, 100)
            attempt = randint(1, 10)
        return func(number, attempt)

    return wrapper


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


if __name__ == '__main__':
    is_game(102, 33)

