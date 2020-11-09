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
    author:fenghao
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


class Solution_iterate_stack:
    """
    date:2020.9.28
    author；fenghao
    思路：迭代

          维护一个数据结构（栈），只要栈非空，则
                如果栈顶节点有左节点，且栈顶节点没有被记录过，则
                    将左节点压入栈
                否则
                    将弹出栈顶元素（当前节点），并将节点的值存入结果
                    如果当前节点还有右节点，则
                        压入当前节点的右节点
                    否则
                        当前节点是叶子节点，需要继续弹出栈顶元素，并将该栈顶节点值存入结果
          不断重复，直到这个数据结构(栈)为空
          [root]
          [root.left, root]
          [root.left.left, root.left, root]

          失败：会进入死循环
          解决：记录弹出节点的父节点，遇到记录过的节点则即使其有左节点也不将左节点压入栈

          这是深度优先遍历DFS

    时间复杂度：O()
    空间复杂度：
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = list()
        nodes_stack = [root]
        nodes_passed = set()     # 记录弹出节点的的父节点，避免死循环
        while nodes_stack:
            node = nodes_stack[0]
            if node.left and node not in nodes_passed:   # 修复bug: 避免进入死循环   “剪枝”？
                nodes_stack.insert(0, node.left)
            else:       # 无左节点
                node = nodes_stack.pop(0)   # 弹出当前节点
                result.append(node.val)
                if nodes_stack:
                    nodes_passed.add(nodes_stack[0])    # 记录弹出节点的的父节点
                if node.right:
                    nodes_stack.insert(0, node.right)
                else:  # 如果是叶子节点
                    if nodes_stack:
                        node = nodes_stack.pop(0)  # 将叶子节点的父节点也弹出
                        result.append(node.val)
                        if nodes_stack:
                            nodes_passed.add(nodes_stack[0])
                        if node.right:
                            nodes_stack.insert(0, node.right)
        return result

   
class Solution_iterate_stack_new:
    """
    date:2020.11.9
    author；fenghao
    思路：迭代
          只要当前节点有左子节点，就入栈（而出栈延迟），直到无左子节点或者左子节点已经遍历过才开始出栈，并将右子节点入栈。
          另外需要额外记忆曾经遍历过的节点（避免进入死循环）。
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = []
        stack_nodes = [root]
        searched_nodes = []

        while stack_nodes:
            node = stack_nodes[-1]
            if node.left and node.left not in searched_nodes:
                stack_nodes.append(node.left)
            else:
                stack_nodes.pop()
                result.append(node.val)
                searched_nodes.append(node)
                if node.right:
                    stack_nodes.append(node.right)

        return result

   
# node_1 = TreeNode(1)
# node_2 = TreeNode(2)
# node_3 = TreeNode(3)
# node_1.right = node_2
# node_2.left = node_3

# node_1 = TreeNode(1)
# node_2 = TreeNode(2)
# node_3 = TreeNode(3)
# node_2.left = node_3
# node_3.left = node_1

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_3.left = node_1
node_3.right = node_2

my_sol = Solution_iterate_stack()
print(my_sol.inorderTraversal(node_3))
