import math

f = open("input.txt", "r")
input = f.readlines()
f.close()

def get_mid(input, upper):
    upper = upper
    lower = 0
    for i in input:
        midpoint = math.floor((upper + lower) / 2)
        if i == "L" or i == "F":
            upper = math.floor(midpoint)
        else:
            lower = math.ceil(midpoint)

    return max(upper, lower)

seat_ids = []

for seat in input:
    row = get_mid(seat[0:7], 127)
    column = get_mid(seat[7:], 7)

    seat_ids.append(row * 8 + column)

# find the missing id
seat_ids = sorted(seat_ids)

compare1 = seat_ids[0]
compare2 = seat_ids[1]
for seat_id in seat_ids[2:]:
    if compare2 - compare1 > 1:
        print(compare1 + 1)
        exit()
    
    compare1 = compare2
    compare2 = seat_id