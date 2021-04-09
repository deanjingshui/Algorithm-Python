"""
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序是基于插入排序的以下两点性质而提出改进方法的：
    1>插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
    2>但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；

原理：
    先将整个待排序的序列按照相距某个“增量”分割成为若干子序列分别进行插入排序，待整个序列中“基本有序”时，
    再对全体序列进行插入排序。

时间复杂度：
    在 O(n）与 O(n^2)之间，具体与所选用的增量序列相关。

稳定性：
    不稳定
"""


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)
