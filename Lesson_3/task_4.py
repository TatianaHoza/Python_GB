"""
Задание №4
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]

count_dict = {}
for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1

new_lst = [el for el in lst if count_dict[el] != 2]

print(new_lst)

  #new_list = [item for item in my_list if my_list.count(item) != 2]