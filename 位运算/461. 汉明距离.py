"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:
输入: x = 1, y = 4
输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
"""


class Solution:
    """
    author:fenghao
    date:2021.4.4
    思路：先将2个数异或计算，然后不断对2做除法，当余数为1时结果+1
    """
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y   # 异或
        result = 0
        while xor > 1:
            xor, yushu = divmod(xor, 2)
            if yushu == 1:
                result += 1
        if xor == 1:
            result += 1
        return result


class Solution_leetcode:
    """
    author:力扣官方
    date:2021.4.4
    思路：移位
            这里采用右移位，每个位置都会被移动到最右边。移位后检查最右位的位是否为 1 即可。
            检查最右位是否为 1，可以使用取模运算（i % 2）或者 AND 操作（i & 1），这两个操作都会屏蔽最右位以外的其他位。
    时间：O(1)
    空间：O(1)
    """
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance


x = 93
y = 73
# x = 1
# y = 4
my_sol = Solution()
print(my_sol.hammingDistance(x, y))
