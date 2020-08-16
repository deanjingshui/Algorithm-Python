"""
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
注意:

nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2020.8.14
    思路：
        1、先找到数组中出现次数最多的那个元素（可能多个）
        2、找到出现次数最多元素（可能多个）首次和末次出现的位置，位置索引差值+1为长度，长度的最小值即结果
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_nums = [nums[0]]
        max_count = nums.count(nums[0])
        for i in set(nums):
            if  i != nums[0]:
                i_count = nums.count(i)
                if i_count > max_count:
                    max_count = i_count
                    max_nums = [i]
                elif i_count == max_count:
                    max_nums.append(i)
        ret = len(nums)
        len_nums = len(nums)
        for num in max_nums:
            index_first = nums.index(num)
            index_last = len_nums - nums[::-1].index(num) - 1
            len_tmp = index_last - index_first + 1
            if len_tmp < ret:
                ret = len_tmp
        return ret

nums = [1, 2, 2, 3, 1, 4, 2]
my_sol = Solution()
print(my_sol.findShortestSubArray(nums))