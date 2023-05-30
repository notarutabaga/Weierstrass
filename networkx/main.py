import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph() # undirected
# DiG = nx.DiGraph() # directed
# MulG = nx.MultiGraph() # multiple edges btwn (undi)
# MulDiG = nx.MultiDiGraph() # multiple edges btwn (di)

# G.add_edge(1, 2) # add edge from 1 to 2 (if either node doens't exist, it is created)
# G.add_edge(2, 3, weight=0.9) # this edge has a def weight (default is 0?)
# G.add_edge("A", "B") # can pass anything that is hashable (ie an object)
# G.add_edge("B", "B")
# G.add_node("C")
# G.add_node(print)

edge_list = [(1, 2), (2, 3), (3, 4), (3,5), (4, 6), (6, 7)]
G.add_edges_from(edge_list)

# draws onto the figure that comes before the draw call
plt.figure()
nx.draw_spring(G, with_labels=True) # labels are the names of the nodes

# draw_circular
# draw_shell
# draw_spectral
# draw_random
# draw_planar (exception is thrown if graph cannot be drawn this way)

# dict turns the degree (set ?) into a dictionary (a hash map ?)
# [2] accesses the key 2 (so the node with the label (?) 2 not at index 2)
print(dict(G.degree)[2]) 

# prints the node label followed by its degree
print(dict(G.degree))

print(nx.shortest_path(G, 1, 5)) # prints the shortest path from 1 to 5
print(nx.shortest_path_length(G, 1, 5)) # length of that shortest path

# centrality functions available 

K_5 = nx.complete_graph(5) # K_5 graph

# same structure made by the constructor, but node labels are changed since
# by default they are numbered like array indexes
K_5 = nx.relabel_nodes(K_5, {0: "A", 
                             1: "B",
                             2: "C",
                             3: "D",
                             4: "E"})

# another K_5 and 
K_5_2 = nx.complete_graph(5)
G_connector = nx.from_edgelist([(4, "X"), ("X", "A")])

# compose all graphs into one given a list of graphs
# (draw function can only draw one graph per figure)
# (note: a connector doesn't have to be made)
G_composed = nx.compose_all([K_5, K_5_2, G_connector])

plt.figure()
nx.draw_spring(G_composed, with_labels=True)

# SHOW SHOULD BE USED ONLY ONCE it only shows the first and crashes after
# shows all figures made in separate windows
plt.show()


