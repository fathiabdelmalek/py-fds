from .node import Node
from .dnode import Node
from .pair import Pair


def change(node1, node2):
    bid = node1.data
    node1.data = node2.data
    node2.data = bid
    del bid
