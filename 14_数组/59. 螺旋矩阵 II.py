"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

https://leetcode-cn.com/problems/spiral-matrix-ii/
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        total = n * n
        top, bottom = 0, n-1
        left, right = 0, n-1
        row, column = 0, 0
        num = 0
        while True:
            for column in range(left, right+1):
               num += 1
               matrix[row][column] = num
            top += 1
            if top > bottom:
                break
            for row in range(top, bottom+1):
                num += 1
                matrix[row][column] = num
            right -= 1
            if left > right:
                break
            for column in range(right, left-1, -1):
                num += 1
                matrix[row][column] = num
            bottom -= 1
            if top > bottom:
                break
            for row in range(bottom, top-1, -1):
                num += 1
                matrix[row][column] = num
            left += 1
        return matrix


n = 3
my_sol = Solution()
print(my_sol.generateMatrix(n))
