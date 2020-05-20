class _Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.__top = None

    def __repr__(self):
        s = "Stack : ["
        tmp = self.__top
        while tmp is not None:
            s += str(tmp.data)
            if tmp.next is not None:
                s += "\n         "
            tmp = tmp.next
        return s + "]"

    def __len__(self):
        size = 0
        tmp = self.__top
        while tmp is not None:
            size += 1
            tmp = tmp.next
        return size

    def empty(self):
        return self.__top is None

    def clear(self):
        while not self.empty():
            ptr = self.__top
            self.__top = self.__top.next
            del ptr

    def push(self, data):
        node = _Node(data, self.__top)
        self.__top = node
        return self.__top

    def pop(self):
        ptr = self.__top
        data = ptr.data
        self.__top = self.__top.next
        del ptr
        return data

    def top(self):
        try:
            return self.__top.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def find(self, data):
        count = 0
        tmp = self.__top
        while tmp is not None:
            if tmp.data == data:
                count += 1
            tmp = tmp.next
        return count

    def reverse(self):
        stck = Stack()
        while not self.empty():
            stck.push(self.pop())
        return stck
    @classmethod
    def merge(self, s1: Stack, s2: Stack):
        try:
            stck = Stack()
            tmp1 = s1.__top
            tmp2 = s2.__top
            while tmp1 is not None:
                stck.push(tmp1.data)
                tmp1 = tmp1.next
            while tmp2 is not None:
                stck.push(tmp2.data)
                tmp2 = tmp2.next
            del tmp1, tmp2
            return stck
        except Exception as ex:
            print("Error, %s" %ex)
    @classmethod
    def swap(self, s1: Stack, s2: Stack):
        bid1 = Stack()
        bid2 = Stack()
        while not t1.empty():
            bid1.push(t1.pop())
        while not t2.empty():
            bid2.push(t2.pop())
        while not bid1.empty():
            t2.push(bid1.pop())
        while not bid2.empty():
            t1.push(bid2.pop())
        del bid1, bid2
    