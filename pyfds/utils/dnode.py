class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, ptr):
        self.__next = ptr

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, ptr):
        self.__prev = ptr


def equals(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    else:
        return (node1.data == node2.data) and equals(node1.next, node2.next) and equals(node1.prev, node2.prev)
