f = open("input.txt", "r")
input = [l.strip() for l in f.readlines()]
f.close()

directions = ["N", "E", "S", "W"]
ship_facing_index = 1
location = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0,
}

for instruction in input:
    movement = instruction[0]
    amount = int(instruction[1:])

    if movement == "F":
        movement = directions[ship_facing_index]

    if movement in ["N", "E", "S", "W"]:
        location[movement] += amount
    
    if movement == "R":
        ship_facing_index = ((amount / 90) + ship_facing_index) % 4
    if movement == "L":
        ship_facing_index = (ship_facing_index - (amount / 90)) % 4

print(location)
print(abs(location["N"] - location["S"]) + abs(location["E"] - location["W"]))