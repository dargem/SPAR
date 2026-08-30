sink = input()

times = list(map(int, input().split()))

sum = 0
for i, time in enumerate(times):
    for j in range(i + 1, len(times)):
        sum += abs(time - times[j])

print(sum)