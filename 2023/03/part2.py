# A gear is any * symbol that is adjacent to exactly two part numbers.
# Its gear ratio is the result of multiplying those two numbers together.
# Test input answer is: 467835
# Wrong answers: 72114486 (too low), 378475894681100730 (too high)

import math

f = open("input.txt", "r")
input = [ line.strip() for line in f ]
f.close()

gear_ratios = []

neighbour_deltas = [
    (-1, -1), (-1, 0), (-1, 1),
    (0,  -1),          (0,  1),
    (1,  -1), (1,  0), (1,  1),
]

row_length = len(input[0])
column_length = len(input)

for y in range(0, column_length):
    for x in range(0, row_length):
        if input[y][x] == "*":
            gear_parts = []
            checked_neighbours = []
            # It's a gear, check neighbours
            for dy, dx in neighbour_deltas:
                yy, xx = y + dy, x + dx
                if (xx < 0 or xx >= row_length) or (yy < 0 or yy >= column_length):
                    continue # out of bounds
                if input[yy][xx].isdigit() and (xx, yy) not in checked_neighbours:
                    checked_neighbours.append((xx, yy))
                    current_number = input[yy][xx]
                    
                    # Go left until not digit
                    xp = xx
                    while xp > 0:
                        xp -= 1
                        checked_neighbours.append((xp, yy))
                        if input[yy][xp].isdigit():
                            current_number = input[yy][xp] + current_number
                        else:
                            break

                    # Go right until not digit
                    xp = xx
                    while xp < row_length - 1:
                        xp += 1
                        checked_neighbours.append((xp, yy))
                        if input[yy][xp].isdigit():
                            current_number = current_number + input[yy][xp]
                        else:
                            break

                    # if current_number not in gear_parts:
                    gear_parts.append(current_number)
            
            if (len(gear_parts) > 1):
                print(gear_parts)
                gear_ratios.append(math.prod([int(v) for v in gear_parts]))

print(gear_ratios)
print(sum([int(x) for x in gear_ratios]))