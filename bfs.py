#!/usr/bin/env python
#
# mjamesruggiero
# Fri May  4 08:20:57 PDT 2012
#
# Implement BFS using a list and a queue.
# The list version has "two performance bugs."
# What are they? What is the actual order of growth for this algorithm?
# Test this code with a range of graph sizes and check your analysis.
# Then use a FIFO implementation to fix the errors
# and confirm that your algorithm is linear.
from redblacktree import RedBlackTree
from timemaps import etime, plot, save, random_string
import matplotlib.pyplot as pyplot
from time import localtime

class Dictfifo(object):
    """After Raymon Hettinger"""

    def __init__(self):
       self.nextin = 0
       self.nextout = 0
       self.data = {}

    def append(self, value):
        self.data[self.nextin] = value
        self.nextin += 1

    def pop(self):
        try:
            value = self.data.pop(self.nextout)
            self.nextout +=1
            return value
        except KeyError:
            return None

    def len(self):
        return len(self.data.keys())
        

def naive_bfs(top_node, visit):
    """Breadth-first search on a graph, 
    starting at top_node. 
    I'm thinking the performance bugs are:
        a. popping a list at the end forces a re-index
        of the entire list and 
        b. 'and c not in queue' requires a search of the
        entire list of nodes"""
    visited = set()
    queue = [top_node]
    while len(queue):
        curr_node = queue.pop(0)  # dequeue
        visit(curr_node)          # visit the node
        visited.add(curr_node)

        # Enqueue non-visited and non-enqueued children
        queue.extend(c for c in curr_node.children()
                     if c not in visited and c not in queue)


def less_naive_bfs(top_node, visit):
    """Uses a FIFO rather than extending
    a list"""
    visited = set()
    queue = Dictfifo()
    while queue.len():
        curr_node = queue.pop()  # FIFO
        visit(curr_node)
        visited.add(curr_node)

        (queue.append(c) for c in curr_node.children()
            if c not in visited and c not in queue)


def visit_node(node):
    print "visited %s" % node.value



def test_etime(func, factor):
    start = etime()
    test_bfs(func, factor)
    end = etime()
    elapsed = end - start
    return elapsed


def test_several_times(func, factor):
    times = []
    results = []
    for i in range(2, 25):
        number = factor * i
        elapsed = test_etime(func, number)
        times.append(elapsed)
        results.append(number)
    return results, times


def test_bfs(func, size):
    rbt = RedBlackTree()
    for i in range (1, size):
        rbt.insert(random_string(14)) 
    this_func = eval(func)
    this_func(rbt.get_root(), visit_node)


def graphit(factor):
    exp = 1.0
    scale = 'log'
    funcnames = {'naive_bfs':'darkgreen',
                 'less_naive_bfs': 'red' }

    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title('')
    pyplot.xlabel('n')
    pyplot.ylabel('run time (n)')

    for funcname, color in funcnames.items():
        data = test_several_times(funcname, factor)
        print data
        plot(*data, label=funcname, color=color, exp=exp)

    pyplot.legend(loc=4)
    stamp = '%4d-%02d-%02d-%02d-%02d-%02d' % localtime()[:6]
    filename = "bfs-comparison-%s" % stamp
    save(filename)

if __name__ == '__main__':

    factor = 10000
    graphit(factor)
