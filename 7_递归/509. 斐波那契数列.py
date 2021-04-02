"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。


示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 

提示：

0 ≤ N ≤ 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution_1:
    """
    author:fenghao
    date:2020.7.22
    思路：递归的关键是找到出口条件
    """

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-2) + self.fib(N-1)


class Solution_2:
    """
    author:fenghao
    date:2020.8.5
    思路：递归，带记忆功能
    缺点： 记忆化存储需要使用 O(N)的额外空间。
    """
    def __init__(self):
        self.mem = {}   # 记忆缓存

    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        # if N-1 in self.mem:
        #     sub_1 = self.mem[N-1]
        # else:
        #     sub_1 = self.fib(N-1)
        #     self.mem[N-1] = sub_1
        # if N-2 in self.mem:
        #     sub_2 = self.mem[N-2]
        # else:
        #     sub_2 = self.fib(N-2)
        #     self.mem[N-2] = sub_2
        # return sub_1 + sub_2
        # 上面写逻辑不够简练，简化成如下
        if N-1 not in self.mem:
            self.mem[N - 1] = self.fib(N-1)
        if N-2 not in self.mem:
            self.mem[N-2] = self.fib(N-2)
        return self.mem[N-1] + self.mem[N-2]


class Solution_3:
    """"
    author:fenghao
    date:2020.8.5
    不使用“递归”，使用“迭代(动态规划？)”，且非常节省内存，只需要2个额外的变量pre、prepre
    空间复杂度：O(n)
    """
    def fib(self, N: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1
        if N > 1:
            for i in range(2, N+1):
                dp[i] = dp[i-2] + dp[i-1]
        return dp[N]


class Solution_4:
    """"
    author:fenghao
    date:2020.7.27
    revision:2020.8.5
    继续优化“迭代”，且非常节省内存，只需要2个额外的变量pre、prepre
    空间复杂度：O(1)
    """
    def fib(self, N: int) -> int:
        if N == 0:
            ret = 0
        elif N == 1:
            ret = 1
        else:
            pre = 0
            prepre = 1
            i = 2
            while i <= N:
                ret = pre + prepre
                pre = prepre
                prepre = ret
                i += 1
        return ret


my_sol = Solution_2()
print(my_sol.fib(11))