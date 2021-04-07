"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

https://leetcode-cn.com/problems/spiral-matrix/
"""
from typing import List


class Solution:
    """
    athor:fenghao
    date:2021.4.7
    思路：找规律
            对于m行n列的矩阵
            由左往右 n 次
            由上往下 m-1 次
            由右往左 n-1 次
            由下往上 m-2 次
            ...
         注意：遍历完所有元素，及时跳出循环
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        row = len(matrix)
        column = len(matrix[0])
        column_steps = column      # 水平方向步进次数
        row_steps = row - 1        # 竖直方向步进次数
        row_index = 0
        column_index = 0
        num = 0
        sum = row * column
        while column_steps > 0 or row_steps > 0:
            # 由左往右
            if column_index == 0 and row_index == 0:
                for i in range(column_steps):
                    column_index = i
                    print((row_index, column_index))
                    result.append(matrix[row_index][column_index])
            else:
                for i in range(column_steps):
                    column_index += 1
                    result.append(matrix[row_index][column_index])
            num += column_steps
            if num == sum:
                break
            column_steps -= 1
            # 由上往下
            for j in range(row_steps):
                row_index += 1
                result.append(matrix[row_index][column_index])
            num += row_steps
            if num == sum:
                break
            row_steps -= 1
            # 由右往左
            for i in range(column_steps):
                column_index -= 1
                result.append(matrix[row_index][column_index])
            num += column_steps
            if num == sum:
                break
            column_steps -= 1
            # 由下往上
            for j in range(row_steps):
                row_index -= 1
                result.append(matrix[row_index][column_index])
            num += row_steps
            if num == sum:
                break
            row_steps -= 1

        return result


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
my_sol = Solution()
print(my_sol.spiralOrder(matrix))

