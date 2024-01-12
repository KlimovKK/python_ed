def merge_sort(array):
    if len(array) <= 1:
        return array

    mid_index = len(array) // 2
    left = array[:mid_index]
    right = array[mid_index:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged_arr = []
    l_index, r_index = 0, 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            merged_arr.append(left[l_index])
            l_index += 1
        else:
            merged_arr.append(right[r_index])
            r_index += 1
    while l_index < len(left):
        merged_arr.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        merged_arr.append(right[r_index])
        r_index += 1

    return merged_arr


n = int(input())
my_array = [int(i) for i in input().split()]
print(*merge_sort(my_array))
