"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1

示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
"""
from typing import List


class Solution:
    """
    date:2020.9.18
    author:fenghao
    思路：
        <1 排序   目的是让出现两次的数字相邻，异或后得到0  （删，没必要）
        <2 依次异或
        <3 最终的值,就是那个只出现一次的数字
    """
    def singleNumber(self, nums: List[int]) -> int:
        # nums.sort()   # 没必要
        result = nums[0]
        for num in nums[1:]:
            result ^= num
        return result


nums = [2,2,1]
# nums = [4,1,2,1,2]
my_sol = Solution()
print(my_sol.singleNumber(nums))
