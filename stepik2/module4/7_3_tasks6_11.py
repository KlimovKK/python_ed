#  Без нулей
QTY = 10

product = 1
for _ in range(QTY):
    num = int(input())
    if num != 0:
        product *= num

print(product)


#  Сумма делителей
n = int(input())

total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(total)


#  Знакочередующаяся сумма
n = int(input())

total = 0
for i in range(1, n + 1):
    total += (- 1) ** (i + 1) * i

print(total)


#  Наибольшие числа
n = int(input())

largest = int(input())
largest_1 = -1
for _ in range(n - 1):
    num = int(input())
    if num > largest_1:
        largest_1 = num
        if largest_1 > largest:
            largest, largest_1 = largest_1, largest

print(largest, largest_1, sep='\n')


#  Only even numbers
QTY = 10

even = True
for _ in range(QTY):
    num = int(input())
    if num % 2 == 1:
        even = False

if even:
    res = 'YES'
else:
    res = 'NO'

print(res)


#  Последовательность Фибоначчи
n = int(input())

num_1 = 0
num_2 = 1
print(num_2, end=' ')
for _ in range(n - 1):
    print(num_1 + num_2, end=' ')
    num_1, num_2 = num_2, num_1 + num_2
