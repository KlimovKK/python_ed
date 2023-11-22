#  Символы в диапазоне
a, b = int(input()), int(input())

for code in range(a, b + 1):
    print(chr(code), end=' ')


#  Простой шифр
text = input()

for ch in text:
    print(ord(ch), end=' ')


#  Шифр Цезаря
ALPHA = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
ciphertext = input()

text = ''
for ch in ciphertext:
    index_code_char = ALPHA.find(ch)
    text += ALPHA[index_code_char - n]

print(text)

#  Другое решение
n = int(input())
s = input()

for el in s:
    cur_n = ord("a") + (ord(el) - ord("a") + 26 - n) % 26
    print(chr(cur_n), end="")
