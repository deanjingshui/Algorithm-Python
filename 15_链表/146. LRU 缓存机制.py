"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
    LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
    int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
"""


class ListNode:
    """
    双向链表
    """
    def __init__(self, val=0, next=None, front=None):
        self.val = val
        self.next = next
        self.front = front


class LRUCache:
    """
    author:fenghao
    date:2021.4.11
    思路：哈希表 + 双向链表
            1>搜索操作get时间复杂度要求O(1)，故需要哈希表；
            2>维护key使用的先后顺序，其顺序更新的时间复杂度要求O(1)，故需要双向链表
            3>哈希表与链表的关联：哈希表中的“值”保存关键字的值的同时保存关键字对应的链表节点
    结果：部分用例下程序异常退出
    """
    def __init__(self, capacity: int):
        self._dict = dict()       # key:[value, node]
        self._head = None         # 链表队列的头
        self._tail = None         # 链表队列的尾
        self.capacity = capacity  # 容量
        self._nums = 0            # 当前已存储数据

    def get(self, key: int) -> int:
        if key in self._dict:
            if self._dict[key][1] != self._head:
                # 更新链表头部
                node = self._dict[key][1]
                if node.front is not None:
                    # 若节点为尾部，则还需更新尾部
                    if self._tail == node:
                        self._tail = node.front
                    if node.front.front is None:
                        node.front.front = node
                    node.front.next = node.next
                if node.next is not None:
                    node.next.front = node.front
                node.next = self._head
                node.front = None
                self._head = node
            return self._dict[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self._dict:
            node = self._dict[key][1]
            if node != self._head:
                # 更新链表头部
                node.front.next = node.next
                if node.next is not None:
                    node.next.front = node.front
                if node == self._tail and node.front is not None:
                    # 更新链表尾部
                    self._tail = node.front
                node.next = self._head
                node.front = None
                self._head = node
            # 更新字典值
            self._dict[key][0] = value
        else:
            if self._nums == self.capacity:
                # 容量已满，先删除俩表尾部节点
                node_delete = self._tail
                if node_delete.front is not None:
                    node_delete.front.next = None
                self._tail = node_delete.front
                self._nums -= 1
                # 字典删除key
                key_delete = node_delete.val
                self._dict.pop(key_delete)
            # 链表头部插入新节点
            node = ListNode(key)
            if self._head is None:
                # 链表第一次插入节点
                self._tail = node
            else:
                self._head.front = node
                node.next = self._head
            self._head = node
            self._nums += 1
            # 字典加入新key
            self._dict[key] = [value, node]


# Your LRUCache object will be instantiated and called as such:
# ["LRUCache","put","put","put","put","get","get"]
# [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
obj = LRUCache(2)
obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
print(obj.get(1))
print(obj.get(2))

