"""
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 2^0 = 1
示例 2:

输入: 16
输出: true
解释: 2^4 = 16
示例 3:

输入: 218
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
"""


class Solution_iterate:
    """
    date:2020.9.18
    author:fenghao
    思路：
        从0开始尝试，计算2的m次幂是否等于n，当计算结果大于n说明无法满足
    时间复杂度：O(log n)
    """
    def isPowerOfTwo(self, n: int) -> bool:
        m = 0
        while 2**m < n:
            m += 1
        if 2**m == n:
            return True
        else:
            return False


class Solution_bit_manipulation:
    """
    date:2020.9.18
    author:labuladong
    思路：
        位运算：去除二进制中最右边的 1
        n&(n-1) 这个操作是算法中常见的，作用是消除数字 n 的二进制表示中的最后一个 1。
        一个整数如果是2的幂，则其二进制表达只有一个1
        反证法：num = 2^n + 2^m = 2^n(1 + 2^(m-n))  括号中的树为基数，则num不可能为2的幂
    时间复杂度：O(1)
    """
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:   # 2的幂不可能为负数、零
            return True
        result = True if n & (n-1) == 0 else False
        return result


class Solution_bit_manipulation_simplify_code:
    """
    date:2020.9.18
    author:labuladong
    思路：
        精简代码
    时间复杂度：O(1)
    """
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


n = 16
my_sol =Solution_bit_manipulation()
print(my_sol.isPowerOfTwo(n))
