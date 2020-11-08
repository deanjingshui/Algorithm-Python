"""
你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

提示：
输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
"""
from typing import List
from collections import deque, defaultdict


class Solution:
    """
    date:2020.11.4
    author:冯浩
    思路：
        注意图的表示方法是“边缘列表”
        不满足的场景有2个：
            <1 课程数与给的目标不相等
            <2 出现闭环

        广度优先搜索（队列）
            遍历图（边缘列表形式），将出度为0的顶点（无前置课程或者前置课程已学习），放进学习队列
            只要队列不为空，出队一个顶点，将以该顶点为前置的顶点的出度减1，并将出度为0的顶点入队
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        search_queue = deque()
        searched_courses = set()  # 避免死循环
        out_degrees = [0] * numCourses
        valid_courses = 0

        for edge in prerequisites:
            out_degrees[edge[0]] += 1

        for course, out_degree in enumerate(out_degrees):
            if out_degree == 0:
                search_queue.append(course)

        while search_queue:
            course = search_queue.popleft()
            if course in searched_courses:  # 有环
                return False

        return numCourses == valid_courses


class Solution:
    """
    date:2020.11.4
    author:力扣官方  https://www.bilibili.com/video/BV1Xp4y1Y7FJ
    思路：
        广度优先搜索
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 存储有向图
        edges = defaultdict(list)   #  字典，键是课程，值是该所有以该课程为先修课程的课程
        # 存储每个顶点的入度
        indeg = [0] * numCourses
        result = 0

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        q = deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            u = q.popleft()
            result += 1
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return result == numCourses


numCourses = 2
graph = [[1, 0]]
my_sol = Solution()
print(my_sol.canFinish(numCourses, graph))

