class Pair:
    def __init__(self, index, open, close):
        self.index = index
        self.open = open
        self.close = close

size = int(input())
arr = list(map(int, input().split()))

size = int(input())

pairs = []

for i in range(size):
    inp = input().split()
    pairs.append(Pair(i, inp[0], inp[1]))

pairs.sort(key=lambda x: x.open)

input_set = {}


