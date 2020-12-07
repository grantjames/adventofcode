import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

# generate all the rules
rules = {}
for line in input:
    key = re.match(r"^\w+ \w+", line).group(0)
    value = re.findall(r"(\d) (\w+ \w+)", line)
    rules[key] = value

def bag_count(colour):
    total = 0
    for rule in rules[colour]:
        total += int(rule[0]) + (int(rule[0]) * bag_count(rule[1]))
    
    return total

print(bag_count("shiny gold"))
