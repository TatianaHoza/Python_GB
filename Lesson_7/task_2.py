'''✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
'''
from random import randint, choice


def pseudonym_generate():
    vowels = 'aeiou'
    consonants = 'qwrtpsdfghjklzxcvbnm'
    name_lines = randint(4, 7)

    name = [choice(vowels + consonants).upper()]

    for i in range(name_lines - 1):
        name.append(choice(consonants))
    for i in range((name_lines - 1) // 2):
        name[choice(range(1, name_lines - 1))] = choice(vowels)
    return ''.join(name)


def save_name(count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for _ in range(count):
            print(pseudonym_generate(), file=file)


if __name__ == '__main__':
    save_name(5, 'task_2.txt')
