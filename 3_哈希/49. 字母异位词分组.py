"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
"""
from typing import List


class Solution:
    """
    哈希探索：设计键
    date:2020.9.21
    author:fenghao
    思路：
        遍历一遍字符串数组，将字符串拆分为字符并排序，将排序后的字符拼成字符串，并作为哈希的键
        遍历到的字符串，判断是否在哈希映射中   {'aet':['eat','tea'],'tan':[ant]}
        关键：
            合理设计哈希的键

    时间复杂度：O(n)   52 ms
    空间复杂度：O(n)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        mapping_dict = dict()
        for str in strs:
            tmp = "".join(sorted(list(str)))
            if tmp in mapping_dict:
                # if str not in mapping_dict[tmp]:
                #     mapping_dict[tmp].append(str)
                mapping_dict[tmp].append(str)
            else:
                mapping_dict[tmp] = [str]

        for key in mapping_dict:
            result.append(mapping_dict[key])
        return result
