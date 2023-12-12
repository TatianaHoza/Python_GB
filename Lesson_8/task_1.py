'''Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.'''
import json


def save_json():
    with(
        open('task_3.txt', 'r', encoding='utf-8') as pairs_tabs,
        open('task_1.json', 'w', encoding='utf-8') as pairs_json,

    ):
        pairs_dict = {line.split(' - ')[0].capitalize():int(
            float(line.split(' - ')[1])) if line.split(' - ')[1].strip().isdigit() else float(line.split(' - ')[1]) for line in list(pairs_tabs)}

    
        json.dump(pairs_dict,pairs_json,ensure_ascii = False, indent = 2)

if __name__ == '__main__':
    save_json()