"""
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution_iterate:
    """
    author:fenghao
    date:2021.4.4
    思路：迭代 + 2个指针
         注意需要2个指针（分别指向当前节点，下一个节点），
         否则，当完成下一个节点指向当前节点后，会进入死循环
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        # 处理异常输入
        if not head:
            return None

        current_node = head
        next_node = head.next
        while next_node is not None:
            tmp = next_node.next
            next_node.next = current_node
            current_node = next_node
            next_node = tmp
        # 返回来处理原头结点
        head.next = None
        head = current_node
        return head


class Solution_iterate_leetcode_simplify:
    """
    author:力扣网友 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
    date:2021.4.4
    思路：思路同上，极大的简化代码
         两个指针pre,cur：
                        pre最开始指向None！
                        cur指向头结点

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        # 处理异常输入
        if not head:
            return None

        # 申请两个指针，pre和 cur，pre指向None
        pre = None
        cur = head
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre


class Solution_recursive:
    """
    author:力扣网友 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
    date:2021.4.4
    思路：递归

    时间复杂度：O(n)
    空间复杂度：O(n) 由于使用递归，将会使用隐式栈空间。递归深度会达到 n层
    """
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归终止条件是当前为空，或者下一个节点为空
        if head is None or head.next is None:
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_1.next = node_2
node_2.next = node_3
node_3.next = None
my_sol = Solution_iterate_leetcode_simplify()
head = my_sol.reverseList(node_1)
node = head
while node:
    print(node.val, end=" ")
    node = node.next
