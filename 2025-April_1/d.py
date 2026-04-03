"""

"""

class Node:

    def __init__(self, string):
        self.element = string
        self.count = 0
        self.outgoing = []
        self.ingoing = []


n = int(input())

nodes = {}

for i in range(n):
    first, comparator, second = input().split(" ")

    if first not in nodes:
        nodes[first] = Node(first)
    if second not in nodes:
        nodes[second] = Node(second)
    
    if (comparator == '<'):
        nodes[first].outgoing.append(nodes[second])
        nodes[second].ingoing.append(nodes[first])
    elif (comparator == '>'):
        nodes[second].outgoing.append(nodes[first])
        nodes[first].ingoing.append(nodes[second])

    
letters = input()

for letter in letters:
    if letter not in nodes:
        nodes[letter] = Node(letter)
    
    nodes[letter].count += 1

nodes = [node for node in nodes.values()]
sorted_nodes = []

def some_removable(node_list):
    for node in node_list:
        if len(node.ingoing) == 0 or node.count == 0:
            return True
    return False


while (some_removable(nodes)):
    remove_list = []
    for node in nodes:
        if (len(node.ingoing)) == 0 or node.count == 0:
            sorted_nodes.append(node)
            remove_list.append(node)

            for other_node in node.outgoing:
                other_node.ingoing.remove(node)
    
    for remove in remove_list:
        nodes.remove(remove)

if (len(nodes) == 0):
    # has removed all
    for node in sorted_nodes:
        print(node.element * node.count, end="")
else:
    print("IMPOSSIBLE")
