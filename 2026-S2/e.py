import math
from functools import cache

cases = int(input())

def area(time, cost, n):
    P = time - cost * n
    area = 1 / math.tan((2*math.pi)/(2 * n))
    area *= P / (2*n)
    area *= P / (2*n)
    area *= 1/2
    area *= (2 * n)
    return area

answers = []
for num in range(cases):
    data = input().split(" ")
    cost = int(data[0])
    time = int(data[1])
    # print(time)
    # print(cost)
    n = 3
    scores = []
    scores.append(-1)
    scores.append(0)
    
    min = 3
    max = time // cost

    if (max < min):
        answers.append(0)
        continue

    
    while (max != min):
        #print(min)
        # 1print(max)
        mid = (min + max) // 2
        if area(time, cost, mid + 1) < area(time, cost, mid):
            max = mid
        elif area(time, cost, mid + 1) > area(time, cost, mid):
            min = mid + 1
    
    answers.append(area(time, cost, min))

for answer in answers:
    print(f"{answer:f}")
    
    

