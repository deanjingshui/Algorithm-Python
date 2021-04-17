"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-elements
"""
from typing import List


class Solution:
    """
    author；fenghao
    date:2021.4.17
    思路：
        先遍历一遍获得数字的频率信息,存进字典dict {num:freq}
        创建一个数组arr，数组长度为最高频率值
        遍历字典dict，将频率freq作为数组的索引，存进nunm
        编译数组arr
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = list()
        freq_dict = dict()
        for num in nums:
            if num in freq_dict.keys():
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        max_freq = 0
        for num, freq in freq_dict.items():
            max_freq = max(max_freq, freq)
        arr = [[] for _ in range(max_freq+1)]
        
        for num, freq in freq_dict.items():
            arr[freq].append(num)

        for i in range(max_freq, 0, -1):
            result.extend(arr[i])
            k -= len(arr[i])
            if k <= 0:
                break
        return result


nums = [1,1,1,2,2,3]
k = 2
my_sol = Solution()
print(my_sol.topKFrequent(nums, k))
