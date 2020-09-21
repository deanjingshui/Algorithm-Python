"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。


示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
"""
from typing import List


class Solution_queue:
    """
    date:2020.9.21
    author:fenghao
    思路：遍历一遍，缓存最近的 k 个值，判断下一个值是否在缓存中
          缓存选用；列表实现的“队列”，保证先进先出
    时间复杂度:O(n*min(k,n))   超出时间限制   当 k 很大时，查找耗时严重
    空间复杂度：O(k)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        cache_queue = list()  # 记忆缓存，队列的最大长度为k
        for num in nums:
            if num in cache_queue:  # 列表查找耗时严重
                return True
            if len(cache_queue) == k:
                cache_queue.pop()
            cache_queue.insert(0, num)  # 列表插入耗时严重

        return False


class Solution_hash:
    """
    date:2020.9.21
    author:力扣 + fenghao
           https://leetcode-cn.com/problems/contains-duplicate-ii/solution/hua-jie-suan-fa-219-cun-zai-zhong-fu-yuan-su-ii-by/
    思路：基于上一方法，只是将列表队列改为哈希集合
          关键：集合是无序的，如何删除最左端的元素？巧妙利用索引！
    时间复杂度:O(n)  60ms
    空间复杂度：O(k)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        cache_hash = set()  # 记忆缓存，哈希集合最大长度为k
        for index, num in enumerate(nums):
            if num in cache_hash:
                return True
            if len(cache_hash) == k:
                cache_hash.remove(nums[index - k])  # 集合是无序的，如何删除最左端的元素？利用索引！
            cache_hash.add(num)

        return False


class Solution_sliding_window:
    """
    date:2020.9.21
    author:fenghao
    思路：双指针 + 哈希集合 ==> 滑窗
         步骤：
            <1 右指针先走 k 个元素，每次右指针移动 1 个元素，判断该元素是否在窗口哈希集合中，
            <2 若在窗口中，返回 True
            <3 若不在，左指针移动 1 个元素，将该元素从哈希集合中去除,重复上面 2 步

    时间复杂度:O(n)    64 ms
    空间复杂度：O(k+1)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = set()  # 哈希集合
        len_nums = len(nums)
        left = right = 0
        while right < len_nums:
            #  右指针移动
            while len(mapping) < k + 1 and right < len_nums:  # 待优化点
                num = nums[right]
                if num in mapping:
                    return True
                else:
                    mapping.add(num)
                right += 1
            # 左指针移动
            num = nums[left]
            mapping.remove(num)
            left += 1
        return False


class Solution_sliding_window_optimize:
    """
    date:2020.9.21
    author:fenghao
    思路：基于上一个方案优化逻辑
         先判断前 k 个元素，然后再开始滑窗
         注意：根据题意滑窗大小为 k+1
    时间复杂度:O(n)    48ms
    空间复杂度：O(k+1)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = set()  # 哈希集合
        len_nums = len(nums)
        left = right = 0
        # 左指针先移动前 k 个元素
        while right < k and right < len_nums:
            num = nums[right]
            if num in mapping:
                return True
            else:
                mapping.add(num)
                right += 1

        # 右、左指针每次移动1个元素
        while right < len_nums:
            num = nums[right]  # 第 k+1 个元素
            if num in mapping:
                return True
            else:
                mapping.add(num)
            right += 1

            num = nums[left]
            mapping.remove(num)
            left += 1
        return False


# nums = [1, 2, 3, 1]
# k = 3
nums = [1, 0, 1, 1]
k = 1
# nums = [1,2,3,1,2,3]
# k = 2
# nums = [1,2,1]
# k = 0
# nums = [1,2,3,1]
# k = 3
my_sol = Solution_hash()
print(my_sol.containsNearbyDuplicate(nums, k))
