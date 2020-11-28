class Pair:
    def __init__(self, first=None, second=None):
        self.__first = first
        self.__second = second

    def __str__(self):
        p = "Pair : ["
        if self.__first and self.__second:
            p += str(self.__first)
            p += ", "
            p += str(self.__second)
        return p + "]"

    @property
    def first(self):
        try:
            return self.__first
        except Exception as ex:
            print("Error, %s" % ex)

    @first.setter
    def first(self, data):
        self.__first = data

    @property
    def second(self):
        try:
            return self.__second
        except Exception as ex:
            print("Error, %s" % ex)

    @second.setter
    def second(self, data):
        self.__second = data

    @classmethod
    def make_pair(cls, first=None, second=None):
        pair = Pair()
        pair.__first = first
        pair.__second = second
        return pair


def equals(pair1, pair2):
    if pair1 is None and pair2 is None:
        return True
    elif pair1 is None or pair2 is None:
        return False
    else:
        return pair1.second == pair2.second
