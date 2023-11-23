#  Значение функции
n = int(input())

values = []
for _ in range(n):
    values.append(int(input()))

print(*values, sep='\n')
print()

functions = []
for val in values:
    func = val ** 2 + 2 * val + 1
    functions.append(func)

print(*functions, sep='\n')


#  Remove outliers
n = int(input())

values = []
for _ in range(n):
    values.append(int(input()))

values.remove(min(values))
values.remove(max(values))

print(*values, sep='\n')


#  Без дубликатов
n = int(input())

values = []
for _ in range(n):
    val = input().lower()
    if val not in values:
        values.append(val)

print(*values, sep='\n')
