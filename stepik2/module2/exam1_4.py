#  Столетие
year = int(input())

if year % 100 == 0:
    print('YES')
else:
    print('NO')

#  Сравнение цвета двух клеток шахматной доски
first_col, first_row = int(input()), int(input())
second_col, second_row = int(input()), int(input())

if ((first_col - first_row) % 2 == 0 and (second_col - second_row) % 2 == 0 or
        (first_col - first_row) % 2 == 1 and (second_col - second_row) % 2 == 1):
    res = 'YES'
else:
    res = 'NO'
print(res)


#  Girls only
AGE_MIN = 10
AGE_MAX = 15
FEMALE = 'f'
age = int(input())
gender = input()

if AGE_MIN <= age <= AGE_MAX and gender == FEMALE:
    res = 'YES'
else:
    res = 'NO'
print(res)


#  Римские цифры
num = int(input())

if 0 < num <= 3:
    res = 'I' * num
elif 3 < num <= 8:
    res = 'I' * (5 - num) + 'V' + 'I' * (num - 5)
elif 8 < num <= 10:
    res = 'I' * (10 - num) + 'X'
else:
    res = 'ошибка'
print(res)

