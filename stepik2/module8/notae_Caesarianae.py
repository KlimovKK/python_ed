"""
Программа, способная шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Запрашивает у пользователя следующие данные:
направление: шифрование или дешифрование;
язык алфавита: русский или английский;
шаг сдвига (со сдвигом вправо)
"""


def caesars_cipher(letter, step, language):
    alpha = ['АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    new_index = (alpha[language].find(letter.upper()) + step) % len(alpha[language])
    if letter.islower():
        return alpha[language][new_index].lower()
    else:
        return alpha[language][new_index]


if __name__ == '__main__':
    direction = input('Введите 1 для шифрования или 2 для дешифрования \n=>')
    while direction not in ['1', '2']:
        print('Что-то пошло не так!')
        direction = input('Введите 1 для шифрования или 2 для дешифрования \n=>')

    language = input('Введите язык алфавита: 1 - русский, 2 - английский \n=>')
    while language not in ['1', '2']:
        print('Что-то пошло не так!')
        language = input('Введите язык алфавита: 1 - русский, 2 - английский \n=>')
    language = int(language) - 1

    step = input('Введите шаг сдвига вправо (целое число)\n=>')
    while not step.isdigit():
        print('Что-то пошло не так!')
        step = input('Введите шаг сдвига вправо (целое число)\n=>')
    if direction == '1':
        step = int(step)
    else:
        step = int('-' + step)

    inp_text = input('Введите текст\n=>')

    out_text = ''
    for char in inp_text:
        if char.isalpha():
            out_text += caesars_cipher(char, step, language)
        else:
            out_text += char

    print(out_text)
