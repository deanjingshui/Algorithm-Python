"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

示例 2:
输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

示例 3:
输入: amount = 10, coins = [10]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
"""
from typing import List


class Solution_dp:
    """
    author:fenghao
    date:2021.3.31
    思路：动态规划  自上而下/递归
              dp[i]的含义：可组成总金额为i的硬币组合数
              状态转移方程：
                 dp[i] = sum(dp[i - {t|t属于coins}])
          难点：如何去重？
    结果：错误，没有去重
    """
    def change(self, amount: int, coins: List[int]) -> int:
        result = 0
        # base case
        if amount <= 0:
            return 0

        for coin in coins:
            if amount == coin:
                result += 1
                continue
            result += self.change(amount-coin, coins)
        return result


class Solution_dp_leetcode:
    """
    author:leetcode
    date:2021.3.31
    思路：动态规划
                dp[i][j]的含义：硬币列表的前缀子区间 [0, i] 能够凑成总金额为 j 的组合数
                状态转移方程：dp[i][j] = sum(dp[i-1][j-coins[i]*t|t属于[0,j/coins[i]]])
                                      = dp[i-1][j-coins[i]*0) +
                                        dp[i-1][j-coins[i]*1) +
                                        ...
                                        dp[i-1][j-coins[i]*s) +
    """
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # 处理异常输入
        if n == 0:
            return 0
        dp = [[0 for i in range(amount+1)] for j in range(n)]

        # base case
        dp[0][0] = 1
        j = coins[0]
        while j <= amount:
            dp[0][j] = 1
            j += coins[0]

        for i in range(1, n):
            for j in range(amount+1):
                k = int(j/coins[i])
                for k in range(0, k+1):
                    dp[i][j] += dp[i-1][j-k*coins[i]]

        return dp[n-1][amount]


amount = 5
coins = [1, 2, 5]
my_sol = Solution_dp_leetcode()
print(my_sol.change(amount, coins))
