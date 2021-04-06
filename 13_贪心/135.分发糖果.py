"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：
    每个孩子至少分配到 1 个糖果。
    评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？
 

示例 1：

输入：[1,0,2]
输出：5
解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。

示例 2：

输入：[1,2,2]
输出：4
解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这已满足上述两个条件。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
"""
from typing import List


class Solution:
    """
    author:fenghao
    date:2021.2.27
    思路：
        相邻元素diff，得到diff列表，diff中元素大于0则所需糖果加1,连续出现大于0则所需糖果加？
        失败，未完成
    """
    def candy(self, ratings: List[int]) -> int:

        children_num = len(ratings)
        candys = [1] * children_num  # 分配列表，每个孩子至少分配到 1 个糖果
        diffs = list()
        for i in range(children_num-1):
            diffs.append(ratings[i+1]-ratings[i])

        for index, diff in enumerate(diffs):
            if diff > 0:
                candys[index+1] += 1
            elif diff < 0:
                candys[index] += 1
            else:
                pass

        ret = 0
        for candy in candys:
            ret += candy
        return ret


class Solution_recursive:
    """
    author:fenghao
    date:2021.2.27
    思路：
        递归
                    1 , n=1
            f(n) =  f(n-1) + 1 , 当第n个孩子评分不高于第n-1个孩子的评分
                    f(n-1) + ? , 当第n个孩子评分高于第n-1个孩子的评分
        失败，未完成
    """
    def candy(self, ratings: List[int]) -> int:
        pass


class Solution_greedy:
    """
    author: https://leetcode-cn.com/problems/candy/solution/135-fen-fa-tang-guo-tan-xin-jing-dian-ti-mu-xiang-/
    date:2021.2.27
    思路：
        本题贪心贪在哪里呢？
        先确定每个孩子左边的情况（也就是从前向后遍历）


    """
    def candy(self, ratings: List[int]) -> int:
        children_num = len(ratings)
        candys = [1] * children_num  # 分配列表初始化，每个孩子至少分配到 1 个糖果

        # 从左往右遍历
        for i in range(1, children_num):
            if ratings[i-1] > ratings[i]:
                candys[i-1] += 1

        # 从右往左遍历
        for i in range(children_num-1, 0, -1):
            if ratings[i-1] < ratings[i]:
                candys[i] += 1

        ret = 0
        for candy in candys:
            ret += candy
        return ret


# children = [1, 0, 2]
children = [1,3,2,2,1]
my_sol = Solution_greedy()
print(my_sol.candy(children))

