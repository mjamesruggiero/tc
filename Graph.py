#!/usr/bin/python
#
# from Think Complexity, chapter 2
# Tue Mar 27 22:42:32 PDT 2012
#
from itertools import *
import pprint
from collections import deque

class Graph(dict):

    def __init__(self, vs=[], es=[]):
        """Create a new graph.
        (vs) is a list of vertices
        (es) is a list of edges."""
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """"Add (v) to the graph"""
        self[v] = {}

    def add_edge(self, e):
        """Add (e) to the graph;
        by adding an entry in both directions.
        If there is already an edge connecting these Vertices,
        the new edge replaces it"""
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, vertex1, vertex2):
        """takes two vertices 
        and returns the edge 
        between them if it exists, 
        else returns 'None'"""
        try:
            return self[vertex1][vertex2]
        except KeyError:
            return None

    def remove_edge(self, edge):
        """Take an edge and remove all references 
        from it in the graph"""
        if self.get_edge(edge[0], edge[1]):
            del self[edge[0]][edge[1]]

    def vertices(self):
        """Get a list of vertices in a graph,
        sorting helps testability"""
        keylist = self.keys()
        keylist.sort()
        return [v for v in keylist]

    def edges(self):
        """return a list of edges in a graph.
        Note that in our undirected graph, there are
        two references to each edge"""
        edges = set()
        for d in self.itervalues():
            potential_edges = d.values()
            for potential in potential_edges:
                edges.add(potential)
        return list(edges)

    def out_vertices(self, vertex):
        """Take a vertex and return a list 
        of adjacent vertices (i.e. connected to 
        the given node by an edge)"""
        return self[vertex].keys()

    def out_edges(self, vertex):
        """Takes a vertex and returns 
        a list of edges connected to that vertex"""
        return self[vertex].values()

    def add_all_edges(self):
        """Makes a complete graph
        by adding edges between all pairs
        of vertices"""
        vertices = self.keys()
        offset = vertices[1:] + [vertices[0]]

        for i in izip(vertices, offset):
            self.add_edge(Edge(*i))

    def add_regular_edges(self, degree=None):
        """Add regular edges to empty graph"""
        if len(self.edges()) > 0:
            message = "cannot set regular edges; "
            message += "graph already contains %d edge(s)" % len(self.edges())
            raise Exception, message
        self.add_all_edges()

    def choose_method(self, degree, vertices_num):
        """Pick the method of populating 
        regular edges"""
        if degree == 1 and vertices_num == 1:
            #do nothing
            return False
        if degree == 1 and vertices_num > 1:
            return self.add_all_edges
        if degree == 2 and vertices_num < 3:
            raise Exception, "cannot create regular of degree 2 \
                             with fewer than 3 vertices"

    def is_regular(self):
        """true if all vertices 
        have the same number of edges"""
        edge_count = []
        for d in self.itervalues():
            edge_count.append(len(d.values()))
        return len(set(edge_count)) <= 1

    def breadth_first_search(self, s):
        visited = set()
        queue = deque([s])

        while queue:
            v = queue.popleft()
            if v in visited: continue
            visited.add(v)
            queue.extend(self.out_vertices(v))

        return visited

    def is_connected(self):
        vs = self.vertices()
        visited = self.breadth_first_search(vs[0])
        return len(visited) ==len(vs)

class Vertex(object):
    """Elements in a Graph"""
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' % repr(self.label)
        
    __str__ = __repr__


class Edge(tuple):
    """
    Edge: the connection between two vertices
    
    For mutable objects, 
    it's common to override __init__ 
    and use the default implementation 
    of __new__; because Edge inherits from
    tuple, it is immutable so we call tuple's __new__
    """
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

    def __eq__(self, other):
        try:
            normal_match = (self[0] == other[0]) and \
                                (self[1] == other[1])

            inverse_match = (self[0] == other[1]) and \
                            (self[1] == other[0])
            return normal_match or inverse_match    
        except:
            return False
