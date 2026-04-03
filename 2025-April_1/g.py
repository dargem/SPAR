"""
Can say each hill is a node, paths are edges between nodes
The cost of a route from hill 1 to hill 2 is
    tallest hill on path - shortest hill on path

There are two parameters to try and optimize for when you have a path from 1 -> 2
The first is trying to remove the shortest hill from the path
The second is removing the tallest hill from the path
This will lead to a reduced difference in height, 
at least if it doesn't disconnect the paths

Trying to optimize for both parameters at once would be too complex
We could start with a given shortest hill,
then try to minimize the tallest hill required to reach hill 2

This could be intuitively through creating an empty graph.
We start at the given shortest hill, keeping track minheight = shortest hill height
We add the shortest hill to the empty graph.
We have no maxheight yet so maxheight = shortest hill height also.
We now want to check all neighbours of this shortest hill.
We grab the shortest neighbours of our graph that are > minheight.
We continually add the shortest neighbours our graph can add until we have added both hill 1 and hill 2.

and check its neighbours.
If a neighbour is hill 1 or hill 

This could be done simply through
    1: Order hills by height
    2: Create a second graph of nodes (empty currently)
    3: Start with a given "shortest hill", say the global shortest for this example
    4: Add the given shortest hill into this new graph
    5: Go one up the list of heights to get the next node
    6: Add thi

"""

nodes, edges = map(int, input().split(" "))
heights = list(map(int, input().split(" ")))

class Node:
    __init__(self):
        
