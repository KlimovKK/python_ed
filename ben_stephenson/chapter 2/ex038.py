"""
Упражнение 38. Угадайте фигуру
Напишите программу, определяющую вид фигуры по количеству ее сто-
рон. Запросите у пользователя количество сторон и выведите сообщение
с указанием вида фигуры. Программа должна корректно обрабатывать
и выводить названия для фигур с количеством сторон от трех до десяти
включительно. Если введенное пользователем значение находится за гра-
ницами этого диапазона, уведомите его об этом.
"""
figure = ''
n_sides = int(input('Введите количество сторон: '))
if n_sides == 3:
    figure = 'треугольник'
elif n_sides == 4:
    figure = 'четырехугольник'
elif n_sides == 5:
    figure = 'пятиугольник'
elif n_sides == 6:
    figure = 'шестиугольник'
elif n_sides == 7:
    figure = 'семиугльник'
elif n_sides == 8:
    figure = 'восьмиугольник'
elif n_sides == 9:
    figure = 'девятиугольник'
elif n_sides == 10:
    figure = 'десятиугольник'

if figure == '':
    print('Количество сторон должно быть от 3 до 10 включительно')
else:
    print('Это', figure)
