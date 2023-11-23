#  Google search - 1
n = int(input())
strings = [input() for i in range(n)]
query = input()

res = []
for el in strings:
    if query.lower() in el.lower():
        res.append(el)

print(*res, sep='\n')


#  Google search - 2
n = int(input())
strings = [input() for _ in range(n)]
k = int(input())
query_strings = [input() for _ in range(k)]

res = []
for el in strings:
    coincidences = 0
    for query in query_strings:
        if query.lower() in el.lower():
            coincidences += 1
    if coincidences == len(query_strings):
        res.append(el)

print(*res, sep='\n')


#  Negatives, Zeros and Positives
n = int(input())
numbers = [int(input()) for _ in range(n)]

res = []
zero = []
positive = []
for num in numbers:
    if num < 0:
        res.append(num)
    elif num == 0:
        zero.append(num)
    else:
        positive.append(num)

res.extend(zero)
res.extend(positive)

print(*res, sep='\n')
