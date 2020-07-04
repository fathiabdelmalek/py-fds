from .stack import Stack
from .utils import change
from .utils.node import Node


class Queue(object):
    def __init__(self):
        self.__front = None
        self.__back = None

    def __str__(self):
        q = "Queue : ["
        tmp = self.__front
        while tmp:
            q += str(tmp.data)
            if tmp.next:
                q += " | "
            tmp = tmp.next
        return q + "]"

    def __len__(self):
        size = 0
        tmp = self.__front
        while tmp:
            size += 1
            tmp = tmp.next
        return size
    
    @property
    def front(self):
        try:
            return self.__front.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    @property
    def back(self):
        try:
            return self.__back.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def empty(self):
        return self.__front is None

    def clear(self):
        while not self.empty():
            ptr = self.__front
            self.__front = self.__front.next
            del ptr

    def enqueue(self, data):
        node = Node(data)
        if self.empty():
            self.__front = self.__back = node
        else:
            self.__back.next = node
            self.__back = node

    def dequeue(self):
        ptr = self.__front
        data = ptr.data
        self.__front = self.__front.next
        del ptr
        return data

    def find(self, data):
        count = 0
        tmp = self.__front
        while tmp:
            if tmp.data == data:
                count += 1
            tmp = tmp.next
        return count

    def reverse(self):
        stck = Stack()
        while not self.empty():
            stck.push(self.enqueue())
        while not stck.empty():
            self.enqueue(stck.pop())
        return self
    
    def sort(self):
        tmp1 = self.__front
        tmp2 = tmp1.next
        while tmp1.next:
            while tmp2:
                if tmp1.data > tmp2.data:
                    change(tmp1, tmp2)
                tmp2 = tmp2.next
            tmp1 = tmp1.next
            tmp2 = tmp1.next
        del tmp1, tmp2

    def exchange(self, n):
        for i in range(n):
            self.enqueue(self.dequeue())

    @classmethod
    def merge(cls, q1, q2):
        try:
            que = Queue()
            tmp1 = q1.__front
            tmp2 = q2.__front
            while tmp1:
                que.enqueue(tmp1.data)
                tmp1 = tmp1.next
            while tmp2:
                que.enqueue(tmp2.data)
                tmp2 = tmp2.next
            del tmp1, tmp2
            return que
        except Exception as ex:
            print("Error, %s" %ex)

    @classmethod
    def swap(cls, q1, q2):
        bid = Queue()
        while not q1.empty():
            bid.enqueue(q1.dequeue())
        while not q2.empty():
            q1.enqueue(q2.dequeue())
        while not bid.empty():
            q2.enqueue(bid.dequeue())
        del bid
