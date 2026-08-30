num_gpu = int(input())

gpus = []

# model at gen 0
buckets = {}

for _ in range(num_gpu):
    data = input().split()

    price = int(data[1])
    generation = int(data[0][0:-3])
    model = int(data[0][-3: -1] + data[0][-1])

    model += generation*10
    
    if model not in buckets:
        buckets[model] = []
    buckets[model].append(price)

tot_val = 0
for bucket in buckets.values():
    highest = 0
    for item in bucket:
        highest = max(item, highest)
    tot_val += highest

print(tot_val)

