str = input()

"""
A lot easier than it sounds just count the number of unpaired letters
Here I use a set lazily but it would be faster to use something like an array
Then index into it by treating the char as an uint switching it between true/false
"""

obs = set()

for char in str:
    if char not in obs:
        obs.add(char)
    else:
        obs.remove(char)

if (len(str) % 2 == 0):
    # even length needs exact match
    if (len(obs) == 0):
        print("yes")
    else:
        print("no")
else:
    # odd match can have 1 unpaired letter
    if (len(obs) == 1):
        print("yes")
    else:
        print("no")
