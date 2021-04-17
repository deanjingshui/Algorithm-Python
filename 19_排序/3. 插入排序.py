"""
注意：要观察插入排序的最典型的代码，我自己写的插入排序并非典型插入方式
Me:
    1、插入排序在头部维护了一个有序的子序列，依次将剩余元素插入到这个有序的子序列中
    2、插入方式：待插入元素与有序子序列比较，从后往前比较
    3、原地修改，不需要额外的空间

时间复杂度：
    与输入的序列排序程度相关
    最佳情况：已排好序，O(n)
    最坏情况：逆序排序的，O(n^2)
    平均情况：O(n^2)

空间复杂度：
    O(1),只需要一个额外空间用于交换

稳定性:
    稳定的

哨兵：
    待补充

优化：
    折半插入排序
    上面的算法的缺点：在第i-1趟插入时，需要把第i个元素插入到前面的 i-1个元素中，该算法总是从 i-1个元素开始逐个比较之前的
    每个元素，直到找到第i个元素的插入位置，这显然没有利用前面 0~i-1个元素已经有序的特点。
    在 0~i-1个有序元素给第 i个元素寻找插入的位置时，使用二分查找法可以有效提高查找插入位置的时间效率，经过优化的插入排序
    称为折半插入排序，折半插入排序的时间复杂度为O(n*logn)。
"""


def insertion_sort_move(nums):
    """
    author:《算法导论》
    date:2020.8.1
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # 将元素向后移
            j -= 1
        nums[j + 1] = key  # 找到插入位置
    return nums


def insertion_sort_swap(nums):
    """
    author:基于《算法导论》,改成两两交换
           其实比第一种解法效率低，每次循环多做了一个赋值动作
    date:2020.8.1
    """
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1], nums[j] = nums[j], nums[j + 1]  # 两两交换，将元素向后移
            j -= 1
    return nums


def insertion_sort_sentinel(nums):
    """
    author:基于《算法导论》 带哨兵
    date:2021.4.15
    """
    nums = [0] + nums
    for i in range(2, len(nums)):
        nums[0] = nums[i]   # 哨兵
        j = i - 1
        while nums[j] > nums[0]:   # while的判断逻辑减少了一半
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = nums[0]
    return nums[1:]


# def insert_sort_1(nums):
#     """
#     author:互联网
#     """
#     for passnum in range(1, len(nums)):  # 轮询次数passnum是列表长度减去1
#         index = passnum
#         for i in list(range(0, passnum))[::-1]:  # Me：负数索引可读性略差
#             if nums[i] < nums[index]:
#                 continue
#             else:
#                 nums[i], nums[index] = nums[index], nums[i]
#                 index = i
#         print('{:>12} {}'.format(str(passnum) + ' time:', nums))
#     return nums


# def insert_sort_2(lst):
#     """
#     author:fenghao
#     date:2020.8.1
#     思路：外层依次遍历输入，内层遍历结果列表，直到发现外层元素小于内层元素，则插入
#     关于插入的方式：
#         找到大于待插入元素i的那个元素j的位置，将j..i整体后移一位，将原来元素j位置的值设置为i
#     """
#     ret =[]
#     for i in lst:
#         flag = False
#         for index, j in enumerate(ret):
#             if i <= j:
#                 temp = ret[index:]
#                 ret = ret[:index]
#                 ret.append(i)
#                 ret.extend(temp)
#                 flag = True
#                 break
#         if not flag:
#             ret.append(i)
#     return ret


# def insert_sort_3(lst):
#     """
#     author:fenghao
#     date:2020.8.1
#     思路：外层依次遍历输入，内层遍历输出列表，直到发现外层元素小于内层元素，则插入
#     原地修改(in place)
#     """
#     for index_i, i in enumerate(lst):
#         for index_j, j in enumerate(lst[:index_i]):  # 前index-1个元素是已经排好序的；当index_i为0时内层循环正好直接结束
#             if i < j:
#                 lst[index_j+1:index_i+1] = lst[index_j:index_i]
#                 lst[index_j] = i
#                 break   # 注意，插入后须结束循环，否则错误，因有序子序列已改变，故不能再继续迭代了
#     return lst


if __name__ == "__main__":
    nums = [54, 36, 12, 29, 50]
    print('{:>12} {}'.format('before 排序:', nums))
    print('{:>12} {}'.format('after 排序:', insertion_sort_move(nums)))
    print('{:>12} {}'.format('after 排序:', insertion_sort_sentinel(nums)))
