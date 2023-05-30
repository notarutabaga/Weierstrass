import random
import igraph as ig

# returns the degree of the divisor (ie sum of chips distrtibuted)
def degree(divisor):
    return sum(divisor)

# an effective divisor has all chips >= 0 (ie all are not in debt)
def is_effective(divisor):
    for div in divisor:
        if div < 0: return False 
    
    return True

# checks to see if the divisor is effective excluding one specified vertex
def is_effective_away(G, away_from):
    for v in G.vs:
        if v.index != away_from:
            if G.vs[v.index]["divisor"] < 0: return False
        
    return True

# checks if all vertices in the vertex set are burned
def is_burned(burned):
    for burn in burned:
        if burn == False: return False
    
    return True 

def save_pic(G, step):
    out = ig.plot(
        G,
        target=str(step)+".png",
        vertex_color=["firebrick" if burned else "steelblue" for burned in G.vs["burned"]],
        vertex_label=G.vs["divisor"],
        edge_color=["firebrick" if burned else "steelblue" for burned in G.es["burned"]]
    )
    
    # out.save(step + '_test.png', format="gml")

# performs dhar's burning algoriothm on G
def dhars_burning(G):
    step = 0
    
    # if D is already effective, done
    if is_effective(G.vs["divisor"]): return G.vs["divisor"]
    
    # find subset of D that is not effective
    in_debt = [v for v in G.vs if G.vs[v.index]["divisor"] < 0]
    
    # choose one of the chips in debt at random
    q = random.choice(in_debt)
    
    step += 1
    save_pic(G, step)
    
    # fire from q while G is not effective away from q
    while is_effective_away(G, q.index) != True:
        # distibute deg(q) chips to each of q's neighbors
        G.vs[q.index]["divisor"] -= G.degree(q)
        for v in G.neighbors(q): 
            G.vs[v]["divisor"] += 1
            
        step += 1
        save_pic(G, step)
           
    # continue the burning and firing process until D is effective or the entire graph is burned
    while is_effective(G.vs["divisor"]) == False and is_burned(G.vs["burned"]) == False:
        G.vs["burned"] = False # reset all vertices
        G.es["burned"] = False # reset all edges
        
        step += 1
        save_pic(G, step)
        
        G.vs[q.index]["burned"] = True
        
        # set all incident edges of q on fire
        incidents = G.incident(q)
        for edge in incidents: 
            G.es[edge]["burned"] = True 
        
        step += 1
        save_pic(G, step)
        
        # add all burned nodes to one list
        burned_nodes = []
        burned_nodes.append(q)
        
        # keep track of unburned neighbors of the burned nodes
        unburned_nodes = []
        
        # controls how far the fire spreads before firing
        spread = True
        
        # loop
        while spread:
            # add all unburned neighbors of burned to another
            for node in burned_nodes:
                curr_neighbors = node.neighbors()
                
                for neighbor in curr_neighbors:
                    if G.vs[neighbor.index]["burned"] == False:
                        unburned_nodes.append(neighbor)
             
            # assume we cannot continue spreading      
            spread = False
    
            for node in unburned_nodes:
                curr_incidents = G.incident(node)
                
                count = 0
                for edge in curr_incidents:
                    if G.es[edge]["burned"] == True: count += 1
                
                # if D(v) < burned incident edges
                if G.vs[node.index]["divisor"] < count:
                    # add v to burned
                    G.vs[node.index]["burned"] = True
                    burned_nodes.append(node)
                    
                    # remove v from unburned
                    unburned_nodes.remove(node)
                    
                    # burn v's edges
                    for edge in curr_incidents:
                        G.es[edge]["burned"] = True
                        
                    step += 1
                    save_pic(G, step)
                    
                    # since we were able to burn another node, we may be able to spread farther
                    spread = True
        
        # fire from unburned nodes along burned edges only
        for node in unburned_nodes:
            curr_neighbors = node.neighbors()
            print("current neighbors: {curr_neighbors}")
            
            for target in curr_neighbors:
                if G.vs[target.index]["burned"]:
                    edge = G.get_eid(node, target)
                    
                    if G.es[edge]["burned"] == True:
                        print("firing from {node} to {target}")
                        G.vs[node.index]["divisor"] -= 1
                        G.vs[target.index]["divisor"] += 1
                        
                step += 1
                save_pic(G, step)
    
    G.vs["burned"] = False
    G.es["burned"] = True
    
    step += 1
    save_pic(G, step)