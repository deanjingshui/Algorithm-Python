"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    date:2020.9.13
    author:fenghao
    思路：双指针   快慢指针？ 叫“前后”指针更贴切
          后指针指向第 1 个结点，前指针先走 k 步
          每次迭代2个指针都步进1个节点，当前指针到达尾部，后指针则会指向倒数第 k 个节点
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

        fast = slow = head
        i = 1
        while i < k and fast.next:
            fast= fast.next
            i += 1
        if i < k:     # 注意异常情况：链表长度小于k
            return None

        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow


node_1 = ListNode(3)
node_2 = ListNode(2)
node_3 = ListNode(0)
node_4 = ListNode(-4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

my_sol = Solution()
print(node_3)
print(my_sol.getKthFromEnd(node_1, 2))