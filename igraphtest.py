import igraph as ig
import matplotlib.pyplot as plt

ig.config["plotting.backend"] = "matplotlib"
ig.config["plotting.layout"] = "auto"
ig.config.save()

n = 5
edges = ([(0, 1), (0, 2),
          (1, 2), (1, 3), (1, 4),
          (2, 3), (2, 4),
          (3, 4)])

g = ig.Graph(n, edges)

divisor = [10, 20, 30, 40, 50]
g.vs["divisor"] = divisor
g.es["att"] = "goodbye"
g.es[g.get_eid(0,2)]["att"] = "hello"

print(g.es.select(_within=[0,2]))

fig, ax = plt.subplots(figsize=(5,5))

ig.plot(
    g,
    target=ax,
    vertex_color="red",
    vertex_label=g.vs["divisor"],
    label_color="white",
    edge_label=g.es["att"]
)

plt.show()