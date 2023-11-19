#  В столбик 1
line = input()

for i in range(0, len(line), 2):
    print(line[i])


#  В столбик 2
line = input()

for i in range(1, len(line) + 1):
    print(line[- i])


#  ФИО
name, surname, patronymic = input(), input(), input()

print(surname[0] + name[0] + patronymic[0])


#  Цифра 1
line = input()

sum_line = 0
for c in line:
    sum_line += int(c)

print(sum_line)


#  Цифра 2
line = input()

digit = False
for c in line:
    if '0' <= c <= '9':
        digit = True
        break

if digit:
    print('Цифра')
else:
    print('Цифр нет')
