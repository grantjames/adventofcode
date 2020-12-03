import math

rows = [[point for point in line.rstrip()] for line in open("input.txt", "r")]

height = len(rows)
width = len(rows[0])

slopes = {
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
}

slope_results = []

for slope in slopes:
    trees_hit = 0
    delta_x, delta_y = slope[0], slope[1]
    x, y = 0, 0

    while y + delta_y < height:
        x = (x + delta_x) % width
        y = y + delta_y

        if rows[y][x] == "#":
            trees_hit += 1

    slope_results.append(trees_hit)
    print(trees_hit)

print(math.prod(slope_results))
