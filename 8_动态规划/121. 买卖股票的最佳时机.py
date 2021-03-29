"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2021.3.28
    思路：
        一次遍历
            以遍历到的元素为卖出点
            并维护已遍历过的前序数组中的最小值
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        if n <= 1:
            return 0
        min_price = prices[0]  # 前序数组中的最小值
        for i in range(1, n):
            result = max(result, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        return result


class Solution_dp:
    """
    author:w3
    date:2021.3.28
    思路：
         动态规划
            dp[i]的含义：第i天卖出时能获取的最大利润
            状态转移方程：
                有2种前置状态
                    前一天没有买：则前一天卖出的最大利润，补上股票前一天与今天的差价
                    前一天才买：则股票前一天与今天的差价
                dp[i] = max(dp[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])

        另外：这道题与"最大子序和"本质一样（将该题的数组经过diff操作...）

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(dp[i-1]+prices[i]-prices[i-1], prices[i]-prices[i-1])
            result = max(result, dp[i])
        return result


prices = [7,1,5,3,6,4]
# my_sol = Solution()
my_sol = Solution_dp()
print(my_sol.maxProfit(prices))
