"""
给定两个数组，编写一个函数来计算它们的交集。


示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]


说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
"""
from typing import List
import collections


class Solution:
    """
    date:2020.9.19
    author:fenghao
    思路：朴素解法
         遍历数组1，数字同时出现在数组2，则将该数字保存进结果。
         直至数组1遍历结束或者数组2已经为空
    时间复杂度：O(n*m)   n为数组1长度，m为数组2长度   遍历一次数组1，同时在数组2中搜索并删除数字   88ms
    空间复杂度：O(n)
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        return result


class Solution_sorted_double_pointer:
    """
    date:2020.9.19
    author:fenghao
    思路：如果给定的数组已经排好序
          双指针，分别指向2个数字的头部，两两比较，相等则存进结果，不相等则小的指针移动
          4 5 9
          4 4 8 9 9

    时间复杂度：O(max(nlogn, mlogm, n+m))   n为数组1长度，m为数组2长度
               可见，如果 nums1 的大小比 nums2 小很多，第一种方法更优
    空间复杂度：O(1)
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        result = []
        len1 = len(nums1)
        len2 = len(nums2)
        p1 = p2 = 0
        while p1 < len1 and p2 < len2:
            num1 = nums1[p1]
            num2 = nums2[p2]
            if num1 == num2:
                result.append(num1)
                p1 += 1
                p2 += 1
            elif num1 < num2:
                p1 += 1
            else:
                p2 += 1
        return result


class Solution_hash:
    """
    date:2020.9.19
    author:fenghao
    思路：哈希映射
          构建哈希：2个数组的映射数字出现的频次  {1：2，2: 2}
          然后遍历1个哈希表，在另一个哈希表搜索对应的数，两者数值相减
    时间复杂度：O(max(n,m))
    空间复杂度：O(max(n,m))
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        mapping1 = collections.Counter(nums1)
        mapping2 = collections.Counter(nums2)
        for num1, freq1 in mapping1.items():
            freq2 = mapping2.get(num1, 0)
            result.extend([num1] * min(freq1, freq2))
        return result


class Solution_hash_optimize:
    """
    date:2020.9.19
    author:力扣
           https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-ii-by-leetcode-solution/
    思路：哈希映射
          只构建长度较短的数组的哈希表
          首先遍历第一个数组，并在哈希表中记录第一个数组中的每个数字以及对应出现的次数，然后遍历第二个数组，
          对于第二个数组中的每个数字，如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。

    时间复杂度：O(max(n,m))
    空间复杂度：O(min(n,m))
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):  # 已优化点1
            return self.intersect(nums2, nums1)

        result = list()
        mapping1 = collections.Counter(nums1)
        for num in nums2:  # 已优化点2
            if mapping1.get(num, 0) > 0:
                result.append(num)
                mapping1[num] -= 1

        return result


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
my_sol = Solution_hash_optimize()
print(my_sol.intersect(nums1, nums2))
