b1, q, n = int(input()), int(input()), int(input())
bn = b1 * q ** (n-1)
print(bn)

sm = int(input())
print(sm // 100)

schoolkids = int(input())
tangerines = int(input())
print(tangerines // schoolkids)
print(tangerines % schoolkids)

population = int(input())
print(population // 2 + population % 2)

seat = int(input())
print((seat + 3) // 4)

minutes = int(input())
print(f'{minutes} мин - это {minutes // 60} час {minutes % 60} минут.')
