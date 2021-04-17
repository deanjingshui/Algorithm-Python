"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
"""
from typing import List
import heapq


class Solution:
    """
    author:fenghao
    date:2021.4.17
    思路：利用堆这个数据结构
            1> 堆化
            2> 取 k 次堆顶
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = 0
        nums = [-1*num for num in nums]  # python只有最小堆
        heapq.heapify(nums)
        for _ in range(k):
            result = heapq.heappop(nums)
        return -1*result


nums = [3,2,3,1,2,4,5,5,6]
k = 4
my_sol = Solution()
print(my_sol.findKthLargest(nums, k))
