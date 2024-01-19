def exp_search(n, data, needle):
    border = 1
    last_el = n - 1
    while border < last_el and data[border] < needle:
        border *= 2
        if border > last_el:
            border = last_el

    return border // 2, border


n = int(input())
my_array = [int(i) for i in input().split()]
num = int(input())
print(*exp_search(n, my_array, num))
