import igraph as ig
from igraph import Graph
import dhars

def new_graph(edges, divisor):
    G = ig.Graph(edges)
    
    G.vs["divisor"] = divisor
    
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

def complete(n):
    G = Graph.Full(n)
    
    G.vs["divisor"] = 0
    
    G.vs["burned"] = False
    G.es["burned"] = False  
    
    return G 
    