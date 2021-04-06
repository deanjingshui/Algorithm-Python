from typing import List


class Solution:
    """
    author:《你也能看得懂的python算法书》+fenghao
    date:2021.4.6
    思路：深度优先遍历
            步骤：
                1>先找岛屿，自左向右、自上向下扫描
                2>一旦找到岛屿，以当前位置为root，从上下左右4个方向深度优先遍历
            难点：访问过的位置需要标记，避免重复计算
    时间：O(m*n) m,n是grid的行,列数   每个网格至多访问1次
    空间：O(m*n) 递归时，最大情况下递归深度为整个网格大小（全1）
    """
    def dps(self, grid, i, j):
        grid[i][j] = 2  # 做标记，已访问
        area = 1
        if i-1 > -1 and grid[i-1][j] == 1:
            area += self.dps(grid, i-1, j)
        if i+1 < len(grid) and grid[i+1][j] ==1:
            area += self.dps(grid, i+1, j)
        if j-1 > -1 and grid[i][j-1] == 1:
            area += self.dps(grid, i, j-1)
        if j+1 < len(grid[0]) and grid[i][j+1] == 1:
            area += self.dps(grid, i, j+1)
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        row = len(grid)
        column = len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:  # 发现岛屿
                    maxArea = max(maxArea, self.dps(grid, i, j))

        return maxArea


grid =  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
my_sol = Solution()
print(my_sol.maxAreaOfIsland(grid))
