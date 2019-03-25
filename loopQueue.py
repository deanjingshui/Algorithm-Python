"""
循环队列
"""

class SqQueue(object):
    def __init__(self, maxsize):
        self.queue = [None] * maxsize
        self.maxsize = maxsize
        self.front = 0
        self.rear = 0

    # 返回当前队列的长度
    def QueueLength(self):
        return (self.rear - self.front + self.maxsize) % self.maxsize

    # 入队
    def EnQueue(self, data):
        # 如果队列未满，则在队尾插入元素，时间复杂度O(1)
        if (self.rear + 1) % self.maxsize == self.front:
            print("The queue is full!")
        else:
            self.queue[self.rear] = data
           # self.queue.insert(self.rear,data)
            self.rear = (self.rear + 1) % self.maxsize

    # 出队
    def DeQueue(self):
        # 如果队列不为空，则删除队头的元素,时间复杂度O(1)
        if self.rear == self.front:
            print("The queue is empty!")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            return data

    # 输出队列中的元素
    def ShowQueue(self):
        for i in range(self.maxsize):
            print(self.queue[i],end=',')
        print(' ')

# 测试程序
if __name__ == "__main__":

    # 建立大小为15的循环队列
    q = SqQueue(15)

    # 0~9入队列
    for i in range(10):
        q.EnQueue(i)
    q.ShowQueue()

    # 删除队头的5个元素：0~4
    for i in range(5):
        q.DeQueue()
    q.ShowQueue()

    # 从队尾增加8个元素：0~7
    for i in range(8):
        q.EnQueue(i)
    q.ShowQueue()
