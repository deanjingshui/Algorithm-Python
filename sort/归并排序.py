def merge_two_sorted_lst(lst_1, lst_2):
    """
    author:fenghao
    date：2020.8.2
    思路：双指针法
    时间复杂度：O(n)
    空间复杂度：O(len(lst_1)+len(lst_2))
    """
    len_lst_1 = len(lst_1)
    len_lst_2 = len(lst_2)
    p1 = p2 = 0
    lst_ret = []
    while p1 <= (len_lst_1 - 1) and p2 <= (len_lst_2 - 1):  # 须小心“数组越界”
        if lst_1[p1] < lst_2[p2]:
            lst_ret.append(lst_1[p1] )
            p1 += 1
        else:
            lst_ret.append(lst_2[p2])
            p2 += 1
    # lst_1或者lst_2可能还有剩余的元素
    if p1 < len_lst_1:
        lst_ret.extend(lst_1[p1:])
    else:
        lst_ret.extend(lst_2[p2:])

    return lst_ret


def merge_sort(lst):
    """
    author:fenghao
    date:2020.8.2
    思路：递归
          递归公式
                     n, len(n)=1
            f(n) =
                    merge_two_sorted_lst(f(前1/2), f(后1/2))， len(n)>1
    """
    if len(lst) == 1:
        return lst
    len_lst = len(lst)
    sub_lst_1 = lst[:len_lst//2]
    sub_lst_2 = lst[len_lst//2:]
    return merge_two_sorted_lst(merge_sort(sub_lst_1), merge_sort(sub_lst_2))


c = [54,26,93,17,77,31,44,55,20]
print(merge_sort(c))
