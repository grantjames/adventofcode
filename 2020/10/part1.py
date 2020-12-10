import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

# convert lines to ints
input = sorted(list(map(int, input)))

device_joltage = max(input) + 3
input.append(device_joltage)

one_jolt_count = 0
three_jolt_count = 0
current_joltage = 0

for adapter_joltage in input:
    # if current_joltage > adapter_joltage:
    #     continue
    if adapter_joltage - current_joltage == 1:
        one_jolt_count += 1
    elif adapter_joltage - current_joltage == 3:
        three_jolt_count += 1

    current_joltage = adapter_joltage

print(one_jolt_count * three_jolt_count)