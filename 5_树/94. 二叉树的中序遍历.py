"""
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal

"""
from typing import List


# Definition for a binary 树 node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        print(self.val)

class Solution:
    """
    fenghao
    2020.7.22
    思路：递归
    """
    def __init__(self):
        self.ret = []  # 结果

    def inorderTraversal_run(self, root: TreeNode):
        # 没有返回值的递归，结果保存在对象的属性中
        # 出口条件，是叶子节点，但是没有return这种返回动作？
        if root.left is None and root.right is None:
            self.ret.append(root.val)
        else:
            # 先对左子树递归
            if root.left is not None:
                self.inorderTraversal_run(root.left)
            # 中间节点
            self.ret.append(root.val)
            # 最后右子树
            if root.right is not None:
                self.inorderTraversal_run(root.right)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:  # 边界条件
            return []
        self.inorderTraversal_run(root)
        return self.ret


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
my_sol = Solution()
print(my_sol.inorderTraversal(node_1))



