#mjamesruggiero
#2012-04-12 21:07:31
#
from context import redblacktree
import unittest
import sys, os
import logging
from ConfigParser import ConfigParser
from redblacktree import RedBlackTree, RedBlackTreeNode

class TestRedBlackTree(unittest.TestCase):
    """
    A red-black tree
    """
    def setUp(self):
        pass
        
    def test_first_node_should_be_black(self):
        rbt = RedBlackTree()
        rbt.insert(5)
        rbt.insert(4)
        self.assertTrue(rbt.get_root().is_black())

    def test_inserting_lesser_value_should_create_left_node(self):
        rbt = RedBlackTree()
        rbt.insert(5)
        rbt.insert(4)
        self.assertTrue(rbt.get_root().get_left().value == 4)

    def test_inserting_greater_value_should_create_right_node(self):
        rbt = RedBlackTree()
        rbt.insert(9)
        rbt.insert(11)
        self.assertTrue(rbt.get_root().get_right().value == 11)

    def test_node_inserted_should_be_red(self):
        rbt = RedBlackTree()
        rbt.insert(9)
        rbt.insert(11)
        self.assertTrue(rbt.get_root().get_right().is_red())

    def test_inserting_unsorted_values_should_alter_root(self):
        """Testing the rotate methods"""
        rbt = RedBlackTree()
        rbt.insert(9)
        rbt.insert(11)
        rbt.insert(10)
        self.assertTrue(rbt.get_root().value == 10)

    def test_find_should_work_for_existing_value(self):
        search_value = 9
        rbt = RedBlackTree()
        for x in [7, 11, 19, 10, search_value]:
            rbt.insert(x) 
        self.assertTrue(rbt.search(search_value))

    def test_find_should_return_none_for_nonexistent_value(self):
        search_value = 5
        rbt = RedBlackTree()
        for x in [7, 11, 19, 10]:
            rbt.insert(x) 
        self.assertTrue(rbt.search(search_value) is None)

if __name__ == '__main__':

    logging.basicConfig(
        format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
        level=logging.DEBUG
    )
    log = logging.getLogger(sys.argv[0])
    unittest.main()
