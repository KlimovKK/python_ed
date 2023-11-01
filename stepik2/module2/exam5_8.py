#  YES or NO вот в чем вопрос
num = int(input())

if num % 2 == 0:
    if 2 <= num <= 5:
        res = 'NO'
    elif 6 <= num <= 20:
        res = 'YES'
    else:
        res = 'NO'
else:
    res = 'YES'
print(res)


#  Ход слона
first_col, first_row = int(input()), int(input())
second_col, second_row = int(input()), int(input())

if abs(first_col - second_col) == abs(first_row - second_row):
    res = 'YES'
else:
    res = 'NO'
print(res)


#  Ход коня
first_col, first_row = int(input()), int(input())
second_col, second_row = int(input()), int(input())

if abs((first_col - second_col) * (first_row - second_row)) == 2:
    res = 'YES'
else:
    res = 'NO'
print(res)


#  Ход ферзя
first_col, first_row = int(input()), int(input())
second_col, second_row = int(input()), int(input())

if abs(first_col - second_col) == abs(first_row - second_row) or first_col == second_col or first_row == second_row:
    res = 'YES'
else:
    res = 'NO'
print(res)
