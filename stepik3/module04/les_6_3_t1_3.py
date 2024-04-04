#  Вершина параболы
a, b, c = [int(input()) for _ in range(3)]

coord = (-b / (2 * a), (4 * a * c - b ** 2) / (4 * a))

print(coord)
