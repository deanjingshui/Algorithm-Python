"""
两个有序列表归并成一个有序序列
author: https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/MergeSort.py
"""

def two_sortedList_merge(lefthalf,righthalf):
    alist = lefthalf + righthalf
    i = 0;j = 0;k = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            alist[k] = lefthalf[i]
            i += 1
        else:
            alist[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        alist[k] = lefthalf[i]
        i += 1
        k += 1
    while j < len(righthalf):
        alist[k] = righthalf[j]
        j += 1
        k += 1

    return alist

# 2个有序的序列
lefthalf=[11,13,15,17]
righthalf=[10,12,14,16]
print(two_sortedList_merge(lefthalf,righthalf))
# 结果
# [10, 11, 12, 13, 14, 15, 16, 17]

