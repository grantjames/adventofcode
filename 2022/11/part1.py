f = open("input.txt", "r")
input = f.readlines()
f.close()

class Monkey:
    items = []
    op = ()
    test = 0
    true_throw = 0
    false_throw = 0
    inspections = 0

    def __str__(self):
        return f"Monkey: {self.items} : {self.op} : {self.test} : {self.true_throw} : {self.false_throw}"

monkeys = []
monkey = Monkey()
    
for line in input:
    line = line.strip()

    if line == "":
        monkeys.append(monkey)
    
    elif line.startswith("Monkey"):
        monkey = Monkey()

    elif line.startswith("Starting"):
        monkey.items = list(map(int, line[16:].split(", ")))
    
    elif line.startswith("Operation"):
        monkey.op = (line[21], line[23:])

    elif line.startswith("Test"):
        monkey.test = int(line[19:])
    
    elif line.startswith("If true"):
        monkey.true_throw = int(line[25])

    elif line.startswith("If false"):
        monkey.false_throw = int(line[26])

for round in range(0, 20):
    for i, monkey in enumerate(monkeys):
        # print("Monkey:", i)
        # inspect each item
        for item in monkey.items:
            monkeys[i].inspections += 1
            # print("Item is:", item)
            other = monkey.op[1]
            if other == "old":
                other = item
            else:
                other = int(other)

            if monkey.op[0] == "*":
                item = item * other
            elif monkey.op[0] == "+":
                item = item + other

            # Now divide by three and round down
            item = int(item / 3)
            # print("New item is:", item)
            
            # Got new priority value, now figure out who to throw to
            if item % monkey.test == 0:
                monkeys[monkey.true_throw].items.append(item)
                # print("Throwing to monkey", monkey.true_throw)
            else:
                monkeys[monkey.false_throw].items.append(item)
                # print("Throwing to monkey", monkey.false_throw)
            
        monkeys[i].items = []

inspections = []
for m in monkeys:
    inspections.append(m.inspections)

inspections.sort(reverse = True)
print(inspections[0] * inspections[1])