f = open("input.txt", "r")
input = f.readlines()
f.close()

x = 1
x_time = [x]

for ins in input:
    if ins.startswith("addx"):
        # first cycle it does nothing
        x_time.append(x)
        # second cycle it completes
        x += int(ins[5:])
    
    x_time.append(x)

print(x_time)
# We now have a log of the middle position of the sprite at each cycle

for row in range(1, 7):
    for col in range(1, 41):
        cycle = ((row - 1) * 40) + col

        sprite_pos = x_time[cycle - 1]

        if col == sprite_pos or col == sprite_pos + 1 or col == sprite_pos + 2:
            print("#", end="")
        else:
            print(".", end="")
    print("")