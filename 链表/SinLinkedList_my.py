"""
单向非循环链表的实现
@author:feng.hao
@date:2019.3.22
"""

# Node的实现
class Node:
    def __init__(self, initdata):
        self._data = initdata
        self._next = None  # 默认值None

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def setData(self, newdata):
        self._data = newdata

    def setNext(self, newnext):
        self._next = newnext

# 单向非循环链表的实现
class SinLinkedList:
    def __init__(self):
        self._head = None  # 头指针初始化时为None

    # 以下用到的临时变量“temp”称为“扫描指针”
    def add(self, newdata):
        """
        在列表前端添加元素
        时间复杂度 O(1)
        :param newdata:
        :return:
        """
        temp = Node(newdata)
        temp.setNext(self._head)
        self._head = temp

    def append(self, newdata):
        """
        在列表尾部添加元素
        :param newdata:
        :return:
        """
        if self._head:       # 非空链表
            temp = self._head
            while temp.getNext():
                temp = temp.getNext()
            newNode = Node(newdata)
            temp.setNext(newNode)
        else:                 # 空链表
            newNode = Node(newdata)
            self._head = newNode

    def insert(self, index, newdata):
        """
        在链表第i个位置的前面插入元素
        关键是找到目标位置的前一个节点
        :param index:
        :param newdata:
        :return:
        """
        len = self.size()
        if not 0 <= index <= len-1:
            print("Error: the given index is out of range")
            return False

        if index == 0:
            newNode = Node(newdata)
            newNode.setNext(self._head)
            self._head = newNode
        else:
            num = 0
            temp = self._head
            while num != index-1:
                temp = temp.getNext()
                num += 1
            newNode = Node(newdata)
            newNode.setNext(temp.getNext())
            temp.setNext(newNode)

    def pop(self):
        """
        删除表首元素,并返回该元素
        :return:
        """
        if self.isempty():
            print("Error: the given index is out of range")
            return False

        popData = self._head.getData()
        self._head = self._head.getNext()
        return popData

    def delete(self,index):
        """
        删除索引为index的元素
        :param index:
        :return:
        """
        len = self.size()
        if not 0 <= index <= len - 1:
            print("Error: the given index is out of range")
            return False

        if index == 0:
            self._head = self._head.getNext()
        else:
            num = 0
            temp = self._head
            while num != index-1:
                temp = temp.getNext()
                num += 1
            temp.setNext(temp.getNext().getNext())

    def find(self, data):
        """
        在链表中寻找值为data的第一个元素，返回其索引
        :param data:
        :return:
        """
        num = 0
        temp = self._head
        while temp and temp.getData() != data:
            temp = temp.getNext()
            num += 1
        if not temp:    # 没有该元素
            return False
        else:
            return num

    def isempty(self):
        """
        判断链表是否为空
        :return:
        """
        if self._head:
            return False
        else:
            return True

    def clear(self):
        """
        清空列表
        :return:
        """
        self._head = None

    def size(self):
        """
        计算链表的长度,注意这里不是索引号
        :return:
        """
        len = 0
        temp = self._head
        while temp:
            len += 1
            temp = temp.getNext()
        # debug
        # print("len of linkedList is ",len)
        return len

    def traverse(self):
        """
        遍历链表
        :return:
        """
        print(r"head",end="-->")
        temp = self._head
        while temp:
            print(temp.getData(), end=r"-->")
            temp = temp.getNext()
        print(r"None")

    def elements(self):
        """
        创建迭代器，以便使用for-in
        :return:
        """
        temp = self._head
        while temp:
            yield temp.getData()
            temp = temp.getNext()

if __name__=="__main__":
    mySinLinkedList = SinLinkedList()

    mySinLinkedList.add(1)
    mySinLinkedList.add(2)
    mySinLinkedList.add(3)
    print("链表长度：", mySinLinkedList.size())

    mySinLinkedList.append(4)
    print("尾部添加元素：")
    mySinLinkedList.traverse()

    mySinLinkedList.insert(0,10)
    print("添加首元素")
    mySinLinkedList.traverse()

    mySinLinkedList.insert(2,8)
    print("定位添加元素：")
    mySinLinkedList.traverse()

    mySinLinkedList.pop()
    print("删除首元素：")
    mySinLinkedList.traverse()

    mySinLinkedList.delete(4)
    print("定位删除元素：")
    mySinLinkedList.traverse()

    print("查找元素：",mySinLinkedList.find(4))

    for i in mySinLinkedList.elements():
        print(i)