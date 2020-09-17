"""
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。

说明：

字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:

输入:
s: "cbaebabacd" p: "abc"

输出:
[0, 6]

解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
 示例 2:

输入:
s: "abab" p: "ab"

输出:
[0, 1, 2]

解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string
"""
from typing import List


class Solution:
    """
    date:2020.9.17
    author:fenghao
    思路：
        滑窗

        难点：
            当窗口满足条件后，按照一般的逻辑，右指针无法继续移动。但题目要求给出满足要求的所有子串
    时间复杂度： O(n)  n为s的长度  276 ms
    空间复杂度： O(n)  n为p的长度
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        len_s = len(s)
        len_p = len(p)
        len_window_p = 0   # 窗口中含有p字符的个数.用于判断是否满足要求
        p_count_dict = dict()
        window_p_count_dict = dict()

        for char in p:
            p_count_dict[char] = p.count(char)

        left = right = 0
        while right < len_s:
            # 右指针移动
            while len_window_p < len_p and right < len_s:   # 注：容易忘记 right < len_p 这个条件
                char = s[right]
                if char in p:
                    if char in window_p_count_dict:
                        if window_p_count_dict[char] < p_count_dict[char]:
                            len_window_p += 1
                        window_p_count_dict[char] += 1
                    else:
                        window_p_count_dict[char] = 1
                        len_window_p += 1
                right += 1

            # 左指针移动
            while right - left != len_window_p:
                char = s[left]
                if char in p:
                    if window_p_count_dict[char] <= p_count_dict[char]:
                        len_window_p -= 1
                    window_p_count_dict[char] -= 1
                left += 1

            # 判断是否满足
            if right - left == len_p:
                result.append(left)
                # 重要：满足条件，需要强制移动一次左指针
                char = s[left]
                if char in p:
                    if window_p_count_dict[char] <= p_count_dict[char]:
                        len_window_p -= 1
                    window_p_count_dict[char] -= 1
                left += 1

        return result


s = "cbaebabacd"
p = "abc"

my_sol = Solution()
print(my_sol.findAnagrams(s, p))