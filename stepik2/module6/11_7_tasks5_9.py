#  Списочное выражение 1
n = int(input())
squares = [num ** 2 for num in range(1, n + 1)]

for square in squares:
    print(square)


#  Списочное выражение 2
numbers = [int(num) ** 3 for num in input().split()]

for num in numbers:
    print(num, end=' ')


#  В одну строку 1
print(*[word for word in input().split()], sep='\n')


#  В одну строку 2
line = [ch for ch in input() if ch.isdigit()]
print(*line, sep='')


#  В одну строку 3
squares = [int(num) ** 2 for num in input().split()
           if int(num) % 2 == 0 and int(num) ** 2 % 10 != 4]
print(*squares)
