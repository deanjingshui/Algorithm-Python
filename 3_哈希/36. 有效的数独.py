"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
示例 2:

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-sudoku
"""
from typing import List


class Solution_force:
    """
    date:2020.9.22
    author:fenghao
    思路：朴素解法   哈希  按行、列、块分别遍历3次
    时间复杂度：O(3*n)   n为所有元素的个数
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 按行判断
        for row in board:
            cache = set()
            for i in row:
                if i in cache:
                    return False
                elif i != '.':
                    cache.add(i)
        # 按列判断
        column = 0
        while column < 9:
            row = 0
            cache = set()
            while row < 9:
                i = board[row][column]
                if i in cache:
                    return False
                elif i != '.':
                    cache.add(i)
                row += 1
            column += 1
        # 按块判断
        bulk_index = [[[0,0],[2,2]],   # 每个九宫格的左上角、右下角元素的行列索引
                      [[0,3],[2,5]],
                      [[0,6],[2,8]],
                      [[3,0],[5,2]],
                      [[3,3],[5,5]],
                      [[3,6],[5,8]],
                      [[6,0],[8,2]],
                      [[6,3],[8,5]],
                      [[6,6],[8,8]],]
        for index in bulk_index:
            row_min, row_max, column_min, column_max = self.get_bulk(index)
            cache = set()
            row = row_min
            while row < row_max + 1:
                column = column_min
                while column < column_max + 1:
                    i = board[row][column]
                    if i in cache:
                        return False
                    elif i != '.':
                        cache.add(i)
                    column += 1
                row += 1
        return True

    def get_bulk(self, index):
        column_min = index[0][1]
        column_max = index[1][1]
        row_min = index[0][0]
        row_max = index[1][0]
        return row_min, row_max, column_min, column_max


class Solution_iterate_once_hash:
    """
    date:2020.9.22
    author:力扣+fenghao
            https://leetcode-cn.com/problems/valid-sudoku/solution/36-jiu-an-zhao-cong-zuo-wang-you-cong-shang-wang-x/
    思路：哈希  只遍历一遍
          由于board中的整数限定在1到9的范围内，因此可以分别建立哈希表来存储任一个数在相应维度上是否出现过。维度有3个：所在的行，所在的列，所在的box。
          记录每个数字出现的位置（行、列、九宫格）  {5:(0,0,0), 3:(0,1,0)}

    时间复杂度：O(n)   n为所有元素的个数
    """
    def get_bulk_num(self, row, column):   # 待优化点
        if row < 3:
            if column < 3:
                return 0
            elif column < 6:
                return 1
            else:
                return 2
        elif row < 6:
            if column < 3:
                return 3
            elif column < 6:
                return 4
            else:
                return 5
        else:
            if column < 3:
                return 6
            elif column < 6:
                return 7
            else:
                return 8

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mapping_dict = dict()
        for row_index, row in enumerate(board):
            for column_index, i in enumerate(row):
                if i != '.':
                    bulk = self.get_bulk_num(row_index, column_index)
                    row_v = "row" + str(row_index)
                    column_v = "column" + str(column_index)
                    if i not in mapping_dict:
                        mapping_dict[i] = {row_v, column_v, bulk}
                    else:
                        if row_v in mapping_dict[i] or column_v in mapping_dict[i] or bulk in mapping_dict[i]:
                            return False
                        else:
                            mapping_dict[i].add(row_v)
                            mapping_dict[i].add(column_v)
                            mapping_dict[i].add(bulk)
        return True


class Solution_iterate_once_simplify:
    """
    date:2020.9.22
    author:力扣+fenghao
            https://leetcode-cn.com/problems/valid-sudoku/solution/36-jiu-an-zhao-cong-zuo-wang-you-cong-shang-wang-x/
    思路：简化代码
          <1 九宫格的定位使用巧妙公式
          <2 构建行、列、九宫格的结构值得学习   row [{num:freq},{},{} ...{}]  外层是列表（可按索引搜索），内层是数字元素出现频率的映射
          <3 巧妙使用 dict.get(key, 0) 简化代码，省去了一个if语句
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # init data
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]

        # validate a board
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    box_index = (i // 3) * 3 + j // 3

                    # keep the current cell value
                    rows[i][num] = rows[i].get(num, 0) + 1    # 简化了代码
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    # check if this value has been already seen before
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True


# board = [
#           ["5","3",".",".","7",".",".",".","."],
#           ["6",".",".","1","9","5",".",".","."],
#           [".","9","8",".",".",".",".","6","."],
#           ["8",".",".",".","6",".",".",".","3"],
#           ["4",".",".","8",".","3",".",".","1"],
#           ["7",".",".",".","2",".",".",".","6"],
#           [".","6",".",".",".",".","2","8","."],
#           [".",".",".","4","1","9",".",".","5"],
#           [".",".",".",".","8",".",".","7","9"]
#         ]
# board = [
#           ["8","3",".",".","7",".",".",".","."],
#           ["6",".",".","1","9","5",".",".","."],
#           [".","9","8",".",".",".",".","6","."],
#           ["8",".",".",".","6",".",".",".","3"],
#           ["4",".",".","8",".","3",".",".","1"],
#           ["7",".",".",".","2",".",".",".","6"],
#           [".","6",".",".",".",".","2","8","."],
#           [".",".",".","4","1","9",".",".","5"],
#           [".",".",".",".","8",".",".","7","9"]
#         ]

board = [[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

my_sol = Solution_iterate_once_simplify()
print(my_sol.isValidSudoku(board))
