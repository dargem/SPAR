# horrendous mistake

def sum(a: list[int]) -> int:
    ans = 0
    for x in a:
        ans += a[x]
    return ans

n = int(input())

numbers = list(map(int, input().split()))

n_mod = int(input())
modifications = [[int(num) for num in input().split()] for _ in range(n_mod)]

class Node:
    def __init__(self, outgoing_index):
        self.outgoing = outgoing_index
        self.ingoing = []

nodeMap = {}

for i, value in enumerate(numbers):
    nodeMap[i] = Node(value)

for i, value in enumerate(numbers):
    nodeMap[nodeMap[i].outgoing].ingoing.append(i)

total = sum(numbers)

for idx, value in modifications:
    changed = nodeMap[idx]
    
    total -= len(changed.ingoing) * changed.outgoing
    total += len(changed.ingoing) * value

    oldOutgoing = changed.outgoing
    changed.outgoing = value
    nodeMap[oldOutgoing].ingoing.remove(idx)
    total -= nodeMap[oldOutgoing].outgoing

    nodeMap[changed.outgoing].ingoing.append(idx)

    total += nodeMap[changed.outgoing].outgoing

    print(total)
