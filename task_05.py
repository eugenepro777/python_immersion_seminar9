from task_02 import validate_ranges
from task_03 import save_to_json
from task_04 import launch_counter

"""
Задание №5
📌 Объедините функции из прошлых задач.
📌 Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
📌 Выберите верный порядок декораторов.
"""


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


is_game(10, 20)