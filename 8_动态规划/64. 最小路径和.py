"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

示例 2：
输入：grid = [[1,2,3],[4,5,6]]
输出：12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2021.3.27
    思路：
        动态规划
            走到[m][n]之前的一步，必然先走到[m-1][n]或者[m][n-1]（即有2个前置状态）
            dp[m][n]含义：从[0][0]走到[m][n]的最小路径和
            状态转移方程：
                              grid[0][0]                                 当m=n=0
                  dp[m][n]    dp[0][n-1] + grid[0][n]                    当m=0，n>0
                              dp[m-1][0] + grid[m][0]                    当n=0，m>0
                              min(dp[m-1][n] + dp[m][n-1]) + grid[m][n]  当m>0,n>0
        特点：base case还有第0行和第0列

    时间复杂度：O(m*n)
    空间复杂度：O(m*n)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)     # row
        n = len(grid[0])  # column
        # dp = [[0] * n] * m   # bug 此法创造的m*n矩阵，修改其中一个元素，会导致整列被修改
        dp = [[0 for i in range(n)] for j in range(m)]

        # 先处理base case
        # [0][0]元素
        dp[0][0] = grid[0][0]
        # 第0列
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # 第0行
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]


# grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
my_sol = Solution()
print(my_sol.minPathSum(grid))


a = [[0]*3]*3
a[1][1] = 1
pass
m = 4
n =3
b =[[0 for i in range(n)] for j in range(m)]
b[1][1] = 1
pass
