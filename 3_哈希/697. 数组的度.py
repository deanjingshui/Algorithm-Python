"""
给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1:

输入: [1, 2, 2, 3, 1]
输出: 2
解释:
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
示例 2:

输入: [1,2,2,3,1,4,2]
输出: 6
注意:

nums.length 在1到50,000区间范围内。
nums[i] 是一个在0到49,999范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/degree-of-an-array
"""
from typing import List


class Solution_1:
    """
    author:fenghao
    date:2020.8.14
    思路：
        思路来源于直接对题目的翻译，但是算法耗时严重
        1、先找到数组中出现次数最多的那个元素（可能多个）
        2、找到出现次数最多元素（可能多个）首次和末次出现的位置，位置索引差值+1为长度，长度的最小值即结果
    力扣测试耗时：1124ms
    时间复杂度：
        count运算O(n)，且遍历1遍====>O(n^2)
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        max_nums = [nums[0]]
        max_count = nums.count(nums[0])
        for i in set(nums):
            if  i != nums[0]:
                i_count = nums.count(i)
                if i_count > max_count:
                    max_count = i_count
                    max_nums = [i]
                elif i_count == max_count:
                    max_nums.append(i)
        ret = len(nums)
        len_nums = len(nums)
        for num in max_nums:
            index_first = nums.index(num)
            index_last = len_nums - nums[::-1].index(num) - 1
            len_tmp = index_last - index_first + 1
            if len_tmp < ret:
                ret = len_tmp
        return ret


class Solution_2:
    """
    author:fenghao
    date:2020.8.16
    思路：
        哈希表
        只遍历一遍，记录数字出现的次数以及首尾索引，具体维护2个哈希表
    力扣测试耗时：176 ms
    时间复杂度：O(n)
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        第一个哈希表存储遍历元素的信息：首末次出现的索引、长度、出现频率
        {1：{'first_index':0 index, 'last_index':4, 'len': 4, 'freq': 2}
         2：{'first_index': 1, 'last_index': 6, 'len': 6, 'freq': 3}}
         第二个哈希表存储整体数组的信息（也可以不用哈希结构，直接用几个变量）：当前的度，度对应的数字、子数组的长度
         {'degree': 1, 'nums': [], 'len':[]}
        """
        nums_map = {}
        degree_map = {'degree': 1, 'nums': [], 'len':[]}
        for index, num in enumerate(nums):
            if nums_map.get(num) is None:
                nums_map[num] = {'first_index': index, 'last_index': index, 'len': 1, 'freq': 1}
            else:
                nums_map[num]['last_index'] = index
                nums_map[num]['len'] = index - nums_map[num]['first_index'] + 1
                nums_map[num]['freq'] += 1
            if degree_map['degree'] < nums_map[num]['freq']:
                degree_map['degree'] = nums_map[num]['freq']
                degree_map['nums'] = [num]    # 有更大的度，则直接覆盖
                degree_map['len'] = [nums_map[num]['len']]
            elif degree_map['degree'] == nums_map[num]['freq']:
                degree_map['nums'].append(num)   # 有相等的度，则追加
                degree_map['len'].append(nums_map[num]['len'])
        return min(degree_map['len'])


class Solution_3:
    """
    author:fenghao
    date:2020.8.16
    思路：
        基于上一个方法
        只是将第一个哈希表去除last_index字段、第二个哈希表去除nums字段
    力扣测试耗时：124 ms
    时间复杂度：O(n)
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        第一个哈希表存储遍历元素的信息
        {1：{'first_index':0 index, 'len': 4, 'freq': 2}
         2：{'first_index': 1, 'last_index': 6, 'len': 6, 'freq': 3}}
         第二个哈希表存储整体数组的信息
         {'degree': 1, 'len':[]}
        """
        nums_map = {}
        degree_map = {'degree': 1, 'len':[]}
        for index, num in enumerate(nums):
            if nums_map.get(num) is None:
                nums_map[num] = {'first_index': index, 'len': 1, 'freq': 1}
            else:
                nums_map[num]['len'] = index - nums_map[num]['first_index'] + 1
                nums_map[num]['freq'] += 1
            if degree_map['degree'] < nums_map[num]['freq']:
                degree_map['degree'] = nums_map[num]['freq']
                degree_map['len'] = [nums_map[num]['len']]
            elif degree_map['degree'] == nums_map[num]['freq']:
                degree_map['len'].append(nums_map[num]['len'])
        return min(degree_map['len'])


class Solution_4(object):
    """
    author:力扣官方
    date:2020.8.16
    思路：
        哈希，用了三个哈希表分别存储了所有元素的首尾索引及频次
        我的方法是用到一个“两层”的哈希，第一层的key是元素，第二层的key是该元素的信息（首末次索引等），官方解法通过三个“单层”的哈希实现更简练
    力扣测试耗时：80 ms
    时间复杂度：O(n)
    """
    def findShortestSubArray(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans


# nums = [1, 2, 2, 3, 1, 4, 2]
nums = [1,2,2,3,1]
my_sol = Solution_2()
print(my_sol.findShortestSubArray(nums))