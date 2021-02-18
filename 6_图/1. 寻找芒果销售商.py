"""
寻找芒果销售商
《图解算法》 第6.3章节

思路：
    有向图
    广度优先搜索
时间复杂度：
    O(V+E)  其中V为顶点（vertice）数，E为边数
"""
from collections import deque


def is_seller(person):
    return person[-1] == "m"


def find_seller(graph):
    # 创建一个队列
    search_queue = deque()
    # 首先将你的邻居都加入到这个搜索队列中
    search_queue += graph["you"]
    # 避免进入死循环，记录检查过的人
    searched = []

    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 取出第一个人
        if person not in searched:
            if is_seller(person):
                return True
            else:
                search_queue += graph[person]  # 如果不是，将这个人的相邻元素都加入这个队列
                searched.append(person)
    return False


# 图的实现  利用映射关系 采用“邻接列表”法
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(find_seller(graph))
