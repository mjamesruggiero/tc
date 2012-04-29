#mjamesruggiero
#2012-04-28 09:41:01
#
#TODO : there usually is one
#
from context import redblackmap
import unittest
import sys, os
import logging
from ConfigParser import ConfigParser
from redblackmap import RedblackMap, KeyVal

class TestTestRedblackMap(unittest.TestCase):
        
    def test_keyval_knows_comparator_lt(self):
        kv_funky = KeyVal('funky', 1)
        kv_monkey = KeyVal('monkey', 1)
        # funky is less than monkey in alpha terms
        self.assertTrue(kv_funky < kv_monkey)

    def test_keyval_knows_comparator_gt(self):
        kv_funky = KeyVal('FUNKY', 1)
        kv_monkey = KeyVal('monkey', 2)
        self.assertTrue(kv_funky < kv_monkey)

    def test_keyval_knows_comparator_eq(self):
        kv_1 = KeyVal('monkey', 1)
        kv_2 = KeyVal('monkey', 2)
        self.assertTrue(kv_1 == kv_2)

    def test_you_can_set_and_get_string(self):
        """docstring for test_you_can_set"""
        rbmap = RedblackMap()
        rbmap.add('funky', 'monkey')
        self.assertTrue(rbmap.get('funky') == 'monkey')

    def test_you_can_set_and_get_string(self):
        """docstring for test_you_can_set"""
        rbmap = RedblackMap()
        test_pairs = (('George', 1943), ('Paul', 1942), ('John', 1940), ('Ringo', 1940))
        for pair in test_pairs:
            rbmap.add(pair[0], pair[1])
        for pair in test_pairs:
            self.assertTrue(rbmap.get(pair[0]) == pair[1])


if __name__ == '__main__':
    logging.basicConfig(
        #filename ="/tmp/python.log",
        format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
        level=logging.DEBUG
    )
    log = logging.getLogger(sys.argv[0])
    unittest.main()
