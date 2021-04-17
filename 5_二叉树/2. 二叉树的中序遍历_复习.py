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


class Solution_recursive:
    """
    思路：递归
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        sub_left = sub_right = []
        if root.left:
            sub_left = self.inorderTraversal(root.left)
        if root.right:
            sub_right = self.inorderTraversal(root.right)

        return sub_left + [root.val] + sub_right


class Solution:
    """
    思路：迭代
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


class Solution_leetcode:
    """
    思路：迭代    栈 + 指针
        author: https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/dai-ma-sui-xiang-lu-chi-tou-qian-zhong-hou-xu-de-d/
        分析一下为什么刚刚写的前序遍历的代码，不能和中序遍历通用呢，因为前序遍历的顺序是中左右，先访问的元素是中间节点，要处理的元素也是中间节点，
        所以刚刚才能写出相对简洁的代码，因为要访问的元素和要处理的元素顺序是一致的，都是中间节点。

        那么再看看中序遍历，中序遍历是左中右，先访问的是二叉树顶部的节点，然后一层一层向下访问，直到到达树左面的最底部，再开始处理节点（也就是在把
        节点的数值放进result数组中），这就造成了处理顺序和访问顺序是不一致的。

        那么在使用迭代法写中序遍历，就需要借用指针的遍历来帮助访问节点，栈则用来处理节点上的元素。

        作者：carlsun-2
        链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/dai-ma-sui-xiang-lu-chi-tou-qian-zhong-hou-xu-de-d/

    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = []
        stack_nodes = []
        cur = root    # "指针"
        while stack_nodes or cur is not None:
            if cur is not None:
                stack_nodes.append(cur)
                cur = cur.left
            else:
                cur = stack_nodes.pop()
                result.append(cur.val)
                cur = cur.right

        return result


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.right = node_2
node_2.left = node_3

# node_1 = TreeNode(1)
# node_2 = TreeNode(2)
# node_3 = TreeNode(3)
# node_2.left = node_3
# node_3.left = node_1

# node_1 = TreeNode(1)
# node_2 = TreeNode(2)
# node_3 = TreeNode(3)
# node_3.left = node_1
# node_3.right = node_2

my_sol = Solution()
print(my_sol.inorderTraversal(node_1))
