"""
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_find_len:
    """
    date:2020.9.11
    author:fenghao
    思路：遍历一遍获得链表的长度l，然后遍历到l/2
    时间复杂度：O(n + n/2)
    空间复杂度：O(1)
    """
    def middleNode(self, head: ListNode) -> ListNode:
        nodes_len = 0
        curr_node = head
        while curr_node:
            nodes_len += 1
            curr_node = curr_node.next

        mid_len = int(nodes_len/2) + 1
        curr_node = head
        i = 0
        while i < mid_len-1:
            curr_node = curr_node.next
            i += 1
        return curr_node


class Solution_fast_slow_pointer:
    """
    date:2020.9.11
    author:力扣 + fenghao
    思路：快慢指针  慢指针每次步进一个节点，快指针步进两个节点，当快指针到达尾部节点，慢指针到达链表的中间节点

        偶数个节点：
            node_1 --> node_2 --> node_3 --> node_4 --> None
        奇数个节点：
            node_1 --> node_2 --> node_3 --> None

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast:   # 快指针是否到达链表尾部
            if fast.next:  # 确保fast有下一个节点，否则fast.next.next会报错
                fast = fast.next.next
                slow = slow.next
            else:
                break
        return slow


class Solution_fast_slow_pointer_simplify_code:
    """
    date:2020.9.11
    author:力扣 + fenghao
    思路：简化代码
          快指针可以前进的条件是：当前快指针和当前快指针的下一个结点都非空。
    """
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:   # 快指针是否到达链表尾部
            # if fast.next:  # 确保fast有下一个节点，否则fast.next.next会报错
            fast = fast.next.next
            slow = slow.next
            # else:
            #     break
        return slow


node_1 = ListNode(3)
node_2 = ListNode(2)
node_3 = ListNode(0)
node_4 = ListNode(-4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

my_sol = Solution_fast_slow_pointer_simplify_code()
print(node_3)
print(my_sol.middleNode(node_1))
