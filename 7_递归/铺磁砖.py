"""
wish面试题目1：
佳佳是一名瓦匠,这天他正在帮别人贴一条走廊上的瓷砖,他的瓷砖的尺寸都是1*2小矩形,走廊的尺寸是2*N的大矩形,
佳佳的问题是：他的瓷砖一共有多少种贴法?
"""

mem = {}


def solution(n):
    """
    author:fenghao
    date:2020.8.5
    思路：递归，只考虑最后一块砖如何摆放
        最后1块转如果竖着摆放，前面还有n-1块砖
        如果最后1块砖横着摆放，则最后2块砖肯定都是横着摆放，前面还有n-2块砖
              1, n=0,1
        f(n)=
              f(n-1) + f(n-2)
        可见这就是一个斐波那契数列
        另外，考虑到原始的递归方法时间复杂度过高，优化为带有记忆功能的递归
    """
    if n in [0,1]:       # 一开始没有考虑n=0的情况
        return 1
    else:
        if n - 1 in mem.keys():
            sub_problem_left = mem[n-1]
        else:
            sub_problem_left = solution(n-1)
            mem[n-1] = sub_problem_left
        if n - 2 in mem.keys():
            sub_problem_right = mem[n-2]
        else:
            sub_problem_right = solution(n-2)
            mem[n-2] = sub_problem_right
        return sub_problem_left + sub_problem_right

test = 10
print(solution(test))


