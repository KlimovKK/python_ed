#  Искомый месяц
# объявление функции
def get_month(language, number):
    ru_months = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en_months = ['', 'january', 'february', 'march', 'april', 'may', 'june',
                 'july', 'august', 'september', 'october', 'november', 'december']

    if language == 'ru':
        return ru_months[number]
    elif language == 'en':
        return en_months[number]


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))


#  Магические даты
# объявление функции
def is_magic(date):
    parts = [int(i) for i in date.split('.')]
    return parts[0] * parts[1] == parts[2] % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))


#  Панграммы
# объявление функции
def is_pangram(text):
    text = ''.join(c for c in text.lower() if c.isalpha())
    text = set(text)
    return len(text) == 26


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
