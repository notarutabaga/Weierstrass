import igraph as ig
from functions import *

def spread_chips(n, x):
    results = []
    spread_chips_recursive(n, x, [0] * x, results)
    return results

def spread_chips_recursive(n, x, current, results):
    if n == 0:
        results.append(list(current))
        return
    if x == 0:
        return
    spread_chips_recursive(n, x - 1, current, results)
    current[x - 1] = 1
    spread_chips_recursive(n - 1, x - 1, current, results)
    current[x - 1] = 0

# Example usage:
n = 2
x = 5
all_spreads = spread_chips(n, x)
for spread in all_spreads:
    print(spread)

def find_rank(G):
    rank = -1
    iteration = 0
    
    loop = True
    
    #while loop:
        
    