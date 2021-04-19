"""
计数排序
"""


def counting_sort(nums):
    """
    author:fenghao
    date:2021.4.13
    局限：只适用于非负整数
    """
    result = list()
    # 找出待排序数组中的最大值
    max_num = max(nums)
    count = [0]*(max_num+1)

    # 统计数组中每个值为i的元素出现的次数
    for i in nums:
        count[i] += 1

    # 数据回写
    for i in range(max_num+1):
        for j in range(count[i]):
            result.append(i)
    return result


def counting_sort_classic(nums):
    """
    auhor: https://blog.csdn.net/ThinkWon/article/details/101544159
    date:2021.4.19
    利用offset
        <1 节省数组空间
        <2 可适用于包含负整数的序列
    """
    if not nums: return []

    n = len(nums)
    _min = min(nums)
    _max = max(nums)
    count = [0] * (_max - _min + 1)

    for num in nums:
        count[num - _min] += 1

    j = 0
    for i in range(n):
        while count[j] == 0:
            j += 1
        nums[i] = j + _min
        count[j] -= 1

    return nums


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50, 12, 54]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', counting_sort(nums)))
    print('{:>12} {}'.format('after 排序:', counting_sort_classic(nums)))
