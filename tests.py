import igraph as ig
import matplotlib.pyplot as plt
from dhars import *
import os

ig.config["plotting.backend"] = "matplotlib"
ig.config["plotting.layout"] = "auto"
ig.config.save()

graphs = [
    {
        "n": 5,
        "edges": [
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4)
        ],
        # divisor to test with (see example 2.5)
        "divisor": [ 2, 2, 1, -1, -1 ]
    }
]


initialCWD = os.getcwd();
outputsCWD = f"{initialCWD}/outputs";

def recursiveDeletion(folderPath):

    os.chdir(folderPath);

    for element in os.listdir():

        ## This element is a folder, recurse down
        if "." not in element:
            nextFolderPath = f"{folderPath}/{element}"
            recursiveDeletion(nextFolderPath)
            os.rmdir(nextFolderPath)
        else:
            if element != ".git":
                os.remove(element)


# ## If we have previous computed outputs
# if "outputs" in os.listdir():

#     ## Recursively empty out the folders
#     recursiveDeletion(outputsCWD)
#     ## Go back a level to parent folder of the outputs folder
#     os.chdir(initialCWD)
#     ## Delete the now empty outputs folder
#     os.rmdir("outputs")


if len(graphs) > 0:
    ## Make a new outputs folder
    os.mkdir("outputs")
    ## Move into the outputs folder
    os.chdir(outputsCWD)

else:
    print("There are no graphs to process!")
    exit()

divs = [[0,0,0,0,0],
        [1,0,0,0,0],
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1]]

for graphIndex, graph in enumerate(graphs):

    # new hosue-x graph G made using the edges list
    G = ig.Graph(graph["n"], graph["edges"])

    # vertex set has the divisor attribute
    G.vs["divisor"] = graph["divisor"]
    deg = degree(graph["divisor"])

    # all edges and vertices start out unburned
    G.vs["burned"] = False
    G.es["burned"] = False

    for divIndex, div in enumerate(divs):
      G_copy = G.copy()
      G_copy.vs["divisor"] = difference(G_copy.vs["divisor"], div)
      
      dhars_burning(G_copy, str(graphIndex) + "_" + str(div), outputsCWD)
      # if not result:
      #   break