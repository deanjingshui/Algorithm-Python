"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

 

示例：

输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
"""


class Solution:
    """
    date:2020.9.18
    author:fenghao
    思路：哈希表
          此题关键点是怎么判断会发生“无限循环”：记录之前计算的值，如果发生重复则说明进入无限循环了
    """
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n != 1:
            # 拆分整数
            tmp = n
            n = 0
            while tmp >= 10:
                mod = tmp % 10
                n += mod**2
                tmp = int(tmp/10)

            n += tmp**2
            if n in cache:
                return False
            cache.add(n)

        return True

n = 19
my_sol = Solution()
print(my_sol.isHappy(n))