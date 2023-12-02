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

print((x_time[19] * 20) + (x_time[59] * 60) + (x_time[99] * 100) + (x_time[139] * 140) + (x_time[179] * 180) + (x_time[219] * 220))