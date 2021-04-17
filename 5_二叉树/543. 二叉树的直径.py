# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    author:fenghao
    date:2021.3.29
    思路：
         遍历每个节点，求每个节点的左子树高度与右子树高度的和，其中的最大值为结果
         但是，如何记录每个节点呢？？？
    结果：未完成
    """
    def getHeight(self, root):
        # 求树的高度
        if root is None:
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def dfs(self, root):
        # 先序遍历
        if root.left:
            sub_left = self.dfs(root.left)
        else:
            sub_left = []
        if root.right:
            sub_right = self.dfs(root.right)
        else:
            sub_right = []
        return [root.val] + sub_left + sub_right

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        result = 0
        # 遍历树
        pass


class Solution_leetcode:
    """
    author:fenghao+力扣
    思路不变
        难点：代码实现  其实递归本身就会遍历所有的节点！
        自顶向下遍历节点，求每个节点的左子树高度与右子树高度的和，取其中的最大值为
    """
    def __init__(self):
        self.max = 0  # 存储结果

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 遍历节点（因为要用递归，故需辅助函数），并求节点的高度
        self.topDown(root)
        return self.max

    def topDown(self, root):
        """
        自定向下遍历（前序遍历）
        """
        if root is None:
            return
        # 求每个节点的左子树高度与右子树高度的和，取其中的最大值为
        height_left = self.getHeight(root.left)     # 左节点的高度
        height_right = self.getHeight(root.right)   # 右节点的高度
        self.max = max(self.max, height_left + height_right)

        self.topDown(root.left)
        self.topDown(root.right)

    def getHeight(self, root):
        """
        求指定节点的高度
        """
        if root is None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


class Solution_leetcode_simplify:
    """
    author:力扣官方
    date:2021.3.29
            简化代码
    """
    def __init__(self):
        self.max = 0  # 存储结果

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.max

    def depth(self, root):
        if root is None:
            return 0
        L = self.depth(root.left)
        R = self.depth(root.right)
        self.max = max(self.max, L+R)

        return max(L, R) + 1

"""
     3
    / \
   4   5
  / \   \
 1   3   1
"""
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
my_sol = Solution_leetcode()
print(my_sol.diameterOfBinaryTree(node_1))
my_sol = Solution_leetcode_simplify()
print(my_sol.diameterOfBinaryTree(node_1))