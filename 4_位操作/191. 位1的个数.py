"""
编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。


示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。


提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。


进阶:
如果多次调用这个函数，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits
"""


class Solution_str:
    """
    date:2020.9.18
    author:fenghao
    思路：字符串处理
        将整数的二进制形式转换成字符串，计算字符串中1的个数
    """

    def hammingWeight(self, n: int) -> int:
        n_bin = bin(n)
        n_str = str(n_bin)
        return n_str.count('1')


class Solution_bit_manipulation_mask_move:
    """
    date:2020.9.18
    author:力扣
           https://leetcode-cn.com/problems/number-of-1-bits/solution/python-de-si-chong-xie-fa-by-jalan/
    思路：位运算
         循环和位移动：把 n 与 1 进行与运算，将得到 n 的最低位数字。因此可以取出最低位数，再将 n 右移一位。循环此步骤，直到 n 等于零。
         n       110101
         mask    000001
         与操作  000001
         注意：位移动是向右移动
    """

    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            if n & 1 == 1:
                result += 1
            n >>= 1  # 右移1位
        return result


class Solution_bit_manipulation:
    """
    date:2020.9.18
    author:labuladong
           https://labuladong.gitbook.io/algo/suan-fa-si-wei-xi-lie/chang-yong-de-wei-cao-zuo
           n&(n-1) 这个操作是算法中常见的，作用是消除数字 n 的二进制表示中的最后一个 1。
    思路：位运算：利用 n & (n - 1)，删去二进制中最右边的 1

    """

    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            n = n & (n - 1)
            result += 1
        return result


n = 0b00000000000000000000000000001011
my_sol = Solution_bit_manipulation()
print(my_sol.hammingWeight(n))
