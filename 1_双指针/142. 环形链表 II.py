"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii

进阶：
你是否可以不用额外空间解决此题？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_cache:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        2020.9.11
        fenghao
        思路：缓存  缓存结构使用字典（哈希）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if head is None:
            return None

        cache = dict()
        curr_node = head
        while curr_node.next:
            if hash(curr_node.next) in cache:
                return curr_node.next
            cache[hash(curr_node)] = 0
            curr_node = curr_node.next
        return None


class Solution_double_pointer:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        力扣
        2020.9.11
        思路：快慢指针
              设环的入口是第x个节点，节点长度k
              1、先求环的大小：快、慢指针第一次相遇（此时两个指针都已经进入环中），到第二次相遇，期间迭代的次数就是环的大小的整数倍（n*k）
              2、指针i从起点开始移动，超前指针先走n*k个节点，直到迭代到x节点，两个指针会相撞
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        has_cycle = False
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                has_cycle = True
                break
        if not has_cycle:
            return None

        cycle_len_n = 1    # 环的长度的整数倍
        fast = fast.next
        while fast != slow:
            fast = fast.next.next
            slow = slow.next
            cycle_len_n += 1
        # print('sycle len: {}'.format(cycle_len))

        i = 0
        left = head
        right = head
        while i < cycle_len_n:
            right = right.next
            i += 1
        while left != right:
            left = left.next
            right = right.next
        return left


class Solution_double_pointer_simplify:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        力扣
        2020.9.11
        思路：快慢指针
              设环的入口是第x个节点
              不需要相遇两次，第一次相遇时，快慢指针走过的节点个数之差就是环的长度的整数倍
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        has_cycle = False
        fast = slow = head
        fast_steps = slow_steps = 0
        while fast and fast.next:
            fast = fast.next.next
            fast_steps += 2
            slow = slow.next
            slow_steps += 1
            if fast == slow:
                has_cycle = True
                break
        if not has_cycle:
            return None

        cycle_len_n = fast_steps - slow_steps    # 环的长度的整数倍
        # print('sycle len: {}'.format(cycle_len_n))

        i = 0
        left = head
        right = head
        while i < cycle_len_n:
            right = right.next
            i += 1
        while left != right:
            left = left.next
            right = right.next
        return left



head = [3,2,0,-4]
pos = 1
node_1 = ListNode(3)
node_2 = ListNode(2)
node_3 = ListNode(0)
node_4 = ListNode(-4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_2

# node_1 = ListNode(1)
# node_2 = ListNode(2)
# node_1.next = node_2
# node_2.next = node_1

# node_1 = ListNode(1)

my_sol = Solution_double_pointer_simplify()
print(my_sol.detectCycle(node_1))
