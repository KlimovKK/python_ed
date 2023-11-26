#  Звездный треугольник
# объявление функции
def draw_triangle():
    height = 8
    print(' ' * 7 + '*')
    for i in range(1, height):
        print(' ' * (height - i - 1) + '*' * (i * 2 + 1))


# основная программа
draw_triangle()  # вызов функции


#  Калькулятор доставки
# объявление функции
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120


# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))


#  Биномиальный коэффициент
from math import factorial


# объявление функции
def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))


#  Число словами
# объявление функции
def number_to_words(num):
    ONES = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    TENS = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    TEENS = ['', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']

    if 10 < num < 20:
        return TEENS[num - 10]

    ones = ONES[num % 10]
    tens = TENS[num // 10]

    return (tens + ' ' + ones).strip()


# считываем данные
n = int(input())

# вызываем функцию
print(number_to_words(n))
