"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
 

说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays
"""
from typing import List


class Solution:
    """
    date:2020.9.18
    author:fenghao
    思路：哈希集合
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in set(nums1):
            if num in nums2:
                result.append(num)
        return result