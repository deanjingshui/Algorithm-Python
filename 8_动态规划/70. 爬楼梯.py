"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
"""


class Solution:
    """
    思路：
        动态规划
        考虑最后一步肯定只有2种走法，即走1个台阶或者走2个台阶
            如果走1个台阶，即走到n-1个台阶
            如果走2个台阶，即走到n-2个台阶
        状态转移方程：
            dp[n]含义  走到第n个台阶有多少种走法
            dp[n] = dp[n-1] + dp[n-2]

            base case
            dp[0] = 1
            dp[1] = 1

        自顶向下（递归）

    结果：大用例超出时间限制
    """
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution_cache:
    """
    思路：
        动态规划
        自顶向下（递归 + 备忘录）
            普通递归有大量的重复计算
        难点：缓存如何实现？
                    类的属性
                    辅助函数
        易错：dp索引超出边界

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def helper(self, n, dp):
        """
        辅助函数
        """
        if dp[n] == -1:  # 需要缓存
            if n > 1:
                dp[n] = self.helper(n-1, dp) + self.helper(n-2, dp)
            else:
                dp[n] = 1
        return dp[n]

    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)  # 缓存  易错：dp索引超出边界 dp = [-1] * n
        return self.helper(n, dp)


class Solution_bottom2top:
    """
    思路：
        动态规划
        自底向上（迭代）

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


class Solution_bottom2top_modify:
    """
    思路：
        动态规划
        自底向上（迭代）
        使用“滚动数组法”降低时间复杂度

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def climbStairs(self, n: int) -> int:
        dp1 = 1
        dp2 = 1
        for i in range(2, n+1):
            tmp = dp1 + dp2
            dp1 = dp2
            dp2 = tmp
        return dp2

n = 38
# my_sol = Solution()
# print(my_sol.climbStairs(n))
my_sol = Solution_cache()
print(my_sol.climbStairs(n))
my_sol = Solution_bottom2top()
print(my_sol.climbStairs(n))
my_sol = Solution_bottom2top_modify()
print(my_sol.climbStairs(n))