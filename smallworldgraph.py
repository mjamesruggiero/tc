#!/usr/bin/env python
#
# mjamesruggiero
# Tue May  8 18:50:33 PDT 2012
from RandomGraph import RandomGraph
from Graph import Vertex, Edge
from pprint import pprint
import GraphWorld
import random
import string


class SmallWorldGraph(RandomGraph):
    """Implementing Watts & Strogatz"""
    def __init__(self, n=8):
        vertex_generator = self.vertex_gen()
        vertices = [Vertex(vertex_generator.next()) for letter in range(n)]
        super(RandomGraph, self).__init__(vertices, [])
        self.add_regular_edges()
        #self.add_random_edges()

    def vertex_gen(self):
        """Generator of values"""
        while True:
            for c in string.uppercase:
                yield c


    def rewire(self, probability):
        """rewires a regular graph
        to be small-world"""
        
        #start with a regular graph
        vs = self.vertices()
        for i,v in enumerate(vs):
            for j,w in enumerate(vs):
                if j <= i: continue
                if random.random() > probability: continue

                #remove edges with these nodes
                for vertex in (v, w):
                    self.remove_existing_edges(vertex)
                #make new random one
                self.add_edge(Edge(v, w))

    def remove_existing_edges(self, vertex):
        """docstring for remove_existing_edges("""
        edges = self.out_edges(vertex)
        for e in edges:
            self.remove_edge(e)

    def clustering_coefficient(self):
        """Returns the clustering coefficient
        for a small world graph"""
        pass
        
def main(script, n=8, p=.01, *args):
    """docstring for main"""
    swg = SmallWorldGraph(int(n))
    #probability = .2
    #swg.rewire(probability)
    pprint(swg)

    layout = GraphWorld.CircleLayout(swg)
    gw = GraphWorld.GraphWorld()
    gw.show_graph(swg, layout)
    gw.mainloop()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
