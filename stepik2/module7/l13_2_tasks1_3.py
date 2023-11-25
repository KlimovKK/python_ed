#  Звездный треугольник
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)


#  ФИО
# объявление функции
def print_fio(name, surname, patronymic):
    fio = [c[0].upper() for c in (surname, name, patronymic)]
    print(*fio, sep='')


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)


#  Сумма цифр
# объявление функции
def print_digit_sum(num):
    res = sum([int(i) for i in str(num)])
    print(res)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
