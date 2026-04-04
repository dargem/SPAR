import math

"""
A lot simpler than it seems. 
By planting flags you are essentially creating a polygon.
Need at least 3 flags or you have a line with no space
The way to optimize area:perimeter are ratio for polygons is having all sides equal length
I.E. equilateral triangle, square this is intuitive
The most efficient area : surface area shape is a circle (kindof like an infinite sided polygon)
So increasing number of vertices (flags) leads to a better area to perimeter ratio
And this has some kindof falloff in efficiency when adding vertices, 
a polygon with -> infinite vertices if you add one more won't get much of a benefit.
While a triangle if you added 10 sides would obviously be able to cover a lot more space for same perimeter.
So we need an algo to find the area of an n sided polygon for a given perimeter
Where we know that polygon has equal length sides, I assume there's some formula for this I don't know
A polygon can be decomposed into triangles though, where the triangles are each vertice of polygon pointing to the center
This creates n equilateral triangles, where the angle is 2pi/n radians and the opposite side is perimeter/n length
I also don't know the formula for equilateral triangles so split this into 2 right angle triangles
Can then simply find area using base * height, then multiple by number of triangles (2n) to get polygon area

We don't know perimeter though but we know cost of a vertex is say C time. Where 1 distance = 1 time
So perimeter = time_budget - vertex_time_cost * number_of_vertices

Then we just start at n = 3 and find area, keep on increasing n_vertices until area stops increasing
That is our answer, can use a binary search to quickly find this point but this shouldn't be needed. 
This is as intuitively as number of vertices increases, the area : perimeter benefit keeps on decreasing.
As n -> infinity the benefit of adding a vertex is going to -> 0, while for small n, n + 1 has a large improvement
With example for this q the case for "most vertices used" is cost of 1 for a vertex, then 10^8 time
There is still only 690 which is basically nothing
"""

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
    print(min)
    answers.append(area(time, cost, min))

for answer in answers:
    print(f"{answer:f}")
    
    

