# Задание №2
# Погружение в Python | Коллекции
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
# """

data = [1, 2.1, True, -5, "Sds"]

for item in data:
    try:
        print(int(item))
        print(float(item))
        if type(item) == str and not item.islower():
            print(item.lower())
        elif type(item) == str:
            print(item.lower())

    except ValueError:
        print("Невозможно преобразовать в целое число или вещественное число")

        print(item.lower())


    except TypeError:
        print("Ошибка")

