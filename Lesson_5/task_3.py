'''✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение,
обращаясь к итератору, а не к словарю.
'''

text = 'davdbvdpvbdwdghcgjhgj'
dct = {item: ord(item) for item in text}

iterator = iter(dct.items())

for _ in range(5):
    print(next(iterator))