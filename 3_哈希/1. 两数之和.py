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


class Solution_force:
    """
    author:fenghao
    date:2020.8.7
    思路：穷举，2层遍历
    注意理解题意：
        1、只要有一次满足即可返回结果
        2、要求返回的是索引，不是元素
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i,i in enumerate(nums[:-1]):
            for index_j,j in enumerate(nums[index_i+1:]):  # 注意这里使用的是enumerate,且不是从nums第一个元素开始，所以索引需要处理
                if i + j == target:
                    return [index_i, index_i+index_j+1]


class Solution_force_modify:
    """
    author:fenghao
    date:2020.8.7
    思路：穷举，2层遍历
          因上一种使用了enumerate且存在数组切片，可读性不佳，使用nums的索引优化代码如下
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 以上两个都是直观思路，穷举了所有的两数搭配的情况，然后判断两数之和是否等于target
# 建议转变思路为====>遍历每个元素 x，并查找是否存在一个值与 target - x 相等的目标元素,即“查找”


class Solution_hash:
    """
    author:https://leetcode-cn.com/problems/two-sum/solution/liang-shu-zhi-he-by-leetcode-2/
    date:2020.8.7
    思路：字典模拟哈希表
          哈希查找的时间复杂度为O(1)
          2次迭代，第一次迭代用于构建哈希表，第二次迭代用于哈希查找
    时间复杂度：O(n)  虽然有2次迭代，但这2次迭代并没有嵌套关系
    空间复杂度：O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}  # 哈希冲突怎么办？
        for index,i in enumerate(nums):
            mapping[i] = index
        print("mapping: {}".format(mapping))
        """
       nums = [3, 3], target = 6 会发生哈希冲突，但解题不会失败的原因：
       哈希表冲突时保存的是最后出现的值，而第二次遍历时最先遍历的是首次出现的值
       """
        for index,i in enumerate(nums):
            if mapping.get(target-i) is not None and mapping[target-i] != index:  # 注意，该目标元素不能是index本身
                return [index, mapping[target-i]]


class Solution_hash_one_iteration:
    """
    author:fenghao
    date:2021.3.13
    思路：字典模拟哈希表
         只迭代一次，在创建哈希表同时进行哈希查找
    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for index,i in enumerate(nums):
            if target-i in hash_table:
                return [hash_table[target-i], index]
            hash_table[i] = index


class Solution_double_pointer:
    """
    author:fenghao
    date:2020.8.7
    思路：排序 + 双指针（左右指针向中间逼近）
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_order = sorted(nums)
        p_left = 0
        p_right = len(nums) - 1

        while p_left < p_right:
            if nums_order[p_left] + nums_order[p_right] == target:
                break
            elif nums_order[p_left] + nums_order[p_right] < target:
                p_left += 1
            else:
                p_right -= 1
        """
       易错用例
       nums = [3, 3]
       target = 6
       需要处理
       """
        m = nums.index(nums_order[p_left])
        nums.pop(m)
        n = nums.index(nums_order[p_right])
        if n >= m:
            n += 1
        return [m, n]


class Solution_double_pointer_modify:
    """
    author:《你也能看得懂的Python算法书》P80
    date:2021.3.13
    思路：优化，提高可读性
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_order = sorted(nums)
        p_left = 0
        p_right = len(nums) - 1

        while p_left < p_right:
            if nums_order[p_left] + nums_order[p_right] == target:
                break
            elif nums_order[p_left] + nums_order[p_right] < target:
                p_left += 1
            else:
                p_right -= 1

        # 查找索引，优化，提高可读性
        # 先后从两个方向找，可避免找到重复的索引
        for i in range(0, len(nums)):  # 从左往右找
            if nums[i] == nums_order[p_left]:
                break
        for j in range(len(nums)-1,-1,-1):  # 从右往左找
            if nums[j] == nums_order[p_right]:
                break

        return [i, j]


nums = [2, 7, 11, 15]
target = 9
# nums = [3, 3]
# target = 6
my_sol = Solution_double_pointer_modify()
print(my_sol.twoSum(nums, target))
