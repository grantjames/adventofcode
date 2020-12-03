# read input into a 2d array
# use rstrip to remove newline char
rows = [[point for point in line.rstrip()] for line in open("test_input.txt", "r")]

height = len(rows)
width = len(rows[0])

trees_hit = 0
delta_x, delta_y = 3, 1
x, y = 0, 0

while y + delta_y < height:
    x = (x + delta_x) % width
    y = y + delta_y

    if rows[y][x] == "#":
        trees_hit += 1

print(trees_hit)