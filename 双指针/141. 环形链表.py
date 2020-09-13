"""
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

进阶：
你能用 O(1)（即，常量）内存解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution_hash_list:
    """
    date:2020.9.11
    author:fenghao
    思路：缓存  选择列表作为缓存的结构
    时间复杂度：O(n)  1112ms
    空间复杂度：O(n)
    """
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False

        cache = []
        curr_node = head
        while curr_node.next:
            cache.append(curr_node)     # 这行应该放在判断逻辑的后面以提高效率
            if curr_node.next in cache:
                return True
            curr_node = curr_node.next
        return False


class Solution_hash_dict:
    """
    date:2020.9.11
    author:fenghao
    思路：哈希  将哈希的结构由列表换为字典
    时间复杂度：O(n)   64ms  可见，字典明显比列表查找速度快
    空间复杂度：O(n)
    """
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False

        cache = dict()
        curr_node = head
        while curr_node.next:
            cache[hash(curr_node)] = 0    # 这行应该放在判断逻辑的后面以提高效率
            if hash(curr_node.next) in cache:
                return True
            curr_node = curr_node.next
        return False


class Solution_double_pointer:
    """
    date:2020.9.11
    author:fenghao
    你能用 O(1)（即，常量）内存解决此问题吗？
    思路：双指针   指针i用于遍历，指针j用于遍历指针i前的i-1个元素
    时间复杂度：O(n^2)   超出时间限制
    空间复杂度：O(1)
    """
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False

        i = 0
        curr_node = head
        while curr_node.next:
            j = 0
            pre_node = head
            while j < i:
                if pre_node == curr_node.next:
                    return True
                pre_node = pre_node.next
                j += 1
            curr_node = curr_node.next
            i += 1
        return False


class Solution_fast_slow_pointer_mod_two:
    """
    date:2020.9.11
    author:力扣 + fenghao
    你能用 O(1)（即，常量）内存解决此问题吗？
    思路：快慢指针  如果形成回环，快指针会追上慢指针
    时间复杂度：O(n)
    空间复杂度：O(1)
    超出时间限制
    """
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False

        fast_p = head
        slow_p = head
        i = 0
        while fast_p.next:
            if fast_p.next == slow_p:
                return True
            fast_p = fast_p.next
            if i % 2 == 0:
                slow_p = slow_p.next
            i += 1
        return False


class Solution_fast_slow_pointer_next_next:
    """
    date:2020.9.11
    author:力扣 + fenghao
    你能用 O(1)（即，常量）内存解决此问题吗？
    思路：快慢指针  如果形成回环，快指针会追上慢指针
          速度控制不使用余数，而是使用链表的原生方法，node.next.next
    时间复杂度：O(n)
    空间复杂度：O(1)
    超出时间限制
    """
    def hasCycle(self, head: ListNode) -> bool:

        if head is None:
            return False

        fast_p = head
        slow_p = head
        while fast_p.next:
            if fast_p.next == slow_p:
                return True
            if fast_p.next.next:
                fast_p = fast_p.next.next     # 快指针步进2个节点
            else:
                return False
            slow_p = slow_p.next              # 慢指针步进1个节点
        return False


class Solution_fast_slow_pointer_next_next_simply_code:
    """
    date:2020.9.12
    author: 力扣 https://leetcode-cn.com/problems/linked-list-cycle/solution/141-linked-list-cycle_li-jie-by-gulugulu_go/
    你能用 O(1)（即，常量）内存解决此问题吗？
    思路：快慢指针  如果形成回环，快指针会追上慢指针
          速度控制不使用余数，而是使用链表的原生方法，node.next.next
          简化代码
    时间复杂度：O(n)
    空间复杂度：O(1)
    超出时间限制
    """
    def hasCycle(self, head: ListNode) -> bool:

        # if head is None:    # 没必要这样写可以加入后面的while循环判断更简洁
        #     return False

        fast_p = head
        slow_p = head
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next  # 快指针步进2个节点
            slow_p = slow_p.next       # 慢指针步进1个节点
            if fast_p == slow_p:       # == 优化为 is 无效果
                return True
        return False


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

my_sol = Solution_fast_slow_pointer_next_next_simply_code()
print(my_sol.hasCycle(node_1))
