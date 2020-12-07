import math

f = open("input.txt", "r")
input = f.readlines()
f.close()

highest_seat_id = 0

for seat in input:
    # calculate row
    row_str = seat[0:7]
    row = 0
    upper = 127
    lower = 0
    for r in row_str:
        midpoint = math.floor((upper + lower) / 2)
        if r == "F":
            upper = math.floor(midpoint)
        else:
            lower = math.ceil(midpoint)

    row = max(upper, lower)

    # calulate column
    column_str = seat[7:]
    column = 0
    upper = 7
    lower = 0
    for c in column_str:
        midpoint = math.floor((upper + lower) / 2)
        if c == "L":
            upper = math.floor(midpoint)
        else:
            lower = math.ceil(midpoint)

    column = max(upper, lower)

    # calculate seat ID
    seat_id = row * 8 + column

    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)

# for line in input:
#     match = re.search(r"(\d+)-(\d+) ([a-z]): (.+)", line)
#     if match:
#         lower = match.group(1)
#         upper = match.group(2)
#         character = match.group(3)
#         password = match.group(4)

#         occurrences = password.count(character)

#         if int(lower) <= occurrences <= int(upper) :
#             valid_passwords += 1

# print(valid_passwords)
    