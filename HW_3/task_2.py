#
# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
#
# Слова разделяются пробелами, апостроф не считается за пробел. Такие слова как dont, its, didnt итд (после того, как убрали знак препинания апостроф) считать одним словом.

# from collections import Counter
# import re
#
text = 'Hello world. Hello Python. Hello again.'
# text = text.lower()
#
# cnt = Counter(x for x in re.findall(r'[A-z\']{2,}', text))
# print(cnt.most_common(10))

import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)