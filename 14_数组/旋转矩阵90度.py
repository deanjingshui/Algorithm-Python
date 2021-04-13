"""
n*n矩阵 顺时针旋转90度
"""


def func(squad):
    """
    author:fenghao
    date:2021.4.1
    思路：画图找规律，第i行变为新矩阵的第n-i列
    """
    n = len(squad)
    result = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = squad[i][j]
    return result


n = 4
squad = [[i*4 + j for j in range(1, n+1)] for i in range(n)]
result = func(squad)
n = len(result)
for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
    print("\n")
