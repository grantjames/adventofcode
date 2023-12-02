from collections import namedtuple

f = open("input.txt", "r")
input = f.readlines()
f.close()

Point = namedtuple("Point", ["x", "y"])

grid = []
for line in input:
    grid.append(list(map(ord, line[:-1])))

start = None
end = None
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if grid[y][x] == 83:
            grid[y][x] = 97
            start = Point(x, y)
        elif grid[y][x] == 69:
            grid[y][x] = 122
            end = Point(x, y)

# Create a dictionary of points with points they can connect to
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
neighbours = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        neighbours[Point(x, y)] = []

        for dir in dirs:
            dx, dy = x + dir[0], y + dir[1]
            if dy >= 0 and dy < len(grid) and dx >= 0 and dx < len(grid[0]):
                neighbour = grid[dy][dx]
                neighbour_point = Point(dx, dy)
                if neighbour <= grid[y][x] + 1:
                    neighbours[Point(x, y)].append(neighbour_point)

count = 0
path_list = [[start]]
path_index = 0
visited = set([start])

result = []

while path_index < len(path_list):
    current_path = path_list[path_index]
    last_node = current_path[-1]
    next_nodes = neighbours[last_node]

    if end in next_nodes:
        current_path.append(end)
        print(len(current_path) - 1)
        exit()
    
    for next_node in next_nodes:
        if next_node not in visited:
            new_path = current_path[:]
            new_path.append(next_node)
            path_list.append(new_path)
            # To avoid backtracking
            visited.add(next_node)
    # Continue to next path in list
    path_index += 1