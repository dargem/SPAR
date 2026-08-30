n = int(input())
raw = input().split()
dat = [int(r) for r in raw]

alarm_fails, max_window_size = dat

window_size = 0
window_fails = 0

data = input()

tot_alarms = 0

for i in range(n):
    if window_size < max_window_size:
        window_size += 1
        if data[i] == "F":
            window_fails += 1
    else:
        if data[i - window_size] == "F":
            window_fails -= 1
        
        if data[i] == "F":
            window_fails += 1

    if window_fails == alarm_fails:
        tot_alarms += 1
        window_fails = 0
        window_size = 0

print(tot_alarms)

        


    
