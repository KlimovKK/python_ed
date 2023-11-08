#  Количество чисел
a, b = int(input()), int(input())

counter = 0
for i in range(a, b + 1):
    last = i ** 3 % 10
    if last == 4 or last == 9:
        counter += 1
print(counter)


#  Сумма чисел
n = int(input())

total = int(input())
for i in range(n - 1):
    num = int(input())
    total += num
print(total)


#  Асимптотическое приближение
from math import log

n = int(input())

total = 0
for i in range(1, n + 1):
    total += 1 / i
res = total - log(n)

print(res)


#  Сумма чисел 2
n = int(input())

total = 0
for i in range(1, n + 1):
    if i % 10 == 5:
        total += i

print(total)


#  Факториал
n = int(input())

fakt = 1
for i in range(2, n + 1):
    fakt *= i

print(fakt)
