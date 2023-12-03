# Any number adjacent to a symbol (i.e. not a number or a .)
# Test input answer is: 4361
# Wrong answers: 324606 <- too low
# Part numbers are repeated

f = open("test_input.txt", "r")
input = [ line.strip() for line in f ]
f.close()

part_numbers = []

neighbour_deltas = [
    (-1, -1), (-1, 0), (-1, 1),
    (0,  -1),          (0,  1),
    (1,  -1), (1,  0), (1,  1),
]

row_length = len(input[0])
column_length = len(input)

for y in range(0, column_length):
    for x in range(0, row_length):
        if not input[y][x].isdigit() and input[y][x] != ".":
            # It's a symbol, check neighbours
            for dy, dx in neighbour_deltas:
                yy, xx = y + dy, x + dx
                if (xx < 0 or xx >= row_length) or (yy < 0 or yy >= column_length):
                    continue # out of bounds
                if input[yy][xx].isdigit():
                    current_number = input[yy][xx]
                    
                    # Go left until not digit
                    xp = xx
                    while xp > 0:
                        xp -= 1
                        if input[yy][xp].isdigit():
                            current_number = input[yy][xp] + current_number
                        else:
                            break

                    # Go right until not digit
                    xp = xx
                    while xp < row_length - 1:
                        xp += 1
                        if input[yy][xp].isdigit():
                            current_number = current_number + input[yy][xp]
                        else:
                            break

                    # based off current_number length

                    part_numbers.append(current_number)

print(part_numbers)
print(sum([int(x) for x in part_numbers]))