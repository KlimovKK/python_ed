#  Список четных
n = int(input())

evens = list(range(2, n + 1, 2))
print(evens)


#  Сумма двух списков
L = [int(i) for i in input().split()]
M = [int(i) for i in input().split()]

res = [i + j for i, j in zip(L, M)]

print(*res, sep=' ')


#  Сумма чисел
line = input().split()

total = sum(map(int, line))
res = '+'.join(line)

print(f'{res}={total}')


#  Валидный номер
phone_number = input().split('-')

res = 'NO'
if len(phone_number) == 4 and phone_number[0] == '7':
    del phone_number[0]
    
digits = all([c.isdigit() for c in phone_number])

if digits:
    if len(phone_number) == 3 and len(phone_number[2]) == 4:
        del phone_number[2]
    if all([len(i) == 3 for i in phone_number]):
        res = 'YES'

print(res)


#  Самый длинный
line = input().split()

lens = [len(i) for i in line]
res = max(lens)

print(res)


#  Молодежный жаргон
res = [word[1:] + word[0] + 'ки' for word in input().split()]

print(*res, sep=' ')
