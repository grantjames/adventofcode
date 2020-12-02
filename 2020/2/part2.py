import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

valid_passwords = 0

for line in input:
    match = re.search(r"(\d+)-(\d+) ([a-z]): (.+)", line)
    if match:
        position1 = int(match.group(1))
        position2 = int(match.group(2))
        character = match.group(3)
        password = match.group(4)

        if (password[position1 - 1] == character) ^ (password[position2 - 1] == character):
            valid_passwords += 1

print(valid_passwords)
    