data = [int(x) for x in input().split()]

for i in map(lambda x: x ** 2 if x % 2 == 1 else - x, range(data[0], data[1], data[2])):
    print(i)
