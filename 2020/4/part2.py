import re

f = open("input.txt", "r")
input = f.read()
f.close()

def byr_is_valid(value):
    return len(value) == 4 and (1920 <= int(value) <= 2002)

def iyr_is_valid(value):
    return len(value) == 4 and (2010 <= int(value) <= 2020)

def eyr_is_valid(value):
    return len(value) == 4 and (2020 <= int(value) <= 2030)

def hgt_is_valid(value):
    match = re.search(r"(\d+)(cm|in)", value)
    if match:
        number = int(match.group(1))
        unit = match.group(2)

        if unit == "cm":
            return 150 <= number <= 193
        
        if unit == "in":
            return 59 <= number <= 76
    
    return False

def hcl_is_valid(value):
    return re.search(r"^#[0-9|a-f]{6}$", value)

def ecl_is_valid(value):
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def pid_is_valid(value):
    return len(value) == 9

passports = input.split("\n\n")

valid_passports = 0

for passport in passports:
    byr = re.search(r"byr:(\S+)", passport)
    byr = byr.group(1) if byr else ""

    iyr = re.search(r"iyr:(\S+)", passport)
    iyr = iyr.group(1) if iyr else ""

    eyr = re.search(r"eyr:(\S+)", passport)
    eyr = eyr.group(1) if eyr else ""

    hgt = re.search(r"hgt:(\S+)", passport)
    hgt = hgt.group(1) if hgt else ""

    hcl = re.search(r"hcl:(\S+)", passport)
    hcl = hcl.group(1) if hcl else ""

    ecl = re.search(r"ecl:(\S+)", passport)
    ecl = ecl.group(1) if ecl else ""

    pid = re.search(r"pid:(\S+)", passport)
    pid = pid.group(1) if pid else ""

    if byr_is_valid(byr) and iyr_is_valid(iyr) and eyr_is_valid(eyr) and hgt_is_valid(hgt) and hcl_is_valid(hcl) and ecl_is_valid(ecl) and pid_is_valid(pid):
        valid_passports += 1

print(valid_passports)