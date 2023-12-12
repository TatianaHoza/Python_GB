'''Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списковархивов
list-архивы также являются свойствами экземпляра
'''

class Archive:
    archives = []
    archives_2 = []

    def __init__(self, text:str, num: int):
        self.num = num
        self.text = text
        self.safe_to_archive(self.archives)
        self.safe_to_archive(self.archives_2)

    def safe_to_archive(self,ar):
        ar.append(f'{self.num}, {self.text}')

f1 = Archive('T1',111)
print(f1.archives)