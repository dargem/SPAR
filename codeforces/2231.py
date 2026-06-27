n = int(input())

for i in range(n):
    input()
    nums = [int(i) for i in input().split()]

    min = 0
    max = 0
    k = 0

    for num in nums:
        if num >= max:
            

            max = num
            continue

