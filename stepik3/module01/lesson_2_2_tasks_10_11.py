#  Кремниевая долина
def sequence_search(line: str):
    """
    Поиск последовательности в переданной строке
    """
    index = 0
    counter = 0
    for c in SEQ:
        if line.find(c, index) == -1:
            return
        else:
            index = line.find(c, index) + 1
            counter += 1

    return counter


SEQ = 'anton'
refrigerators = [input() for i in range(int(input()))]

ref_numbers = []
for i, el in enumerate(refrigerators):
    if sequence_search(el) == len(SEQ):
        ref_numbers.append(i + 1)

if ref_numbers:
    print(*ref_numbers)

#  Роскомнадзор запретил букву а
a = ord('а')
ALPHA = ''.join([chr(i) for i in range(a, a + 32)])
word = input() + ' запретил букву'

for c in ALPHA:
    if c in word:
        print(word + ' ' + c)
    else:
        continue

    word = word.replace(c, '')
    word = word.replace('  ', ' ').strip()

    if not word.strip():
        break
#  Другое решение
word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()
