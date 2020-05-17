class _Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self):
        self.__head = None

    def __repr__(self):
        l = "List : ["
        tmp = self.__head
        while tmp is not None:
            l += str(tmp.data)
            if tmp.next is not None:
                l += " -> "
            tmp = tmp.next
        return l + "]"

    def __len__(self):
        size = 0
        tmp = self.__head
        while tmp is not None:
            tmp = tmp.next
            size += 1
        return size 

    def empty(self):
        return self.__head is None

    def clear(self):
        while not self.empty():
            ptr = self.__head
            self.__head = self.__head.next
            del ptr

    def insert(self, data, pos=0):
        node = _Node(data)
        if self.empty():
            self.__head = node
        elif pos == 0:
            node.next = self.__head
            self.__head = node
        else:
            tmp = self.__head
            count = 0
            while tmp is not None and count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            cur.next = node
            node.next = tmp
        
    def append(self, data):
        node = _Node(data)
        if self.empty():
            self.__head = node
        else:
            tmp = self.__head
            while tmp.next is not None:
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
                while tmp.next is not None:
                    cur = tmp
                    tmp = tmp.next
                cur.next = None
            while count < pos:
                cur = tmp
                tmp = tmp.next
                count += 1
            cur.next = tmp.next
            del tmp
        except Exception as ex:
            print("Error, %s" %ex)
    
    def delete(self, data):
        try:
            if self.__head.data == data:
                ptr = self.__head
                self.__head = self.__head.next
                del ptr
            cur = self.__head
            tmp = cur.next
            while tmp.next is not None:
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
            tmp = self.__head
            while tmp.next is not None:
                tmp = tmp.next
            return tmp.data
        except Exception as ex:
            print("Error, %s" %ex, end=', ')
