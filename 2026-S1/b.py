days = int(input())
alc_size, other_size = map(int, input().split())
alc_decay, other_decay = map(int, input().split())

for i in range(days):
    alc_size = max(alc_size - alc_decay, 0)
    other_size = max(other_size - other_decay, 0)


if (alc_size == 0):
    print(0)
elif (other_size == 0):
    print(100)
else:
    print(alc_size * 100 / (alc_size + other_size))
