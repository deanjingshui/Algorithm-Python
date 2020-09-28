"""
94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution_recursive_1:
    """
    date:2020.8.4
    author；fenghao
    思路：递归
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:  # 异常输入
            return []

        sub_left = [] if root.left is None else self.inorderTraversal(root.left)
        sub_right = [] if root.right is None else self.inorderTraversal(root.right)

        ret = sub_left + [root.val] + sub_right
        return ret


class Solution_recursive_2:
    """
    date:2020.9.28
    author:fenghao
    思路：递归
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # 递归结束条件
        if not root:
            return []

        left = right = []
        if root.left:
            left = self.inorderTraversal(root.left)
        if root.right:
            right = self.inorderTraversal(root.right)
        return left + [root.val] + right


class Solution_recursive:
    """
    date:2020.7.22
    author:fenghao
    思路：递归
        递归思想：学习如下
        https://leetcode-cn.com/problems/fibonacci-number/solution/dong-tai-gui-hua-tao-lu-xiang-jie-by-labuladong/
    """
    def __init__(self):
        self.ret = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # 如果左子树非空
            # 左子树调用自身

        # 否则
            # 记录中间节点

            # 右子树调用自身

        if root.left is not None:
            self.inorderTraversal(root.left)
        else:
            self.ret.append(root.val)
            self.inorderTraversal(root.right)
        return self.ret


class Solution_iterate:
    """
    date:2020.9.28
    author；fenghao
    思路：迭代

          维护一个数据结构（栈），每次压入左节点，直到无左节点，则
                        将弹出栈顶元素（当前节点），并将节点的值存入结果
                        如果当前节点还有右节点，则
                            压入当前节点的右节点
                            否则，当前节点是叶子节点，需要继续弹出栈顶元素，并将该栈顶节点值存入结果
          不断重复，直到这个数据结构(栈)为空
          [root]
          [root.left, root]
          [root.left.left, root.left, root]

          这是深度优先遍历DFS

    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        nodes_stack = [root]
        while nodes_stack:
            node = nodes_stack[0]
            if node.left:
                nodes_stack.insert(0, node.left)
            else:       # 无左节点
                node = nodes_stack.pop(0)   # 弹出当前节点
                result.append(node.val)
                if node.right:
                    nodes_stack.insert(0, node.right)
                else:  # 如果是叶子节点
                    if nodes_stack:
                        node = nodes_stack.pop(0)  # 将叶子节点的父节点也弹出
                        result.append(node.val)
        return result


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
my_sol = Solution_iterate()
print(my_sol.inorderTraversal(node_1))
