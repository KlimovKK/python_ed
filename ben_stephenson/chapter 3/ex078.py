"""
Упражнение 78. Гипотеза Коллатца
Представьте себе последовательность целых чисел, организованную сле-
дующим образом.
Начинаться последовательность должна с любого положительного числа
Пока последний элемент последовательности не равен единице, выполнять
Если последний элемент последовательности четный, тогда
Добавить новый элемент к последовательности путем деления последнего элемента
на два с округлением вниз
Иначе
Добавить новый элемент к последовательности путем умножения последнего элемента
на три с добавлением единицы.
Гипотеза Коллатца утверждает, что подобная последовательность при
условии того, что начинается с положительного числа, рано или поздно
завершится единицей. И хотя это так и не было доказано, все указывает
на то, что это так и есть.
Напишите программу, которая будет запрашивать у пользователя целое
число и выводить все числа, начиная с введенного числа и заканчивая
единицей. После этого пользователь должен иметь возможность ввести
другое число и снова получить ряд чисел, называемый сиракузской по-
следовательностью. Условием выхода из программы должен быть ввод
пользователем нуля или отрицательного числа.
"""

from math import floor

num = int(input('Введите положительное целое число: '))

print(num)

while num > 0:
    while num != 1:
        if num % 2 == 0:
            num = floor(num / 2)
            print(num)
        else:
            num = num * 3 + 1
            print(num)
    num = int(input('Введите положительное целое число (0 или отрицательное для выхода): '))