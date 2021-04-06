"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pascals-triangle
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        for i in range(numRows):
            if i in [0, 1]:
                continue
            lastRow = result[-1]
            n = len(lastRow)
            tmp = list()
            for j in range(n-1):
                tmp.append(lastRow[j]+lastRow[j+1])
            tmp = [1] + tmp + [1]
            result.append(tmp)
        return result


numRows = 5
my_sol = Solution()
print(my_sol.generate(5))
