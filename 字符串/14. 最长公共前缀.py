"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
"""
from typing import List


class Solution_1:
    """
    author:fenghao
    date:2020.8.11
    思路：
        迭代 + 索引移动，不要两两比较
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        if len(strs) == 0:
            return ret
        min_len = len(strs[0])
        # 先求最短字符串的长度，确定后续使用的索引的范围
        for s in strs[1:]:
            s_len = len(s)
            if s_len < min_len:
                min_len = s_len
        for index in range(min_len):
            char = strs[0][index]
            is_same = True
            for s in strs[1:]:
                if s[index] == char:
                    continue
                else:
                    is_same = False
                    break
            if is_same:
                ret += char
            else:
                return ret
        return ret


class Solution_2:
    """
    author:fenghao
    date:2020.8.11
    思路：
        针对上一个方案，精简逻辑
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        if len(strs) == 0:
            return ret
        min_len = len(strs[0])
        # 先求最短字符串的长度，确定后续使用的索引的范围
        for s in strs[1:]:
            s_len = len(s)
            if s_len < min_len:
                min_len = s_len
        for index in range(min_len):
            char = strs[0][index]
            # is_same = True
            for s in strs[1:]:
                if s[index] != char:
                    return ret  # 直接函数返回
                    # continue
                # else:
                    # is_same = False
                    # break
            # if is_same:
            ret += char
            # else:
            #     return ret
        return ret




strs = ["flower","flow","flight"]
my_sol = Solution_2()
print(my_sol.longestCommonPrefix(strs))
