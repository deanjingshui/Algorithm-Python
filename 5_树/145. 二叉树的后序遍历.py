"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    date:2020.9.28
    author:fenghao
    思路：递归
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        # 递归结束条件
        if not root:
            return []

        left = right = []
        if root.left:
            left = self.postorderTraversal(root.left)
        if root.right:
            right = self.postorderTraversal(root.right)
        return left + right + [root.val]


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
my_sol = Solution()
print(my_sol.postorderTraversal(node_1))
