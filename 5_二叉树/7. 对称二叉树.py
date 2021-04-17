"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
 

进阶：
你可以运用递归和迭代两种方法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_BFS:
    """
    date:2020.10.10
    author:fenghao
    思路：
        层序遍历（广度优先遍历）获得每一层的节点队列、节点值队列
        判断每层的节点组成的队列是否对称
        注意：
            <1、遇到无节点的情况，队列追加None
            <2、循环结束的条件是队列中元素全部为None

    超出时间限制
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        nodes_queue = [root]
        none_count = 0
        length = 1
        while none_count != 2 * length:
            length = len(nodes_queue)
            level = []
            none_count = 0
            for _ in range(length):
                node = nodes_queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        nodes_queue.append(node.left)
                    else:
                        none_count += 1
                        nodes_queue.append(None)
                    if node.right:
                        nodes_queue.append(node.right)
                    else:
                        none_count += 1
                        nodes_queue.append(None)
                else:
                    none_count += 2
                    level.append(None)
                    nodes_queue.append(None)
                    nodes_queue.append(None)
            # 判断该层是否对称
            level_rev = level[::-1]   # 待优化点
            if level != level_rev:
                return False
        return True


class Solution_BFS_optimize:
    """
    date:2020.10.10
    author:fenghao
    思路：
        优化判断队列是否对称的算法

    依然超出时间限制
    """
    def judge(self, level, length):
        for i in range(length//2):
            if level[i] != level[length-i-1]:
                return False
        return True

    def isSymmetric(self, root: TreeNode) -> bool:
        nodes_queue = [root]
        none_count = 0
        length = 1
        while none_count != 2 * length:
            length = len(nodes_queue)
            level = []
            none_count = 0
            for _ in range(length):
                node = nodes_queue.pop(0)
                if node:
                    level.append(node.val)
                    if node.left:
                        nodes_queue.append(node.left)
                    else:
                        none_count += 1
                        nodes_queue.append(None)
                    if node.right:
                        nodes_queue.append(node.right)
                    else:
                        none_count += 1
                        nodes_queue.append(None)
                else:
                    none_count += 2
                    level.append(None)
                    nodes_queue.append(None)
                    nodes_queue.append(None)
            # 判断该层是否对称
            if not self.judge(level, length):
                return False
        return True


class Solution_BFS_optimize_optimize:
    """
    date:2020.10.10
    author:fenghao
    思路：
        优化判断队列是否对称的算法

    超出时间限制
    """

    def isSymmetric(self, root: TreeNode) -> bool:
        nodes_queue = [root]
        none_count = 0
        length = 1
        while none_count != 2 * length:
            length = len(nodes_queue)
            level = []
            none_count = 0
            for i in range(length//2):
                pass

        return True


class Solution_recursive:
    """
    date:2020.10.10
    author:力扣
    思路：
        二叉树对称的条件：
            左右子树互为镜像，条件：
                <1 左子树与右子树的根节点相等
                <2 左子树的左子树与右子树的右子树镜像
                   左子树的右子树与右子树的左子树镜像
            可见，这是递归的逻辑

        难点：发现左右子树的镜像是一个递归

    """
    def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        # if left is None and right is not None:   # 待逻辑优化点
        #     return False
        # if left is not None and right is None:
        #     return False
        if left is None or right is None:
            return False

        # if left.val != right.val:   # 待逻辑优化点
        #     return False
        # if self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left):   # 待逻辑优化点
        #     return True
        return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        # if self.isMirror(root.left, root.right):  # 冗余代码，直接return这个表达式即可
        #     return True
        # else:
        #     return False
        return self.isMirror(root.left, root.right)


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(2)
node_4 = TreeNode(3)
node_5 = TreeNode(4)
node_6 = TreeNode(4)
node_7 = TreeNode(3)
node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.left = node_6
node_3.right = node_7

# my_sol = Solution_BFS_optimize()
my_sol = Solution_recursive()
print(my_sol.isSymmetric(node_1))
