#  Список чисел
n = int(input())

print(list(range(1, n + 1)))


#  Список букв
n = int(input())

letters = ''
for i in range(ord('a'), ord('a') + n):
    letters += chr(i)

print(list(letters))
