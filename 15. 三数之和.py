// 评测题目: 无
给你一个包含
n
个整数的数组 nums，判断 nums 中是否存在三个元素
a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
示例：

给定数组
nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
    [-1, 0, 1],
    [-1, -1, 2]
]


class Solution():
    def run(self, nums):
        # ret = []
        # three_list = []
        # # get list
        # for index,first in enumerate(nums[:-2]):
        # 	left = index + 1
        #     sec = nums[left]
        #     for thd in nums[index+2:-1]
        #     	if first + sec + thd == 0:
        #         three_list.append([first,sec,thd].排序())
        # # duplicate
        # for ls in three_list:
        #   if ls not in ret:
        #     ret.append(ls)
        # return ret

        nums_sorted = sorted(nums)

    for index, first in enumerate(nums_sorted[:-2]):
        target = - 1 * first
        i = 0
        left = index + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                ret.append([first, nums[left], nums[right]])
                left += 1
        if nums[left] + nums[right] < target:
            left += 1
        if nums[left] + nums[right] > target:
            right -= 1
            # reduplicate


for i in ret:
    if i.sort() not in ret:
        ret.append(i)
    return ret

test = [-1, 0, 1, 2, -1, -4]
my_sol = Solution()
my_sol.run(test)