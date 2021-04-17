from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = list()
        nodes_queue = deque()
        nodes_queue.append(root)

        while nodes_queue:
            length = len(nodes_queue)
            level = []
            for _ in range(length):
                node = nodes_queue.popleft()
                level.append(node.val)
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)
            result.append(level)

        return result

    def levelOrderSort(self, root: TreeNode) -> List[int]:
        """
        不区分层，只是返回层序遍历的排序结果
        """
        result = list()
        nodes_queue = deque()
        nodes_queue.append(root)

        while nodes_queue:
            node = nodes_queue.popleft()
            result.append(node.val)
            if node.left:
                nodes_queue.append(node.left)
            if node.right:
                nodes_queue.append(node.right)

        return result

"""
    3
   / \
  9  20
    /  \
   15   7
"""

node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7

my = Solution()
print(my.levelOrder(node_3))
print(my.levelOrderSort(node_3))
