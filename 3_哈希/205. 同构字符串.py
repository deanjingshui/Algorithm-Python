"""
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:

输入: s = "egg", t = "add"
输出: true
示例 2:

输入: s = "foo", t = "bar"
输出: false
示例 3:

输入: s = "paper", t = "title"
输出: true
说明:
你可以假设 s 和 t 具有相同的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/isomorphic-strings
"""

class Solution:
    """
    date:2020.9.19
    author:fenghao
    思路：哈希映射
         迭代s字符串。字符出现在哈希映射中，则与t字符串相同位置比较，不一致返回false,否则继续。
                     若字符未出现在哈希映射中，则保存映射关系
    时间复杂度：O(n)
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()   # 哈希映射
        for index, char_s in enumerate(s):
            char_t = t[index]
            char_mapping = mapping.get(char_s, None)
            if char_mapping is not None:
                if char_mapping != char_t:
                    return False
            else:
                if char_t in t[:index]:  # 判断是否 两个字符映射到同一个字符上
                    return False
                mapping[char_s] = char_t
        return True


# s = "egg"
# t = "add"
# s = "foo"
# t = "bar"
s = "ab"
t = "aa"
my_sol = Solution()
print(my_sol.isIsomorphic(s, t))
