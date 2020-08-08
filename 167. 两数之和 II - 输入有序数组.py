"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2020.8.8
    思路：双指针（向中间逼近）
    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p_left = 0
        p_right = len(numbers) - 1
        while p_left < p_right:
            if numbers[p_left] + numbers[p_right] == target:
                break
            elif numbers[p_left] + numbers[p_right] < target:
                p_left += 1
            else:
                p_right -= 1
        p_left += 1
        p_right += 1
        return [p_left, p_right]


numbers = [2, 7, 11, 15]
target = 9
my_sol = Solution()
print(my_sol.twoSum(numbers, target))

