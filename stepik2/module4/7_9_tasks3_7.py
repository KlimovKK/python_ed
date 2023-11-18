#  Делители-1
a, b = int(input()), int(input())

max_div_sum = 0
num = 0
for i in range(a, b + 1):
    div_sum = 0
    for j in range(1, i + 1):
        if i % j == 0:
            div_sum += j
    if div_sum >= max_div_sum:
        max_div_sum = div_sum
        num = i

print(num, max_div_sum)


#  Делители-2
n = int(input())

for i in range(1, n + 1):
    print(i, end='')
    for j in range(1, i + 1):
        if i % j == 0:
            print('+', end='')
    print()


#  Цифровой корень
n = int(input())

while n > 9:
    sum_digit = 0
    while n > 0:
        sum_digit += n % 10
        n //= 10
    n = sum_digit

print(n)


#  Сумма факториалов
n = int(input())

sum_fact = 0
for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum_fact += fact

print(sum_fact)


# Простые числа
a, b = int(input()), int(input())

for i in range(a, b + 1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
