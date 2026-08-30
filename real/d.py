sink = input().split()
filt = [int(n) for n in sink]

num_emp, num_days = filt

suspect_map = {}

# def log(text):
#     with open("log.txt", "a") as f:
#         f.write(str(text) +'\n')

for _ in range(num_emp):
    suspect_map[input()] = True

for _ in range(num_days):
    sink = input().split()
    filt = [int(n) for n in sink]
    employees, taken = filt

    taken_info = {}
    taken_sum = 0
    for _ in range(employees):
        sink = input().split()
        temp_taken = int(sink[1])

        taken_info[sink[0]] = temp_taken
        taken_sum += temp_taken

    # log(taken)
    # log(taken_sum)
    if taken_sum != taken:
        # Thief
        stole = taken - taken_sum
        # log(f"stole is {stole}")
        # print("Theft")
        for name, breaks in taken_info.items():
            # log(f"{name} has {breaks}")
            if breaks != stole:
                suspect_map[name] = False

        for suspect in suspect_map.keys():
            if suspect not in taken_info:
                suspect_map[suspect] = False

    else:
        # No thefts everyone clear
        for name, breaks in taken_info.items():
            # log("No theft")
            suspect_map[name] = False

# print(suspect_map)
for suspect, stat in suspect_map.items():
    if stat == False: continue
    print(suspect)


     


