"""
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定不同的子数组为好子数组。
（例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。）
返回 A 中好子数组的数目。

示例 1：
输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

示例 2：
输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarrays-with-k-different-integers
"""
from typing import List


class Solution_force:
    """
    author:fenghao
    date:2021.3.23
    思路：
        暴力解法，穷举所以有子数组 + 哈希桶

        考虑所有连续子区间，时间复杂度为O(n^2)
        每一个连续子区间，需要检查子区间里出现的不同的数字的种数，时间复杂度为O(n)
        总的时间复杂度为O(n^3)
    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        pass


class Solution_sliding_window:
    """
    author:fenghao
    date:2021.3.23
    思路：滑窗（双指针）

          窗口中不同整数的个数 vs 目标
              小于目标，右边界移动1位
              等于目标，仍然是右边界移动1位
              等于目标+1，右边界先回退1位，然后针对这个窗口计算
                    [1 2 1 2]

          难点： 这道题并不像之前的滑窗简单
                当窗口属性等于目标，右边界还需要往回移动！
                     1 2 1 2
                     1 2 1
          结果：未完成
    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # 处理异常输入
        if A is None or len(A) < K:
            return 0

        ret = 0
        length = len(A)
        left = 0
        right = 0
        k_tmp = 1  # 滑窗中不同整数的个数
        hash_table = dict()  # 滑窗中每个字符的出现的频率
        hash_table[A[0]] = 1

        # 难点：外层循环结束的条件
        while right < length - 1:
            # 右指针移动
            while k_tmp <= K and right < length - 1:
                right += 1
                if A[right] not in hash_table:
                    k_tmp += 1
                    hash_table[A[right]] = 1
                else:
                    hash_table[A[right]] += 1
            if k_tmp == K + 1:
                right = right - 1
                hash_table.pop(A[right])
                k_tmp = K

            # 针对这个窗口计算
            while k_tmp == K:
                ret += 1



                left += 1
                if hash_table[A[left]] == 1:
                    hash_table.pop(hash_table[A[left]])
                    k_tmp -= 1
                else:
                    hash_table[A[left]] -= 1

            # 左指针移动

        return ret


class Solution_sliding_window_leetcode:
    """
    author:leetcode
            https://leetcode-cn.com/problems/subarrays-with-k-different-integers/solution/cong-zui-jian-dan-de-wen-ti-yi-bu-bu-tuo-7f4v/
    date:2021.3.23
    思路：滑窗（双指针）

          一般性滑窗问题
            “至少”、“最多”等字眼

          因为
            恰好由 K 个不同整数的子数组的个数 = 最多由 K 个不同整数的子数组的个数 - 最多由 K - 1 个不同整数的子数组的个数
          所以
            将问题转化为2个一般的滑窗问题

    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:


A = [1,2,1,2,3]
K = 2
my_sol = Solution_sliding_window()
print(my_sol.subarraysWithKDistinct(A, K))
