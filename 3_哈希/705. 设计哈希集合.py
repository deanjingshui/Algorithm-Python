"""
不使用任何内建的哈希表库设计一个哈希集合

具体地说，你的设计应该包含以下的功能

add(value)：向哈希集合中插入一个值。
contains(value) ：返回哈希集合中是否存在这个值。
remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);        
hashSet.add(2);        
hashSet.contains(1);    // 返回 true
hashSet.contains(3);    // 返回 false (未找到)
hashSet.add(2);          
hashSet.contains(2);    // 返回 true
hashSet.remove(2);          
hashSet.contains(2);    // 返回  false (已经被删除)

注意：

所有的值都在 [0, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-hashset
"""


class MyHashSet:
    """
    date:2020.9.18
    author:fenghao
    思路：初始化一个数值范围长度的列表，哈希函数：y = x   x是key,y是哈希值
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [None for i in range(1000000+1)]

    def add(self, key: int) -> None:
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.arr[key] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.arr[key]:
            return True
        else:
            return False
