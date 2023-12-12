''' Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
'''
str_ = "Каждый охотник желает знать где сидит фазан"

def my_function(text):
    my_list = []
    ch_list = list(text)
    for ch in ch_list:
        my_list.append(ord(ch))
    return sorted(my_list, reverse=True)

print(my_function(str_))

'''my_list = set([ord(ch) for ch in text])
return sorted(my_list, reverse=True)'''