'''Задание №2
Напишите функцию, которая в бесконечном цикле
запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в
JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо
от уровня доступа.
При перезапуске функции уже записанные в файл данные
должны сохраняться.
'''
import json


def level_id():
    try:
        with open("task_2.json", 'r', encoding='utf-8') as level_json:
            user_data_by_level = json.load(level_json)
    except FileNotFoundError:
        user_data_by_level = {}

    while True:
        name = input("enter name: ")
        if name.lower().strip() == 'exit':
            break
        personal_id = input("enter id: ")
        level = ("enter level from 1 to 7: ")

        while personal_id in user_data_by_level.get(level, {}):
            print("User's id is find in dict. Enter other")
            personal_id = input("enter id: ")

        if level not in user_data_by_level:
            user_data_by_level[level] = {}
        user_data_by_level[level][personal_id] = name

    with open('task_2.json', 'w', encoding='utf-8') as level_json:
        json.dump(user_data_by_level, level_json, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    level_id()
