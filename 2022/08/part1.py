f = open("input.txt", "r")
input = f.readlines()
f.close()

grid = []

for line in input:
    grid.append(list(map(int, list(line)[:-1]))) # put newline in input so last line doesn't get trimmed

# How many trees are visible from the outside of the grid?
visible_trees = 0

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        current_tree = grid[y][x]
        vnorth, vsouth, veast, vwest = True, True, True, True
        
        for dy in range(0, len(grid)):
            if grid[dy][x] >= current_tree:
                if dy < y:
                    vnorth = False
                elif dy > y:
                    vsouth = False
        
        for dx in range(0, len(grid[y])):
            if grid[y][dx] >= current_tree:
                if dx < x:
                    vwest = False
                elif dx > x:
                    veast = False

        if vnorth or vsouth or veast or vwest:
            visible_trees += 1
        
# Got interior visible, now count outer
visible_trees += (len(grid[0]) * 2)
visible_trees += ((len(grid) - 2) * 2)

print(visible_trees)