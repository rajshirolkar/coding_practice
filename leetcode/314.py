# from typing import List


# def searchRange(nums: List[int], target: int) -> List[int]:
#     l, r = 0, len(nums) - 1
#     res = []
#     if not nums:
#         return [-1, -1]
#     print("1")
#     mid = 0
#     while l < r:
#         mid = (l + r) // 2
#         print("mid : ", mid)
#         if nums[mid] < target:
#             l = mid + 1
#             print("2")
#         elif nums[mid] > target:
#             r = mid - 1
#         elif nums[mid] == target:
#             print("we here ")
#             res.append(mid)
#             print("this")
#             break
#             print("???")
#         print("3")
#     if not res:
#         return [-1, -1]
#     elif len(nums) == 1 and res:
#         res.append(mid)
#         return res

#     l, r = mid - 1, mid + 1
#     while l >= 0 or r < len(nums):
#         if l >= 0 and nums[l] == target:
#             res.insert(0, l)
#             l -= 1
#         if r < len(nums) and nums[r] == target:
#             res.append(r)
#             r += 1
#     return res


# print(searchRange([5, 7, 7, 8, 8, 10], 7))
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]

    # First pass: find the target
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            break
    else:  # No target found
        return [-1, -1]

    # Second pass: find the left boundary of the target
    print(mid)
    left = mid
    while left > 0 and nums[left - 1] == target:
        left -= 1

    # Third pass: find the right boundary of the target
    right = mid
    while right < len(nums) - 1 and nums[right + 1] == target:
        right += 1

    return [left, right]


# Test the function with your example
print(searchRange([5, 7, 7, 7, 8, 8, 10], 7))  # It should print [1, 2]
