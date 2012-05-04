#!/usr/bin/env python

# Wed May  2 18:27:31 PDT 2012
# from Think Complexity chapter 4
# implement a Fifo

def appendLinkedList(linked_list, new_node):
    node = linked_list
    while True:
        if node.next == None:
            node.next = new_node
            new_node.prev = node
            break
        else:
            node = node.next

class Node(object):
    """A node has a next and previous"""
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Fifo(object):
    """docstring for Fifo"""
    def __init__(self):
        self.root_node = None

    def append(self, elem):
        """Put the item at the end of the list"""
        node = Node(elem)
        if self.root_node is None:
            self.root_node = node
        else:
            appendLinkedList(self.root_node, node)

    def pop(self):
        """remove and return the item at the front"""
        if self.root_node == None:
            return None
        
        node_to_pop = self.root_node
        self.root_node.prev = None
        self.root_node = self.root_node.next
        return node_to_pop.value
