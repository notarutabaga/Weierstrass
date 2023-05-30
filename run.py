import igraph as ig
import matplotlib.pyplot as plt
from functions import *

ig.config["plotting.backend"] = "matplotlib"
ig.config["plotting.layout"] = "auto"
ig.config.save()

n = 5
edges = ([(0, 1), (0, 2),
          (1, 2), (1, 3), (1, 4),
          (2, 3), (2, 4),
          (3, 4)])

# new hosue-x graph G made using the edges list
G = ig.Graph(n, edges)

# divisor to test with (see example 2.5)
divisor = [2, 2, 1, -1, -1]

# vertex set has the divisor attribute
G.vs["divisor"] = divisor
deg = degree(divisor)

# all edges and vertices start out unburned
G.vs["burned"] = False
G.es["burned"] = False

dhars_burning(G)

# G.vs[3]["burned"] = True
# incidents = G.incident(3, mode="ALL")
# for edge_id in incidents:
#     G.es[edge_id]["burned"] = True

# displaying the end state of G
# fig, ax = plt.subplots(figsize=(5,5))
# ig.plot(
#     G,
#     target=ax,
#     vertex_color=["firebrick" if burned else "steelblue" for burned in G.vs["burned"]],
#     vertex_label=G.vs["divisor"],
#     edge_color=["firebrick" if burned else "steelblue" for burned in G.es["burned"]]
# )
# plt.show()