''' Создайте несколько переменных разных типов
 Проверьте к какому типу относятся переменные'''

data = [1, True, 5.2, 'text', None, b'12']

for item in data:
    print(type(item))

for i in range(1, len(data)):
    print(type(data[i]))


