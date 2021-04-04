"""
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false

示例 2:
输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    author:fenghao
    date:2021.4.4
    思路：遍历一遍链表，将val存进数组，对撞指针判断数组是否为回文
    时间：O(n)
    空间：O(n)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        n = 0
        cur = head
        val_list = list()
        while cur:
            val_list.append(cur.val)
            cur = cur.next
            n += 1
        half = int(n/2)
        for i in range(half):
            if val_list[i] != val_list[n-i-1]:
                return False
        return True


class Solution_two_pointer:
    """
    author:力扣网友 https://leetcode-cn.com/problems/palindrome-linked-list/solution/wo-de-kuai-man-zhi-zhen-du-cong-tou-kai-shi-gan-ju/
    date:2021.4.4
    思路：快慢指针(找中点)
            快指针走到末尾，慢指针刚好到中间。其中慢指针将前半部分反转
    时间：O(n)
    空间：O(1)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head
        pre = head
        prepre = None
        while fast and fast.next:
            # pre记录反转的前半个列表，slow一直是原表一步步走
            pre = slow
            slow = slow.next
            fast = fast.next.next

            pre.next = prepre
            prepre = pre

        if fast:  # 长度是奇数还是偶数对应不同情况
            slow = slow.next

        while slow and pre:
            if slow.val != pre.val:
                return False
            slow = slow.next
            pre = pre.next
        return True


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(2)
node_4 = ListNode(3)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = None
my_sol = Solution()
print(my_sol.isPalindrome(node_1))
my_sol = Solution_two_pointer()
print(my_sol.isPalindrome(node_1))