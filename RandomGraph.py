#!/usr/bin/python

# From Think Complexity, chapter 2
# Tue Apr  3 08:29:49 PDT 2012
# A random graph is a graph with edges 
# generated at random

import string
import random 

from collections import deque

from Graph import *

class RandomGraph(Graph):

    def add_random_edges(self, p = 0.5):
         """Starting with an empty graph,
         add edges to form a random graph
         where (p) is the probability
         that there is an edge between
         any pair of vertices"""
         vs = self.vertices()
         for i,v in enumerate(vs):
            for j,w in enumerate(vs):
                if j <= i: continue
                rand_num = random.random()
                if random.random() > p: continue
                #print "adding edge %s %s" % (v, w)
                self.add_edge(Edge(v, w))

    def bfs(self, s, visit=None):
        """Breadth-first search, starting with (s)
        If (visit) is provided, it is invoked on each
        vertex.
        Returns the set of visited vertices"""
        visited = set()

        queue = deque([s])

        #loop until the queue is cleared
        while queue:
            
            #get next vertex
            v = queue.popleft()

            #skip if already visited
            if v in visited: continue

            #mark visited
            #and invoke function
            visited.add(v)
            if visit: visit(v)

            #add it's out vertices to the queue
            queue.extend(self.out_vertices(v))

        #return the visited vertices
        return visited

    def is_connected(self):
        """Returns true if there is a path from any 
        vertex to any other vertex in this graph;
        returns false otherwise"""
        #print self.vertices()
        vs = self.vertices()
        visited = self.bfs(vs[0])
        return len(visited) ==len(vs)
            
def show_graph(g):
    import GraphWorld

    for v in g.vertices():
        g.color = 'blue'
        #if v.visited():
        #    g.color = 'white'
        #else:
        #    g.color = 'red'

    layout = GraphWorld.CircleLayout(g)
    gw = GraphWorld.GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

def test_graph(n, p):
    """Generates test random graph with (n)
    vertices and probability (p).
    Returns true if connected and false otherwise"""
    labels = string.lowercase + string.uppercase + string.punctuation
    vs = [Vertex(c) for c in labels[:n]]
    g = RandomGraph(vs)
    g.add_random_edges(p=p)
    show_graph(g)
    return g.is_connected()

def test_p(n, p, num):
    """Generates (num) random graphs with (n) vertices 
    and (p) probability and returns the count of how
    many are connected"""
    count = 0
    for i in range(num):
        if test_graph(n, p):
            count += 1
    return count

def main(script, n=26, p=0.1, num=1, *args):
    n = int(n)
    p = float(p)
    num = int(num)
    count = test_p(n, p, num)
    print "count is %d" % count

if __name__ == '__main__':
    import sys
    main(*sys.argv)
