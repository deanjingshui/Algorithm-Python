"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    author:fenghao
    date:2121.4.5
    思路：深度优先遍历（递归） 前序遍历
         这是一道典型的利用递归实现前序遍历二叉树的题目

    时间：O(n)
    空间：O(height) 栈花销
    """
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        if (not root1) and root2:
            root1 = root2
        elif root1 and root2:
            root1.val += root2.val                                 # 先“做事”
            root1.left = self.mergeTrees(root1.left, root2.left)   # 再依次递归调用左、右子树--->前序遍历
            root1.right = self.mergeTrees(root1.right, root2.right)

        return root1


