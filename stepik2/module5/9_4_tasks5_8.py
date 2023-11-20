#  .com or .ru
line = input()

if line.endswith('.com', - 4) or line.endswith('.ru', - 3):
    print('YES')
else:
    print('NO')


#  Самый частотный символ
line = input()

most_freq_symbol = ' '
for ch in line:
    if line.count(ch) >= line.count(most_freq_symbol):
        most_freq_symbol = ch

print(most_freq_symbol)


#  Первое и последнее вхождение
LETTER = 'f'

line = input()

first = line.find(LETTER)
last = line.rfind(LETTER)
if first + last == - 2:
    print('NO')
elif first == last:
    print(first)
else:
    print(first, last)


#  Удаление фрагмента
LETTER = 'h'

line = input()

first = line.find(LETTER)
last = line.rfind(LETTER)
res = line[:first] + line[last + 1:]
print(res)
