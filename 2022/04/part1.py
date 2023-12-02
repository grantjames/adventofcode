f = open("input.txt", "r")
input = f.read().splitlines()
f.close()

count = 0

for line in input:
    # split into two elves
    elf1, elf2 = line.split(",")

    elf1 = elf1.split("-")
    elf2 = elf2.split("-")
    
    if (int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])):
        # elf 1 contains elf 2
        count+=1

print(count)

# not 569 (too high)
# not 542 (too low)

# answer is 547