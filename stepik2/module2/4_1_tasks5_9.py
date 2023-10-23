num1, num2, num3 = int(input()), int(input()), int(input())
if num2 == (num1 + num3) / 2:
    print('YES')
else:
    print('NO')

num1, num2 = int(input()), int(input())
if num1 < num2:
    print(num1)
else:
    print(num2)

num1, num2, num3, num4 = int(input()), int(input()), int(input()), int(input())
min1 = num1
for num in (num2, num3, num4):
    if min1 > num:
        min1 = num
print(min1)

age = int(input())
if age <= 13:
    age_group = 'детство'
elif 13 < age <= 24:
    age_group = 'молодость'
elif 24 < age <= 59:
    age_group = 'зрелость'
else:
    age_group = 'старость'
print(age_group)

num1, num2, num3 = int(input()), int(input()), int(input())
sum_positive = 0
if num1 > 0:
    sum_positive += num1
if num2 > 0:
    sum_positive += num2
if num3 > 0:
    sum_positive += num3
print(sum_positive)
