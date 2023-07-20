# Не моё
str = [int(i) for i in input().split()]
ans = []
[ans.append(x) for x in str if x not in ans and str.count(x) > 1]
print(*ans)