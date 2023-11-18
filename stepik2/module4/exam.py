#  Ревью кода - 7
n = int(input())
s = 0
while n > 0:
    if n % 10 % 2 == 0:
        s += n % 10
    n //= 10
print(s)


#  Ревью кода - 8
n = 8
count = 0
maximum = - 10 ** 12 - 1
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


#  Ревью кода - 9
n = 4
count = 0
maximum = - 10 ** 8
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


#  Звездная рамка
COL = 19

n = int(input())

print('*' * COL)
for i in range(1, n):
    if i == n - 1:
        print('*' * COL)
    else:
        print('*' + ' ' * (COL - 2) + '*')


#  Третья цифра
n = int(input())

while n > 999:
    n //= 10

res = n % 10
print(res)


#  Все вместе 2
N0 = 0
N3 = 3
N5 = 5
N7 = 7

num = int(input())

count_3 = 0
last_digit = num % 10
count_last = 0
count_even = 0
total_5 = 0
product_7 = 1
count_0_5 = 0

while num:
    cur_digit = num % 10
    if cur_digit == N3:
        count_3 += 1
    if cur_digit == last_digit:
        count_last += 1
    if cur_digit % 2 == 0:
        count_even += 1
    if cur_digit > N5:
        total_5 += cur_digit
    if cur_digit > N7:
        product_7 *= cur_digit
    if cur_digit == N0 or cur_digit == N5:
        count_0_5 += 1
    num //= 10

print(count_3, count_last, count_even, total_5, product_7, count_0_5, sep='\n')
