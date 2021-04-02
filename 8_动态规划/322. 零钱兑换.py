"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
 

说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    """
    author:http://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/dong-tai-gui-hua-xiang-jie-jin-jie
    date:2020.7.28
    思路：递归
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        ret = float('INF')
        for c in coins:
            subproblem = self.coinChange(coins, amount - c)
            if subproblem == -1:
                continue
            ret = min(ret, 1 + subproblem)
        return ret


class Solution_dp:
    """
    author:fenghao
    date:2021.3.31
    思路：动态规划(自底向上)
            dp[i]的含义：组成金额为i最少需要的硬币个数
            状态转移方程：dp[i] = min(dp[i - {t|t属于coins}]) + 1

    时间复杂度：O(n * amount)，n是可选硬币的种类数，amount是题目输入的面值
    空间复杂度：O(amount)，dp数组的大小为 amount
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        # base case
        dp[0] = 0

        for i in range(1, amount+1):
            if i in coins:
                dp[i] = 1
                continue
            tmp = []
            for coin in coins:
                if i-coin > 0 and dp[i-coin] != -1:
                    tmp.append(dp[i-coin])
            if len(tmp) != 0:
                dp[i] = min(tmp) + 1
            else:
                dp[i] = -1

        return dp[amount]


coins = [1, 2, 5]
amount = 11
my_sol = Solution()
print(my_sol.coinChange(coins, amount))

