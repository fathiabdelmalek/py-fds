from .utils import change
from .utils.node import Node


class Stack:
    def __init__(self):
        self.__top = None

    def __str__(self):
        s = "Stack : ["
        tmp = self.__top
        while tmp:
            s += str(tmp.data)
            if tmp.next:
                s += "\n         "
            tmp = tmp.next
        return s + "]"

    def __len__(self):
        size = 0
        tmp = self.__top
        while tmp:
            size += 1
            tmp = tmp.next
        return size

    @property
    def top(self):
        try:
            return self.__top.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def empty(self):
        return self.__top is None

    def clear(self):
        while not self.empty():
            ptr = self.__top
            self.__top = self.__top.next
            del ptr

    def push(self, data):
        node = Node(data, self.__top)
        self.__top = node

    def pop(self):
        ptr = self.__top
        data = ptr.data
        self.__top = self.__top.next
        del ptr
        return data

    def find(self, data):
        count = 0
        tmp = self.__top
        while tmp:
            if tmp.data == data:
                count += 1
            tmp = tmp.next
        return count

    def reverse(self):
        stck = Stack()
        while not self.empty():
            stck.push(self.pop())
        return stck

    def sort(self):
        tmp1 = self.__top
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
        bid1 = Stack()
        bid2 = Stack()
        for i in range(n):
            bid1.push(self.pop())
        while not self.empty():
            bid2.push(self.pop())
        while not bid1.empty():
            self.push(bid1.pop())
        while not bid2.empty():
            self.push(bid2.pop())

    @classmethod
    def merge(cls, s1, s2):
        try:
            stck = Stack()
            tmp1 = s1.__top
            tmp2 = s2.__top
            while tmp1:
                stck.push(tmp1.data)
                tmp1 = tmp1.next
            while tmp2:
                stck.push(tmp2.data)
                tmp2 = tmp2.next
            del tmp1, tmp2
            return stck
        except Exception as ex:
            print("Error, %s" %ex)

    @classmethod
    def swap(cls, s1, s2):
        bid1 = Stack()
        bid2 = Stack()
        while not s1.empty():
            bid1.push(s1.pop())
        while not s2.empty():
            bid2.push(s2.pop())
        while not bid1.empty():
            s2.push(bid1.pop())
        while not bid2.empty():
            s1.push(bid2.pop())
        del bid1, bid2
