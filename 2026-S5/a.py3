sink, sink2 = input().split()
variation = int(sink2)
radiation = [int(val) for val in input().split()]


rad_min = (radiation[0], 0)
rad_max = (radiation[0], 0)

for day, rad in enumerate(radiation):
    min_score = abs(rad - rad_min[0]) - variation * (day - rad_min[1])
    max_score = abs(rad - rad_max[0]) - variation * (day - rad_max[1])

    score = max(min_score, max_score)
    score = max(score, 0)

    print(score, end=" ")

    weighted_min = rad_min[0] + variation * (day - rad_min[1])
    weighted_max = rad_max[0] - variation * (day - rad_max[1])

    rad_min = rad_min if weighted_min < rad else (rad, day)
    rad_max = rad_max if weighted_max > rad else (rad, day)


    