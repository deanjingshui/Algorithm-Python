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


class Solution:
    """
    author:fenghao
    date:2021.3.19
    思路：滑窗（双指针）

          当窗口中不同整数的个数 vs 目标
              小于，右边界移动1位
              等于，右边界移动1位
              大于，先右边界回退1位，移动左边界
                    1）如果窗口长度大于目标，左边界移动1位，直到窗口小于目标
                    2）左边界移动1位

           难点：当滑窗超过目标，不能只简单的移动左边界


    """
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # 处理异常输入
        if A is None or len(A) < K:
            return 0

        result = 0
        length = len(A)
        left = 0
        right = 0
        k_tmp = 1            # 滑窗中不同整数的个数
        hash_table = dict()  # 滑窗中每个字符的出现的频率
        hash_table[A[0]] = 1

        while right < length:
            if k_tmp == K:
                result += 1
            if k_tmp <= K:    # 滑窗右边界移动1位
                right += 1
                if right == length:
                    break
                if A[right] not in hash_table:
                    k_tmp += 1
                    hash_table[A[right]] = 1
                else:
                    hash_table[A[right]] += 1
            else:             # 滑窗左边界移动1位
                left += 1
                A_sub = A[left:right]
                k_tmp += self.subarraysWithKDistinct(A_sub, K)  # 递归
                if hash_table[A[left]] == 1:
                    k_tmp -= 1
                    hash_table.pop(A[left])
                else:
                    hash_table[A[right]] -= 1

        return result


A = [1,2,1,2,3]
K = 2
my_sol = Solution()
print(my_sol.subarraysWithKDistinct(A, K))
