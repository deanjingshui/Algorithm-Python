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


class Solution_1:
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
            # if numbers[p_left] + numbers[p_right] == target:
            #     break
            # elif numbers[p_left] + numbers[p_right] < target:
            #     p_left += 1
            total = numbers[p_left] + numbers[p_right]   # 抽离出来，减少重复计算量
            if total == target:
                break
            elif total < target:
                p_left += 1
            else:
                p_right -= 1
        p_left += 1
        p_right += 1
        return [p_left, p_right]


class Solution_2:
    """
    author:https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/solution/liang-shu-zhi-he-ii-shu-ru-you-xu-shu-zu-by-leet-2/
    date:2020.8.8
    思路：二分查找
    时间复杂度：O(nlgn)
    空间复杂度：O(1)
    """
    def binary_search(self, array: List, key):
        # 模拟二分查找
        try:
            return array.index(key)
        except ValueError:
            return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index in range(1, len(numbers)):
            key = target - numbers[index]
            # 避免重复计算
            j = self.binary_search(numbers[:index], key)    # 为了避免重复寻找，在寻找第二个数时，只在第一个数的右侧（或左侧？）寻找。
            if j is not None:
                return [j+1, index+1]




# numbers = [2, 7, 11, 15]
# target = 9
# numbers = [3, 3]
# target = 6
numbers = [2,3,4]
target = 6
my_sol = Solution_2()
print(my_sol.twoSum(numbers, target))

