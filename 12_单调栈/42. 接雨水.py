"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
"""
from typing import List


class Solution:
    """
    auhtor；fenghao
    date:2021.4.5
    思路：双指针
         步骤：
            <1 先定位左指针，柱子下降
            <2 找右指针，从左往右遍历，找到大于等于左指针的柱子，则找到一个洼地
            <3 右指针移动同时，记录窗口中的面积
            <4 返回第一步
    结果:失败  有部分情况计算错误
    """
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = 1
        result = 0
        while right < n:
            while left < n-1 and height[left] <= height[left+1]:
                left += 1
            right = left + 1
            tmp = 0
            while right < n and height[left] > height[right]:
                tmp += height[left] - height[right]
                right += 1
            if right == n and height[left] > height[right-1]:
                break
            result += tmp
            left = right

        return result


height = [0,1,0,2,1,0,1,3,2,1,2,1]
my_sol = Solution()
print(my_sol.trap(height))
