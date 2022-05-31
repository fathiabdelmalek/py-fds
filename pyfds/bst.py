from pyfds.utils.tnode import Node, equals as node_equals


class BST:
    def __init__(self):
        self.__root = None
        self.__number_of_nodes = 0
        self.__number_of_liefs = 0

    def __go_to_target(self, data):
        tmp = self.__root
        while tmp:
            if data == tmp.data:
                return tmp
            elif data < tmp.data:
                tmp = tmp.left
            else:
                tmp = tmp.right

    def __min(self, data):
        tmp = self.__go_to_target(data)
        while tmp.left:
            tmp = tmp.left
        return tmp

    def __max(self, data):
        tmp = self.__go_to_target(data)
        while tmp.right:
            tmp = tmp.right
        return tmp

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
    def min(self):
        root = self.__root
        while root.left:
            root = root.left
        return root.data

    @property
    def max(self):
        root = self.__root
        while root.right:
            root = root.right
        return root.data

    def pre_order(self):
        def _pre_order(tmp):
            if tmp:
                print(tmp.data, end=', ')
                _pre_order(tmp.left)
                _pre_order(tmp.right)
        _pre_order(self.__root)
        if self.__root:
            print("end")

    def in_order(self):
        def _pre_order(tmp):
            if tmp:
                _pre_order(tmp.left)
                print(tmp.data, end=', ')
                _pre_order(tmp.right)
        _pre_order(self.__root)
        if self.__root:
            print("end")

    def post_order(self):
        def _pre_order(tmp):
            if tmp:
                _pre_order(tmp.left)
                _pre_order(tmp.right)
                print(tmp.data, end=', ')
        _pre_order(self.__root)
        if self.__root:
            print("end")

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
        tmp = self.__go_to_target(data)
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
        tmp = self.__go_to_target(data)
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
        def _change_child(_cur, _node):
            Node.chain(_cur, _node)

        def _change_parents_child(_p, _node):
            if data < _p.data:
                _p.left = _node
            else:
                _p.right = _node

        def _delete(_node):
            _p = self.parent(data)
            if _p:
                if _node.left:
                    _change_parents_child(_p, _node.left)
                else:
                    _change_parents_child(_p, _node.right)
            else:
                self.__root = None
            del _p

        node = self.__go_to_target(data)
        if node:
            if not node.left and not node.right:
                _delete(node)
            elif node.left and not node.right:
                _delete(node)
            elif not node.left and node.right:
                _delete(node)
            else:
                s = self.successor(data)
                p = self.parent(s.data)
                s.left = node.left
                p.left = None
                _change_child(s, p)
                p = self.parent(data)
                if p:
                    _change_parents_child(p, s)
                else:
                    self.__root = s
                del s, p
            d = node.data
            node.left = node.right = None
            del node
            self.__number_of_nodes -= 1
            return d
        return None

    def equals(self, bst):
        return node_equals(self.__root, bst.__root)
