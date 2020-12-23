import re
from copy import deepcopy

f = open("input.txt", "r")
input = f.readlines()
f.close()

grid = [list(l.strip("\n")) for l in input]
width = len(grid[0])
height = len(grid)

def count_occupied_neighbours(row, column):
    occupied_neighbours = 0
    for row_delta in [-1, 0, 1]:
        for column_delta in [-1, 0, 1]:
            if row_delta == 0 and column_delta == 0:
                continue

            neighbour_row = row + row_delta
            neighbour_column = column + column_delta

            # check bounds first
            if 0 <= neighbour_row < height and 0 <= neighbour_column < width: 
                if grid[neighbour_row][neighbour_column] == "#":
                    occupied_neighbours += 1
            
    return occupied_neighbours

next_grid_state = deepcopy(grid)
stable = False

while not stable: 
    stable = True
    next_grid_state = deepcopy(grid)

    for row in range(height):
        for column in range(width):
            if grid[row][column] == ".":
                continue

            occupied_neighbours = count_occupied_neighbours(row, column)

            if grid[row][column] == "#" and occupied_neighbours >= 4:
                next_grid_state[row][column] = "L"
                stable = False
            elif grid[row][column] == "L" and occupied_neighbours == 0:
                next_grid_state[row][column] = "#"
                stable = False
        
    grid = deepcopy(next_grid_state)

occupied_count = 0
for row in range(height):
    for column in range(width):
        if grid[row][column] == "#":
            occupied_count += 1

print(occupied_count)