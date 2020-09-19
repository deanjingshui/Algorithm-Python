"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2


提示：你可以假定该字符串只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
"""
import collections


class Solution_hash:
    """
    date:2020.9.19
    author:fenghao
    思路：哈希映射
         遍历一遍，获得每个字符出现的频次，构建哈希映射，保存字符频次： {'l':1, 'e':2}
         第二次遍历，并从哈希映射中获得其频次，第一个频次的为 1 的字符的索引即为结果
    时间复杂度：O(n)  两次遍历，字典插入、搜索均为 O(1)
    可见复杂度：O(n)
    """

    def firstUniqChar(self, s: str) -> int:
        char_freq_mapping = dict()  # 哈希映射：字符频率
        for char in s:
            if char in char_freq_mapping:
                char_freq_mapping[char] += 1
            else:
                char_freq_mapping[char] = 1

        for index, char in enumerate(s):
            if char_freq_mapping[char] == 1:
                return index
        return -1


class Solution:
    """
    date:2020.9.19
    author:力扣
           https://leetcode-cn.com/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-fu-by-leet/
    思路：哈希映射
          使用 collections.Counter(s) 构建哈希映射
    时间复杂度：O(n)  两次遍历，字典插入、搜索均为 O(1)
    可见复杂度：O(n)
    """

    def firstUniqChar(self, s: str) -> int:
        char_freq_mapping = collections.Counter(s)  # 哈希映射：字符频率
        for index, char in enumerate(s):
            if char_freq_mapping[char] == 1:
                return index
        return -1


# s = "leetcode"
# s = "loveleetcode"
s = "lleettcocdedo"
my_sol = Solution()
print(my_sol.firstUniqChar(s))
