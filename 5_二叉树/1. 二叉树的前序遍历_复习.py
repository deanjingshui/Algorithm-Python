"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_recursive:
    """
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        sub_left = sub_right = []
        if root.left:
            sub_left = self.preorderTraversal(root.left)
        if root.right:
            sub_right = self.preorderTraversal(root.right)
        return [root.val] + sub_left + sub_right


class Solution:
    """
        手动迭代
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        nodes_stack = []
        nodes_stack.append(root)
        result = []

        while nodes_stack:
            node = nodes_stack.pop()
            result.append(node.val)
            if node.right:
                nodes_stack.append(node.right)
            if node.left:
                nodes_stack.append(node.left)

        return result



node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
my_sol = Solution_recursive()
print(my_sol.preorderTraversal(node_1))
