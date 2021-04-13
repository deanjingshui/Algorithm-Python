"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

https://leetcode-cn.com/problems/spiral-matrix/
"""
from typing import List


class Solution_simulation:
    """
    author:fenghao
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
        rows = len(matrix)          # 矩阵行数
        columns = len(matrix[0])    # 矩阵列数
        column_steps = columns      # 水平方向步进次数
        row_steps = rows - 1        # 竖直方向步进次数
        row_index = 0               # 当前行坐标
        column_index = -1           # 当前列坐标，初始位置不在（0,0），而是（0，-1）
        num = 0                     # 已遍历元素个数
        total = rows * columns      # 矩阵元素总个数
        while column_steps > 0 or row_steps > 0:
            # 由左往右
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


class Solution_leetcode:
    """
    author:力扣网友 https://leetcode-cn.com/problems/spiral-matrix/solution/cxiang-xi-ti-jie-by-youlookdeliciousc-3/
    date:2021.4.13
    思路：设定上下左右边界
             区别于“模拟”的思路，这里不再关心每次要走多少步，而只关心是否走到了“边界”
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = list()
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        row, column = 0, 0
        while True:
            for column in range(left, right + 1):
                result.append(matrix[row][column])
            top += 1
            if top > bottom:
                break
            for row in range(top, bottom + 1):
                result.append(matrix[row][column])
            right -= 1
            if left > right:
                break
            for column in range(right, left - 1, -1):
                result.append(matrix[row][column])
            bottom -= 1
            if top > bottom:
                break
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][column])
            left += 1
            if left > right:
                break
        return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# my_sol = Solution()
my_sol = Solution_leetcode()
print(my_sol.spiralOrder(matrix))
# print(matrix)
# print(*matrix)
# print(list(zip(*matrix)))
