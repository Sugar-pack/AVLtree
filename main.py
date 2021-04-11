class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class AVLtree:
    def __init__(self, *args):
        self.node = None
        self.bfactor = 0
        self.height = 0
        if len(args) == 1:
            listtoadd = []
            if isintorfloat(args[0]):
                listtoadd.append(args[0])
            else:
                listtoadd = args[0]
            for i in listtoadd:
                self.append(i)

    def getheight(self):
        if self.node:
            return self.height
        else:
            return 0

    def getbfactor(self):
        if self.node:
            return self.getbfactor
        else:
            return 0

    def append(self, value):
        prevnode = self.node
        newnode = Node(value)
        if prevnode is None:
            self.node = newnode
            self.node.left = AVLtree()
            self.node.right = AVLtree()
        elif value < prevnode.value:
            self.node.left.append(value)
        elif value > prevnode.value:
            self.node.right.append(value)
        else:
            return False
        self.upd_h_and_b()
        self.fixbalance()
        return True

    def upd_h(self):
        if self.node is not None:
            lh = 0
            rh = 0
            if self.node.right is not None:
                self.node.left.upd_h()
                lh = self.node.left.getheight()
            if self.node.right is not None:
                self.node.right.upd_h()
                rh = self.node.right.getheight()

            self.height = max(rh, lh) + 1
        else:
            self.height = 0

    def upd_bfactor(self):
        if self.node is not None:
            lh = 0
            rh = 0
            if self.node.left is not None:
                self.node.left.upd_bfactor()
                lh = self.node.left.height
            if self.node.right is not None:
                self.node.right.upd_bfactor()
                rh = self.node.right.height

            self.bfactor = lh - rh
        else:
            self.bfactor = 0

    def rotate_right(self):

        top = self.node
        mid = self.node.left.node
        bot = mid.right.node

        self.node = mid
        mid.right.node = top
        top.left.node = bot

    def rotate_left(self):

        top = self.node
        mid = self.node.right.node
        bot = mid.left.node

        self.node = mid
        mid.left.node = top
        top.right.node = bot

    def upd_h_and_b(self):
        self.upd_h()
        self.upd_bfactor()

    def fixbalance(self):
        self.upd_h_and_b()
        if self.bfactor == 2:
            if self.node.left.bfactor < 0:
                self.node.left.rotate_left()
                self.upd_h_and_b()
                return True
            self.rotate_right()
            self.upd_h_and_b()
            return True

        if self.bfactor == -2:
            if self.node.right.bfactor > 0:
                self.node.right.rotate_right()
                self.upd_h_and_b()
                return True
            self.rotate_left()
            self.upd_h_and_b()
            return True
        return False

    def contains(self, item):
        if self.node is None:
            return False
        elif item < self.node.value:
            return self.node.left.contains(item)
        elif item > self.node.value:
            return self.node.right.contains(item)
        else:
            return True


def isintorfloat(val):
    return type(val) == int or type(val) == float
