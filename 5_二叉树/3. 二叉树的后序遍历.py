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


class Solution_recursive:
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


class Solution_iterate_stack:
    """
    date:2020.9.29
    author:fenghao
    思路：迭代
            维护一个数据结构（栈），每次压入左节点，直到无左节点，则
                        如果当前节点被记录过，则
                            弹出当前节点，并将该节点值存入结果
                        否则
                            如果当前节点还有右节点，则
                                压入当前节点的右节点，并记录当前节点（中间节点）
                            否则
                                是叶子节点，如果当前节点是右侧节点，弹出该节点，并将该节点值存入结果

            不断重复，直到这个数据结构(栈)为空
            [root]
            [root.left, root]
            [root.left.left, root.left, root]

            BUG:进入死循环

    时间复杂度：O()
    空间复杂度：O()
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = list()
        nodes_stack = [root]
        nodes_passed = set()     # 记录由左节点跨到右节点时所经过的父节点，避免死循环
        while nodes_stack:
            node = nodes_stack[0]
            if node in nodes_passed:
                node = nodes_stack.pop(0)
                result.append(node.val)
                continue
            if node.left and node not in nodes_passed:   # 修复bug: 避免进入死循环
                nodes_stack.insert(0, node.left)
            else:       # 无左节点
                if node.right:
                    nodes_passed.add(node)     # 记录由左节点跨到右节点时所经过的父节点
                    nodes_stack.insert(0, node.right)
                else:  # 如果是叶子节点
                    node = nodes_stack.pop(0)  # 将叶子节点的父节点也弹出
                    result.append(node.val)
        return result


class Solution_iterate_stack_bugfix:
    """
    date:2020.9.29
    author:fenghao
    思路：
         基于上一个解法，解决进入死循环的bug
         不再记录由左节点跨到右节点时所经过的父节点
         而是，记录所有存储过值的节点，一旦发现当前节点的左右节点被记录过，说明当前节点是中间节点

    时间复杂度：O()
    空间复杂度：O()
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        result = list()
        nodes_stack = [root]
        nodes_passed = set()     # 记录由左节点跨到右节点时所经过的父节点，避免死循环
        while nodes_stack:
            node = nodes_stack[0]
            if node.left and node.left not in nodes_passed:   # 修复bug: 避免进入死循环
                nodes_stack.insert(0, node.left)
            elif node.right and node.right not in nodes_passed:
                nodes_stack.insert(0, node.right)
            else:       # 无左节点 或 左右节点均已记录
                node = nodes_stack.pop(0)  # 弹出当前节点
                result.append(node.val)
                nodes_passed.add(node)  # 记录当前节点
        return result


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3
my_sol = Solution_iterate_stack_bugfix()
print(my_sol.postorderTraversal(node_1))
