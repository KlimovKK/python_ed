#  Наибольшее и наименьшее
num1, num2, num3, num4, num5 = int(input()), int(input()), int(input()), int(input()), int(input())

print('Наименьшее число =', min(num1, num2, num3, num4, num5))
print('Наибольшее число =', max(num1, num2, num3, num4, num5))


#  Сортировка трёх
num1, num2, num3 = int(input()), int(input()), int(input())

min_num = min(num1, num2, num3)
max_num = max(num1, num2, num3)
avg_num = (num1 + num2 + num3) - min_num - max_num
print(max_num, avg_num, min_num, sep='\n')


#  Интересное число
num = input()
d1 = int(num[0])
d2 = int(num[1])
d3 = int(num[2])

min_d = min(d1, d2, d3)
max_d = max(d1, d2, d3)
avg_d = (d1 + d2 + d3) - min_d - max_d
if max_d - min_d == avg_d:
    res = 'Число интересное'
else:
    res = 'Число неинтересное'
print(res)


#  Абсолютная сумма
num1, num2, num3, num4, num5 = [abs(float(input())) for i in range(5)]

print(num1 + num2 + num3 + num4 + num5)


#  Манхэттенское расстояние
p1, p2, q1, q2 = [int(input()) for i in range(4)]

dist = abs(p1 - q1) + abs(p2 - q2)
print(dist)
