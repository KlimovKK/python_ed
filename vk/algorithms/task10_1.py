from collections import Counter


def is_most_half(n, data):
    most_common_el = Counter(data).most_common(1)
    if most_common_el[0][1] > n // 2:
        return most_common_el[0][0]

    return -1


n = int(input())
my_array = input().split()
print(is_most_half(n, my_array))
