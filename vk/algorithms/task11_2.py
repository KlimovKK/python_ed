def min_in_tree(n, root):
    if 2 * root + 1 < n:
        return min_in_tree(n, 2 * root + 1)
    else:
        return root


n = int(input())
my_array = [int(i) for i in input().split()]
min_val = my_array[min_in_tree(n, 0)]
print(min_val)
