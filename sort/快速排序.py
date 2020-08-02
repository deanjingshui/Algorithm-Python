

def diverse(lst):
    """
    author:fenghao
    date:2020.8.2
    快速排序所需的辅助函数
    根据中间的mid元素，将序列分割为2个子序列，左序列中的元素都小于mid，有序列大于等于mid
    """
    if len(lst) == 0:    # 注意边界条件0
        return [], [], []

    left = []   # 小于mid的子序列
    right = []  # 大于等于mid的子序列
    mid = lst[len(lst)//2]
    lst.pop(len(lst)//2)    # 注意删除中间元素
    for i in lst:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
    return left, right, mid


def quick_sort(lst):
    """
    author:fenghao
    date:2020.8.2
    思路：递归
        递归公式
                f(n), n=0,1
        f(n) =
                f(小于mid的子序列) + mid + f(大于等于mid的子序列) , n>1

        子函数g(list),返回以list中间位置为mid，以及小于/大于等于mid的2个子序列
    """
    if len(lst) == 1 or len(lst) == 0:   # 注意边界条件0
        return lst
    left, right, mid = diverse(lst)
    ret = quick_sort(left) + [mid] + quick_sort(right)
    return ret


a = [54,26,93,17,77,31,44,55,20]
# print(diverse(a))
print(quick_sort(a))


