from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """

    """
    def rob(self, root: TreeNode) -> int:



node_1 = TreeNode(3)
node_2 = TreeNode(4)
node_3 = TreeNode(5)
node_4 = TreeNode(1)
node_5 = TreeNode(3)
node_6 = TreeNode(1)
node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.right = node_6
my_sol = Solution()
print(my_sol.rob(node_1))