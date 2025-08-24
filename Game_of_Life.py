import random
import time

def random_grid(n):
    grid = [[0] * n for i in range(n)]
    return grid

def living_cells(grid, size, cell):
    created = set()
    while len(created) < cell:
        x = random.randint(0, size)
        y = random.randint(0, size)
        if (x, y) not in created:
            created.add((x, y))
            grid[x][y] = 1

def display(grid):
    for row in grid:
        print(" ".join('#' if live else '.' for live in row))
    print("\n")
    time.sleep(0.5)

def count_neighbors(grid, row, col):
    sizeRow, sizeCol = len(grid), len(grid[0])
    neighbors = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            new_i = (i + row) % sizeRow
            new_j = (j + col) % sizeCol
            if grid[new_i][new_j] == 1:
                neighbors += 1
    return neighbors

def next_generation(grid):
    board = random_grid(len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and neighbors in [2,3]:
                board[i][j] = 1
            elif grid[i][j] == 0 and neighbors == 3:
                board[i][j] = 1
            else:
                board[i][j] = 0
    return board

size = int(input("What size board do you want to create? "))
grid = random_grid(size)
cells = int(input("How many living cells do you want to create? "))
living_cells(grid, size-1, cells)
times = int(input("How many life cycles do you want to see? "))
display(grid)
while times > 0:
    grid = next_generation(grid)
    display(grid)
    times -= 1