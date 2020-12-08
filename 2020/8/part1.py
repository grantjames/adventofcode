import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

instructions = []
for line in input:
    # [instruction, value, ran]
    instructions.append({"op": line[0:3], "arg": int(line[4:].rstrip("\n")), "ran": False})

# run program
accumulator = 0
address = 0
current_instruction = instructions[address]

while not current_instruction["ran"]:
    if current_instruction["op"] == "acc":
        accumulator += current_instruction["arg"]
        address += 1
    elif current_instruction["op"] == "jmp":
        address += current_instruction["arg"]
    elif current_instruction["op"] == "nop":
        address += 1
    
    current_instruction["ran"] = True
    current_instruction = instructions[address]


print(accumulator)