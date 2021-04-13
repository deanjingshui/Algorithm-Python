"""
计数排序
"""


def count_sort(nums):
    result = list()
    # 找出待排序的数组中最大和最小的元素
    min_num = nums[0]
    max_num = nums[0]
    for i in nums:
        min_num = min(min_num, i)
        max_num = max(max_num, i)
    count = [0]*(max_num+1)

    # 统计数组中每个值为i的元素出现的次数
    for i in nums:
        count[i] += 1

    # 数据回写
    for i in range(max_num+1):
        for j in range(count[i]):
            result.append(i)
    return result


def count_sort_optimize(nums):
    """
    https://blog.csdn.net/ThinkWon/article/details/101544159
    利用offset
        <1 节省数组空间
        <2 可适用于包含负整数的序列
    """
    pass


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50, 12, 54]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', count_sort(nums)))
