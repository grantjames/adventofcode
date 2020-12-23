f = open("input.txt", "r")
input = [l.strip() for l in f.readlines()]
f.close()

directions = ["N", "E", "S", "W"]
ship = {
    "X": 0,
    "Y": 0
}
waypoint = {
    "X": 10,
    "Y": 1
}

for instruction in input:
    movement = instruction[0]
    amount = int(instruction[1:])

    if movement == "F":
        ship["X"] += waypoint["X"] * amount
        ship["Y"] += waypoint["Y"] * amount

    if movement == "N":
        waypoint["Y"] += amount
    elif movement == "S":
        waypoint["Y"] -= amount
    elif movement == "E":
        waypoint["X"] += amount
    elif movement == "W":
        waypoint["X"] -= amount
    
    if movement == "R":
        for turn in range(amount / 90):
            old_x = waypoint["X"]
            waypoint["X"] = waypoint["Y"]
            waypoint["Y"] = -old_x
    if movement == "L":
        for turn in range(amount / 90):
            old_x = waypoint["X"]
            waypoint["X"] = -waypoint["Y"]
            waypoint["Y"] = old_x

print(ship)
print(abs(ship["X"]) + abs(ship["Y"]))

# For each 90 degree turn, swap and negate the second for R, negate the first for L
# 10 units east and 4 units north (10, 4)
# 4 units east and 10 units south (4, -10)
# 10 units west and 4 units south (-10, -4)
# 4 units west and 10 units north (-4, 10)