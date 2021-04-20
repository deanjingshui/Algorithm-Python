"""
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"

https://leetcode-cn.com/problems/base-7/
"""


class Solution:
    """
    author:fenghao
    date:2021.4.20
    """
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        result = ""
        flag = 1 if num > 0 else -1
        num = abs(num)
        while num:
            num, mod = divmod(num, 7)
            result = str(mod) + result   # 倒序
        return str(int(result)*flag)


# num = 101
num = 7
# num = -7
my_sol = Solution()
print(my_sol.convertToBase7(num))
