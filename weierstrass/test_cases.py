import igraph as ig
from igraph import Graph
import dhars

def new_graph(edges, divisor):
    G = ig.Graph(edges)
    
    G.vs["divisor"] = divisor
    G.vs["weier"] = False
    
    G.vs["burned"] = False
    G.es["burned"] = False  
    
    return G 

def housex():
    edges = [(0, 1), (0, 2),
            (1, 2), (1, 3), (1, 4),
            (2, 3), (2, 4),
            (3, 4)]
    divisor = 0

    G = new_graph(edges, divisor)
    return G

def sun():
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 0)]
    return new_graph(edges, 0)

def tulip():
    edges = [(0, 1), (0, 2), (0, 3),
             (1, 4),
             (2, 4),
             (3, 4),
             (4, 5), (4, 6), (4, 7), (4, 8),
             (5, 9),
             (6, 9),
             (7, 10),
             (8, 10)]
    
    return new_graph(edges, 0)

def complete(n):
    G = Graph.Full(n)
    
    G.vs["divisor"] = 0
    
    G.vs["burned"] = False
    G.es["burned"] = False  
    
    return G 

def compl_bipart(n, m):
    G = new_graph([], 0)
    G.add_vertices(n + m)

    for i in range(n):
        for j in range(m):
            G.add_edge(i, n + j)
            
    return G