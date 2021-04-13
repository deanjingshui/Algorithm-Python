"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
"""
from typing import List


class Solution:
    """
    author；fenghao
    date:2021.4.13
    思路：思考不使用额外的空间
         将矩阵看成一圈一圈组成的“环形数组”组成，旋转90度，就是将每一圈“环形数组”都转90度
    时间：O(n^2)
    空间：O(1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        levels = n//2  # 矩阵的层数
        nums = n      # 每层的元素个数
        for level in range(levels):
            # 该层元素（“环形数组”）顺时针移动nums个元素
            for num in range(nums-1):
                tmp = matrix[level][level+num]
                matrix[level][level+num] = matrix[(n-1)-level-num][level]
                matrix[(n-1)-level-num][level] = matrix[(n-1)-level][(n-1)-level-num]
                matrix[(n-1)-level][(n-1)-level-num] = matrix[level+num][(n-1)-level]
                matrix[level+num][(n-1)-level] = tmp
            nums -= 2


n = 4
matrix = [[4*i+j for j in range(1, n+1)] for i in range(n)]
print(matrix)
my_sol = Solution()
my_sol.rotate(matrix)
print(matrix)
