"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列
类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:
输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:
输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-iii
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    author:leetcode
    date:2021.3.31
    思路：树形动态规划
             思路与“打家劫舍”一致
             状态转移方程：
                  有2种前置状态
                     <1偷root节点：root.val + rob(root.left.left) + rob(root.left.right) + rob(root.right.left) + rob(root.right.right)
                     <2不偷root节点：rob(root.left) + rob(root.right)
                  rob(root) = max(<1, <2)

    结果：大用例超出时间限制
    """
    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        money_1 = root.val
        if root.left:
            money_1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money_1 += self.rob(root.right.left) + self.rob(root.right.right)

        money_2 = self.rob(root.left) + self.rob(root.right)

        return max(money_1, money_2)



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
my_sol = Solution()
print(my_sol.rob(node_1))