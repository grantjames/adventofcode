f = open("input.txt", "r")
input = f.read().splitlines()
f.close()

count = 0

for line in input:
    # split into two elves
    elf1, elf2 = line.split(",")

    elf1 = elf1.split("-")
    elf2 = elf2.split("-")
    
    if (int(elf1[1]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])):
        count+=1

print(count)

# 917 is too high
# answer is 843