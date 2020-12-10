import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

# convert lines to ints
input.append(0)
input = sorted(list(map(int, input)))


device_joltage = max(input) + 3
input.append(device_joltage)

cache = {}
def ways_from_index(i):
    total = 0

    if i in cache:
        return cache[i]

    if i == len(input) - 1:
        return 1

    for j in range(i + 1, len(input)):
        if input[j] - input[i] <= 3:
            total += ways_from_index(j)
        else:
            break
    
    cache[i] = total
    return total

print(ways_from_index(0))


# for index, adapter_joltage in enumerate(input):
#     if in

#     # if current_joltage > adapter_joltage:
#     #     continue
#     if adapter_joltage - current_joltage == 1:
#         one_jolt_count += 1
#     elif adapter_joltage - current_joltage == 3:
#         three_jolt_count += 1

#     current_joltage = adapter_joltage

# print(one_jolt_count, three_jolt_count)