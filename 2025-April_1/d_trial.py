"""
n = int(input())

lst_pairs = []

for i in range(n):
    temp = i.split(' ')
    if i[1] == '>':
        idx1 = 2
        idx2 = 0
    if i[1] == '<':
        idx1 = 0
        idx2 = 2
    
    pair = (i[idx1], i[idx2])
    lst_pairs.append(pair)

collection = input()
max = ''
letter_order = ''
name = ''

letters = collection.split()
seen = []
for i in letters:
    if i not in seen:
        seen.append(i)

while len(letter_order) < len(collection):
    for i in lst_pairs:
        if i.reverse() in lst_pairs:
            name = "IMPOSSIBLE"
        if max in i and max != i[1]:
            max = i[1]
            letter_order += max
            seen.remove(max)

    for letter in letter_order:
        for occurence in collection:
            # name += 
            pass



    

def build_tuple_list(inp):
    lst = []
    for i in inp:
        if i[1] == '>':
            idx1 = 2
            idx2 = 0
        if i[1] == '<':
            idx1 = 0
            idx2 = 2
        
        tup = (i[idx1], i[idx2])
        lst.append(tup)

    return lst

"""