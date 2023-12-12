''' нарисовать елку'''

rows = 5
spase = ' '
simbol = '*'

simbols = 1
spases = rows - 1

for i in range(rows):
    print((spase * spases) + (simbol * simbols) + (spase * spases))
    simbols += 2
    spases -= 1
