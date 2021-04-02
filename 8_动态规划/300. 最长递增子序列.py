"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
 
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

示例 2：
输入：nums = [0,1,0,3,2,3]
输出：4

示例 3：
输入：nums = [7,7,7,7,7,7,7]
输出：1
 

提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104

进阶：
你可以设计时间复杂度为 O(n^2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
"""
from typing import List


class Solution:
    """
    author:w3
    date:2021.3.27
    思路：
          动态规划
                dp[i]的含义：以第i个元素结尾的最长上升子序列的长度
                状态转移方程：
                    dp[i]=max( {dp[j]|j属于[0,i),nums[i]>nums[j]} U {0} ) + 1

          难点：  <1 前置状态有很多个    {dp[j]|j属于[0,i),nums[i]>nums[j]}
                  <2 需意识到，dp[n]并不是结果，而是取dp列表中的最大值为结果

    时间复杂度：O(n^2)
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        # base case
        dp[0] = 1
        ret = 1
        for i in range(1, n):
            preLen = 0
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    preLen = max(preLen, dp[j])
            dp[i] = preLen + 1
            ret = max(ret, dp[i])
        return ret

# nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
my_sol = Solution()
print(my_sol.lengthOfLIS(nums))