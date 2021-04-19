"""
冒泡排序
"""


def bubble_sort(nums):
    """
    author：fenghao
    """
    n = len(nums)
    for passnum in range(n-1):  # 轮询次数passnum是列表长度减去1
        for i in range(n-1-passnum):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        print('{:>12} {}'.format(str(passnum)+' time:', nums))
    return nums


def bubble_sort_modify(nums):
    """
    bubble sort
    author：https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BubbleSort.py
    思路： 改进的冒泡排序, 加入一个校验, 如果某次循环发现没有发生数值交换, 直接跳出循环
    """
    exchange = True
    passnum = len(nums) - 1
    while passnum >= 1 and exchange:
        exchange = False
        for i in range(passnum):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                exchange = True
        passnum -= 1
        print('{} time: {}'.format(passnum, nums))
    return nums


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', bubble_sort(nums)))
