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
