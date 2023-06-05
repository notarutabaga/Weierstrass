import igraph as ig
import matplotlib.pyplot as plt
from functions import *

def new_graph(edges, divisor):
    G = ig.Graph(edges)
    
    
    
    G.vs["divisor"] = divisor
    
    G.vs["burned"] = False
    G.es["burned"] = False
    
    return G

ig.config["plotting.backend"] = "matplotlib"
ig.config["plotting.layout"] = "auto"
ig.config.save()

G1 = new_graph(
        ([(0, 1), (0, 2),
          (1, 2), (1, 3), (1, 4),
          (2, 3), (2, 4),
          (3, 4)]),
        [2, 2, 1, -1, -1]
    )

G2 = new_graph(
        [(0, 1), (0, 2),
          (1, 2), (1, 3),
          (2, 4),
          (3, 4)],
        [-10, 1, 1, 1, 1]
    )