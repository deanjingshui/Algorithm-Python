"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，
这条路径上所有节点值相加等于目标和 targetSum 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/path-sum

"""
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_bfs:
    """
    author:fenghao
    date:2021.4.2
    思路：层序遍历  2个队列
          分别存储将要遍历的节点，以及根节点到这些节点的路径和
          当节点没有子节点说明到达叶子节点，然后判断当前的val是否是目标值
          关键：对到达叶子节点的判断

    时间复杂度：O(N)，其中N是树的节点数。对每个节点访问一次
    空间复杂度：O(N)，其中N是树的节点数。空间复杂度主要取决于队列的开销，队列中的元素个数不会超过树的节点数
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        queue = deque([root])
        queue_val = deque([root.val])
        while len(queue) != 0:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                val = queue_val.popleft()
                if node.left is None and node.right is None and val == sum:
                    return True
                if node.left:
                    queue.append(node.left)
                    queue_val.append(val+node.left.val)
                if node.right:
                    queue.append(node.right)
                    queue_val.append(val + node.right.val)
        return False


class Solution_dfs:
    """
    author:fenghao
    date:2021.4.2
    思路：深度优先遍历
            sum_list[root] = [root.val+root.left.val, root.val+root.right.val]
            创建一个辅助函数dfs，用来获取当前节点的左右子树的路径和
            最终判断目标值是否在顶层节点的sum_list中
    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False

        sum_list = self.dfs(root)
        if sum in sum_list:
            return True
        return False

    def dfs(self, root):
        if root is None:
            return [0]

        sum_left = [root.val + i for i in self.dfs(root.left)]
        sum_right = [root.val + i for i in self.dfs(root.right)]
        return sum_left + sum_right


class Solution_dfs_leetcode:
    """
    author:leetcode  https://leetcode-cn.com/problems/path-sum/solution/lu-jing-zong-he-by-leetcode-solution/
    date:2021.4.2
    思路：深度优先遍历

    """
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if self.hasPathSum(root.left, sum-root.val):
            return True
        if self.hasPathSum(root.right, sum-root.val):
            return True
        return False



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
my_sol = Solution_bfs()
print(my_sol.hasPathSum(node_1, 8))
my_sol = Solution_dfs()
print(my_sol.hasPathSum(node_1, 8))