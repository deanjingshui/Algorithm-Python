"""
合并有序数组
form 《你也能看懂的Python算法书》
"""


def func(list_1=None, list_2=None):
    """
    author: fenghao
    :param list_1:
    :param list_2:
    :return:
    """
    index_1 = 0
    index_2 = 0
    ret = []
    while True:
        print("index_1:{}".format(index_1))
        print("index_2:{}".format(index_2))
        if list_1[index_1] <= list_2[index_2]:
            ret.append(list_1[index_1])
            if index_1 < len(list_1)-1:
                index_1 += 1
            else:
                ret.append(list_2[index_2])
                break
        else:
            ret.append(list_2[index_2])
            if index_2 < len(list_2)-1:
                index_2 += 1
            else:
                ret.append(list_1[index_1])
                break

    # print("index_1:{}".format(index_1))
    # print("index_2:{}".format(index_2))
    print(ret)
    # 补上剩余的元素
    if index_1 < len(list_1) -1:
        ret.extend(list_1[index_1:])
    if index_2 < len(list_2) -1:
        ret.extend(list_2[index_2:])

    return ret


if __name__=="__main__":
    array_1 = [1,3,5]
    array_2 = [2,4]
    print(func(array_1,array_2))

    array_1 = [1, 3, 5, 6, 7]
    array_2 = [2, 4]
    print(func(array_1, array_2))

    array_1 = [1, 3, 5, 6, 7]
    array_2 = [2, 4, 100]
    print(func(array_1, array_2))

    arr = array_1.copy()