import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

valid_passwords = 0

for line in input:
    match = re.search(r"(\d+)-(\d+) ([a-z]): (.+)", line)
    if match:
        lower = match.group(1)
        upper = match.group(2)
        character = match.group(3)
        password = match.group(4)

        occurrences = password.count(character)

        if int(lower) <= occurrences <= int(upper) :
            valid_passwords += 1

print(valid_passwords)
    