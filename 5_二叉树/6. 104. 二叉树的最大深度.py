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


class Solution_dfs:
    """
    date:2020.10.10
    author:fenghao + 力扣
    思路：
        深度优先遍历  递归
            dp[root]的含义：root为根节点的树的深度
            递归方程：
                根节点的深度为左子树深度、右子树深度中的最大值，再加 1
                dp[root] = max(dp[root.left], dp[root.right]) + 1

        也可参考：
              力扣“自顶向下”的模板
              https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/

    时间复杂度：O(n)   因为需要遍历每一个节点
    空间复杂度：O(height)   因为使用递归，需要栈空间取决于递归深度即树的深度
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


class Solution_dfs_simplify:
    """
    date:2020.10.10
    author:fenghao + 力扣
    思路：
        删除多余代码
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


class Solution_dfs_bottom2top:
    """
    author:力扣官方leetbook   https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
    date:2021.4.2
    思路：深度优先遍历-递归-自底向上-模板
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)  # 先依次访问左右子树
        right = self.maxDepth(root.right)
        result = max(left, right) + 1  # 再“做事”--->后序遍历！
        return result


class Solution_dfs_top2bottom:
    """
    author:力扣官方leetbook  https://leetcode-cn.com/leetbook/read/data-structure-binary-tree/xefb4e/
    date:2021.4.2
    思路：深度优先遍历-递归-自底向下-模板
         Me：自底向上，是需要传递参数的？
    Me: 代码没看懂
    """
    def maxDepth(self, root: TreeNode) -> int:
        result = self.dfs(root, 0)  # don't forget to initialize answer before call dfs
        return result

    def dfs(self, root, depth):
        if not root:
            return depth
        left = self.dfs(root.left, depth+1)
        right = self.dfs(root.right, depth+1)
        return max(left, right)


from collections import deque
class Solution_bfs:
    """
    author:力扣官方
    date:2021.3.29
    思路：
        广度优先遍历（层序遍历） 迭代
    时间复杂度：O(n)
    空间复杂度：O(m)  每一层节点的最大数量
    """
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        level = 0
        queue = deque()
        queue.append(root)
        while len(queue) != 0:
            level_len = len(queue)  # 注：取出当前队列的长度
            for i in range(level_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level


"""
     3
    / \
   4   5
  / \   \
 1   3   1
"""
node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7

my_sol = Solution_dfs_simplify()
print(my_sol.maxDepth(node_3))
my_sol = Solution_bfs()
print(my_sol.maxDepth(node_3))
my_sol = Solution_dfs_top2bottom()
print(my_sol.maxDepth(node_3))