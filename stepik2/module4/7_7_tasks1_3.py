#  Ревью кода-1
count = 0
p = 1
for i in range(10):
    x = int(input())
    if x >= 0:
        p = p * x
        count = count + 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')

#  Ревью кода-2
mx = - int(1e7)
s = 0
for i in range(10):  
    x = int(input())
    if x < 0:
        s += x
        if x > mx:
            mx = x
if s != 0:
    print(s)
    print(mx)
else:
    print('NO')


#  Ревью кода-3
s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)
