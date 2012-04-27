#!/usr/bin/python

# Fri Apr  6 18:07:22 PDT 2012
# from chapter 2 of Think Complexity

import string
import logging


class LinearMap(object):
    """A simple implementation of a map using a list of tuples
    where each tuple is a key-value pair."""

    def __init__(self):
        self.items = []

    def add(self, k, v):
        """Adds a new item that maps from key (k) to value (v).
        Assumes that they keys are unique."""
        self.items.append((k, v))

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError

    def iteritems(self):
        """docstring for iteritems"""
        for k, v in self.items:
            yield k, v

class BetterMap(object):
    """A faster implementation of a map using a list of LinearMaps
    and the built-in function hash() to determine which LinearMap
    to put each key into."""

    def __init__(self, n=100):
        """Appends (n) LinearMaps onto (self)."""
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        """Finds the right LinearMap for key (k)."""
        index = hash(k) % self.__len__()
        return self.maps[index]

    def add(self, k, v):
        """Adds a new item to the appropriate LinearMap for key (k)."""
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        """Finds the right LinearMap for key (k) and looks up (k) in it."""
        m = self.find_map(k)
        return m.get(k)

    def __len__(self):
        return len(self.maps)



class HashMap(object):
    """An implementation of a hashtable using a BetterMap
    that grows so that the number of items never exceeds the number
    of LinearMaps.

    The amortized cost of add should be O(1) provided that the
    implementation of sum in resize is linear."""

    def __init__(self):
        """Starts with 2 LinearMaps and 0 items."""
        self.maps = BetterMap(2)
        self.num = 0

        logging.basicConfig(
            format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
            level=logging.DEBUG
        )
        self.log = logging.getLogger(sys.argv[0])

    def get(self, k):
        """Looks up the key (k) and returns the corresponding value,
        or raises KeyError if the key is not found."""
        return self.maps.get(k)

    def add(self, k, v):
        """Resize the map if necessary and adds the new item."""
        if self.num == len(self.maps.maps):
            self.log.info("adding %s; resizing because num is %d" % (v, self.num))
            self.resize()

        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        """Makes a new map, twice as big, and rehashes the items."""
        new_map = BetterMap(self.num * 2)

        for m in self.maps.maps:
            for k, v in m.iteritems():
                self.log.info("remapping value %s to key %d" % (v, k))
                new_map.add(k, v)

        self.maps = new_map


def main(script):
    m = HashMap()
    s = string.ascii_lowercase

    for k, v in enumerate(s):
        m.add(k, v)

    for k in range(len(s)):
        print k, m.get(k)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
