import re

f = open("input.txt", "r")
input = f.read()
f.close()

passports = input.split("\n\n")

valid_passports = 0

for passport in passports:
    byr = passport.count("byr:")
    iyr = passport.count("iyr:")
    eyr = passport.count("eyr:")
    hgt = passport.count("hgt:")
    hcl = passport.count("hcl:")
    ecl = passport.count("ecl:")
    pid = passport.count("pid:")

    if sum((byr, iyr, eyr, hgt, hcl, ecl, pid)) == 7:
        valid_passports += 1

print(valid_passports)

# for line in input:
#     match = re.search(r"(\d+)-(\d+) ([a-z]): (.+)", line)
#     if match:
#         lower = match.group(1)
#         upper = match.group(2)
#         character = match.group(3)
#         password = match.group(4)

#         occurrences = password.count(character)

#         if int(lower) <= occurrences <= int(upper) :
#             valid_passwords += 1

# print(valid_passwords)
    