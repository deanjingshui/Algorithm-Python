"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
"""
from typing import List


class Solution_1:
    """
    author:fenghao
    date:2020.8.22
    思路：
        暴力穷举所有子序列
    时间复杂度：O(n^2)  力扣提交超出时间限制
    """
    def maxSubArray(self, nums: List[int]) -> int:
        sum_max = nums[0]
        len_array = len(nums)
        for i in range(len_array):
            sum_tmp = nums[i]   # 累积和
            sum_max = max(sum_max, sum_tmp)
            for j in range(i+1, len_array):
                sum_tmp += nums[j]
                sum_max = max(sum_max, sum_tmp)
        return sum_max


class Solution_2:
    """
    author:fenghao
    date:2020.8.19
    思路：
        一次性遍历
        难点是考虑清楚条件
    时间复杂度：O(n)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num < 0:          # 考虑元素全是负值的情况，避免影响后面的算法
            return max_num

        sum_max = nums[0]
        sum_tmp = nums[0]   # 维护一个当前指针前的非负的累加和，会视情况清零
        for num in nums[1:]:
            if sum_max < 0:
                if num > 0:
                    sum_tmp = num
                else:
                    sum_tmp = 0    # 清零
                sum_max = max(sum_max, num)
            else:
                if sum_tmp + num <= 0:   # 一旦加上新元素后变为小于等于0，则清零
                    sum_tmp = 0    # 清零
                else:
                    sum_tmp += num
                sum_max = max(sum_max, sum_tmp)
        return sum_max


class Solution_3:
    """
    author:fenghao
    date:2020.8.19
    思路：
        增强可读性
    时间复杂度：O(n)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        pass


nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,1]
my_sol = Solution_1()
print(my_sol.maxSubArray(nums))