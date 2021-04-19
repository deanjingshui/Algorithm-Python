"""
快速排序
author:https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/QuickSort.py
"""


def quick_sort(nums):
    helper(nums, 0, len(nums) - 1)


def helper(nums, first, last):
    if first < last:
        splitPoint = partition(nums, first, last)

        helper(nums, first, splitPoint - 1)
        helper(nums, splitPoint + 1, last)


def partition(nums, first, last):
    pivot = nums[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and nums[left] <= pivot:  # 先比较index, 不然数组会越界
            left += 1
        while right >= left and nums[right] >= pivot:
            right -= 1
        if left > right:
            done = True
        else:
            nums[left], nums[right] = nums[right], nums[left]
    nums[right], nums[first] = nums[first], nums[right]

    return right


nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(nums)
print(nums)
