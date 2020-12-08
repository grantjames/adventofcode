import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

instructions = []
for line in input:
    # [instruction, value, ran]
    instructions.append({"op": line[0:3], "arg": int(line[4:].rstrip("\n")), "ran": False})

def run_program():
    reset_program()

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

        if address < len(instructions):
            current_instruction = instructions[address]
        else:
            return accumulator

    return None

def reset_program():
    for index, instruction in enumerate(instructions):
        instructions[index]["ran"] = False

# run program
for index, instruction in enumerate(instructions):
    # change the instruction
    if instructions[index]["op"] == "jmp":
        instructions[index]["op"] = "nop"
    elif instructions[index]["op"] == "nop":
        instructions[index]["op"] = "jmp"
    
    result = run_program()

    # change the instructions[index] back
    if result == None:
        if instructions[index]["op"] == "jmp":
            instructions[index]["op"] = "nop"
        elif instructions[index]["op"] == "nop":
            instructions[index]["op"] = "jmp"
    else:
        print(result)
        break