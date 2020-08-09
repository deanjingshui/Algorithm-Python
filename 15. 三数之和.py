"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
"""
from typing import List


class Solution_1:
    """
    author:fenghao
    date:2020.8.9
    思路：3层迭代穷举
    时间复杂度：O(n^3)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass


class Solution_2():
    """
    author:fenghao
    date:2020.8.9
    思路：转换成两数之和
    时间复杂度：O(n^2)  超出时间限制
    注意：
        1、要求返回的是数值，不是索引
        2、要求返回的是所有满足条件的组合
    """
    def twoSum(self, nums: List[int], target:int):
        ret = []
        p_left = 0
        p_right = len(nums) - 1
        while p_left < p_right:
            total = nums[p_left] + nums[p_right]
            if total == target:
                ret.append([nums[p_left], nums[p_right]])
                p_left += 1
            elif total < target:
                p_left += 1
            else:
                p_right -= 1
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for index,i in enumerate(nums[:-2]):
            target = -1*i
            nums_sub = self.twoSum(nums[index+1:], target)
            # print(target)
            # print(nums_sub)
            if len(nums_sub) != 0:
                for i_sub in nums_sub:
                    temp = [i] + i_sub
                    if temp not in ret:  # 避免重复
                        ret.append([i] + i_sub)
        return ret


test = [-1, 0, 1, 2, -1, -4]
my_sol = Solution_2()
print(my_sol.threeSum(test))

