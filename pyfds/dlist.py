from .utils import change
from .utils.dnode import Node


class DList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        l = "DList : ["
        tmp = self.__head
        while tmp:
            l += str(tmp.data)
            if tmp.next:
                l += " <=> "
            tmp = tmp.next
        return l + "]"

    def __len__(self):
        size = 0
        tmp = self.__head
        while tmp:
            tmp = tmp.next
            size += 1
        return size

    @property
    def first(self):
        try:
            return self.__head.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    @property
    def last(self):
        try:
            return self.__tail.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def empty(self):
        return self.__head is None

    def clear(self):
        while not self.empty():
            ptr = self.__head
            self.__head = self.__head.next
            del ptr
    
    def add_begin(self, data):
        node = Node(data)
        if self.empty():
            self.__head = self.__tail = node
        else:
            node.next=  self.__head
            self.__head.prev = node
            self.__head = node

    def add_fin(self, data):
        node = Node(data)
        if self.empty():
            self.__head=  self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node

    def insert(self, data, pos=0):
        node = Node(data)
        if self.empty():
            self.__head = self.__tail = node
        elif pos == 0:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node
        elif pos == -1:
            self.add_fin(data)
        else:
            tmp = self.__head
            count = 0
            while tmp and count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            cur.next = node
            node.prev = cur
            node.next = tmp

    def remove(self, pos=0):
        try:
            tmp = self.__head
            count = 0
            if pos == 0:
                ptr = self.__head
                data = self.__head.data
                self.__head = self.__head.next
                self.__head.prev= None
                del ptr
                return data
            elif pos == -1:
                while tmp.next:
                    cur = tmp
                    tmp = tmp.next
                data = tmp.data
                cur.next = None
                self.__tail = cur
                del tmp
                return data
            while count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            nxt = tmp.next
            data = tmp.data
            cur.next = tmp.next
            nxt.prev = cur
            del tmp
            return data
        except Exception as ex:
            print("Error, %s" %ex)
    
    def delete(self, data):
        try:
            while self.__head.data == data:
                ptr = self.__head
                self.__head = self.__head.next
                self.__head.prev = None
                del ptr
            cur = self.__head
            tmp = cur.next
            while tmp:
                if tmp.data == data:
                    ptr = tmp
                    tmp = tmp.next
                    cur.next = tmp
                    del ptr
                else:
                    cur = tmp
                    tmp = tmp.next
            self.__tail = cur
        except Exception as ex:
            print("Error, %s" %ex)
    
    def find(self, data):
        count = 0
        tmp = self.__head
        while tmp:
            if tmp.data == data:
                count += 1
            tmp = tmp.next
        return count

    def reverse(self):
        prv = self.__head
        tmp = prv.next
        prv.next = None
        prv.prev = tmp
        while tmp:
            nxt = tmp.next
            tmp.next = prv
            tmp.prev = nxt
            prv = tmp
            tmp = nxt
        self.__head = prv

    def sort(self):
        tmp1 = self.__head
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
            self.add_fin(self.remove())

    @classmethod
    def merge(cls, dl1, dl2):
        try:
            lst = DList()
            tmp1 = dl1.__head
            tmp2 = dl2.__head
            while tmp1:
                lst.add_fin(tmp1.data)
                tmp1 = tmp1.next
            while tmp2:
                lst.add_fin(tmp2.data)
                tmp2 = tmp2.next
            del tmp1, tmp2
            return lst
        except Exception as ex:
            print("Error, %s" %ex)

    @classmethod
    def swap(cls, dl1, dl2):
        bid = DList()
        while not dl1.empty():
            bid.add_fin(dl1.remove())
        while not dl2.empty():
            dl1.add_fin(dl2.remove())
        while not bid.empty():
            dl2.add_fin(bid.remove())
        del bid
