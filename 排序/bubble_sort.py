"""
bubble sort
author：feng hao
"""

def bubble_sort(list_case):

    list_test = list_case.copy()

    for passnum in range(len(list_test)-1):  # 轮询次数passnum是列表长度减去1
        for i in range(len(list_test)-1):
            j = i + 1                   # 待比较的相邻元素
            if list_test[i]>list_test[j]:
                list_test[i],list_test[j]=list_test[j],list_test[i]  # 相邻元素进行交换

        print('{:>12} {}'.format(str(passnum)+' time:', list_test))

    return list_test


if __name__=="__main__":

    list_test_case1 = [54,36,12,29,50]
    print('{:>12} {}'.format('before 排序:',list_test_case1))
    print('{:>12} {}'.format('after 排序:', bubble_sort(list_test_case1)))