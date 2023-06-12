import random
import igraph as ig
import os
from misc import *

# returns the degree of the divisor (ie sum of chips distrtibuted)
def degree(divisor):
    return sum(divisor)

# an effective divisor has all chips >= 0 (ie all are not in debt)
def is_effective(divisor):
    for div in divisor:
        if div < 0: 
            return False 
    
    return True

# checks to see if the divisor is effective excluding one specified vertex
def is_effective_away(G, away_from):
    for v in G.vs:
        if v.index != away_from:
            if G.vs[v.index]["divisor"] < 0: 
                return False
        
    return True

# checks if all vertices in the vertex set are burned
def is_burned(burned):
    for burn in burned:
        if burn == False: 
            return False
    
    return True 

def genus(G):
    return G.ecount() - G.vcount() + 1

def difference(list1, list2):
    diff = []
    zipped = zip(list1, list2)
    
    for item1, item2 in zipped:
        diff.append(item1 - item2)
    
    return diff

def save_pic(G, graphIndex, step, caption, outputFolderCWD):

    out = ig.plot(
        G,
        target=f"{outputFolderCWD}/graph{graphIndex}/fig{step}.png",
        vertex_color=["firebrick" if burned else "steelblue" for burned in G.vs["burned"]],
        vertex_label=G.vs["divisor"],
        edge_color=["firebrick" if burned else "steelblue" for burned in G.es["burned"]]
    )
    
    print("fig {}:".format(step))
    print("divisor: {}".format(G.vs["divisor"]))
    if caption != "":
        print(caption)
    print()
    
# performs dhar's burning algoriothm on G
def dhars_burning(G, graphIndex, outputFolderCWD):

    os.mkdir(f"graph{graphIndex}")
    step = 0
    
    # if D is already effective, done
    if is_effective(G.vs["divisor"]): 
        return G.vs["divisor"]
    
    # find subset of D that is not effective
    in_debt = [v for v in G.vs if G.vs[v.index]["divisor"] < 0]
    
    # choose one of the chips in debt at random
    q = random.choice(in_debt)
    
    save_pic(G, graphIndex, step, "initial graph", outputFolderCWD)
    step += 1
    
    # fire from q while G is not effective away from q
    while not is_effective_away(G, q.index):
        # distibute deg(q) chips to each of q's neighbors
        G.vs[q.index]["divisor"] -= G.degree(q)
        for v in G.neighbors(q): 
            G.vs[v]["divisor"] += 1
           
    # continue the burning and firing process until D is effective or the entire graph is burned
    while not is_effective(G.vs["divisor"]) and not is_burned(G.vs["burned"]):
        G.vs["burned"] = False # reset all vertices
        G.es["burned"] = False # reset all edges
        
        save_pic(G, graphIndex, step, "reset", outputFolderCWD)
        step += 1
        
        G.vs[q.index]["burned"] = True
        
        # set all incident edges of q on fire
        incidents = G.incident(q)
        for edge in incidents: 
            G.es[edge]["burned"] = True 
        
        # add all burned nodes to one list
        burned_nodes = []
        burned_nodes.append(q)
        
        # keep track of unburned neighbors of the burned nodes
        unburned_nodes = []
        
        save_pic(G, graphIndex, step, "send fire from q", outputFolderCWD)
        step += 1
        
        # controls how far the fire spreads before firing
        spread = True
        
        # loop
        while spread:
            # add all unburned neighbors of burned to another
            for node in burned_nodes:
                curr_neighbors = node.neighbors()
                
                for neighbor in curr_neighbors:
                    if not G.vs[neighbor.index]["burned"]:
                        if neighbor not in unburned_nodes:
                            unburned_nodes.append(neighbor)
             
            # assume we cannot continue spreading      
            spread = False
    
            # loop through each unburned neighbor to see if the fire can spread
            for node in unburned_nodes:
                curr_incidents = G.incident(node)
                
                # number of incident edges burned
                count = 0
                for edge in curr_incidents:
                    if G.es[edge]["burned"]: 
                        count += 1
                
                # if D(v) < burned incident edges
                if G.vs[node.index]["divisor"] < count:
                    # burn the current node
                    G.vs[node.index]["burned"] = True
                    
                    if node not in burned_nodes:
                        burned_nodes.append(node)
                    
                    unburned_nodes.remove(node)

                    for edge in curr_incidents:
                        G.es[edge]["burned"] = True
                    
                    save_pic(G, graphIndex, step, "{} catches fire".format(node.index), outputFolderCWD)
                    step += 1
                    
                    # since we were able to burn another node, we may be able to spread farther
                    spread = True
        
        # fire from unburned nodes along burned edges only
        for node in unburned_nodes:
            curr_neighbors = node.neighbors()
            
            # check each neighbor of the current node
            for target in curr_neighbors:
                if G.vs[target.index]["burned"]:
                    edge = G.get_eid(node, target)
                    
                    # only fire from an unburned node along a burned edge
                    if G.es[edge]["burned"]:
                        G.vs[node.index]["divisor"] -= 1
                        G.vs[target.index]["divisor"] += 1
                        
                        save_pic(G, graphIndex, step, "firing from {} to {}".format(node.index, target.index), outputFolderCWD)
                        step += 1
    
    save_pic(G, graphIndex, step, "", outputFolderCWD)
    step += 1
    
    # reset
    G.vs["burned"] = False
    G.es["burned"] = False

    save_pic(G, graphIndex, step, "final graph", outputFolderCWD)
    step += 1
    
    # # if dhar's ends due to reaching an effective divisor
    # if is_effective(G.vs["divisor"]):
    #     return True 
    
    # # otherwise, the divisor reached was not effective
    # return False