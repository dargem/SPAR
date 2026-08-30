data = input().split()
filt = [int(d) for d in data]

row, column = filt

# load
acid_grid: list[str] = []

for i in range(row):
    acid_grid.append(input())

alkanity_grid: list[list] = []
for i in range(row):
    data = input().split()
    alkanity_grid.append([int(d) for d in data])

output_grid: list[str] = []

for r in range(row):
    output_grid.append([])
    for c in range(column):
        acidity = 0

        # top
        if r - 1 >= 0:
            acidity += (acid_grid[r - 1][c] == "#")
            if c - 1 >= 0:            
                acidity += (acid_grid[r - 1][c - 1] == "#")
            if c + 1 < column:
                acidity += (acid_grid[r - 1][c + 1] == "#")

        # bottom
        if r + 1 < row:
            acidity += (acid_grid[r + 1][c] == "#")
            if c - 1 >= 0:            
                acidity += (acid_grid[r + 1][c - 1] == "#")
            if c + 1 < column:
                acidity += (acid_grid[r + 1][c + 1] == "#")

        # left / right
        if c + 1 < column:
            acidity += (acid_grid[r][c + 1] == "#")

        if c - 1 >= 0:
            acidity += (acid_grid[r][c - 1] == "#")

        alk = alkanity_grid[r][c]

        if alk == acidity:
            output_grid[r] += "M"
        else:
            output_grid[r] += "."

for out in output_grid:
    print("".join(out))