#  Good password
# объявление функции
def is_password_good(password):
    good_len_password = len(password) >= 8
    presence_lowcase = any(c.islower() for c in password)
    presence_uppcase = any(c.isupper() for c in password)
    presence_digit = any(c.isdigit() for c in password)
    if good_len_password and presence_lowcase and presence_uppcase and presence_digit:
        result = True
    else:
        result = False

    return result


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


#  Ровно в одном
# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        differences = len(word1)
        for c1, c2 in zip(word1, word2):
            if c1 == c2:
                differences -= 1
        if differences == 1:  # Вместо конструкции if проще было использовать return differences == 1
            return True
        else:
            return False


# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))


#  Палиндром
# объявление функции
def is_palindrome(text):
    text = ''.join(c for c in text.lower() if c.isalpha())
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
