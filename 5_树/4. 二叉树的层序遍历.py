"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution:
    """
    date:2020.10.9
    author:fenghao
    思路：
        注意：
            乍一看来，这个遍历顺序和 BFS 是一样的，我们可以直接用 BFS 得出层序遍历结果。
            然而，层序遍历要求的输入结果和 BFS 是不同的。层序遍历要求我们区分每一层，也就是返回一个二维数组。
            而 BFS 的遍历结果是一个一维数组，无法区分每一层。
            https://leetcode-cn.com/problems/binary-tree-level-order-traversal/solution/bfs-de-shi-yong-chang-jing-zong-jie-ceng-xu-bian-l/
        
        设置一个临时列表，用于存储下一层的节点，并在遍历完节点列表之后更新节点列表
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        nodes_list = [root]
        while nodes_list:
            tmp = []
            nodes_list_tmp = []
            for node in nodes_list:
                tmp.append(node.val)
                if node.left:
                    nodes_list_tmp.append(node.left)
                if node.right:
                    nodes_list_tmp.append(node.right)
            result.append(tmp)
            nodes_list = nodes_list_tmp

        return result   

 
class Solution:
    """
    date:2020.10.9
    author:力扣 + fenghao
    思路：
        上一解法，没有使用队列是因为，考虑出队的同时还需要入队，不知道何时才停止。
        解决：利用当前队列的长度，控制操作次数

    时间复杂度：O(n)
    空间复杂度：O(m)  m是树最多节点层的节点个数
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 异常输入
        if not root:
            return []

        result = []
        nodes_queue = [root]
        while nodes_queue:
            length = len(nodes_queue)
            level = []
            for _ in range(length):
                node = nodes_queue.pop(0)
                level.append(node.val)
                if node.left:
                    nodes_queue.append(node.left)
                if node.right:
                    nodes_queue.append(node.right)
            result.append(level)

        return result

   
node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_3.left = node_9
node_3.right = node_20
node_20.left = node_15
node_20.right = node_7

my = Solution()
print(my.levelOrder(node_3))
