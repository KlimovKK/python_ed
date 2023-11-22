#  Все сразу 1
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[- 1])
print(numbers[::- 1])
if 5 in numbers and 17 in numbers:
    print('YES')
else:
    print('NO')
print(numbers[1:-1])


#  Список строк
n = int(input())

list_of_strings = []
for _ in range(n):
    line = input()
    list_of_strings.append(line)

print(list_of_strings)


#  Алфавит
alphabet = []
code_a = ord('a')
for code in range(code_a, code_a + 26):
    qty = code - code_a + 1
    alphabet.append(chr(code) * qty)

print(alphabet)


#  Список кубов
n = int(input())

list_of_cubes = []
for _ in range(n):
    num = int(input())
    list_of_cubes.append(num ** 3)

print(list_of_cubes)


#  Список делителей
n = int(input())

res = [1]
for i in range(2, n // 2 + 1):
    if n % i == 0:
        res.append(i)

res.append(n)

print(res)
