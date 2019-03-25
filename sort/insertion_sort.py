"""
insertion sort
author: feng.hao
"""


def insertion_sort(list_case):
    list_test = list_case.copy()

    for passnum in range(1,len(list_test)):  # 轮询次数passnum是列表长度减去1
        index = passnum
        for i in list(range(0, passnum))[::-1]:
            if list_test[i]<list_test[index]:
                continue
            else:
                list_test[i],list_test[index]=list_test[index],list_test[i]
                index = i

        print('{:>12} {}'.format(str(passnum) + ' time:', list_test))

    return list_test


if __name__=="__main__":

    list_test_case1 = [54,36,12,29,50]
    print('{:>12} {}'.format('before sort:',list_test_case1))
    print('{:>12} {}'.format('after sort:', insertion_sort(list_test_case1)))