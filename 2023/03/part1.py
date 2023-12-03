# Any number adjacent to a symbol (i.e. not a number or a .)
# Test input answer is: 4361
# Wrong answers: 324606 (too low), 526434(too low), 712543 (too high)
# Part numbers are repeated

f = open("input.txt", "r")
input = [ line.strip() for line in f ]
f.close()

part_numbers = []

neighbour_deltas = [
    (-1, -1), (-1, 0), (-1, 1),
    (0,  -1),          (0,  1),
    (1,  -1), (1,  0), (1,  1),
]

# Find numbers and check if a neighbouring cell is a symbol
row_length = len(input[0])
column_length = len(input)
current_number = ""
current_number_has_symbol = False

y = 0
x = 0

for y in range(0, column_length):
    # Started a new row, if we were building up a number
    # No longer looking at a number
    if current_number != "" and current_number_has_symbol:
        part_numbers.append(int(current_number))
    
    current_number = ""
    current_number_has_symbol = False

    for x in range(0, row_length):
        if input[y][x].isdigit():
            current_number += input[y][x]
            # Check neighbours for symbol
            for dy, dx in neighbour_deltas:
                yy, xx = y + dy, x + dx
                if (xx < 0 or xx >= row_length) or (yy < 0 or yy >= column_length):
                    continue # out of bounds
                if not input[yy][xx].isdigit() and input[yy][xx] != ".":
                    current_number_has_symbol = True
        else:
            # No longer looking at a number
            if current_number != "" and current_number_has_symbol:
                part_numbers.append(int(current_number))
            
            current_number = ""
            current_number_has_symbol = False

if current_number != "" and current_number_has_symbol:
    part_numbers.append(int(current_number))


print(part_numbers)
print(sum([int(x) for x in part_numbers]))