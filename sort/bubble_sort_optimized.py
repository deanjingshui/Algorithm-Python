"""
bubble sort
author：https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/BubbleSort.py
"""

# 改进的冒泡排序, 加入一个校验, 如果某次循环发现没有发生数值交换, 直接跳出循环
def modiBubbleSort(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum >= 1 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                exchange = True
        passnum -= 1

        print('{} time: {}'.format(passnum, alist))

    return alist

if __name__=="__main__":

    list_test_case1 = [54,36,12,29,50]
    print('before sort:', list_test_case1)
    print('after sort:', modiBubbleSort(list_test_case1))