"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
"""
from typing import List


class Solution_force:
    """
    author:fenghao
    date:2021.4.5
    思路：暴力法
            两层循环穷举所有可能
    时间：O(n^2)
    空间：O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        pass


class Solution_two_pointer:
    """
    author:力扣+fenghao
    date:2021.4.5
    思路：双指针
        难点：左右指针移动的条件，应该移动左or右指针？
    时间：O(n)
    空间：O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            tmp = min(height[left], height[right])*(right-left)
            maxArea = max(maxArea, tmp)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


height = [1,8,6,2,5,4,8,3,7]
my_sol = Solution()
print(my_sol.maxArea(height))