"""
insertion sort
author: https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/MergeSort.py
"""


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # 以下是，把两个有序列表归并成一个有序列表
        i = 0; j = 0; k = 0
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

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)