"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    date:2020.10.9
    author:力扣 + fenghao
    思路：
        上一解法，没有使用队列是因为，考虑出队的同时还需要入队，不知道何时才停止。
        解决：利用当前队列的长度，控制操作次数

    时间复杂度：O(n)
    空间复杂度：O(m)  m是树最多节点层的节点个数
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 异常输入
        if not root:
            return []

        result = []
        nodes_queue = [root]
        while nodes_queue:
            length = len(nodes_queue)
            level = []
            for _ in range(length):
                node = nodes_queue.pop(0)
                level.append(node.val)
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)
            result.append(level)

        return result