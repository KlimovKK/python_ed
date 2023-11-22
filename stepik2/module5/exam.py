#  Каждый третий
line = input()

print(''.join([line[i] for i in range(len(line)) if i % 3 != 0]))

#  с циклом
s = input()
n = len(s)

new_s = ""
for i in range(n):
    if i % 3 == 0:
        continue

    new_s += s[i]

print(new_s)


#  Замени меня полностью
line = input()

print(line.replace('1', 'one'))


#  Удали меня полностью
line = input()

print(line.replace('@', ''))


#  Второе вхождение
line = input()

first_index = line.find('f')
second_index = line.find('f', first_index + 1)
if first_index != - 1:
    res = second_index
else:
    res = first_index + second_index

print(res)


#  Переворот
LETTER = 'h'

line = input()

start = line.find(LETTER)
end = line.rfind(LETTER)
res = line[:start] + line[end:start:-1] + line[end:]
print(res)
