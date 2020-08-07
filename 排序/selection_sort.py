"""
selection sort
author：feng hao
"""

def selection_sort(list_case):
    list_test = list_case.copy()

    for passnum in range(len(list_test) - 1):  # 轮询次数passnum是列表长度减去1
        temp_max_index = 0
        for i in range(len(list_test)-passnum):
            if list_test[i]>list_test[temp_max_index]:
                temp_max_index = i

        list_test[len(list_test)-passnum-1],list_test[temp_max_index]=list_test[temp_max_index],list_test[len(list_test)-passnum-1]
        print('{:>12} {}'.format(str(passnum) + ' time:', list_test))

    return list_test

if __name__=="__main__":

    list_test_case1 = [54,36,12,29,50]
    print('{:>12} {}'.format('before 排序:',list_test_case1))
    print('{:>12} {}'.format('after 排序:', selection_sort(list_test_case1)))
