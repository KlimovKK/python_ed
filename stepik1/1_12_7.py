"""
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет,
счастливый ли ему попался. Билет считается счастливым, если сумма первых трех цифр
совпадает с суммой последних трех цифр номера билета.
Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу, которая
проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный",
если суммы различны.
На вход программе подаётся строка из шести цифр.
Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
"""
Number = int(input())
Sum1 = Number // 100000 + Number // 10000 % 10 + Number // 1000 % 10
Sum2 = Number // 100 % 10 + Number // 10 % 10 + Number % 10
if Sum1 == Sum2:
    print('Счастливый')
else:
    print('Обычный')