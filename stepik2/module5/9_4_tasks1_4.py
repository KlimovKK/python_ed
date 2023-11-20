#  Количество слов
line = input()

print(line.count(' ') + 1)


#  Минутка генетики
gen_code_string = input().upper()

print(f'Аденин: {gen_code_string.count("А")}')
print(f'Гуанин: {gen_code_string.count("Г")}')
print(f'Цитозин: {gen_code_string.count("Ц")}')
print(f'Тимин: {gen_code_string.count("Т")}')


#  Очень странные дела
n = int(input())

count_11_message = 0
for _ in range(n):
    message = input()
    if message.count('11') >= 3:
        count_11_message += 1

print(count_11_message)


#  Количество цифр
line = input()

number_of_digits = 0
for digit in range(10):
    number_of_digits += line.count(str(digit))

print(number_of_digits)
