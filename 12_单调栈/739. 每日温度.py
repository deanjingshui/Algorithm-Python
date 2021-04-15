"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2021.4.7
    思路：2层遍历
    时间：O(n^2)
    空间：O(1)
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        pass


class Solution_stack:
    """
    author:fenghao
    date:2021.4.7
    思路：单调栈
    时间：O()
    空间：O()
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = list()
        stack = list()
        stack.append(0)
        while stack:
            while T[stack[-1]] >= T[stack[-1]+1]:
                stack.append()

