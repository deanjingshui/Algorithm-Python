"""
选择排序
selection sort
"""


def selection_sort(nums):
    """
    author：fenghao
    """
    n = len(nums)
    for passnum in range(n - 1):  # 轮询次数passnum是列表长度减去1
        temp_max_index = 0
        for i in range(n - passnum):
            if nums[i] > nums[temp_max_index]:
                temp_max_index = i
        nums[n-passnum-1], nums[temp_max_index] = nums[temp_max_index], nums[n-passnum-1]
        print('{:>12} {}'.format(str(passnum) + ' time:', nums))

    return nums


if __name__=="__main__":
    nums = [54, 36, 12, 29, 50]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', selection_sort(nums)))

