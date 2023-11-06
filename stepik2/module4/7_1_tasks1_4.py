#  Python is awesome
ITER = 10
OUT = 'Python is awesome!'

for i in range(ITER):
    print(OUT)


#  Повторяй за мной 1
text = input()
iterations = int(input())

for i in range(iterations):
    print(text)


#  Последовательность символов
CHAR_1 = 'A'
NUM_CHAR_1 = 3
ITER_CHAR_1 = 6
CHAR_2 = 'B'
NUM_CHAR_2 = 4
ITER_CHAR_2 = 5
CHAR_3 = 'E'
CHAR_4 = 'T'
NUM_CHAR_4 = 5
ITER_CHAR_4 = 9
CHAR_5 = 'G'

for i in range(ITER_CHAR_1):
    print(CHAR_1 * NUM_CHAR_1)
for i in range(ITER_CHAR_2):
    print(CHAR_2 * NUM_CHAR_2)
print(CHAR_3)
for i in range(ITER_CHAR_4):
    print(CHAR_4 * NUM_CHAR_4)
print(CHAR_5)


#  Звездный прямоугольник
NUM = 19
n = int(input())

for i in range(n):
    print('*' * NUM)
