#  Заглавные буквы
line = input()

if line == line.title():
    print('YES')
else:
    print('NO')


#  sWAP cASE
line = input()

print(line.swapcase())


#  Хороший оттенок
SUBSTRING = 'хорош'

line = input()

if SUBSTRING in line.lower():
    print('YES')
else:
    print('NO')


#  Нижний регистр
line = input()

cnt_lowercase = 0
for ch in line:
    if ch.islower():
        cnt_lowercase += 1

print(cnt_lowercase)
