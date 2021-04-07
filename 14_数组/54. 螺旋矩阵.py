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
         注意：每次走完一个边，判断是否遍历完所有元素，及时跳出循环
    时间：O(m*n)
    空间：O(1)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        rows = len(matrix)
        columns = len(matrix[0])
        column_steps = columns      # 水平方向步进次数
        row_steps = rows - 1        # 竖直方向步进次数
        row_index = 0
        column_index = 0
        num = 0
        total = rows * columns
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
            if num == total:
                break
            column_steps -= 1
            # 由上往下
            for j in range(row_steps):
                row_index += 1
                result.append(matrix[row_index][column_index])
            num += row_steps
            if num == total:
                break
            row_steps -= 1
            # 由右往左
            for i in range(column_steps):
                column_index -= 1
                result.append(matrix[row_index][column_index])
            num += column_steps
            if num == total:
                break
            column_steps -= 1
            # 由下往上
            for j in range(row_steps):
                row_index -= 1
                result.append(matrix[row_index][column_index])
            num += row_steps
            if num == total:
                break
            row_steps -= 1

        return result


class Solution_peel_apple:
    """
    athor:力扣网友
    date:2021.4.7
    思路：“削苹果”
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]  # 巧用zip、[::-1]，将矩阵翻转90度，另外使用星号*解包运算简化了代码
        return res


class Solution_recursive:
    """
    athor:力扣网友+fenghao
    date:2021.4.7
    思路：递归
    """
    def helper(self, ):
        pass

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        column = len(matrix[0])
        # base case
        if row == 0:
            return []

        result = list()
        result += matrix[0]
        result += matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# my_sol = Solution()
my_sol = Solution_peel_apple()
print(my_sol.spiralOrder(matrix))
# print(matrix)
# print(*matrix)
# print(list(zip(*matrix)))