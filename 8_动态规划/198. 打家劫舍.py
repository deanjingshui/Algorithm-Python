"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
"""
from typing import List


class Solution_dp:
    """
    author:fenghao
    date:2021.3.29
    思路：动态规划
            dp[i][j]的含义：第i家偷（j=1）和不偷（j=0）分别获得的最大金额
            状态转移方程：          max(dp[i-1][1], dp[i-1][0])    j=0
                        dp[i][j] =
                                   dp[i-1][0] + nums[i]           j=1
    时间复杂度：O(2n)
    空间复杂度：O(2n)
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(2)] for j in range(n)]

        # base case
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            for j in range(2):
                if j == 0:
                    dp[i][j] = max(dp[i-1][1], dp[i-1][0])
                else:
                    dp[i][j] = dp[i-1][0] + nums[i]

        return max(dp[n-1][0], dp[n-1][1])


class Solution_dp_leetcode:
    """
    author:leetcode
    date:2021.3.29
    思路：
          动态规划
            dp[i]的含义：有i户人家时可获得的最大金额
            状态转移方程：
                有2个前置状态
                    偷第i人家，则第i-1户不能偷   dp[i-2] + nums[i]
                    不偷第i户人家    dp[i-1]
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 0:
            return 0

        # base case
        if n > 0:
            dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]


class Solution_dp_leetcode_modify_space:
    """
    author:leetcode
    date:2021.3.29
    思路：
          动态规划 + 滚动数组
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            实际上只需要知道最后的状态，观察状态转移方程可知更新每个状态只依赖之前的2个状态

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        # base case
        if n > 0:
            first = nums[0]
        if n > 1:
            second = max(nums[0], nums[1])

        for i in range(2, n):
            tmp = second
            second = max(first + nums[i], second)
            first = tmp
        return second

# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
nums = [2,1,1,2]
my_sol = Solution_dp_leetcode_modify_space()
print(my_sol.rob(nums))
