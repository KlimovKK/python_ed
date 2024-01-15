def even_first(n, array):
    even_index = 0
    for i in range(n):
        if array[i] % 2 == 0:
            array[i], array[even_index] = array[even_index], array[i]
            even_index += 1

    return array


n = int(input())
my_array = [int(i) for i in input().split()]
my_array = even_first(n, my_array)
print(*my_array)
