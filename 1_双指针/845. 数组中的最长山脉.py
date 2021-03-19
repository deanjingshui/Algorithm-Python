"""
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：

B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 A，返回最长 “山脉” 的长度。
如果不含有 “山脉” 则返回 0。

示例 1：
输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。

示例 2：
输入：[2,2,2]
输出：0
解释：不含 “山脉”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2021.3.19
    思路：
        一旦发现arr[index+1]>arr[index]，就开始推测是“山脉”的起始
        todo

    结果：太复杂的逻辑判断，未完成
    """

    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        len_arr = len(arr)
        index = 1
        front = 0  # 山脉起始索引
        top = 0  # 山顶索引
        back = 0  # 山脉结束索引
        front_flag = False  # 处于上升沿
        back_flag = False  # 处于下降沿
        while index < len_arr:
            if arr[index] > arr[index - 1]:
                if not front_flag:
                    front_flag = True
                    front = index - 1
                    top = index
                else:
                    # todo
                    pass
        return result


class Solution_1:
    """
    author:fenghao
    date:2021.3.19
    思路：
        双指针，背向指针
        找到所有的顶点，从每个顶点处开始，左右2个指针向两边移动
    时间复杂度：O(n)
    空间复杂度：O(n)  记录顶点
    """

    def longestMountain(self, arr: List[int]) -> int:
        result = 0
        top_list = list()
        arr_len = len(arr)

        # 找到所有的顶点
        for index in range(1, arr_len - 1):
            if arr[index - 1] < arr[index] > arr[index + 1]:
                top_list.append(index)

        # 从每个顶点处开始，左右2个指针向两边移动
        for top in top_list:
            tmp = 0
            for i in range(top, 0, -1):
                if arr[i] > arr[i - 1]:
                    tmp += 1
                else:
                    break
            for j in range(top, arr_len - 1):
                if arr[j] > arr[j + 1]:
                    tmp += 1
                else:
                    break
            result = max(result, tmp + 1)

        return result


# arr = [2, 1, 4, 7, 3, 2, 5]
# arr = [2,2,2]
arr = [2, 1, 4, 7, 3, 2, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4]
my_sol = Solution_1()
print(my_sol.longestMountain(arr))
