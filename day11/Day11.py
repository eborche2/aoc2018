serial = 7347
matrix = [[0 for i in range(300)] for i in range(300)]
for y, row in enumerate(matrix):
    for x, item in enumerate(row):
        cy = y + 1
        cx = x + 1
        rackId = cx + 10
        pLevel = rackId * cy
        pLevel += serial #Puzzle input
        pLevel = pLevel * rackId
        if len(str(pLevel)) >= 3:
            matrix[y][x] = int(str(pLevel)[-3:-2]) - 5
        else:
            matrix[y][x] = -5

grid = 3
while True:
    current = [None, None, None]
    for y, row in enumerate(matrix):
        for x, item in enumerate(row):
            if x > 300 -grid:
                continue
            if y > 300 -grid:
                continue
            check = 0
            for addx in range(grid):
                for addy in range(grid):
                    check += matrix[y+addy][x+addx]
            if current[0]:
                if current[0] < check:
                    current[0] = check
                    current[1] = x + 1
                    current[2] = y + 1
            else:
                current[0] = check
                current[1] = x + 1
                current[2] = y + 1
    if current[0] < 0:
        break
    print(grid, current)
    del current
    grid += 1

