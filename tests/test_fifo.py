#!/usr/bin/env python
# mjamesruggiero
# 2012-05-02 18:29:00
#
import unittest
import sys, os
import logging
from context import fifo
from fifo import Fifo, Node, appendLinkedList

class TestFifo(unittest.TestCase):
    """
    Build a FIFO
    """
    def setUp(self):
        logging.basicConfig(
            #filename ="/tmp/python.log",
            format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
            level=logging.DEBUG
        )
        self.log = logging.getLogger(self.__class__.__name__)

    def test_fifo(self):
        fifo = Fifo()
        test_word = 'coltrane'
        fifo.append(test_word)
        fifo.append('mingus')
        fifo.append('monk')
        popped = fifo.pop()
        self.assertTrue(test_word == popped)

    def test_node(self):
        node_funk = Node('funk')
        node_jazz = Node('jazz')
        node_funk.next = node_jazz
        node_jazz.prev = node_funk
        self.assertTrue(node_funk.next.value == 'jazz')

    def test_doubly_linked_list(self):
        ll = Node('funk')
        appendLinkedList(ll, Node('classical'))
        appendLinkedList(ll, Node('r&b'))
        appendLinkedList(ll, Node('country'))
        appendLinkedList(ll, Node('idm'))
        self.assertTrue(ll.next.next.next.value == 'country')

if __name__ == '__main__':
    unittest.main()
