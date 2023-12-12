'''Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)
'''

import time

class MyString(str):
    ''' класс-наследник класса str'''

    def __new__(cls, text, author_name):
        instance = super().__new__(cls,text)
        print(instance)
        instance.author_name = author_name
        instance.create_time = time.strftime("%H:%M:$S")
        return instance

my_str1 = MyString('Your text', 'Tanya')

