#!/usr/bin/python
# Sat Apr 28 09:26:37 PDT 2012
# from chapter 2 of Think Complexity
import sys
import string
import logging
from bettermap import LinearMap, BetterMap, HashMap
from redblacktree import RedBlackTree

# TODO inherit red black map and overload the search
# so that it takes a key

class KeyVal(object):
    """docstring for KeyVal"""
    def __init__(self, k, v):
        self.key = k
        self.val = v
        
    def __lt__(self, other):
        return self.key.__lt__(other.key)

    def __gt__(self, other):
        return self.key.__gt__(other.key)

    def __eq__(self, other):
        return self.key.__eq__(other.key)

class RedblackMap(object):
    """An implementation of a hashtable using a BetterMap
    backed by a red black tree"""

    def __init__(self):
        self.map = RedBlackTree()

        logging.basicConfig(
            format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
            level=logging.DEBUG
        )
        self.log = logging.getLogger(sys.argv[0])

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        return self.map.search_by_key(k)

    def add(self, k, v):
        """Resize the map if necessary and adds the new item."""
        kv = KeyVal(k, v)
        self.map.insert(kv)
