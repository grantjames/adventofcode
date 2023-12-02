f = open("input.txt", "r")
input = f.readlines()
f.close()

current_elf = 0
calories = []
for i, x in enumerate(input):
    if not x.isspace():
        current_elf += int(x)
    else:
        calories.append(current_elf)
        current_elf = 0

calories.append(current_elf)

calories.sort(reverse=True)
print(sum(calories[:3]))