"""
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。
每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interval-list-intersections
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2021.3.19
    思路：
        两个指针分别指向两个列表
        通过比较列表中区间的左右边界，来判断应该向后移动哪个指针
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = list()
        len_first = len(firstList)
        len_second = len(secondList)
        p_first = 0
        p_second = 0
        while p_first < len_first and p_second < len_second:
            if firstList[p_first][1] < secondList[p_second][0]:     # first区间整体比second区间小
                p_first += 1
            elif firstList[p_first][0] > secondList[p_second][1]:   # first区间整体比second区间小
                p_second += 1
            else:                                                   # first区间与second区间有交集
                front = max(firstList[p_first][0], secondList[p_second][0])
                back = min(firstList[p_first][1], secondList[p_second][1])
                result.append([front, back])
                if firstList[p_first][1] < secondList[p_second][1]:
                    p_first += 1
                else:
                    p_second += 1

        return result


firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
my_sol = Solution()
print(my_sol.intervalIntersection(firstList, secondList))
