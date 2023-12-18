import collections
from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    deq_nums = deque(nums)
    for _ in range(n):
        deq_nums.appendleft(deq_nums.pop())

    return list(deq_nums)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
