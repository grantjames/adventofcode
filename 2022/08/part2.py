f = open("input.txt", "r")
input = f.readlines()
f.close()

grid = []

# for i in range(10, -1, -1):
#     print(i)
# exit()

for line in input:
    grid.append(list(map(int, list(line)[:-1]))) # put newline in input so last line doesn't get trimmed

# How many trees are visible from the outside of the grid?
visible_trees = 0
best_score = 0

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[0]) - 1):
        current_tree = grid[y][x]
        score = 0
        # print("For tree", x, y)
        # print("height is", current_tree)
        snorth, ssouth, seast, swest = 0, 0, 0, 0

        # First look north
        for dy in range(y - 1, -1, -1):
            snorth += 1
            if grid[dy][x] >= current_tree:
                break
        # print("Score North is", score)

        # Then look south
        for dy in range(y + 1, len(grid)):
            ssouth += 1
            if grid[dy][x] >= current_tree:
                break
        # print("Score North and south is", score)

        # Look east
        for dx in range(x + 1, len(grid[y])):
            seast += 1
            if grid[y][dx] >= current_tree:
                break
        # print("Score North and south and east is", score)

        # Look west
        for dx in range(x -1, -1, -1):
            swest += 1
            if grid[y][dx] >= current_tree:
                break
        # print("Score North and south and east and west is", score)

        score = snorth * ssouth * seast * swest
        
        if score > best_score:
            best_score = score
        
print(best_score)