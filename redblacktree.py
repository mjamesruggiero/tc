#!/usr/bin/python
import logging

# with an obvious debt to
# http://bit.ly/JEfBil

class RedBlackTree(object):
    def __init__(self):
        self._tree = None

    def insert(self, n):
        if self._tree == None:
            self._tree = RedBlackTreeNode(n)
            self._tree.set_color("Black")
        else:
            self._tree = self._tree.insert(n)

    def show(self):
        if self._tree == None:
            print "Empty"
        else:
            self._tree.show(1)

    def get_root(self):
        return self._tree


class RedBlackTreeNode(object):
    def __init__(self, value):
        self.value = value
        self._right = None
        self._left = None
        self._parent = None
        self.set_color("Red")

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_left(self):
        return self._left

    def set_left(self, left):
        self._left = left

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._right = right

    def get_grandparent(self):
        if self.get_parent() != None:
            return self.get_parent().get_parent()
        return None

    def get_uncle(self):
        grand = self.get_grandparent()
        if grand is not None:
            if grand.get_left() == self.get_parent():
                return grand.get_right()
            else:
                return grand.get_left()
        else:
            return None
    
    def is_red(self):
        return self.get_color() == "Red"

    def is_black(self):
        return self.get_color() == "Black"

    def rebalance(self):
        # case one: tree root
        if self.get_parent() is None:
            self.set_color("Black")
            return self

        # case 2: parent of the target node is BLACK
        # so the tree is in fine balance shape, just return
        # the tree's root
        if self.get_parent().get_color() == "Black":
            return self.get_root()

        # from here on, we know the parent is RED.
        # case 3: self, parent and uncle are all RED.
        if self.get_uncle() is not None and \
                self.get_uncle().get_color() == "Red":
            self.get_uncle().set_color("Black")
            self.get_parent().set_color("Black")
            self.get_grandparent().set_color("Red")
            return self.get_grandparent().rebalance()

        # by now, we know that self and parent are red, uncle is black.
        # we also know that the grandparent is not None, because if it were,
        # parent would be root, which must be black. So this means we need
        # to do a pivot on the parent
        return self.pivot_and_rebalance()

    def get_root(self):
        if self.get_parent() is None:
            return self
        else:
            return self.get_parent().get_root()

    def pivot_and_rebalance(self):
        # First, distinguish between the case where my parent
        # is a left child or right child
        if self.get_grandparent().get_left() == self.get_parent():
            if self.get_parent().get_right() == self:
                # case 4: I'm the right child of my parent,
                # and my parent is the left child of my grandparent.
                # Pivot right around me.
                return self.pivot_left(False)
            else:
                # case 5
                # If I'm the left child, and my parent is the left child,
                # pivot right around my parent
                return self.get_parent().pivot_right(True)
        else:  
            # my parent is the right child
            if self.get_parent().get_left() == self:
                # case 4, reverse
                return self.pivot_right(False)
            else:
                # case 5 reverse
                return self.get_parent().pivot_left(True)

    def pivot_right(self, recolor):
        left = self.get_left()
        right = self.get_right()
        parent = self.get_parent()
        grand = self.get_grandparent()

        #move my right child to be left of my soon-to-be former parent
        parent.set_left(right)
        if right is not None:
            right.set_parent(parent)

        #move up, and make my old parent my right child
        self.set_parent(grand)
        if grand is not None:
            if grand.get_right() == parent:
                grand.set_right(self)
            else:
                grand.set_left(self)
        self.set_right(parent)
        parent.set_parent(self)
        if recolor is True:
            parent.set_color("Red")
            self.set_color("Black")
            return self.get_root()
        else:
            # rebalance from the new position of my former parent
            return parent.rebalance()

    def pivot_left(self, recolor):
        left = self.get_left()
        right = self.get_right()
        parent = self.get_parent()
        grand = self.get_grandparent()

        #move my left child to be the right of my soon to be
        #former parent
        parent.set_right(left)
        if left is not None:
            left.set_parent(parent)

        #move up, and make my old parent my right child
        self.set_parent(grand)
        if grand is not None:
                if grand.get_right() == parent:
                    grand.set_right(self)
                else:
                    grand.set_left(self)
        self.set_left(parent)
        parent.set_parent(self)
        if recolor is True:
                parent.set_color("Red")
                self.set_color("Black")
                return self.get_root()

        #rebalance from the position of my former parent
        return parent.rebalance()

    def insert(self, value):
        if self.value > value:
            if self.get_left() is None:
                self.set_left(RedBlackTreeNode(value))
                self.get_left().set_parent(self)
                return self.get_left().rebalance()
            else:
                return self.get_left().insert(value)
        else:
            if self.get_right() is None:
                self.set_right(RedBlackTreeNode(value))
                self.get_right().set_parent(self)
                return self.get_right().rebalance()
            else:
                return self.get_right().insert(value)

    def show(self, indent=0):
        for i in range(indent):
            print " ",
            print "%s (%s)" % (self.value, self.get_color())
        if self.get_left() is None:
            for i in range(indent + 1):
                print " ",
            print "None(Black)"
        else:
            self.get_left().show(indent + 1)
        if self.get_right() is None:
            for i in range(indent + 1):
                print " ",
            print "None(Black)"
        else:
            self.get_right().show(indent + 1)
