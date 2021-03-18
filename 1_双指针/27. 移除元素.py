"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 
示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        author:fenghao
        date:2021.3.15
        思路：
            排序 + 双指针
            先排序
            左指针指向第一个出现的目标元素，右指针指向最后一个出现的目标元素的下一个元素
            用右指针元素值覆盖左指针元素值，然后左右指针向后移动1位，直到右指针遍历至数组尾部

        时间复制度：O(nlogn) 这是排序的时间复制度
        空间复杂度：O(1)
        """
        # 处理异常用例
        if nums is None or len(nums) == 0:
            return 0
        if val not in nums:
            return len(nums)

        nums.sort()
        left = nums.index(val)
        right = left + nums.count(val)
        while right < len(nums):
            nums[left] = nums[right]
            left += 1
            right += 1

        return left


class Solution_quick_slow_pointer:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        author:力扣 + fenghao
        date:2021.3.15
        思路：
            双指针(快慢指针)
            慢指针维护不含目标值的子数组，指向该子数组的尾部的后一位，快指针只管向后遍历
            如果快指针指向的元素与目标值不同
                将快指针指向值覆盖慢指针指向的值，快慢指针均向后移动1位
            否则
                快指针向后移动1位，慢指针不动
            注意：子数组的长度为慢指针

        时间复制度：O(n)
        空间复杂度：O(1)
        """
        # 处理异常用例
        if nums is None or len(nums) == 0:
            return 0
        if val not in nums:
            return len(nums)

        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1

        return left


my_solution = Solution_quick_slow_pointer()
nums = [0,1,2,2,3,0,4,2]
val = 2
# nums = [2]
# val = 3
ret = my_solution.removeElement(nums, val)
print(ret)

for i in range(ret):
    print(nums[i], end=" ")