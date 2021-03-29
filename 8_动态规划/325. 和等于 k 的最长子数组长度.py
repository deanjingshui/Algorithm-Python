"""
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。

注意:
 nums 数组的总和是一定在 32 位有符号整数范围之内的。

示例 1:
输入: nums = [1, -1, 5, -2, 3], k = 3
输出: 4 
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。

示例 2:
输入: nums = [-2, -1, 2, 1], k = 1
输出: 2 
解释: 子数组 [-1, 2] 和等于 1，且长度最长。

进阶:
你能使时间复杂度在 O(n) 内完成此题吗?
"""


def func(nums, K):
    """
    author:w3
    date:2021.3.28
    """
    ret = 0
    mapping = dict()
    mapping[0] = 0
    prefixSum = 0
    n = len(nums)
    for i in range(n):
        prefixSum += nums[i]
        if prefixSum - K in mapping:
            t = mapping.get(prefixSum - K)
            ret = max(ret, i - t + 1)
        if prefixSum not in mapping:
            mapping[prefixSum+1] = i
    return ret


nums = [1, -1, 5, -2, 3]
k = 3
print(func(nums, k))