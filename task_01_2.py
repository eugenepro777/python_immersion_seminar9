
"""
Задание №1.
Создайте функцию-замыкание, которая запрашивает два целых
числа:
- от 1 до 100 для загадывания;
- от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток.
"""


def guessing_func(number, attempts):

    def game():
        nonlocal attempts
        print(f"Угадайте число от 1 до {number}")
        while attempts > 0:
            count = int(input(f'Введите число: '))
            if count == number:
                return "Угадали"
            attempts -= 1
            print(f'У вас осталось {attempts} попыток')
        return "Не угадали"
    return game


# создали нашу функцию-замыкатель
start_game = guessing_func(10, 5)
# вызвали её
start_game()

