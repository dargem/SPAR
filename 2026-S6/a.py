forward, back = list(map(int, input().split()))
moves, steps_wanted = list(map(int, input().split()))

for backward_steps in range(moves + 1):
    forward_steps = moves - backward_steps

    steps_made = forward * forward_steps - back * backward_steps
    if steps_made == steps_wanted:
        print("Yes")
        exit()

print("No")