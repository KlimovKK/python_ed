from typing import List


def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
    res = []
    for i, el in enumerate(zip(nums1, nums2)):
        if el[0] < el[1]:
            res.append(i)
    return res


# code = []
# while data := input():
#    code.append(data)
# code = "\n".join(code)
# exec(code)
