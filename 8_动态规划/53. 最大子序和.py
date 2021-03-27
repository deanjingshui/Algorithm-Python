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


class Solution_force:
    """
    author:fenghao
    date:2020.8.22
    思路：
        暴力穷举所有连续子序列
    时间复杂度：O(n^2)  力扣提交超出时间限制
    """
    def maxSubArray(self, nums: List[int]) -> int:
        len_array = len(nums)
        sum_max = nums[0]
        for i in range(len_array):
            sum_tmp = nums[i]   # 累积和
            sum_max = max(sum_max, sum_tmp)
            for j in range(i+1, len_array):
                sum_tmp += nums[j]
                sum_max = max(sum_max, sum_tmp)
        return sum_max


class Solution_iterate:
    """
    author:fenghao
    date:2020.8.19
    思路：
        从左往右遍历，遇到sum<0就重新开始计算

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


class Solution_iterate_modify:
    """
    author:力扣
    date:2021.3.27
    思路：
        提高可读性
            其实不需要判断列表是否全是负值

    时间复杂度：O(n)
    """

    # def maxSubArray(self, nums: List[int]) -> int:
    #     len_array = len(nums)
    #     sum_max = nums[0]
    #     sum_tmp = max(0, nums[0])        # 累积和,非负
    #     for i in range(1,len_array):
    #         if sum_max < 0:
    #             sum_max = max(sum_max, nums[i])
    #             sum_tmp = max(0, nums[i])
    #         else:
    #             sum_tmp += nums[i]
    #             sum_max = max(sum_max, sum_tmp)
    #             # 判断是否将累积和清零，注意维持累积和为非负,否则没必要累加
    #             sum_tmp = max(0, sum_tmp)
    #     return sum_max

    def maxSubArray(self, nums: List[int]) -> int:
        len_array = len(nums)
        ret = nums[0]
        sum = 0
        for i in range(len_array):
            sum += nums[i]
            ret = max(ret, sum)
            if sum < 0:
                sum = 0
        return ret


class Solution_dp:
    """
    author:w3
    date:2021.3.27
    思路：
        动态规划
            dp[i]的含义：以第1个元素结尾的子数组的最大和
            状态转移方程：
                dp[i]=max(dp[i-1]+nums[i], nums[i])
                base case
                dp[0] = nums[0]

        难点：想不到怎么用动态规划
        注意：结果并不是dp[n]，而是对dp[i]进行取max

    时间复杂度：O(n)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [nums[0]] * n
        dp[0] = nums[0]
        ret = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            ret = max(ret, dp[i])    # 注意：结果并不是dp[n]
        return ret


nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,1]
# nums = [-1,1,2,1]
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1,2]
my_sol = Solution_iterate_modify()
print(my_sol.maxSubArray(nums))
my_sol = Solution_dp()
print(my_sol.maxSubArray(nums))