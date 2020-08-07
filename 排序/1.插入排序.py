"""
注意：要观察插入排序的最典型的代码，我自己写的插入排序并非典型插入方式
Me:
    1、插入排序在头部维护了一个有序的子序列，依次将剩余元素插入到这个有序的子序列中
    2、插入方式：待插入元素与有序子序列比较，且是从后往前比较
    3、原地修改，不需要额外的空间
时间复杂度与输入的序列排序程度相关：
    最佳情况：已排好序，O(n)
    最坏情况：逆序排序的，O(n^2)
    平均情况：O(n^2)
空间复杂度：
    O(1),只需要一个额外空间用于交换
稳定性分析:
    稳定的
【如果待排序的序列中存在两个或两个以上具有相同关键词的数据，排序后这些数据的相对次序保持不变，即它们的位置保持不变，
通俗地讲，就是两个相同的数的相对顺序不会发生改变，则该算法是稳定的；如果排序后，数据的相对次序发生了变化，则该算法
是不稳定的。】

哨兵：
    待补充

优化：
    折半插入排序
    上面的算法的缺点：在第i-1趟插入时，需要把第i个元素插入到前面的i-1个元素中，该算法总是从i-1个元素开始逐个比较之前的
    每个元素，直到找到第i个元素的插入位置，这显然没有利用前面0~i-1个元素已经有序的特点。
    在0~i-1个有序元素给第i个元素寻找插入的位置时，使用二分查找法可以有效提高查找插入位置的时间效率，经过优化的插入排序
    称为折半插入排序，折半插入排序的时间复杂度为O(n*logn)。

"""

def insertion_sort_classic(list_case):
    """
    author:《算法导论》
    date:2020.8.1
    """
    for i in range(1, len(list_case)):
        key = list_case[i]
        j = i - 1
        while j >= 0 and list_case[j] > key:
            list_case[j+1] = list_case[j]  # 向后移
            j -= 1
        list_case[j+1] = key  # 找到插入位置
    return list_case


def insertion_sort_classic_2(list_case):
    """
    author:基于《算法导论》,可读性优化
    date:2020.8.1
    """
    for i in range(1, len(list_case)):
        key = list_case[i]
        j = i - 1
        while j >= 0 and list_case[j] > key:
            list_case[j+1], list_case[j] = list_case[j], list_case[j+1]  # 两两交换，向后移
            j -= 1
    return list_case


def insert_sort_1(list_case):
    """
    author:internet
    """
    list_test = list_case.copy()

    for passnum in range(1,len(list_test)):  # 轮询次数passnum是列表长度减去1
        index = passnum
        for i in list(range(0, passnum))[::-1]:  # Me：负数索引可读性略差
            if list_test[i]<list_test[index]:
                continue
            else:
                list_test[i],list_test[index]=list_test[index],list_test[i]
                index = i

        print('{:>12} {}'.format(str(passnum) + ' time:', list_test))

    return list_test


def insert_sort_2(lst):
    """
    author:fenghao
    date:2020.8.1
    思路：外层依次遍历输入，内层遍历结果列表，直到发现外层元素小于内层元素，则插入
    关于插入的方式：
        找到大于待插入元素i的那个元素j的位置，将j..i整体后移一位，将原来元素j位置的值设置为i
    """
    ret =[]
    for i in lst:
        flag = False
        for index, j in enumerate(ret):
            if i <= j:
                temp = ret[index:]
                ret = ret[:index]
                ret.append(i)
                ret.extend(temp)
                flag = True
                break
        if not flag:
            ret.append(i)
    return ret


def insert_sort_3(lst):
    """
    author:fenghao
    date:2020.8.1
    思路：外层依次遍历输入，内层遍历输出列表，直到发现外层元素小于内层元素，则插入
    原地修改(in place)
    """
    for index_i, i in enumerate(lst):
        for index_j, j in enumerate(lst[:index_i]):  # 前index-1个元素是已经排好序的；当index_i为0时内层循环正好直接结束
            if i < j:
                lst[index_j+1:index_i+1] = lst[index_j:index_i]
                lst[index_j] = i
                break   # 注意，插入后须结束循环，否则错误，因有序子序列已改变，故不能再继续迭代了
    return lst

if __name__=="__main__":

    list_test_case1 = [54,36,12,29,50]
    print('{:>12} {}'.format('before 排序:',list_test_case1))
    print('{:>12} {}'.format('after 排序:', insertion_sort_classic_2(list_test_case1)))