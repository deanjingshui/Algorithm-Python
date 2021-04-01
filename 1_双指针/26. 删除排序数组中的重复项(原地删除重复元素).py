# 给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 示例1:

# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 你不需要考虑数组中超出新长度后面的元素。

# 示例2:
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
# 你不需要考虑数组中超出新长度后面的元素。


# 说明:
# 为什么返回数值是整数，但输出的答案是数组呢?
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:

# // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int len = removeDuplicates(nums);

# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
#   print(nums[i]);
# }


def removeDuplicates_sliding_window(nums):
    """
    author:fenghao
    date:2021.3.14
    思路：双指针，滑窗
          左右指针维护一个子数组，保证这个子数组内无重复
          关键要求空间复杂度O(1)
    时间复杂度：O(n^2)
    空间复杂度：O(1)
    结果：fail
          滑窗这个思路想复杂了，而且代码有bug
    """

    left = 0
    right = 1
    while right < len(nums) - 1:
        if nums[right] == nums[left]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
        else:
            right += 1

    return left + 1


def removeDuplicates(nums):
    """
    author:fenghao
    date:2021.3.15
    思路：双指针，快慢指针
          慢指针指向非重复子数组的尾部，快指针每次向后步进1个元素。
          如果快指针与慢指针元素值相同：
              慢指针不动，快指针向后移动1个元素
          否则：
              慢指针后移一个元素
              然后快指针与慢指针元素交换
              最后快指针后移一个元素

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    # 处理异常用例
    if nums is None or len(nums) == 0:
        return 0

    left = 0
    right = 1
    while right < len(nums):
        # 慢指针移动条件
        if nums[left] != nums[right]:
            # nums[left + 1], nums[right] = nums[right], nums[left + 1]
            # left += 1
            # right += 1

            # 优化，修改先后顺序，提高代码可读性
            left += 1
            # 我这里做交换的目的是不破坏数组中的元素
            # 当然根据题意可以直接覆盖：nums[left]=nums[right]
            nums[left], nums[right] = nums[right], nums[left]
        right += 1

    return left + 1


nums = [0,0,1,1,1,2,2,2,3,3,4]
ret = removeDuplicates(nums)
print(ret)

for i in range(ret):
    print(nums[i], end=" ")
