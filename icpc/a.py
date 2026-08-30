input()

inp = input().split()
data = [int(n) for n in inp]

toggle = {}

for num in data:
    if num not in toggle:
        toggle[num] = True
    
    elif toggle[num] == False:
        toggle[num] = True

    elif toggle[num] == True:
        toggle[num] = False

count = 0
for v in toggle.values():
    count += v

print(count)
