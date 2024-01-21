n = int(input())
my_array = [int(i) for i in input().split()]
K = int(input())

max_prod = 1
for i in range(K, n + 1):
    prod = 1
    for j in range(i - K, i):
        prod *= my_array[j]
    if max_prod < prod:
        max_prod = prod

print(max_prod)
