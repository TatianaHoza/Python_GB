'''
Задание №6
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.

'''

lst = [1, 3, -5, 7, 5, 8, 4, -9, 2]

inx1 = 5

inx2 = 10


def func(lst, inx1, inx2):
    if inx1 >= inx2:
        print('No el')
        return
    elif inx1 < 0 and inx2 > len(lst):
        return sum(lst[:])
    elif inx1 < 0:
        return sum(lst[:inx2])
    elif inx2 > len(lst):
        return sum(lst[inx1 + 1:])
    else:
        return sum(lst[inx1 + 1:inx2])


print(func(lst, inx1, inx2))
