# from functools import cache

"""
Задание №4
📌 Создайте декоратор с параметром.
📌 Параметр - целое число, количество запусков декорируемой
функции.
"""


def launch_counter(count):
    counters = []

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                counters.append(func(*args, **kwargs))
            return counters

        return wrapper
    return decorator


@launch_counter(7)
def factorial(n: int) -> int:
    print(f'Вычисляю факториал {n}!')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# res = launch_counter(7)(factorial)
# print(res(5))


if __name__ == '__main__':
    print(f'{factorial(20) = }')