import random
START_OF_RANGE = 1
END_OF_RANGE = 100


def is_valid(num):
    return num.isdigit() and START_OF_RANGE <= int(num) <= END_OF_RANGE


number = random.randint(START_OF_RANGE, END_OF_RANGE)

print('Добро пожаловать в числовую угадайку')

while True:
    user_input = input(f'Введите число от {START_OF_RANGE} до {END_OF_RANGE}: ')

    if is_valid(user_input):
        user_input = int(user_input)
    else:
        print(f'А может быть все-таки введем целое число от {START_OF_RANGE} до {END_OF_RANGE}?')
        continue

    if user_input < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif user_input > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break

