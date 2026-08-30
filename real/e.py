sink = input().split()
filt = [int(s) for s in sink]

building_floors, route_length = filt

sink = input().split()
elevator_floors = [int(s) for s in sink]

sink = input().split()
filt = [int(s) for s in sink]
maya, kurt, party = filt

maya_latest = None
time = 0

elevator_floors.insert(0, 0)

for i, floor in enumerate(elevator_floors):
    if floor == maya:
        maya_latest = time

    if floor == kurt:
        if time >= party:
            if maya_latest != None:
                print(maya_latest)
                exit()
        else:
            maya_latest = None

    if i == len(elevator_floors) - 1:
        break

    next_floor = elevator_floors[i + 1]
    if next_floor > floor:
        if maya > floor and maya <= next_floor:
            intercept = maya - floor + time
            maya_latest = intercept

        if kurt > floor and kurt <= next_floor:
            intercept = kurt - floor + time

            if intercept >= party and maya_latest != None and maya_latest < intercept:
                print(maya_latest)
                exit()
            else:
                maya_latest = None

    if next_floor < floor:
        if maya < floor and maya >= next_floor:
            intercept = abs(maya - floor) + time
            maya_latest = intercept

        if kurt > floor and kurt <= next_floor:
            intercept = abs(kurt - floor) + time

            if intercept >= party and maya_latest != None and maya_latest < intercept:
                print(maya_latest)
                exit()
            else:
                maya_latest = None

    time += abs(next_floor - floor)

    



                    