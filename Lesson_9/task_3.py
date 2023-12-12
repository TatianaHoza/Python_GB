'''Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.'''

import json
import os


def save_to_json(func):
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


@save_to_json
def add_element(*args, **kwargs):
    return sum(args)


if __name__ == '__main__':
    add_element(2, 66, test='4', text='Привет', log=True)