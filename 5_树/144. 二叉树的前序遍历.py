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
    date:2020.9.23
    author:fenghao
    思路：递归
    时间复杂度：O(2^n)  n为二叉树的高度
    空间复杂度：O()
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        left = right = []
        if root.left:
            left = self.preorderTraversal(root.left)
        if root.right:
            right = self.preorderTraversal(root.right)

        return [root.val] + left + right


class Solution:
    """
    date:2020.9.23
    author:fenghao
    思路：迭代
    时间复杂度：O()  n为二叉树的高度
    空间复杂度：O()
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        pass


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
my_sol = Solution()
print(my_sol.preorderTraversal(node_1))
