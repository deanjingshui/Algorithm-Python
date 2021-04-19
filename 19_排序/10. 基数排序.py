"""
基数排序
"""


def radix_sort(nums):
    if not nums:
        return []

    _max = max(nums)
    maxDigit = len(str(_max))  # 最大位数
    bucketList = [[] for _ in range(10)]
    # 从低位开始排序
    div, mod = 1, 10
    for i in range(maxDigit):
        for num in nums:
            bucketList[num % mod // div].append(num)
        div *= 10
        mod *= 10
        idx = 0
        for j in range(10):
            for item in bucketList[j]:
                nums[idx] = item
                idx += 1
            bucketList[j] = []
    return nums


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50, 12, 54]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', radix_sort(nums)))
