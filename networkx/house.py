import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3),
                  (2, 3), (2, 4), (2, 5),
                  (3, 4), (3, 5),
                  (4, 5)])

nx.draw_spring(G, with_labels=True) # spring has house shape but it's tilted
plt.show()

