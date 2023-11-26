#  Is Valid Triangle?
# объявление функции
def is_valid_triangle(side1, side2, side3):
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        result = True
    else:
        result = False

    return result


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))


#  Is a Number Prime?
# объявление функции
def is_prime(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return len(divisors) == 2


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))


#  Next Prime
# объявление функций
def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1

    return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
