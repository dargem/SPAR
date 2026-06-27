
pairs = int(input())

virus = []
antivirus = []



for _ in range(pairs):
    string = input()

    # score the string, want to go through each factor
    # see if repeating that gets the string

    length = len(string)

    value = 0 # holder
    for take in range(1, length + 1):
        if (length % take != 0):
            continue

        repeats = length // (take)
        substring = string[:take]
        if substring * repeats == string:
            value = take
            break
    
    # will always find a valid substring
    virus.append(value)

for _ in range(pairs):
    string = input()

    # score the string, want to go through each factor
    # see if repeating that gets the string

    length = len(string)

    value = 0 # holder
    for take in range(1, length + 1):
        if (length % take != 0):
            continue

        repeats = length // (take)
        substring = string[:take]
        # print(substring * repeats)
        if substring * repeats == string:
            value = take
            break
    
    # will always find a valid substring
    antivirus.append(value)

virus.sort()
antivirus.sort()

damage = 0
for i in range(pairs):
    damage += (virus[i] - antivirus[i]) * (virus[i] - antivirus[i])

print(damage)