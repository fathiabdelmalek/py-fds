from .utils import change
from .utils.node import Node


class List:
    def __init__(self):
        self.__head = None

    def __str__(self):
        l = "List : ["
        tmp = self.__head
        while tmp:
            l += str(tmp.data)
            if tmp.next:
                l += " -> "
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
            print("Error, %s" % ex, end=', ')
    
    @property
    def last(self):
        try:
            tmp = self.__head
            while tmp.next:
                tmp = tmp.next
            return tmp.data
        except Exception as ex:
            print("Error, %s" % ex, end=', ')

    def empty(self):
        return self.__head is None

    def clear(self):
        while not self.empty():
            ptr = self.__head
            self.__head = self.__head.next
            del ptr

    def insert(self, data, pos=0):
        node = Node(data)
        if self.empty():
            self.__head = node
        elif pos == 0:
            node.next = self.__head
            self.__head = node
        elif pos == -1:
            self.append(data)
        else:
            tmp = self.__head
            count = 0
            while tmp and count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            cur.next = node
            node.next = tmp
        
    def append(self, data):
        node = Node(data)
        if self.empty():
            self.__head = node
        else:
            tmp = self.__head
            while tmp.next:
                tmp = tmp.next
            tmp.next = node

    def remove(self, pos=0):
        try:
            tmp = self.__head
            count = 0
            if pos == 0:
                ptr = self.__head
                data = self.__head.data
                self.__head = self.__head.next
                del ptr
                return data
            elif pos == -1:
                while tmp.next:
                    cur = tmp
                    tmp = tmp.next
                data = tmp.data
                cur.next = None
                del tmp
                return data
            while count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            data = tmp.data
            cur.next = tmp.next
            del tmp
            return data
        except Exception as ex:
            print("Error, %s" %ex)
    
    def delete(self, data):
        try:
            while self.__head.data == data:
                ptr = self.__head
                self.__head = self.__head.next
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
        prv = None
        cur = self.__head
        nxt = cur.next
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
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
            self.append(self.remove())

    @classmethod
    def merge(cls, l1, l2):
        try:
            lst = List()
            tmp1 = l1.__head
            tmp2 = l2.__head
            while tmp1:
                lst.append(tmp1.data)
                tmp1 = tmp1.next
            while tmp2:
                lst.append(tmp2.data)
                tmp2 = tmp2.next
            del tmp1, tmp2
            return lst
        except Exception as ex:
            print("Error, %s" %ex)

    @classmethod
    def swap(cls, l1, l2):
        bid = List()
        while not l1.empty():
            bid.append(l1.remove())
        while not l2.empty():
            l1.append(l2.remove())
        while not bid.empty():
            l2.append(bid.remove())
        del bid
