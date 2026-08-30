sink = input()

class Node:
    def __init__(self, parent = None):
        self.edge = False
        self.count = 0
        self.parent = parent

parents = list(map(int, input().split()))
targets = list(map(int, input().split()))

nodes = []

# nodes start indexing at 1 so going to append an empty base
nodes.append(Node())

# Then this is root at index 1
nodes.append(Node())

for parent in parents:
    nodes.append(Node(parent))

for target in targets:
    me = nodes[target]

    if me.count > 0:
        me.count -= 1

        while me.parent != None:
            me = me.parent
            me.count -= 1
        
        continue

    # We need to see if there's an edge to "reuse"
    node = me
    parent_is_edge = False
    while True:
        if node.edge == True:
            parent_is_edge = True
            break

        if node.parent == None:
            # We've traversed to root
            break

        node = node.parent
    
    if parent_is_edge:
        node = me

        while node.parent != None:
            node = node.parent
            node.count += 1
            if node.edge:
                node.edge = False
                break
    
    if 
        



