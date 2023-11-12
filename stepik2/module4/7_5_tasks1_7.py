#  Обратный порядок 1
num = int(input())

while num:
    last_digit = num % 10
    print(last_digit)
    num //= 10


#  Обратный порядок 2
num = int(input())

while num:
    last_digit = num % 10
    print(last_digit, end='')
    num //= 10


#  max и min
num = int(input())

max_digit = - 1
min_digit = 10
while num:
    last_digit = num % 10
    if last_digit > max_digit:
        max_digit = last_digit
    if last_digit < min_digit:
        min_digit = last_digit
    num //= 10

print(f'Максимальная цифра равна {max_digit}', f'Минимальная цифра равна {min_digit}', sep='\n')


#  Все вместе
num = int(input())

sum_digits = 0
count_digits = 0
prod_digits = 1
last_digit = num % 10

while num:
    cur_digit = num % 10
    sum_digits += cur_digit
    count_digits += 1
    prod_digits *= cur_digit
    num //= 10

average = sum_digits / count_digits
first_digit = cur_digit
sum_fist_last = first_digit + last_digit

print(sum_digits, count_digits, prod_digits, average, first_digit, sum_fist_last, sep='\n')


#  Вторая цифра
num = int(input())

len_num = len(str(num))
second_digit = (num % 10 ** (len_num - 1)) // 10 ** (len_num - 2)

print(second_digit)


#  Одинаковые цифры
num = int(input())

flag = True
last_digit = num % 10
num //= 10
while num:
    cur_digit = num % 10
    if last_digit != cur_digit:
        flag = False
    num //= 10

if flag:
    print('YES')
else:
    print('NO')


#  Упорядоченные цифры
num = int(input())

flag = True
while num > 9:
    if num % 10 > (num // 10) % 10:
        flag = False
    num //= 10

if flag:
    print('YES')
else:
    print('NO')
