
"""
Задание №1.
Создайте функцию-замыкание, которая запрашивает два целых
числа:
- от 1 до 100 для загадывания;
- от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def guessing_func(number, count):

    def is_game():
        print(f"Угадайте число от 1 до {number}")
        for _ in range(count):
            answer = int(input(f'Введите число: '))
            if answer == number:
                print(f'Угадал, загадано {number}')
                return True
            elif answer < number:
                print('Загадано большее число. Попробуйте еще раз')
            else:
                print('Загадано меньшее число. Попробуйте еще раз')
        print(f'Попытки закончились. Загадано число {number}')
        return False

    return is_game


# создали нашу функцию-замыкатель
start_game = guessing_func(10, 5)
# вызвали её
start_game()

