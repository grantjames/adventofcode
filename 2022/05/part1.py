import re

f = open("input.txt", "r")
input = f.read().splitlines()
f.close()

count = 0

# Figure out how many stacks there are
stacks = {}
stack_count = int((len(input[0]) + 1) / 4)
# Initialise dictionary of stacks
for i in range(1, stack_count + 1):
    stacks[i] = []

# Parse input to create into data structures
for index, line in enumerate(input):
    if line.startswith(" 1"):
        break
    
    # Use some maths to figure out indexes
    for i in range(1, stack_count + 1):
        box_index = ((i - 1) * 4) + 1
        if line[box_index] != " ":
            stacks[i].insert(0, line[box_index])

# Now continue looping over instructions
for line in input[index+2:]:
    result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
    times = result.group(1)
    from_stack = result.group(2)
    to = result.group(3)

    for x in range(0, int(times)):
        moving = stacks[int(from_stack)].pop()
        stacks[int(to)].append(moving)

result = ""
for i in range(1, stack_count + 1):
    result += stacks[i].pop()

print(result)