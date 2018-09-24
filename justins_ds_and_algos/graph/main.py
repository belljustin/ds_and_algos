class Node(object):
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def isLeaf(self):
        if not self.children \
                or all(c is None for c in self.children):
            return True
        return False

    def __repr__(self):
        return "{}".format(self.value)

class BinaryNode(Node):
    def __init__(self, value, left=None, right=None):
        Node.__init__(self, value, [left, right])

    def setLeft(self, left):
        self.children[0] = left

    def getLeft(self):
        return self.children[0]

    def setRight(self, right):
        self.children[1] = right

    def getRight(self):
        return self.children[1]
