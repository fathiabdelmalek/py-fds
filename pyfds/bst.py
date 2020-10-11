from pyfds.utils.tnode import Node


class BST:
    def __init__(self):
        self.__root = None
        self.__number_of_nodes = 0
        self.__number_of_liefs = 0

    def __gototarget(self, tmp, data):
        while tmp:
            if data == tmp.data:
                break
            elif data < tmp.data:
                tmp = tmp.left
            else:
                tmp = tmp.right
        return tmp

    def __change_parents_child(self, data, p, node):
        if data < p.data:
            p.left = node
        else:
            p.right = node

    def __delete(self, data, tmp):
        p = self.parent(data)
        if p:
            self.__change_parents_child(data, p, tmp.left)
        else:
            self.__root = None
        del p

    def __min(self, data):
        tmp = self.__root
        tmp = self.__gototarget(tmp, data)
        while tmp.left:
            tmp = tmp.left
        return tmp

    def __max(self, data):
        tmp = self.__root
        tmp = self.__gototarget(tmp, data)
        while tmp.right:
            tmp = tmp.right
        return tmp

    @property
    def pre_order(self):
        def _pre_order(tmp):
            if tmp:
                print(tmp.data, end=', ')
                _pre_order(tmp.left)
                _pre_order(tmp.right)
        _pre_order(self.__root)
        if self.__root:
            print("end")

    @property
    def in_order(self):
        def _pre_order(tmp):
            if tmp:
                _pre_order(tmp.left)
                print(tmp.data, end=', ')
                _pre_order(tmp.right)
        _pre_order(self.__root)
        if self.__root:
            print("end")

    @property
    def post_order(self):
        def _pre_order(tmp):
            if tmp:
                _pre_order(tmp.left)
                _pre_order(tmp.right)
                print(tmp.data, end=', ')
        _pre_order(self.__root)
        if self.__root:
            print("end")

    @property
    def number_of_nodes(self):
        return self.__number_of_nodes

    @number_of_nodes.setter
    def number_of_nodes(self, num):
        self.__number_of_nodes += num

    @property
    def number_of_liefs(self):
        def _number_of_liefs(root):
            if root is None:
                return 0
            else:
                if root.left is None and root.right is None:
                    return 1
                else:
                    return _number_of_liefs(root.left) + _number_of_liefs(root.right)
        return _number_of_liefs(self.__root)

    @property
    def height(self):
        def _height(root):
            if root is None:
                return 0
            else:
                return 1 + max(_height(root.left), _height(root.right))
        return _height(self.__root)

    @property
    def max(self):
        root = self.__root
        while root.right:
            root = root.right
        return root.data

    @property
    def min(self):
        root = self.__root
        while root.left:
            root = root.left
        return root.data

    def empty(self):
        return self.__root is None

    def clear(self):
        def _clear(root):
            if root:
                _clear(root.right)
                _clear(root.left)
                root.right = None
                root.left = None
                del root
        _clear(self.__root)
        self.__root = None

    def append(self, data):
        node = Node(data)
        if self.empty():
            self.__root = node
        else:
            Node.chain(self.__root, node)
        self.__number_of_nodes += 1

    def find(self, data):
        def _search(root):
            while root:
                if data == root.data:
                    return root
                elif data < root.data:
                    root = root.left
                else:
                    root = root.right
            return None
        return _search(self.__root)

    def parent(self, data):
        s = self.find(data)
        if s:
            if data == self.__root.data:
                return None
            else:
                tmp = self.__root
                p = None
                while tmp.data != data:
                    p = tmp
                    if data < tmp.data:
                        tmp = tmp.left
                    elif data > tmp.data:
                        tmp = tmp.right
                return p
        return None

    def successor(self, data):
        tmp = self.__root
        tmp = self.__gototarget(tmp, data)
        if tmp:
            if tmp.right:
                return self.__min(tmp.right.data)
            else:
                p = self.parent(data)
                while p.data < tmp.data:
                    if tmp == self.__root:
                        return None
                    else:
                        p = self.parent(p.data)
                return p
        return None

    def predecessor(self, data):
        tmp = self.__root
        tmp = self.__gototarget(tmp, data)
        if tmp:
            if tmp.left:
                return self.__max(tmp.left.data)
            else:
                p = self.parent(data)
                while p.data > tmp.data:
                    if tmp == self.__root:
                        return None
                    else:
                        p = self.parent(p.data)
                return p
        return None

    def delete(self, data):
        tmp = self.__root
        tmp = self.__gototarget(tmp, data)
        if tmp:
            if not tmp.left and not tmp.right:
                self.__delete(data, tmp)
            elif tmp.left and not tmp.right:
                self.__delete(data, tmp)
            elif not tmp.left and tmp.right:
                self.__delete(data, tmp)
            else:
                s = self.successor(data)
                p = self.parent(s.data)
                p.left = None
                s.left = tmp.left
                s.right = p
                p = self.parent(data)
                if p:
                    self.__change_parents_child(data, p, s)
                else:
                    self.__root = s
                del s, p
            d = tmp.data
            tmp.left = tmp.right = None
            del tmp
            self.__number_of_nodes -= 1
            return d
        return None

    @classmethod
    def equals(cls, bst1, bst2):
        def _equals(bst1, bst2):
            if bst1 is None and bst2 is None:
                return True
            else:
                if bst1 is None or bst2 is None:
                    return False
                else:
                    return (bst1.data == bst2.data) and (_equals(bst1.right, bst2.right)) and (_equals(bst1.left, bst2.left))
        return _equals(bst1.__root, bst2.__root)
