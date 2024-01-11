def insertion_sort(n, array):
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


n = int(input())
my_array = [int(i) for i in input().split()]
insertion_sort(n, my_array)
print(*my_array)
