f = open("input.txt", "r")
input = f.readlines()
f.close()

values = []
for line in input:
    # Get first int
    value = ""
    for char in line:
        if char.isdigit():
            value += char
            break
    for char in reversed(line):
        if char.isdigit():
            value += char
            break

    values.append(int(value))

print(sum(values))