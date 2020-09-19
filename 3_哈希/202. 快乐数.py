"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

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


class Solution_hash_set:
    """
    date:2020.9.18
    author:fenghao
    思路：哈希集合
          此题关键点是怎么判断会发生“无限循环”：记录之前计算的值，如果发生重复则说明进入无限循环了
          另外考察了如何获取整数的每一位：“取余数”
    """

    def isHappy(self, n: int) -> bool:
        cache = set()  # 哈希集合
        while n != 1:
            # 计算整数每一位的平方和
            tmp = n
            n = 0
            while tmp >= 10:
                digit = tmp % 10
                n += digit ** 2
                tmp = int(tmp / 10)
            n += tmp ** 2

            if n in cache:
                return False
            cache.add(n)

        return True


class Solution_hash_set_modify:
    """
    date:2020.9.18
    author:fenghao
    思路：优化获取整数的每一位的代码
    """

    def isHappy(self, n: int) -> bool:
        cache = set()  # 哈希集合
        while n != 1:
            # 计算整数每一位的平方和
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit ** 2
                n = n // 10
            n = sum

            if sum in cache:
                return False
            cache.add(sum)

        return True


class Solution:
    """
    date:2019.9.19
    author:力扣 + fenghao
           https://leetcode-cn.com/problems/happy-number/solution/shi-yong-kuai-man-zhi-zhen-si-xiang-zhao-chu-xun-h/
    思路：快慢指针判断是否有循环
          注意：此题不建议用集合记录每次的计算结果来判断是否进入循环，因为这个集合可能大到无法存储；
          另外，也不建议使用递归，同理，如果递归层次较深，会直接导致调用栈崩溃。不要因为这个题目给出的整数是 int 型而投机取巧。
    """

    def bitSquareSum(self, n: int) -> int:
        """
        计算整数每一位的平方和
        """
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 2
            n = n // 10
        return sum

    def isHappy(self, n: int) -> bool:
        fast = slow = n
        while fast != 1:
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
            slow = self.bitSquareSum(slow)
            if fast != 1 and fast == slow:  # 判断是不是因为 1 引起的循环，是的话就是快乐数，否则不是快乐数
                return False
        return True


n = 19
my_sol = Solution_hash_set_modify()
print(my_sol.isHappy(n))