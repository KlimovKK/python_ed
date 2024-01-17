def index_search(n, array, needle):
    left = 0
    right = n - 1
    index = 0

    while array[left] < needle < array[right]:
        if array[left] == array[right]:
            break
        index = left + (right - left)*(needle - array[left]) // (array[right] - array[left])
        if array[index] > needle:
            right = index - 1
        elif array[index] < needle:
            left = index + 1
        else:
            return index
    index += 1

    if array[left] == needle:
        return left
    if array[right] == needle:
        return right

    return index


n = int(input())
my_array = [int(i) for i in input().split()]
num = int(input())
print(index_search(n, my_array, num))
