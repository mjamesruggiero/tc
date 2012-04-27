#mjamesruggiero
#2012-04-12 21:07:31
#
#TODO : put the log level in a config
#
import unittest
import sys, os
import logging
from ConfigParser import ConfigParser
from redblacktree import Redblacktree, Node

class TestRedblacktree(unittest.TestCase):
    """
    A red-black tree
    """
    def setUp(self):
        pass
        
#    def test_first_node_should_be_black(self):
#        rbt = Redblacktree()
#        rbt.add(Node(5))
#        rbt.add(Node(4))
#        self.assertTrue(rbt.root.is_black())
#
#    def test_adding_lesser_value_should_create_left_node(self):
#        rbt = Redblacktree()
#        rbt.add(Node(5))
#        rbt.add(Node(4))
#        self.assertTrue(rbt.root.left.value == 4)
#
#    def test_adding_greater_value_should_create_right_node(self):
#        rbt = Redblacktree()
#        rbt.add(Node(9))
#        rbt.add(Node(11))
#        self.assertTrue(rbt.root.right.value == 11)
#
#    def test_node_added_should_be_red(self):
#        rbt = Redblacktree()
#        rbt.add(Node(9))
#        rbt.add(Node(11))
#        self.assertTrue(rbt.root.right.is_red)
#
#    def test_nodes_should_obey_less_than(self):
#        less = Node(9)
#        more = Node(11)
#        self.assertTrue(less < more)
#
#    def test_nodes_should_obey_greater_than(self):
#        less = Node(1234)
#        more = Node(12312876)
#        self.assertTrue(more > less)
#
    def test_adding_unsorted_values_should_alter_root(self):
        """Testing the rotate methods"""
        rbt = Redblacktree()
        rbt.add(Node(9))
        rbt.add(Node(11))
        operations = rbt.add(Node(10))
        log.debug("there were %d operations when you added 10" % operations)
        log.debug("the root is actually %d" % rbt.root.value)
        #rbt.print_tree()
        self.assertTrue(rbt.root.value == 10)

    #def test_both_children_of_a_red_node_are_black(self):
    #    """Where we start to test for pivots"""
    #    pass

if __name__ == '__main__':

    logging.basicConfig(
        #filename ="/tmp/python.log",
        format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
        level=logging.DEBUG
    )
    log = logging.getLogger(sys.argv[0])
    unittest.main()
