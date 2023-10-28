n, k = int(input()), int(input())

if n > k:
    answer = 'NO'
elif n < k:
    answer = 'YES'
else:
    answer = "Don't know"
print(answer)


a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    triangle = 'Равносторонний'
elif a == b or b == c or a == c:
    triangle = 'Равнобедренный'
else:
    triangle = 'Разносторонний'
print(triangle)


num1, num2, num3 = int(input()), int(input()), int(input())

if num1 < num2 < num3 or num3 < num2 < num1:
    average = num2
elif num2 < num1 < num3 or num3 < num1 < num2:
    average = num1
else:
    average = num3
print(average)


month = int(input())

if month == 2:
    days = 28
elif (month % 2 == 1 and month <= 7) or (month % 2 == 0 and month > 7):
    days = 31
else:
    days = 30
print(days)
