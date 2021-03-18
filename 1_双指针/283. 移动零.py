"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
"""
from typing import List


class Solution_1:
    """
    fenghao
    2020.9.6
    注意：题目要求“原地修改”
    思路：遍历，遇到0元素，就将0之后的元素依次前移一位
    结果：失败，[0,0,1]用例无法通过
          错在只“前移一位”不一定足够，遇到有连续零元素则会有零元素没有被移走的情况
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        p = 0
        while p < nums_len:
            if nums[p] == 0:
                nums[p:] = nums[p+1:nums_len] + [0]
            p += 1


class Solution_2:
    """
    fenghao
    2020.9.1
    思路：
        遍历一遍，遇到0则一直往后找到第一个非0的元素，将两者交换位置，然后继续向后遍历
        本质上是“双指针”的解法，一个外层指针作为遍历一遍用，一个内层指针用于查找外层指针后续的第一个非零元素。
        这就是“快慢指针”么？非也，第二个指针还会根据第一个指针重新定位
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0           # 外层指针作为遍历一遍用
        while i < len_nums:
            if nums[i] == 0:
                j = i + 1    # 内层指针用于查找外层指针后续的第一个非零元素
                while j < len_nums and nums[j] == 0:
                    j += 1
                if j < len_nums and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1


class Solution_3:
    """
    fenghao
    2020.9.1
    思路：
        优化内部循环的逻辑
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        i = 0
        while i < len_nums:
            if nums[i] == 0:
                j = i + 1
                while j < len_nums:    # 优化点，提前结束
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break           # 内部迭代可提前结束
                    j += 1
                if j == len_nums and nums[j - 1] == 0:    # 优化点，提前结束
                    break               # 外部迭代可提前结束
            i += 1


class Solution_4:
    """
    力扣
    2020.9.1
    思路：
        快慢指针
        这才是真正的“快慢指针”
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        len_nums = len(nums)
        i = 0  # 快指针 用于遍历数组
        j = 0  # 慢指针 用于维护非零子数组，并指向非零子数组的尾部
        while i < len_nums:
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        while j < len_nums:
            nums[j] = 0
            j += 1


class Solution_5:
    """
    author:fenghao
    date:2021.3.18
    思路：
        快慢指针
        慢指针指向已处理子数组的尾部，快指针指向未处理子数组的头部（用于遍历）

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        if nums is None or len(nums) == 0:
            return

        left = 0
        right = 1
        nums_len = len(nums)
        while right < nums_len:
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            elif nums[left] != 0:
                left += 1
            right += 1


class Solution_6:
    """
    author:力扣
    date:2021.3.18
    思路：
        快慢指针
        慢指针指向已处理子数组的尾部，快指针指向未处理子数组的头部（用于遍历）
        简化逻辑，初始的快慢指针都指向数组第一个元素

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def moveZeroes(self, nums: List[int]) -> None:
        if nums is None or len(nums) == 0:
            return

        left = 0
        right = 0
        nums_len = len(nums)
        while right < nums_len:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


nums = [0,1,0,3,12]
# nums = [0,0,1]
my_sol = Solution_6()
my_sol.moveZeroes(nums)
print(nums)