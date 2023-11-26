#  Конвертер километров
# объявление функции
def convert_to_miles(km):
    return km * 0.6214


# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))


#  Количество дней
# объявление функции
def get_days(month):
    if month == 2:
        days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        days = 31
    return days


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))


#  Делители 1
# объявление функции
def get_factors(num):
    result = [i for i in range(1, num + 1) if num % i == 0]
    return result


# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))


# Делители 2
# объявление функции
def get_factors(num):
    result = [i for i in range(1, num + 1) if num % i == 0]
    return result


def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
