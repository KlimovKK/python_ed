#  Сколько раз?
"""CHAR_1 = '+'
CHAR_2 = '*'

line = input()

count_char_1 = 0
count_char_2 = 0
for c in line:
    if c == CHAR_1:
        count_char_1 += 1
    if c == CHAR_2:
        count_char_2 += 1

print(f'Символ {CHAR_1} встречается {count_char_1} раз')
print(f'Символ {CHAR_2} встречается {count_char_2} раз')"""


#  Одинаковые соседи
"""line = input()

count = 0
for i in range(- len(line), -1):
    if line[i] == line[i + 1]:
        count += 1

print(count)"""


#  Гласные и согласные
"""VOWELS = 'уеыаоэяиюёУЕЫАОЭЯИЮЁ'
CONSONANTS = 'йцкнгшщзхфвпрлджчсмтбЙЦКНГШЩЗХФВПРЛДЖЧСМТБ'

line = input()

cnt_vowels, cnt_consonants = 0, 0
for c in line.lower():
    if c in VOWELS:
        cnt_vowels += 1
    elif c in CONSONANTS:
        cnt_consonants += 1

print('Количество гласных букв равно', cnt_vowels)
print('Количество согласных букв равно', cnt_consonants)"""


#  Decimal to Binary
num = int(input())

binary = ''
while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print(binary)
