import fds.stack

class _Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.__front = None
        self.__back = None

    def __repr__(self):
        q = "Queue : ["
        tmp = self.__front
        while tmp is not None:
            q += str(tmp.data)
            if tmp.next is not None:
                q += " | "
            tmp = tmp.next
        return q + "]"

    def __len__(self):
        size = 0
        tmp = self.__front
        while tmp is not None:
            size += 1
            tmp = tmp.next
        return size

    def empty(self):
        return self.__front is None

    def clear(self):
        while not self.empty():
            ptr = self.__front
            self.__front = self.__front.next
            del ptr

    def enqueue(self, data):
        node = _Node(data)
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
    
    def front(self):
        try:
            return self.__front.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def back(self):
        try:
            return self.__back.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def find(self, data):
        count = 0
        tmp = self.__front
        while tmp is not None:
            if tmp.data = data:
                count += 1
            tmp = tmp.next
        return count

    def reverse(self):
        stck = stack.Stack()
        while not self.empty():
            stck.push(self.enqueue())
        while not stck.empty():
            self.enqueue(stck.pop())
        return self
    