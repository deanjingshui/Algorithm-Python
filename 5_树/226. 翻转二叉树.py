"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_recursive:
    """
    date:2020.9.24
    author:fenghao
    思路：递归

          递归实现也就是深度优先遍历的方式，“从上到下”

    时间复杂度：O(n)  每个元素都需要访问一次
    空间复杂度：O(h)  h是树的高度
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        if root.left is not None or root.right is not None:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


class Solution_recursive_simplify_code:
    """
    date:2020.9.24
    author:力扣
            https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/
    思路：递归
            总结出递归的两个条件如下：
                终止条件：当前节点为 null 时返回
                交换当前节点的左右节点，再递归的交换当前节点的左节点，递归的交换当前节点的右节点
            递归有两种方式，一种是先交换，再递归调用。还一种是先递归调用，再交换。两种方式都可以实现

    时间复杂度：O(n)  每个元素都需要访问一次
    空间复杂度：O(h)  h是树的高度
        使用的空间由递归栈的深度决定，它等于当前节点在二叉树中的高度。
        在平均情况下，二叉树的高度与节点个数为对数关系，即 O(log N)。
        而在最坏情况下，树形成链状，空间复杂度为 O(N)。
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归函数的终止条件，节点为空时返回
        if not root:
            return None

        # 将当前节点的左右子树交换
        root.left, root.right = root.right, root.left

        # 递归交换当前节点的 左子树和右子树
        self.invertTree(root.left)
        self.invertTree(root.right)
        # 函数返回时就表示当前这个节点，以及它的左右子树
        # 都已经交换完了
        return root


class Solution_iterate:
    """
    date:2020.9.24
    author:fenghao
            https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/
    思路：迭代  利用栈缓存暂未遍历到的节点

            如果左右节点并非都为None（即非叶子节点）
                    则交换左右节点
                        若有左节点
                            则将左节点压入栈缓存
                        若有右节点
                            则移动到右节点
                            否则，出栈，并移动到出栈的节点
        此题难点是迭代的实现方法

        我的这这种解法本质上是DFS，特点是利用了栈
        这个链接，提到了这是DFS
        https://leetcode-cn.com/problems/invert-binary-tree/solution/di-gui-bfshe-dfsduo-chong-fang-shi-jie-jue-quan-bu/

    时间复杂度：O(n)   每个元素都需要访问一次？
    空间复杂度：O(h)   栈最大为树的高度h
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        node = root
        cache_stack = []
        # while node.left is not None or node.right is not None:
        #     # 左右节点交换
        #     node.left, node.right = node.right, node.left
        #     # 缓存左节点
        #     if node.left:
        #         cache_stack.append(node.left)
        #     # 下一次移动到右节点
        #     node = node.right   # 二叉树有2个分支，如何往下迭代？

        while node is not None:
            # 左右节点交换
            node.left, node.right = node.right, node.left

            # 缓存左节点
            if node.left:
                cache_stack.append(node.left)

            # 移动到下一个节点
            if node.right:
                node = node.right     # 如有右节点，则移动到右节点
            else:
                node = cache_stack.pop(-1) if cache_stack else None  # 否则，移到到出栈的节点

        return root


class Solution_iterate_leetcode:
    """
    date:2020.9.24
    author:力扣
            https://leetcode-cn.com/problems/invert-binary-tree/solution/dong-hua-yan-shi-liang-chong-shi-xian-226-fan-zhua/
    思路：迭代  队列
        递归实现也就是深度优先遍历的方式，那么对应的就是广度优先遍历。
        广度优先遍历需要额外的数据结构-->队列，来存放临时遍历到的元素。
        深度优先遍历的特点是一竿子插到底，不行了再退回来继续；而广度优先遍历的特点是层层扫荡。
        所以，我们需要先将根节点放入到队列中，然后不断的迭代队列中的元素。
        对当前元素调换其左右子树的位置，然后：
            * 判断其左子树是否为空，不为空就放入队列中
            * 判断其右子树是否为空，不为空就放入队列中

    时间复杂度：O(n)  每个元素都需要访问一次
    空间复杂度：O()
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
        queue = [root]
        while queue:
            # 每次都从队列中拿一个节点，并交换这个节点的左右子树
            tmp = queue.pop(0)
            tmp.left, tmp.right = tmp.right, tmp.left
            # 如果当前节点的左子树不为空，则放入队列等待后续处理
            if tmp.left:
                queue.append(tmp.left)
            # 如果当前节点的右子树不为空，则放入队列等待后续处理
            if tmp.right:
                queue.append(tmp.right)
        # 返回处理完的根节点
        return root


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_6 = TreeNode(6)
node_7 = TreeNode(7)
node_9 = TreeNode(9)
node_4.left = node_2
node_4.right = node_7
node_2.left = node_1
node_2.right = node_3
node_7.left = node_6
node_7.right = node_9


my_sol = Solution_iterate()
root = my_sol.invertTree(node_4)
print(root)
pass