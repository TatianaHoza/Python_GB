'''Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.'''

from random import randint


def guessing_func(func):
    def wrapper(number, attempts):
        number = number if 1 < number < 100 else randint(1, 100)
        attempts = attempts if 1 < attempts < 100 else randint(1, 10)
        return func(number, attempts)
    return wrapper
@guessing_func
def game(number:int, attempts:int):
    print(f"Угадайте число от 1 до 100")
    while attempts > 0:
        count = int(input(f'Введите число: '))
        if count == number:
            return "Угадали"
        attempts -= 1
        print(f'У вас осталось {attempts} попыток')
    return "Не угадали"

if __name__ == '__main__':
    print(game(45, 5))



