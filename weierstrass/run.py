import test_cases as test
from weierstrass import *
import igraph as ig
import matplotlib.pyplot as plt

ig.config["plotting.backend"] = "matplotlib"
ig.config["plotting.layout"] = "auto"
ig.config.save()

G = test.complete(7)

fig, ax = plt.subplots(figsize=(5,5))
ig.plot(
    G,
    target=ax,
    layout="auto", # print nodes in a circular layout
    vertex_color="steelblue"
)

plt.show()

g = genus(G)

for v in G.vs:
    # only weierstrass vertices have a gap sequence and weight
    if is_weierstrass(G, v.index):
        # reset the divisor to be [0]
        G.vs["divisor"] = 0
        
        ranks = []
        
        # want to test divisors n(v) for 0 <= n <= 2g-2 (and then a couple more)
        for n in range((2 * g) + 2):
            # D = [n, 0, 0, ..., 0]
            G.vs[v.index]["divisor"] = n 
            
            r = rank(G, v.index, g)
            ranks.append(r)
        
        gap_seq = compute_gap_seq(ranks)
        w = weight(gap_seq, g)
        
        print("vertex " + str(v.index))
        print("n: ", end="")
        for n in range(len(ranks)):
            print(n, end="\t")
        
        print()
        print("r: ", end="")
        for r in ranks:
            print(r, end="\t")
        
        print()
        print("gap seq = " + str(gap_seq))
        print("weight = " + str(w))
            
        print()
        
        