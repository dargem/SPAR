sink = input().split()
filt = [int(n) for n in sink]

city, guards, repositions = filt
sink = input().split()
positions = [int(n) for n in sink]

city_has_guard: dict[int, bool] = {}
for i in range(city):
    city_has_guard[i] = False


excess = 0
last_guard_pos_cache = city - 1

for pos in positions:
    if not city_has_guard[pos]:
        city_has_guard[pos] = True
    else:
        excess += 1

for i in range(city):
    if city_has_guard[i]:
        continue

    if not city_has_guard[i]:
        if repositions > 0 and excess > 0:
            repositions -= 1
            excess -= 1
            continue

        if repositions > 0 and excess == 0:
            # Find last guard to move to pos
            while not city_has_guard[last_guard_pos_cache] and last_guard_pos_cache > 0:
                last_guard_pos_cache -= 1

            # Find the last guard we can move to here
            if last_guard_pos_cache < i:
                print(i + 1)
                exit()

            city_has_guard[last_guard_pos_cache] = False
            last_guard_pos_cache -= 1
            repositions -= 1

            continue

        if repositions == 0:
            print(i + 1)
            exit()

print(city)





