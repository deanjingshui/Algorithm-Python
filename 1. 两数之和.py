"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
"""
from typing import List


class Solution_1:
    """
    author:fenghao
    date:2020.8.7
    思路：暴力2层遍历
    注意理解题意：
        1、只要有一次满足即可返回结果
        2、要求返回的是索引，不是元素
    时间复杂度：O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i,i in enumerate(nums[:-1]):
            for index_j,j in enumerate(nums[index_i+1:]):  # 注意这里使用的是enumerate,且不是从nums第一个元素开始，所以索引需要处理
                if nums[index_i] + nums[index_i+index_j] == target:
                    return [index_i, index_i+index_j]


class Solution_2:
    """
    author:fenghao
    date:2020.8.7
    思路：暴力2层遍历
    因上一种使用了enumerate且存在数组切片，可读性不佳，优化代码如下
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 以上两个都是直观思路，穷举所有的两数搭配的情况，然后判断两数之和是否等于target
# 建议转变思路为---->遍历每个元素 x，并查找是否存在一个值与 target - x 相等的目标元素,即“查找”


class Solution_3:
    """
    author:https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/
    date:2020.8.7
    思路：两遍哈希表
        哈希查找的时间复杂度为O(1)
    时间复杂度：O(n)  虽然有2次迭代，但并没有嵌套关系
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}  # 哈希冲突怎么办？
        for index,i in enumerate(nums):
            mapping[i] = index
        for index,i in enumerate(nums):
            if mapping.get(target-i) is not None and mapping[target-i] != index:  # 注意，该目标元素不能是index本身
                return [index, mapping[target-i]]


class Solution_4:
    """
    author:https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/
    date:2020.8.7
    思路：一遍哈希表
        哈希查找的时间复杂度为O(1)
    时间复杂度：O(n)  
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for index,i in enumerate(nums):
            if mapping.get(target-i) is not None and mapping[target-i] != index:
                return [index, mapping[target - i]]
            mapping[i] = index


nums = [2, 7, 11, 15]
target = 9
# nums = [3, 3]
# target = 6
my_sol = Solution_4()
print(my_sol.twoSum(nums, target))
