n = int(input())
inp = input()
inp = inp.split(" ")

times = [int(time) for time in inp]

point1 = 0
point2 = 2

remove_index = 0
lowest_time = 9999999999999999

while (point2 < len(times)):
    difference = times[point2] - times[point1]

    # print(difference)
    if (difference < lowest_time):
        lowest_time = difference
        remove_index = point1 + 1

    point1 += 1
    point2 += 1

# the remove index is best removal

times.remove(times[remove_index])

shortest_distance = 0
point1 = 0
point2 = 1

while (point2 < len(times)):
    distance = times[point2] - times[point1]
    
    shortest_distance = max(distance, shortest_distance)

    point1 += 1
    point2 += 1

print(shortest_distance)