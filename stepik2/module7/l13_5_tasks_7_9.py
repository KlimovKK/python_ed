#  BEEGEEK
# объявление функций
def is_prime(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return len(divisors) == 2


def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]


def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False
    else:
        return is_palindrome(parts[0]) and is_prime(int(parts[1])) and int(parts[2]) % 2 == 0

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))


#  Правильная скобочная последовательность
# объявление функции
def is_correct_bracket(text):
    counter = 0
    for c in text:
        if c == '(':
            counter += 1
        elif c == ')':
            counter -= 1
        else:
            return False

        if counter < 0:
            return False

    return counter == 0


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))


#  Змеиный регистр
# объявление функции
def convert_to_python_case(text):
    python_text = text[:1].lower()
    for c in text[1:]:
        if c.isupper():
            python_text += '_' + c.lower()
        else:
            python_text += c

    return python_text


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
