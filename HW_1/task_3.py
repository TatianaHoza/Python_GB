list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

list3 = []

for i in list1:
    if i in list2:
        list3.append(i)
        i += 1
print(f'Количество совпадающих чисел: {len(list3)-1}')
