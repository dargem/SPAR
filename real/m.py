from itertools import combinations

n = int(input())

names = [input() for i in range(n)]
output = []

for i in range(len(names)):
    name = names[i]
    propositions = set()

    for i in range(len(name) - 2):
        for j in range(i + 1, len(name) - 1):
            for k in range(j + 1, len(name)):
                propositions.add(name[i] + name[j] + name[k])

    restrictions = set()
    for other_name in names:
        if other_name == name:
            continue

        for i in range(len(other_name) - 2):
            for j in range(i + 1, len(other_name) - 1):
                for k in range(j + 1, len(other_name)):
                    restrictions.add(other_name[i] + other_name[j] + other_name[k])

    for prop in propositions:
        if prop not in restrictions:
            output.append(prop)
            break

for name in output:
    print(name)
        





