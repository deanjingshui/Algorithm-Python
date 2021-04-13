"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
"""
from typing import List


class Solution:
    """
    author；fenghao
    date:2021.4.12
    思路：先全排序
         但是，当数组很大，而K很小，做全排序就会很浪费时间
    时间：O(n*logn)
    空间：O(1)
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


class Solution_1:
    """
    author；fenghao
    date:2021.4.12
    思路：只遍历一遍，维护一个有序的长度为k的数组
    结果：超大用例超出时间限制
    """
    def insertNums(self, arr):
        # 有序插入尾部元素
        i = len(arr) - 1
        while i > 0 and arr[i-1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        result = list()
        if k == 0:
            return result
        for num in arr:
            if len(result) < k:
                result.append(num)
                # 有序插入，从后向前比较
                self.insertNums(result)
            else:
                if num > result[-1]:
                    continue
                else:
                    # 先pop尾部值，然后有序插入尾部元素
                    result.pop()
                    result.append(num)
                    self.insertNums(result)
        return result


import heapq
class Solution_heap:
    """
    author；力扣官方
    date:2021.4.12
    思路：堆
    """
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


arr = [3,2,1]
k = 2
# my_sol = Solution()
my_sol = Solution_1()
print(my_sol.getLeastNumbers(arr, k))
