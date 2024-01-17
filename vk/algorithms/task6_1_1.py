def last_even(n, array):
    even = -1
    for i in range(n - 1, -1, -1):
        if array[i] % 2 == 0:
            even = array[i]
            return even

    return even


n = int(input())
try:
    my_array = [int(i) for i in input().split()]
    print(last_even(n, my_array))
except EOFError:
    print(-1)
