class _Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def __str__(self):
        l = "DList : ["
        tmp = self.__head
        while tmp is not None:
            l += str(tmp.data)
            if tmp.next is not None:
                l += " <=> "
            tmp = tmp.next
        return l + "]"

    def __len__(self, value):
        size = 0
        tmp = self.__head
        while tmp is not None:
            tmp = tmp.next
            size += 1
        return size

    def empty(self):
        return self.__head == None

    def clear(self):
        while not self.empty():
            ptr = self.__head
            self.__head = self.__head.next
            del ptr
    
    def add_begin(self, data):
        node = _Node(data)
        if self.empty():
            self.__head = self.__tail = node
        else:
            node.next=  self.__head
            self.__head.prev = node
            self.__head = node

    def add_fin(self, data):
        node = _Node(data)
        if self.empty():
            self.__head=  self.__tail = node
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node

    def insert(self, data, pos=0):
        node = _Node(data)
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
            while tmp is not None and count < pos:
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
                while tmp.next is not None:
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
            deta = tmp.data
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
            while tmp is not None:
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

    def first(self):
        try:
            return self.__head.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')

    def last(self):
        try:
            return self.__tail.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')
    
    def find(self, data):
        count = 0
        tmp = self.__head
        while tmp is not None:
            if tmp.data == data:
                count += 1
            tmp = tmp.next
        return count