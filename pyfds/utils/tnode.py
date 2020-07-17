class Node:
    def __init__(self, data=None, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, ptr):
        self.__left = ptr

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, ptr):
        self.__right = ptr

    @classmethod
    def chain(cls, cur, node):
        try:
            assert node.data != cur.data
        except Exception:
            raise Exception("this number is already exist")
        if node.data < cur.data:
            if cur.left is None:
                cur.left = node
            else:
                cls.chain(cur.left, node)
        else:
            if cur.right is None:
                cur.right = node
            else:
                cls.chain(cur.right, node)
