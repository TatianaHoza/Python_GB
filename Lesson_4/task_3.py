'''✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.'''

str_ = '90 48'

# def codes_dict(str_):
#     lst = [int(num) for num in str_.split()]
#     dct = {}
#     for i in range(lst[0],lst[1]+1):
#         dct[chr(i)] = i
#     return dct
#
# print(codes_dict(str_))

def codes_dict1(str_):
    lst = [int(num) for num in str_.split()]
    if lst[0]>lst[1]:
        lst[0],lst[1] = lst[1],lst[0]
    dct = {chr(i): i for i in range(lst[0],lst[1]+1)}
    return dct
print(codes_dict1(str_))