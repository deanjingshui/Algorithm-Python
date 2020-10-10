"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_recursive:
    """
    date:2020.10.10
    author:fenghao + 力扣
    思路：
        递归  每一次递归调用，深度+1
        难点：如何求最值
        解决：
              参考力扣“自顶向下”的模板
              https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

              二叉树每个节点至多有2个子节点，那么分别求左、右子树的最大深度，最后返回两者中的最大值

    时间复杂度：O()
    空间复杂度：O()
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = right_depth = 1
        if root.left:     # 多余，待优化点
            left_depth = 1 + self.maxDepth(root.left)
        if root.right:    # 多余，待优化点
            right_depth = 1 + self.maxDepth(root.right)
        return max(left_depth, right_depth)


class Solution_recursive_simplify:
    """
    date:2020.10.10
    author:fenghao + 力扣
    思路：
        删除多余代码

    时间复杂度：O()
    空间复杂度：O()
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7

my_sol = Solution_recursive_simplify()
print(my_sol.maxDepth(node_3))
