# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

lst = [1, 1, 2, 2, 3, 3]
new_lst = []
for i in lst:
    if lst[i] in new_lst:
        print(new_lst)

    else:
        new_lst.append(lst[i])
        i += 1
print(new_lst)

