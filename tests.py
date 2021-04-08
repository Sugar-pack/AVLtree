from unittest import TestCase

from main import AVLtree


class TestAVLtree_init(TestCase):
    def test_initbynone(self):
        testempty = AVLtree()
        self.assertEqual(testempty.node, None)
        self.assertEqual(testempty.height, 0)
        self.assertEqual(testempty.bfactor, 0)

    def test_initbylist(self):
        l = [1,2,3,4]
        testinit = AVLtree(l)
        self.assertEqual(testinit.node.value, 2)
        self.assertEqual(testinit.node.right.node.value, 3)
        self.assertEqual(testinit.node.left.node.value, 1)
        self.assertEqual(testinit.node.right.node.right.node.value, 4)
        self.assertEqual(testinit.bfactor, -1)
        self.assertEqual(testinit.getheight(), 3)
        self.assertEqual(testinit.node.left.getheight(), 1)
        self.assertEqual(testinit.node.right.getheight(), 2)
        self.assertEqual(testinit.node.right.node.right.getheight(), 1)

    def test_initbynum(self):
        testnum=AVLtree(1)
        self.assertEqual(testnum.node.value,1)
        self.assertEqual(testnum.getheight(),1)
        self.assertEqual(testnum.bfactor, 0)

class TestAVLappend(TestCase):
    def test_append(self):
        l = [1, 2, 3, 4]
        testtree = AVLtree()
        for i in l:
            testtree.append(i)
        self.assertEqual(testtree.node.value, 2)
        self.assertEqual(testtree.node.right.node.value, 3)
        self.assertEqual(testtree.node.left.node.value, 1)
        self.assertEqual(testtree.node.right.node.right.node.value, 4)
        self.assertEqual(testtree.bfactor, -1)
        self.assertEqual(testtree.getheight(), 3)
        self.assertEqual(testtree.node.left.getheight(), 1)
        self.assertEqual(testtree.node.right.getheight(), 2)
        self.assertEqual(testtree.node.right.node.right.getheight(), 1)

class TestAVLiscontain(TestCase):
    def test_iscontain(self):
        l = [1, 2, 3, 4]
        testtree= AVLtree(l)
        self.assertTrue(testtree.iscontain(4))
        self.assertFalse(testtree.iscontain(7))







