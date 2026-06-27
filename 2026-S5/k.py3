needs = set()

input()
for knot in input().split():
    needs.add(knot)

for knot in input().split():
    needs.remove(knot)

elements = list(needs)

print(int(elements[0]))