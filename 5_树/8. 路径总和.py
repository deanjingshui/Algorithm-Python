"""
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例: 
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    date:2020.10.30
    author:fenghao
    思路：
        维护一个栈1，存储根节点到当前节点路径上的节点的值
        遍历直到根节点，计算此时栈的数值和
        维护一个栈2，记录曾经走过的节点，避免进入死循环

    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        node = root
        val_stack = []    # 存储根节点到当前节点路径上的节点的值
        nodes_stack = []  # 记录曾经走过的节点，避免进入死循环
        while node:
            val_stack.append(node.val)
            if node.left and node.left not in nodes_stack:
                node = node.left
            else:




node_5 = TreeNode(5)
node_4 = TreeNode(4)
node_8 = TreeNode(8)
node_11 = TreeNode(11)
node_13 = TreeNode(13)
node_4_2 = TreeNode(4)
node_7 = TreeNode(7)
node_2 = TreeNode(2)
node_1 = TreeNode(1)

node_5.left = node_4
node_5.right = node_8
node_4.left = node_11
node_8.left = node_13
node_8.right = node_4_2
node_11.left = node_7
node_11.right = node_2
node_4_2.right = node_1


my_sol = Solution()
print(my_sol.hasPathSum(node_5, 22))

my_sol=Solution()
my_sol=Solution()
