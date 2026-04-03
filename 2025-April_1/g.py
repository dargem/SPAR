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
        self.size = [1 for _ in range(indices)]

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
            if (self.size[a] < self.size[b]):
                a, b = b, a # swap so a is always same or larger in size
            self.parent[b] = a
            self.size[a] += self.size[b]
    

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
    # For each arbitrary bottom we need to find the minimum max'
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