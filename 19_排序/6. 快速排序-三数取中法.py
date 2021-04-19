"""
快排 三数取中法选取基准值
author:https://www.cnblogs.com/chengxiao/p/6262208.html
date:2021.4.19
"""


def quick_sort(nums):
    helper(nums, 0, len(nums) - 1)


def helper(nums, left, right):
    if left < right:
        dealPivot(nums, left, right)   # 获取枢纽值，并将其放在当前待处理序列末尾（倒数第二）
        pivot = right - 1   # 枢纽值被放在序列末尾(倒数第二)
        i = left            # 左指针
        j = right - 1       # 右指针
        while True:
            while j > i and nums[i] < nums[pivot]:
                i += 1
            while j > i and nums[j] > nums[pivot]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        if i < pivot:
            nums[i], nums[pivot] = nums[pivot], nums[i]
        helper(nums, left, i-1)
        helper(nums, i+1, right)


def dealPivot(nums, left, right):
    mid = (left + right) // 2
    if nums[left] > nums[mid]:
        nums[left], nums[mid] = nums[mid], nums[left]
    if nums[left] > nums[right]:
        nums[left], nums[right] = nums[right], nums[left]
    if nums[right] < nums[mid]:
        nums[right], nums[mid] = nums[mid], nums[right]
    nums[right-1], nums[mid] = nums[mid], nums[right-1]


nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
res_stable = sorted(nums)
quick_sort(nums)
print(nums)
print(res_stable)
assert all(map(lambda x: x[0] == x[1], zip(nums, res_stable)))
