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


def can_hold(target_colour, parent_bag):
    result = False
    for rule in rules[parent_bag]:
        if rule[1] == target_colour:
            return True
        else:
            result = result or can_hold(target_colour, rule[1])
    
    return result

total = 0
for bag in rules:
    if can_hold("shiny gold", bag):
        total += 1
    
print(total)