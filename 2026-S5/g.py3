s1, s2 = input().split()

districts = int(s1)
parties = int(s2)

# go through and see n. bribed to win each district
# sort by n. bribed and choose smallest n

needed_to_win = []

for _ in range(districts):
    votes = [int(val) for val in input().split()]
    our_votes = votes[0]
    votes.pop(0)

    # decrement from most popular until we win
    votes.sort(reverse=True)
    needed_bribes = 0

    while True:
        # print(votes)
        if (our_votes > votes[0]): break
        votes[0] -= 1
        our_votes += 1
        needed_bribes += 1

        votes.sort(reverse=True)
    
    needed_to_win.append(needed_bribes)

needed_districts = (districts // 2) + 1

needed_to_win.sort()

sum = 0
for i in range(needed_districts):
    sum += needed_to_win[i]

# print(needed_to_win)
print(sum)

