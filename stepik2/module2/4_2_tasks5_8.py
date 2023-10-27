a, b, c = int(input()), int(input()), int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print('YES')
else:
    print('NO')


year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')


first_col, first_row = int(input()), int(input())
second_col, second_row = int(input()), int(input())

if first_col == second_col or first_row == second_row:
    print('YES')
else:
    print('NO')


first_col, first_row = int(input()), int(input())
second_col, second_row = int(input()), int(input())

if second_col - 1 <= first_col <= second_col + 1 and second_row - 1 <= first_row <= second_row + 1:
    print('YES')
else:
    print('NO')
