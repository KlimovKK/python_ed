def is_price_found(len_arr, price_list, price):
    left = 0
    right = len_arr
    if right == 0 or price < price_list[0] or price > price_list[right - 1]:
        return "false"

    while left <= right:
        mid = (left + right) // 2
        if price < price_list[mid]:
            right = mid - 1
        elif price > price_list[mid]:
            left = mid + 1
        else:
            return "true"

    return "false"


n = int(input())
goods = [int(i) for i in input().split()]
price_tag = int(input())
print(is_price_found(n, goods, price_tag))
