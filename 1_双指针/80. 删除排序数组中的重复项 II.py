"""
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

说明：
为什么返回数值是整数，但输出的答案是数组呢？
请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下：

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 

示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 你不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        author:fenghao
        date:2021.3.18
        思路：
             快慢指针
             慢指针指向已处理的子数组尾部，快指针指向待处理数字的头部
             维护一个变量counter，用于记录快指针指向的字符出现的次数

        注意：返回的是left+1，而不是left

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if nums is None or len(nums) == 0:
            return 0

        left = 0
        right = 1
        nums_len = len(nums)
        counter = 1  # 快指针指向的字符出现的次数
        while right < nums_len:
            if nums[left] == nums[right]:
                counter += 1
            else:
                counter = 1
            # 慢指针移动条件
            if counter < 3:
                left += 1
                nums[left] = nums[right]
                right += 1
            else:
                right += 1

        return left + 1


class Solution_modify:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        author:力扣
        date:2021.3.18
        思路：
             快慢指针
             慢指针指向已处理的子数组尾部，快指针指向待处理数字的头部

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        if nums is None or len(nums) == 0:
            return 0

        left = 1
        right = 2
        nums_len = len(nums)
        k = 2  # 将题目泛化到字符最多重复k个
        while right < nums_len:
            # 慢指针移动条件
            if nums[right] != nums[left-k+1]:
                left += 1
                nums[left] = nums[right]
            right += 1

        return left + 1


my_solution = Solution_modify()
nums = [1,1,1,2,2,3]
# nums = [0,0,1,1,1,1,2,3,3]
ret = my_solution.removeDuplicates(nums)
print(ret)

for i in range(ret):
    print(nums[i], end=" ")
