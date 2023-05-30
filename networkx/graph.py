import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

# nodes
a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'

# place nodes and edges in the classic house shape

g.add_nodes_from([a,b,c,d,e])

pos = {a:(0,0),
       b:(-1,-1),
       c:(1,-1),
       d:(-1,-2),
       e:(1,-2)}

g.add_edges_from([(a,b), (a,c),
                  (b,c), (b,d), (b,e),
                  (c,d), (c,e),
                  (d,e)])

# initial chip config
starting_labels = {a:3, b:2, c:3, d:1, e:0}

# draw graph
nx.draw(g, with_labels=False, node_color="blue", font_color="white", pos=pos)
nx.draw_networkx_labels(g, labels=starting_labels, pos=pos, font_color="white")
plt.show()