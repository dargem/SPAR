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

n_nodes, n_edges = map(int, input().split(" "))
heights = list(map(int, input().split(" ")))

class Node:
    def __init__(self, index, data):
        self.index = index
        self.data = data
        self.neighbours = []

class DisjointSetUnion:
    
    def __init__(self, indices: int):
        self.parent = list(range(indices))

    def find_set(self, v):
        if v == self.parent[v]:
            return v 
        # if its not its own parent, need parent of representative
        # and reassign itself to flatten the graph
        self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def union_sets(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)

        if a != b:
            self.parent[b] = a
    

nodes = {index: Node(index, data) for (index, data) in enumerate(heights)}

for i in range(n_edges):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbours.append(nodes[b])
    nodes[b].neighbours.append(nodes[a])

items = []
for (key, node) in nodes.items():
    items.append((key, node))

items.sort(key=lambda x: x[1].data) 

sorted_indices = [item[0] for item in items]

bot_start = 0

distances = []

while bot_start < len(sorted_indices):
    # For each arbitary bottom we need to find the minimum max'
    minHeight = nodes[sorted_indices[bot_start]].data
    maxHeight = nodes[sorted_indices[bot_start]].data

    up_pointer = bot_start + 1

    dsu = DisjointSetUnion(len(nodes))
    while (up_pointer < len(sorted_indices) and dsu.find_set(0) != dsu.find_set(1)):
        # We move upwards adding nodes to our graph
        # adding until we have connected start and end node

        node = nodes[sorted_indices[up_pointer]]
        maxHeight = node.data

        for neighbour in node.neighbours:
            if (neighbour.data >= minHeight and neighbour.data <= maxHeight):
                dsu.union_sets(node.index, neighbour.index)

        up_pointer += 1

    if (dsu.find_set(0) == dsu.find_set(1)):
        distances.append(maxHeight - minHeight)
    elif (up_pointer == len(sorted_indices)):
        break

    bot_start += 1

print(min(distances))