'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка
-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
 то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
 равнобедренным или равносторонним, только если треугольник существует .'''

import logging

logging.basicConfig(filename='log_task_1.log',
                    filemode='w',
                    format='{levelname} - {asctime} - {msg}',
                    style='{',
                    encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger('app')


def triangle(a, b, c):
    try:
        if a == b and b == c:
            print('Треугольник равносторонний')

        elif ((a != b) and (a != c) and (b != c)) and ((a+b) > c or (a+c) > b or (b+c) > a):
            print('Треугольник разносторонний')

        elif ((a == b) or (a == c) or (a == c)) and ((a+b) > c or (a+c) > b or (b+c) > a):
            print('Треугольник равнобедренный')
        logger.info('Треугольник существует')
    except ValueError as e:
        logger.error(f'Поймал ошибку {e}.')

triangle(5,5,5)
triangle(5,10,7)
triangle(5,2,5)
triangle(5,10,200)