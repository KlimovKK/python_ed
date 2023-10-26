"""INTERVAL_MIN = -1
INTERVAL_MAX = 17

x = int(input())

if INTERVAL_MIN < x < INTERVAL_MAX:
    res = 'Принадлежит'
else:
    res = 'Не принадлежит'
print(res)"""


"""INTERVAL1 = -3
INTERVAL2 = 7

x = int(input())

if x <= INTERVAL1 or x >= INTERVAL2:
    res = 'Принадлежит'
else:
    res = 'Не принадлежит'
print(res)"""


"""INTERVAL1_MIN = -30
INTERVAL1_MAX = -2
INTERVAL2_MIN = 7
INTERVAL2_MAX = 25

x = int(input())

if (INTERVAL1_MIN < x <= INTERVAL1_MAX) or (INTERVAL2_MIN < x <= INTERVAL2_MAX):
    res = 'Принадлежит'
else:
    res = 'Не принадлежит'
print(res)"""


num = int(input())

if (1000 <= num <= 9990) and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')
