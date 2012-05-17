#mjamesruggiero
#2012-03-29 08:23:38
#
from context import Graph
import unittest
import sys, os
import logging
from Graph import Graph
from Graph import Vertex
from Graph import Edge
import pprint

class TestGraph(unittest.TestCase):
    """
    testing graph class from Think Complexity
    """
    def setUp(self):
        logging.basicConfig(
            #filename ="/tmp/python.log",
            format="%(levelname)-10s %(asctime)s %(filename)s %(lineno)d %(message)s",
            level=logging.DEBUG
        )
        self.log = logging.getLogger(sys.argv[0])

        self.v = Vertex('v')
        self.w = Vertex('w')
        self.e = Edge(self.v, self.w)

        self.g = Graph([self.v, self.w], [self.e])
        
    def test_get_edge_returns_edge(self):
        q = Vertex('q')
        e2 = Edge(self.v, q)
        self.g.add_vertex(q)
        self.g.add_edge(e2)

        edge = self.g.get_edge(self.v, self.w)
        self.assertTrue(edge == self.e)

    #this one was giving me trouble
    def test_edges_returns_edges(self):
        expected = [self.e]
        self.assertEqual(self.g.edges(), expected)

    def test_vertices_should_return_vertices(self):
        self.assertTrue(self.v in self.g.vertices() \
                and self.w in self.g.vertices() \
                and len(self.g.vertices()) == 2)

    def test_get_edge_returns_none_for_missing_edge(self):
        """look for an edge that isn't there"""
        x = Vertex('x')
        edge = self.g.get_edge(x, self.w)
        self.assertTrue(edge == None)

    def test_remove_edge_removes_edge(self):
        """delete an edge"""
        self.g.remove_edge(self.e)
        self.assertTrue(self.g.get_edge(self.v, self.w) == None)

    def test_equality_of_edges(self):
        e1 = Edge(self.v, self.w) 
        e2 = Edge(self.w, self.v) 
        self.assertEquals(e1, e2)

    def test_out_edges(self):
        """Test that you get edges attached 
        to a vertex"""
        q = Vertex('q')
        e2 = Edge(self.v, q)
        self.g.add_vertex(q)
        self.g.add_edge(e2)

        self.assertTrue(self.e in self.g.out_edges(self.v), [self.e, e2])
        self.assertTrue(e2 in self.g.out_edges(self.v), [self.e, e2])
        self.assertTrue(len(self.g.out_edges(self.v)) == 2)
    
    def test_out_vertices(self):
        """Need this for the random graph"""
        x = Vertex('x')
        y = Vertex('y')
        z = Vertex('z')
        a = Vertex('a')
        edge_xy = Edge(x, y) 
        edge_ay = Edge(a, y) 
        g = Graph([x, y, z, a])
        g.add_edge(edge_ay)
        g.add_edge(edge_xy)

        self.assertTrue(len(g.out_vertices(y)) == 2)
        self.assertTrue(x in g.out_vertices(y))
        self.assertTrue(a in g.out_vertices(y))

    def test_add_all_edges(self):
        """Add edges foe each node"""
        empty_g = Graph()

        letters = ['l', 'm', 'o']
        for l in letters:
            empty_g.add_vertex(Vertex(l))

        empty_g.add_all_edges()
        self.assertTrue(len(empty_g.edges()) == 3)

    def test_regular_edges_works_with_6_vertices(self):
        """to build .add_regular_edges,
        we'll need a way tp count a Vertex's 
        number of edges"""
        vertices = [Vertex('x'), Vertex('y'), Vertex('z'), Vertex('a'), Vertex('b')]
        g = Graph(vertices, [])
        g.add_regular_edges()
        self.assertTrue(len(g.edges()) == 5)
        self.assertTrue(g.is_regular())

    def test_regular_edges_works_with_three_vertices(self):
        """to build .add_regular_edges,
        we'll need a way tp count a Vertex's 
        number of edges"""
        vertices = [Vertex('a'), Vertex('b'), Vertex('c')]
        g = Graph(vertices, [])
        g.add_regular_edges()
        self.assertTrue(len(g.edges()) == 3)
        self.assertTrue(g.is_regular())

    def test_regular_edges_works_with_six_vertices(self):
        """to build .add_regular_edges,
        we'll need a way tp count a Vertex's 
        number of edges"""
        import string
        six_letters = [c for c in string.ascii_lowercase][:6]
        vertices = [Vertex(l) for l in six_letters]
        g = Graph(vertices, [])
        g.add_regular_edges()
        #pp = pprint.PrettyPrinter()
        #pp.pprint(g)
        self.assertTrue(len(g.edges()) == 6)
        self.assertTrue(g.is_regular())

    def test_regular_edges_fail_when_edges_exist(self):
        """should raise exception when edge exists"""
        vertices = [Vertex('a'), Vertex('b')]
        e = Edge(*vertices)
        g = Graph(vertices)
        g.add_edge(e)

        with self.assertRaises(Exception):
            g.add_regular_edges()

    def test_choose_method(self):
        """The object should choose the righ method
        for populating edges based on graph rules"""
        g = Graph()
        self.assertFalse(g.choose_method(1, 1))
        self.assertEquals(g.choose_method(1, 2), g.add_all_edges)
        with self.assertRaises(Exception):
            g.choose_method(2, 2)
    
    def test_is_regular_should_return_true_for_regular(self):
        """Should return true when each node has the
        same number of edges"""
        vertices = [Vertex('a'), Vertex('b'), Vertex('9')]
        g = Graph(vertices, [])
        g.add_regular_edges()
        self.assertTrue(g.is_regular())

    def test_is_regular_should_return_false_for_nonregular(self):
        """Should return false when each node has the
        same number of edges"""
        vertices = Vertex('a'), Vertex('c')
        g = Graph(vertices, [])
        b = Vertex('b')
        g.add_vertex(b)
        e = Edge(b, vertices[1])
        g.add_edge(e)
        self.assertFalse(g.is_regular())

    def test_is_connected_sees_connected_graph(self):
        """a graph is connected if there is a path
        from every node to every other node"""
        a, b, c, d  = Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d')
        g = Graph([a, b, c, d]) 
        g.add_edge(Edge(a, b))
        g.add_edge(Edge(b, c))
        g.add_edge(Edge(c, d))
        g.add_edge(Edge(d, a))
        self.assertTrue(g.is_connected())

    def test_is_connected_sees_non_connected_graph(self):
        a, b, c, d  = Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d')
        e = Vertex('e')
        g = Graph([a, b, c, d, e]) 
        g.add_edge(Edge(a, b))
        g.add_edge(Edge(b, c))
        g.add_edge(Edge(c, d))
        g.add_edge(Edge(d, a))
        self.assertFalse(g.is_connected())

if __name__ == '__main__':
    unittest.main()
