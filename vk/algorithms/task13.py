def max_in_tree(n, root):
    if 2 * root + 2 < n:
        return max_in_tree(n, 2 * root + 2)
    else:
        return root


n = int(input())
my_array = [int(i) for i in input().split()]
max_val = my_array[max_in_tree(n, 0)]
print(max_val)
